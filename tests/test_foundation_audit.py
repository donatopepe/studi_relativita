import csv
import pathlib
import re
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "audit" / "claims.csv"
EQUATIONS = ROOT / "audit" / "equations" / "equations.csv"
IT = ROOT / "audit" / "audit-report-it.md"
EN = ROOT / "audit" / "audit-report-en.md"
DIMENSIONS = ROOT / "audit" / "dimensional-analysis" / "foundations.md"
ALLOWED = {"SUPPORTED", "SUPPORTED_WITH_CONDITIONS", "CORRECTABLE", "UNPROVEN", "CONTRADICTED", "OUT_OF_SCOPE"}
SELECTED = {
    "UMCH-CLM-0008", "UMCH-CLM-0009", "UMCH-CLM-0010", "UMCH-CLM-0011",
    "UMCH-CLM-0049", "UMCH-CLM-0050", "UMCH-CLM-0051", "UMCH-CLM-0052",
    "UMCH-CLM-0092", "UMCH-CLM-0093", "UMCH-CLM-0094",
}


def report_ids(path):
    return set(re.findall(r"UMCH-CLM-\d{4}", path.read_text(encoding="utf-8")))


class FoundationAuditTests(unittest.TestCase):
    def test_selected_foundational_claims_are_reviewed(self):
        with CLAIMS.open(encoding="utf-8", newline="") as stream:
            rows = {row["claim_id"]: row for row in csv.DictReader(stream)}
        self.assertTrue(SELECTED <= rows.keys())
        for claim_id in SELECTED:
            row = rows[claim_id]
            self.assertIn(row["status"], ALLOWED, claim_id)
            self.assertTrue(row["reviewer"], claim_id)
            self.assertTrue(row["decision"], claim_id)
            self.assertTrue(row["rationale"], claim_id)
            self.assertNotEqual("NOT_CHECKED", row["dimensional_check"], claim_id)
            self.assertTrue(row["reference_ids"], claim_id)

    def test_bilingual_reports_cover_identical_selected_claims(self):
        self.assertEqual(SELECTED, report_ids(IT))
        self.assertEqual(SELECTED, report_ids(EN))
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            self.assertIn("κ₀", text)
            self.assertIn("geodesic", text.lower())
            self.assertIn("UNPROVEN", text)

    def test_dimensions_and_equations_are_audited(self):
        text = DIMENSIONS.read_text(encoding="utf-8")
        self.assertIn("[κ] = L⁻¹", text)
        self.assertIn("[a^μ] = L T⁻²", text)
        self.assertIn("[P^μP_μ] = M² L² T⁻²", text)
        with EQUATIONS.open(encoding="utf-8", newline="") as stream:
            audited = [row for row in csv.DictReader(stream) if row["source_paragraph_id"] in {"UMCH-SRC-P0010", "UMCH-SRC-P0011", "UMCH-SRC-P0051", "UMCH-SRC-P0052", "UMCH-SRC-P0093"}]
        self.assertGreaterEqual(len(audited), 4)
        self.assertTrue(all(row["status"] != "UNREVIEWED" for row in audited))
        self.assertTrue(all(row["dimensional_check"] != "NOT_CHECKED" for row in audited))

    def test_reviewed_inventory_is_deterministic(self):
        result = subprocess.run(["python3", "tools/inventory_source.py", "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()
