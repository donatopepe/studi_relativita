import csv
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "audit" / "claims.csv"
EQUATIONS = ROOT / "audit" / "equations" / "equations.csv"
SUMMARY = ROOT / "audit" / "inventory-summary.json"
TOOL = ROOT / "tools" / "inventory_source.py"

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


class InventoryTests(unittest.TestCase):
    def run_tool(self, *args, check=True):
        return subprocess.run(
            ["python3", str(TOOL), *args], cwd=ROOT, check=check,
            text=True, capture_output=True,
        )

    def test_claim_registry_has_schema_and_represents_every_source_paragraph(self):
        with CLAIMS.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            self.assertEqual(CLAIM_FIELDS, reader.fieldnames)
            rows = list(reader)
        self.assertEqual(602, len(rows))
        self.assertEqual("UMCH-CLM-0001", rows[0]["claim_id"])
        self.assertEqual("UMCH-CLM-0602", rows[-1]["claim_id"])
        self.assertEqual("UMCH-SRC-P0001", rows[0]["source_paragraph_id"])
        allowed = {"UNREVIEWED", "SUPPORTED", "SUPPORTED_WITH_CONDITIONS", "CORRECTABLE", "UNPROVEN", "CONTRADICTED", "OUT_OF_SCOPE"}
        self.assertTrue(all(row["status"] in allowed for row in rows))
        self.assertGreater(sum(row["status"] == "UNREVIEWED" for row in rows), 500)
        self.assertTrue(all(row["translation_en"] or row["reviewer"] for row in rows if row["status"] != "UNREVIEWED"))

    def test_equation_candidates_are_linked_from_claims(self):
        with CLAIMS.open(encoding="utf-8", newline="") as stream:
            claims = list(csv.DictReader(stream))
        with EQUATIONS.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            self.assertEqual(EQUATION_FIELDS, reader.fieldnames)
            equations = list(reader)
        self.assertGreater(len(equations), 50)
        ids = {row["equation_id"] for row in equations}
        self.assertEqual(len(ids), len(equations))
        linked = {item for row in claims for item in row["equation_ids"].split(";") if item}
        self.assertEqual(ids, linked)
        allowed = {"UNREVIEWED", "SUPPORTED", "SUPPORTED_WITH_CONDITIONS", "CORRECTABLE", "UNPROVEN", "CONTRADICTED", "OUT_OF_SCOPE"}
        self.assertTrue(all(row["status"] in allowed for row in equations))
        self.assertGreater(sum(row["status"] == "UNREVIEWED" for row in equations), 150)
        self.assertTrue(all(row["normalized_latex"] for row in equations if row["status"] != "UNREVIEWED"))

    def test_summary_and_committed_artifacts_are_current(self):
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
        self.assertEqual(602, summary["source_paragraphs"])
        self.assertEqual(602, summary["claims"])
        self.assertEqual(summary["equation_candidates"], summary["linked_equation_candidates"])
        result = self.run_tool("--check", check=False)
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()
