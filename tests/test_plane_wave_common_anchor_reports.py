import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-common-anchor-report-en.md"
IT = ROOT / "audit/plane-wave-common-anchor-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-common-anchor.md"
STATUS = "EXACT_PLANE_WAVE_COMMON_ORIENTED_ANCHOR_RECOVERS_REVERSAL_SIGN_CONDITIONALLY_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_ORIENTED_ENDPOINT_ANCHOR_NOT_DERIVED"


class PlaneWaveCommonAnchorReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_ledger_parity(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_scope_and_quotient_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("SO(2)", "O(2)", "SO(2) x SO(2)", "a(B)", "B^T", "ell0"):
            self.assertIn(token, joined)
        self.assertIn("not source-established", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())

    def test_no_dead_end_or_evidence_overclaim(self):
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
