import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references" / "library.bib"
LOG = ROOT / "references" / "verification-log.md"


class PaperIIBSourceTests(unittest.TestCase):
    def test_arxiv_ids_are_attached_to_canonical_entries(self):
        bib = BIB.read_text(encoding="utf-8")
        sections = {
            "ArreagaCapovillaGuven2001": "hep-th/0105040",
            "CapovillaGuvenRojas2002": "hep-th/0111014",
        }
        for key, identifier in sections.items():
            section = bib.split(f"@article{{{key},", 1)[1].split("\n}", 1)[0]
            self.assertIn(f"eprint = {{{identifier}}}", section)
            self.assertIn("archivePrefix = {arXiv}", section)

    def test_verification_log_records_exact_imported_formulas(self):
        log = LOG.read_text(encoding="utf-8")
        required = [
            "ACG2001-E42", "ACG2001-E45", "ACG2001-E46",
            "CGR2002-E19", "CGR2002-E24", "CGR2002-E25",
            "CGR2002-E26", "CGR2002-E28", "CGR2002-E29",
        ]
        for identifier in required:
            self.assertIn(identifier, log)
        self.assertIn("https://arxiv.org/abs/hep-th/0105040", log)
        self.assertIn("https://arxiv.org/abs/hep-th/0111014", log)
        self.assertIn("Imported formula scope:", log)
        self.assertIn("does not establish full stability", log)


if __name__ == "__main__":
    unittest.main()
