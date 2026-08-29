import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-covariant-screen-phase-report-en.md"
IT = ROOT / "audit/plane-wave-covariant-screen-phase-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-covariant-screen-phase.md"

CLASSIFICATION = "EXACT_SPACETIME_COVARIANT_SCREEN_PHASE_MAP_CORRECTION_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
STATUS = "EXACT_PLANE_WAVE_ROTATING_SCREEN_CONNECTION_TERMS_REQUIRED_NAIVE_TRANSPORTED_JACOBI_MAP_SUPERSEDED_NOT_ELL0"
GATE = "PHYSICAL_SCREEN_CONNECTION_ENDPOINT_ANGULAR_VELOCITY_AND_DETECTOR_PHASE_VARIABLES_NOT_DERIVED"


class CovariantScreenPhaseReportTests(unittest.TestCase):
    def test_bilingual_theory_parity(self):
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            for token in (CLASSIFICATION, STATUS, GATE, "A_prime", "G_source", "G_observer", "P_naive_conjugated_profile", "P_covariant", "UNPROVEN", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)
            self.assertIn("10.1088/0264-9381/29/23/235023", text)
            self.assertIn("PR #76", text)

    def test_correction_source_limits_and_no_dead_end(self):
        en, it = EN.read_text(), IT.read_text()
        for phrase in ("not established by the source", "not a structural dead end", "rotating-coordinate interpretation is superseded"):
            self.assertIn(phrase, en)
        for phrase in ("non stabiliti dalla fonte", "non è un vicolo cieco strutturale", "interpretazione in coordinate rotating è superseded"):
            self.assertIn(phrase, it)


if __name__ == "__main__":
    unittest.main()
