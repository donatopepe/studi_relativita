import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-screen-transport-report-en.md"
IT = ROOT / "audit/plane-wave-screen-transport-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-screen-transport.md"

CLASSIFICATION = "EXACT_SPACETIME_TRANSPORT_WINDOW_JACOBI_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
STATUS = "EXACT_PLANE_WAVE_SCREEN_TRANSPORT_AVERAGE_ORDER_OPERATOR_AND_JACOBI_PROTOCOL_DEPENDENT_AFFINE_SCALE_BLIND_NOT_ELL0"
GATE = "PHYSICAL_SCREEN_CONNECTION_PATH_KERNEL_AND_COMMON_ENDPOINT_STANDARD_NOT_DERIVED"


class PlaneWaveScreenTransportReportTests(unittest.TestCase):
    def test_bilingual_authority_and_theory_parity(self):
        texts = [EN.read_text(), IT.read_text(), THEORY.read_text()]
        for text in texts:
            for token in (CLASSIFICATION, STATUS, GATE, "K", "omega", "Q", "W_raw", "W_transport", "P_raw", "P_naive_conjugated_profile", "UNPROVEN", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)
            self.assertIn("10.1088/0264-9381/29/23/235023", text)
            self.assertIn("top-hat", text.lower())
            self.assertIn("triangular", text.lower())

    def test_limits_and_no_dead_end_are_explicit(self):
        en, it = EN.read_text(), IT.read_text()
        for phrase in ("not established by the source", "not a structural dead end", "project protocol input"):
            self.assertIn(phrase, en)
        for phrase in ("non stabiliti dalla fonte", "non è un vicolo cieco strutturale", "input di protocollo progettuale"):
            self.assertIn(phrase, it)


if __name__ == "__main__":
    unittest.main()
