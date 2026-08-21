import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
IT = ROOT / "papers" / "foundation" / "it" / "main.tex"
EN = ROOT / "papers" / "foundation" / "en" / "main.tex"
README = ROOT / "papers" / "foundation" / "README.md"


def labels(text):
    return set(re.findall(r"\\label\{([^}]+)\}", text))


def citations(text):
    found = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        found.update(item.strip() for item in group.split(","))
    return found


def claims(text):
    return set(re.findall(r"UMCH-CLM-\d{4}", text))


class PaperAlignmentTests(unittest.TestCase):
    def test_paper_sources_and_build_status_exist(self):
        self.assertTrue(IT.is_file())
        self.assertTrue(EN.is_file())
        status = README.read_text(encoding="utf-8")
        self.assertIn("NOT COMPILED LOCALLY", status)
        self.assertIn("pdflatex", status)

    def test_versions_have_aligned_labels_claims_and_citations(self):
        italian = IT.read_text(encoding="utf-8")
        english = EN.read_text(encoding="utf-8")
        self.assertGreaterEqual(len(labels(italian)), 8)
        self.assertEqual(labels(italian), labels(english))
        self.assertEqual(claims(italian), claims(english))
        self.assertEqual(citations(italian), citations(english))
        self.assertGreaterEqual(len(citations(italian)), 2)

    def test_required_sections_and_disclosures_are_present(self):
        required_labels = {
            "sec:status", "sec:definitions", "sec:hypothesis", "sec:derivation",
            "sec:tension", "sec:limits", "sec:falsification", "sec:limitations",
            "sec:ai",
        }
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            self.assertTrue(required_labels <= labels(text))
            self.assertIn("UNPROVEN", text)
            self.assertIn(r"\kappa_0", text)
            self.assertIn(r"u^\mu=\frac{dx^\mu}{d\tau}", text)
            self.assertNotRegex(text, r"(?i)(we prove|dimostriamo)\s+(?:that\s+)?\\?kappa_0\s*>\s*0")
            self.assertNotRegex(text, r"(?i)(established result|risultato acquisito).*κ_0\s*>\s*0")

    def test_only_audited_claim_ids_are_used(self):
        allowed = {
            "UMCH-CLM-0008", "UMCH-CLM-0009", "UMCH-CLM-0010", "UMCH-CLM-0011",
            "UMCH-CLM-0049", "UMCH-CLM-0050", "UMCH-CLM-0051", "UMCH-CLM-0052",
            "UMCH-CLM-0092", "UMCH-CLM-0093", "UMCH-CLM-0094",
        }
        self.assertTrue(claims(IT.read_text(encoding="utf-8")) <= allowed)
        self.assertTrue(claims(EN.read_text(encoding="utf-8")) <= allowed)


if __name__ == "__main__":
    unittest.main()
