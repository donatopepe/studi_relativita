import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-sachs-optics-report-en.md"
IT = ROOT / "audit/plane-wave-sachs-optics-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-sachs-optics.md"
STATUS = "EXACT_PLANE_WAVE_SACHS_EXPANSION_SHEAR_CALIBRATION_MOVABLE_TWIST_ZERO_AFFINE_SCALE_BLIND_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_SACHS_ENDPOINT_CALIBRATION_TWIST_SOURCE_AND_ELL0_LAW_NOT_DERIVED"


class PlaneWaveSachsOpticsReportTests(unittest.TestCase):
    def test_files_and_ledger_parity(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)
            text = path.read_text()
            for token in (STATUS, CLASSIFICATION, OPEN, "UMCH remains `UNPROVEN`", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)

    def test_channel_native_boundary_and_quotient_scope(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("S=DB^{-1}", "B", "D", "vertex", "caustic", "screen", "expansion", "shear", "twist", "H_o", "SO(2)", "affine", "ell0"):
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
