import hashlib
import json
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "archive" / "original" / "Dimostrazione e Prove Relatività Einstein.docx"
TOOL = ROOT / "tools" / "extract_docx.py"
OUTPUT = ROOT / "archive" / "extracted" / "document-it.md"
MANIFEST = ROOT / "archive" / "extracted" / "extraction-manifest.json"


class DocxExtractionTests(unittest.TestCase):
    def run_tool(self, *args, check=True):
        return subprocess.run(
            ["python3", str(TOOL), *map(str, args)],
            cwd=ROOT,
            check=check,
            text=True,
            capture_output=True,
        )

    def test_extracts_stable_paragraph_ids_and_headings(self):
        with tempfile.TemporaryDirectory() as temp:
            output = pathlib.Path(temp) / "document.md"
            manifest = pathlib.Path(temp) / "manifest.json"
            self.run_tool("--source", SOURCE, "--output", output, "--manifest", manifest)
            text = output.read_text(encoding="utf-8")
            self.assertIn("<!-- UMCH-SRC-P0001 | style=Heading1 -->", text)
            self.assertIn("# Dimostrazione e Prove Relatività Einstein", text)
            self.assertIn("UMCH-SRC-P0602", text)
            self.assertIn("https://gemini.google.com/app/7be2a2bff8704a94", text)

    def test_manifest_records_source_and_deterministic_counts(self):
        with tempfile.TemporaryDirectory() as temp:
            output = pathlib.Path(temp) / "document.md"
            manifest = pathlib.Path(temp) / "manifest.json"
            self.run_tool("--source", SOURCE, "--output", output, "--manifest", manifest)
            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), data["source_sha256"])
            self.assertEqual("umch-docx-extractor/1.0", data["extractor_version"])
            self.assertEqual(602, data["nonempty_paragraphs"])
            self.assertGreaterEqual(data["paragraphs_total"], 602)
            self.assertEqual(8, data["headings"]["Heading1"])
            self.assertEqual(44, data["headings"]["Heading2"])
            self.assertEqual(63, data["headings"]["Heading3"])
            self.assertIn("equation", " ".join(data["known_limitations"]).lower())

    def test_committed_artifacts_match_fresh_extraction(self):
        result = self.run_tool("--check", check=False)
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)
        self.assertTrue(OUTPUT.is_file())
        self.assertTrue(MANIFEST.is_file())


if __name__ == "__main__":
    unittest.main()
