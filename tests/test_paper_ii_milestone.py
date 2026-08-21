import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "roadmap.md"
IT = ROOT / "docs" / "overview-it.md"
EN = ROOT / "docs" / "overview-en.md"


class PaperIIMilestoneTests(unittest.TestCase):
    def test_roadmap_records_review_ready_but_deferred_downstream_state(self):
        text = ROADMAP.read_text(encoding="utf-8")
        self.assertIn("Paper II review-ready milestone", text)
        self.assertIn("A: `INCOMPLETE`", text)
        self.assertIn("B: `INCOMPLETE`", text)
        self.assertIn("C: `NON_IDENTIFIABLE`", text)
        self.assertIn("`NO_GO_NOT_ESTABLISHED`", text)
        self.assertIn("Paper III remains scientifically deferred", text)

    def test_overviews_report_same_paper_ii_tokens(self):
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            for token in ["Paper II", "INCOMPLETE", "NON_IDENTIFIABLE", "ALTERNATIVE_HYPOTHESIS", "NO_GO_NOT_ESTABLISHED"]:
                self.assertIn(token, text)
            self.assertIn("Paper III", text)


if __name__ == "__main__":
    unittest.main()
