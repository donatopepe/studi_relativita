import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-sachs-shear-transfer-report-en.md"
IT = ROOT / "audit/plane-wave-sachs-shear-transfer-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-sachs-shear-transfer.md"
CLASSIFICATION = "EXACT_SPACETIME_SACHS_CALIBRATION_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
STATUS = "EXACT_PLANE_WAVE_SACHS_SOURCE_SHEAR_ABSORBED_BY_BOUNDARY_OBSERVER_SHEAR_MOVES_OPTICS_NOT_ELL0"
OPEN = "PHYSICAL_SACHS_SOURCE_BOUNDARY_AND_OBSERVER_CALIBRATION_NOT_DERIVED"


class PlaneWaveSachsShearTransferReportTests(unittest.TestCase):
    def test_files_and_ledger_parity(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)
            text = path.read_text()
            for token in (CLASSIFICATION, STATUS, OPEN, "UMCH remains `UNPROVEN`", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)

    def test_raw_objects_equations_and_nuisance_scope(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("P", "X", "V", "S", "S_0", "H_s", "H_o", "S=VX^{-1}", "S'_0=S_0+H_s", "S'_o=S_o+H_o", "boundary", "calibration", "affine", "caustic", "ell0"):
            self.assertIn(token, joined)

    def test_source_limits_and_no_dead_end_are_bilingual(self):
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
