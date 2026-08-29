import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-full-jacobi-report-en.md"
IT = ROOT / "audit/plane-wave-full-jacobi-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-full-jacobi.md"
STATUS = "EXACT_PLANE_WAVE_FULL_JACOBI_LABELLED_ENDPOINT_ORDER_CONDITIONAL_SWAP_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_ENDPOINT_LABELS_AND_CALIBRATION_NOT_DERIVED"


class PlaneWaveFullJacobiReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_status_parity(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_native_blocks_boundary_and_scaling_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("A", "B", "C", "D", "P_rev=E P^T E", "B^{-1}A", "DB^{-1}", "endpoint swap", "ell0"):
            self.assertIn(token, joined)
        self.assertIn("not source-established", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())

    def test_no_dead_end_or_detection_overclaim(self):
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
