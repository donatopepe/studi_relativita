import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-canonical-reduction-report-en.md"
IT = ROOT / "audit/plane-wave-canonical-reduction-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-canonical-reduction.md"
STATUS = "EXACT_PLANE_WAVE_FULL_MAP_TRANSITIVE_UNDER_INDEPENDENT_CANONICAL_ENDPOINT_CALIBRATION_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_CANONICAL_ENDPOINT_CALIBRATION_GROUP_NOT_DERIVED"


class PlaneWaveCanonicalReductionReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_status_parity(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
                self.assertIn(token, text)

    def test_group_action_and_raw_scope_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("A", "B", "C", "D", "Sp(4)", "G_o=P_2P_1^{-1}", "G_oP_1G_s^{-1}=P_2", "trace", "ell0"):
            self.assertIn(token, joined)
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())

    def test_conditional_group_and_no_dead_end_are_bilingual(self):
        self.assertIn("strongest project nuisance group", EN.read_text())
        self.assertIn("gruppo nuisance progettuale più forte", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
