import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-endpoint-shear-report-en.md"
IT = ROOT / "audit/plane-wave-endpoint-shear-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-endpoint-shear.md"
STATUS = "EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED"


class PlaneWaveEndpointShearReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_status_parity(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
                self.assertIn(token, text)

    def test_equations_raw_blocks_and_nuisance_scope_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("A", "B", "C", "D", "S(H)", "P'=S(H_o)P S(H_s)^{-1}", "B^{-1}A-H_s", "DB^{-1}+H_o", "ell0"):
            self.assertIn(token, joined)
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())

    def test_limits_and_no_dead_end_are_bilingual(self):
        self.assertIn("does not erase every full-map invariant", EN.read_text())
        self.assertIn("non elimina ogni invariante della full map", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
