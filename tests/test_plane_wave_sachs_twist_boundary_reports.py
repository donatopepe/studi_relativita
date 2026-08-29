import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-sachs-twist-boundary-report-en.md"
IT = ROOT / "audit/plane-wave-sachs-twist-boundary-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-sachs-twist-boundary.md"
STATUS = "EXACT_PLANE_WAVE_NONVERTEX_TWIST_BOUNDARY_PROPAGATED_ORIENTATION_AND_AFFINE_SCALE_CONDITIONAL_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_SACHS_BOUNDARY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_ROTATING_CONGRUENCE_BOUNDARY_PARITY_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED"


class PlaneWaveSachsTwistBoundaryReportTests(unittest.TestCase):
    def test_files_and_ledger_parity(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)
            text = path.read_text()
            for token in (STATUS, CLASSIFICATION, OPEN, "UMCH remains `UNPROVEN`", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)

    def test_raw_boundary_orientation_and_scale_scope(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("X", "V", "S=VX^{-1}", "S_0", "twist", "det X", "SO(2)", "O(2)", "boundary", "affine", "caustic", "ell0"):
            self.assertIn(token, joined)

    def test_source_limit_and_no_dead_end_are_bilingual(self):
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
