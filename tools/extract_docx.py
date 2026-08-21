#!/usr/bin/env python3
"""Deterministic, loss-aware text extraction from the UMCH source DOCX."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import sys
import tempfile
import zipfile
from xml.etree import ElementTree as ET


VERSION = "umch-docx-extractor/1.0"
ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "archive" / "original" / "Dimostrazione e Prove Relatività Einstein.docx"
DEFAULT_OUTPUT = ROOT / "archive" / "extracted" / "document-it.md"
DEFAULT_MANIFEST = ROOT / "archive" / "extracted" / "extraction-manifest.json"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "r": R, "pr": PKG_REL}


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relationships(archive: zipfile.ZipFile) -> dict[str, str]:
    try:
        root = ET.fromstring(archive.read("word/_rels/document.xml.rels"))
    except KeyError:
        return {}
    return {
        item.attrib["Id"]: item.attrib.get("Target", "")
        for item in root.findall("pr:Relationship", NS)
        if "Id" in item.attrib
    }


def paragraph_text(paragraph: ET.Element, rels: dict[str, str]) -> tuple[str, bool]:
    pieces: list[str] = []
    has_equation = False
    for node in paragraph.iter():
        local = node.tag.rsplit("}", 1)[-1]
        if local == "t" and node.text:
            pieces.append(node.text)
        elif local == "tab":
            pieces.append("\t")
        elif local in {"br", "cr"}:
            pieces.append("\n")
        elif local in {"oMath", "oMathPara"}:
            has_equation = True
        elif local == "hyperlink":
            relation_id = node.attrib.get(f"{{{R}}}id")
            target = rels.get(relation_id or "")
            visible = "".join(child.text or "" for child in node.iter() if child.tag == f"{{{W}}}t")
            if target and target not in visible:
                pieces.append(f" <{target}>")
    return "".join(pieces).strip(), has_equation


def extract(source: pathlib.Path) -> tuple[str, dict]:
    with zipfile.ZipFile(source) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
        rels = relationships(archive)

    paragraphs = root.findall(".//w:body/w:p", NS)
    records: list[dict] = []
    headings: collections.Counter[str] = collections.Counter()
    empty_equation_paragraphs = 0

    for paragraph in paragraphs:
        text, has_equation = paragraph_text(paragraph, rels)
        if not text and not has_equation:
            continue
        style_node = paragraph.find("./w:pPr/w:pStyle", NS)
        style = style_node.attrib.get(f"{{{W}}}val", "body") if style_node is not None else "body"
        if style.startswith("Heading"):
            headings[style] += 1
        if has_equation and not text:
            empty_equation_paragraphs += 1
        records.append({"text": text, "style": style, "has_equation": has_equation})

    lines = [
        "---",
        "title: \"Estrazione storica — Dimostrazione e Prove Relatività Einstein\"",
        f'source_sha256: "{sha256(source)}"',
        f'extractor: "{VERSION}"',
        "status: historical-source",
        "---",
        "",
        "> Estrazione deterministica del documento storico. Testo non verificato; non costituisce prova scientifica.",
        "",
    ]
    for number, record in enumerate(records, 1):
        identifier = f"UMCH-SRC-P{number:04d}"
        flags = [f"style={record['style']}"]
        if record["has_equation"]:
            flags.append("contains-equation-markup=true")
        lines.append(f"<!-- {identifier} | {' | '.join(flags)} -->")
        level = {"Heading1": "#", "Heading2": "##", "Heading3": "###"}.get(record["style"])
        text = record["text"] or "[EQUATION MARKUP WITHOUT EXTRACTED PLAIN TEXT]"
        lines.append(f"{level} {text}" if level else text)
        lines.append("")

    markdown = "\n".join(lines).rstrip() + "\n"
    manifest = {
        "extractor_version": VERSION,
        "source_file": source.name,
        "source_sha256": sha256(source),
        "paragraphs_total": len(paragraphs),
        "nonempty_paragraphs": len(records),
        "empty_equation_paragraphs": empty_equation_paragraphs,
        "headings": dict(sorted(headings.items())),
        "known_limitations": [
            "Office Math equation structure is flagged but flattened text may lose mathematical layout and semantics.",
            "Pagination, floating layout, embedded font behavior, comments, and tracked changes are not reproduced.",
            "Hyperlinks are recovered only when represented by standard document relationships.",
        ],
    }
    return markdown, manifest


def render_manifest(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def check(source: pathlib.Path, output: pathlib.Path, manifest_path: pathlib.Path) -> int:
    markdown, manifest = extract(source)
    expected_manifest = render_manifest(manifest)
    mismatches = []
    if not output.exists() or output.read_text(encoding="utf-8") != markdown:
        mismatches.append(str(output))
    if not manifest_path.exists() or manifest_path.read_text(encoding="utf-8") != expected_manifest:
        mismatches.append(str(manifest_path))
    if mismatches:
        print("Generated extraction differs: " + ", ".join(mismatches), file=sys.stderr)
        return 1
    print("Extraction artifacts are current.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=pathlib.Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=pathlib.Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        return check(args.source, args.output, args.manifest)

    markdown, manifest = extract(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    args.manifest.write_text(render_manifest(manifest), encoding="utf-8")
    print(f"Wrote {args.output} and {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
