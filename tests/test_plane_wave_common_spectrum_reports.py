import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/plane-wave-common-spectrum-report-en.md"
IT = ROOT / "audit/plane-wave-common-spectrum-report-it.md"
THEORY = ROOT / "theory/spacetime/plane-wave-common-spectrum.md"
STATUS = "EXACT_PLANE_WAVE_COMMON_CANONICAL_SPECTRUM_PROFILE_INFORMATIVE_REVERSAL_AND_AFFINE_SCALE_BLIND_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"
OPEN = "PHYSICAL_COMMON_CANONICAL_STANDARD_AND_ELL0_LAW_NOT_DERIVED"


class PlaneWaveCommonSpectrumReportTests(unittest.TestCase):
    def test_reports_and_theory_exist(self):
        for path in (EN, IT, THEORY):
            self.assertTrue(path.exists(), path)

    def test_exact_status_parity(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (STATUS, CLASSIFICATION, OPEN, "NO_POSITIVE_DETECTION_CLAIM", "UMCH remains `UNPROVEN`"):
                self.assertIn(token, text)

    def test_spectrum_group_and_scale_scope_are_explicit(self):
        joined = EN.read_text() + IT.read_text() + THEORY.read_text()
        for token in ("A", "B", "C", "D", "P -> GPG^{-1}", "characteristic polynomial", "P_rev=E P^T E", "T_s", "ell0"):
            self.assertIn(token, joined)
        self.assertIn("not established by the source", EN.read_text())
        self.assertIn("non stabiliti dalla fonte", IT.read_text())

    def test_conditional_information_and_no_dead_end_are_bilingual(self):
        self.assertIn("profile-informative", EN.read_text())
        self.assertIn("informativo sul profilo", IT.read_text())
        self.assertIn("not a structural dead end", EN.read_text())
        self.assertIn("non è un vicolo cieco strutturale", IT.read_text())
        for text in (EN.read_text(), IT.read_text(), THEORY.read_text()):
            self.assertNotIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)


if __name__ == "__main__":
    unittest.main()
