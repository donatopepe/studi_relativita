import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references" / "library.bib"
LOG = ROOT / "references" / "verification-log.md"
REQUIRED = {
    "ArreagaCapovillaGuven2001": "10.1088/0264-9381/18/23/304",
    "CapovillaGuvenRojas2002": "10.1088/0264-9381/19/8/315",
    "NesterenkoEtAl1995": "10.1063/1.531332",
}


class ClassicalDynamicsBibliographyTests(unittest.TestCase):
    def test_required_entries_have_canonical_dois(self):
        bibliography = BIB.read_text(encoding="utf-8")
        for key, doi in REQUIRED.items():
            self.assertIn(f"@article{{{key},", bibliography)
            self.assertIn(f"doi = {{{doi}}}", bibliography)
            self.assertIn(f"url = {{https://doi.org/{doi}}}", bibliography)

    def test_verification_log_states_support_and_non_support(self):
        log = LOG.read_text(encoding="utf-8")
        for key, doi in REQUIRED.items():
            self.assertIn(f"## {key}", log)
            section = log.split(f"## {key}", 1)[1].split("\n## ", 1)[0]
            self.assertIn(f"https://api.crossref.org/works/{doi}", section)
            self.assertIn("Exact supported topic:", section)
            self.assertIn("Limits:", section)
            self.assertIn("does not establish", section)
            self.assertIn("Access date: 2026-08-21", section)


if __name__ == "__main__":
    unittest.main()
