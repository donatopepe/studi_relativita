#!/usr/bin/env python3
"""Create a conservative, deterministic inventory of extracted source paragraphs."""

from __future__ import annotations

import argparse
import csv
import io
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "archive" / "extracted" / "document-it.md"
CLAIMS = ROOT / "audit" / "claims.csv"
EQUATIONS = ROOT / "audit" / "equations" / "equations.csv"
SUMMARY = ROOT / "audit" / "inventory-summary.json"
REVIEWS = ROOT / "audit" / "foundation-reviews.json"
MARKER = re.compile(r"^<!-- (UMCH-SRC-P\d{4}) \| style=([^ |]+)(?: \| [^>]+)? -->$")
FORMULA_HINT = re.compile(r"(?:[=≥≤≈∝]|\b(?:κ|tau|omega|Gamma|Delta|Lambda|alpha|beta)\b|[κμντℏħΔΓΛ∇∫√])")

CLAIM_FIELDS = [
    "claim_id", "source_paragraph_id", "original_text", "normalized_it",
    "translation_en", "sector", "claim_type", "prerequisites",
    "equation_ids", "reference_ids", "dimensional_check", "evidence_level",
    "status", "reviewer", "decision", "rationale",
]
EQUATION_FIELDS = [
    "equation_id", "source_paragraph_id", "original_text", "normalized_latex",
    "symbols", "declared_units", "dimensional_check", "status", "rationale",
]


def parse_source(path: pathlib.Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    records = []
    current = None
    body: list[str] = []
    for line in lines:
        match = MARKER.match(line)
        if match:
            if current:
                current["text"] = "\n".join(body).strip().lstrip("# ")
                records.append(current)
            current = {"source_id": match.group(1), "style": match.group(2)}
            body = []
        elif current is not None:
            body.append(line)
    if current:
        current["text"] = "\n".join(body).strip().lstrip("# ")
        records.append(current)
    return records


def claim_type(record: dict[str, str]) -> str:
    text = record["text"].lower()
    if record["style"].startswith("Heading"):
        return "DEFINITION" if "definiz" in text or "definition" in text else "CONCLUSION"
    if any(word in text for word in ("postul", "assum", "ipotes", "hypoth")):
        return "ASSUMPTION"
    if any(word in text for word in ("si dimostra", "we demonstrate", "si ricava", "yields")):
        return "DERIVATION"
    if any(word in text for word in ("prediz", "prediction", "misurabil")):
        return "PREDICTION"
    if any(word in text for word in ("simulazione", "simulation", "numeric")):
        return "NUMERICAL_RESULT"
    if any(word in text for word in ("confront", "comparison", "versus", " vs.")):
        return "COMPARISON"
    return "CONJECTURE"


def sector(text: str) -> str:
    low = text.lower()
    sectors = [
        ("cosmology", ("cosmolog", "hubble", "universo", "universe")),
        ("gravitation", ("gravit", "spacetime", "spaziotempo", "einstein")),
        ("quantum-fields", ("qed", "quant", "fotoni", "photon", "graviton")),
        ("radiation-reaction", ("abraham", "lorentz-dirac", "radiation reaction", "runaway")),
        ("geometry", ("curvatur", "geodes", "frenet", "κ")),
    ]
    return next((name for name, words in sectors if any(word in low for word in words)), "unclassified")


def is_equation_candidate(record: dict[str, str]) -> bool:
    text = record["text"]
    if record["style"].startswith("Heading") or len(text) > 700:
        return False
    return bool(FORMULA_HINT.search(text))


def csv_text(fields: list[str], rows: list[dict[str, str]]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def load_reviews(path: pathlib.Path) -> dict:
    if not path.exists():
        return {"claims": {}, "equations": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def apply_review(row: dict[str, str], review: dict[str, str]) -> None:
    unknown = set(review) - set(row)
    if unknown:
        raise ValueError(f"Unknown review fields: {sorted(unknown)}")
    row.update(review)


def build(source: pathlib.Path, reviews_path: pathlib.Path = REVIEWS) -> tuple[str, str, str]:
    records = parse_source(source)
    reviews = load_reviews(reviews_path)
    claims = []
    equations = []
    for index, record in enumerate(records, 1):
        equation_id = ""
        if is_equation_candidate(record):
            equation_id = f"UMCH-EQ-{len(equations) + 1:04d}"
            equations.append({
                "equation_id": equation_id,
                "source_paragraph_id": record["source_id"],
                "original_text": record["text"],
                "normalized_latex": "",
                "symbols": "",
                "declared_units": "",
                "dimensional_check": "NOT_CHECKED",
                "status": "UNREVIEWED",
                "rationale": "Automatically detected formula candidate; requires human mathematical review.",
            })
        claims.append({
            "claim_id": f"UMCH-CLM-{index:04d}",
            "source_paragraph_id": record["source_id"],
            "original_text": record["text"],
            "normalized_it": "",
            "translation_en": "",
            "sector": sector(record["text"]),
            "claim_type": claim_type(record),
            "prerequisites": "",
            "equation_ids": equation_id,
            "reference_ids": "",
            "dimensional_check": "NOT_CHECKED",
            "evidence_level": "NONE_ASSIGNED",
            "status": "UNREVIEWED",
            "reviewer": "",
            "decision": "",
            "rationale": "Pending atomicity and scientific review.",
        })
    claim_rows = {row["claim_id"]: row for row in claims}
    equation_rows = {row["equation_id"]: row for row in equations}
    missing_claims = set(reviews.get("claims", {})) - set(claim_rows)
    missing_equations = set(reviews.get("equations", {})) - set(equation_rows)
    if missing_claims or missing_equations:
        raise ValueError(f"Review IDs missing from inventory: claims={sorted(missing_claims)}, equations={sorted(missing_equations)}")
    for identifier, review in reviews.get("claims", {}).items():
        apply_review(claim_rows[identifier], review)
    for identifier, review in reviews.get("equations", {}).items():
        apply_review(equation_rows[identifier], review)
    status_counts: dict[str, int] = {}
    for row in claims:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    summary = {
        "source_paragraphs": len(records),
        "claims": len(claims),
        "equation_candidates": len(equations),
        "linked_equation_candidates": sum(bool(row["equation_ids"]) for row in claims),
        "status": dict(sorted(status_counts.items())),
        "warning": "Inventory is automatic and conservative; classification is not scientific validation.",
    }
    return csv_text(CLAIM_FIELDS, claims), csv_text(EQUATION_FIELDS, equations), json.dumps(summary, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=pathlib.Path, default=SOURCE)
    parser.add_argument("--claims", type=pathlib.Path, default=CLAIMS)
    parser.add_argument("--equations", type=pathlib.Path, default=EQUATIONS)
    parser.add_argument("--summary", type=pathlib.Path, default=SUMMARY)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = build(args.source)
    paths = (args.claims, args.equations, args.summary)
    if args.check:
        mismatches = [str(path) for path, text in zip(paths, generated) if not path.exists() or path.read_text(encoding="utf-8") != text]
        if mismatches:
            print("Inventory artifacts differ: " + ", ".join(mismatches), file=sys.stderr)
            return 1
        print("Inventory artifacts are current.")
        return 0
    for path, text in zip(paths, generated):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
    print(f"Wrote {len(paths)} inventory artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
