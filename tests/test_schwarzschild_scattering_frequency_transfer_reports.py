import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/schwarzschild-scattering-frequency-transfer-report-en.md"
IT = ROOT / "audit/schwarzschild-scattering-frequency-transfer-report-it.md"
THEORY = ROOT / "theory/spacetime/schwarzschild-scattering-frequency-transfer.md"
STATUS = "SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildScatteringFrequencyTransferReportTests(unittest.TestCase):
    def test_bilingual_reports_preserve_authoritative_contract(self):
        for path in (EN, IT):
            text = path.read_text()
            for token in (
                STATUS,
                GATE,
                "DIRECT_REVIEW_NO_SUBAGENT",
                "UMCH=UNPROVEN",
                "ell0_identified=false",
                "structural_dead_end=NOT_DECLARED",
                "NO_POSITIVE_DETECTION_CLAIM",
                "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
                "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE",
            ):
                self.assertIn(token, text)
            self.assertIn("omega(r)=E_infinity/sqrt(1-2M/r)", text)
            self.assertIn("P_a=D_a P_1 D_a^-1", text)
            self.assertIn("diag(-1,+1) 3 M b^2/r^5", text)

    def test_reports_match_deterministic_values(self):
        en = EN.read_text()
        it = IT.read_text()
        for token in (
            "0.18257418583505539",
            "0.03333333333333334",
            "2.842170943040401e-14",
            "[0,0,1]",
            "rank_shape_boundary=2",
            "rank_with_log_M=2",
        ):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_theory_preserves_raw_object_and_bounded_scope(self):
        text = THEORY.read_text()
        for token in (
            STATUS,
            GATE,
            "FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY",
            "TOY_EXTERNAL_FREQUENCY_STANDARD_NOT_DETECTOR_DERIVED",
            "ell0_identified=false",
            "structural_dead_end=NOT_DECLARED",
        ):
            self.assertIn(token, text)
        self.assertIn("not an interior geometric scale", text.lower())


if __name__ == "__main__":
    unittest.main()
