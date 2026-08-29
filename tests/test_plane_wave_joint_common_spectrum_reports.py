import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-joint-common-spectrum-report-en.md"
IT = ROOT / "audit/plane-wave-joint-common-spectrum-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-joint-common-spectrum.md"
STATUS = "EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED"


class PlaneWaveJointCommonSpectrumReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_ledger_parity(self):
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
                self.assertIn(token, text)

    def test_joint_raw_object_and_scale_orbit_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("W", "A", "B", "C", "D", "characteristic polynomial", "K_s(u)=s^{-2}K(u/s)", "T_s", "top-hat", "triangular", "ell0"):
            self.assertIn(token, joined)

    def test_source_scope_and_no_dead_end_are_bilingual(self):
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
