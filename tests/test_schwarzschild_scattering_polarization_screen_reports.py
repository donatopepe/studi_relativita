import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-scattering-polarization-screen-report-en.md",
    ROOT / "audit/schwarzschild-scattering-polarization-screen-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-scattering-polarization-screen.md",
]
STATUS = "SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildScatteringPolarizationScreenReportTests(unittest.TestCase):
    def test_authoritative_contract_is_aligned(self):
        for path in FILES:
            text = path.read_text()
            for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT"):
                self.assertIn(token, text)
            self.assertIn("R_polarization=(j_R,J_R,Phi_clock,P_frequency_converted)", text)
            self.assertIn("j_s=(cos psi_s,exp(i delta_s) sin psi_s)", text)
            self.assertIn("(polar,in-plane)", text)
            self.assertIn("4x4", text)

    def test_exact_diagnostics_are_bilingual(self):
        for path in FILES[:2]:
            text = path.read_text()
            for token in ("max_interior_raw_covariant_derivative=0.1767889727337515", "max_interior_screen_quotient_residual=1.9939515283841326e-05", "coherency_determinant_abs=2.7755575615628914e-17", "power_difference=0.5145493419909759", "converted_phase_map_residual=5.9117155615240335e-12", "rank_raw_with_log_M=2", "rank_quotient_with_log_M=2", "[0,0,1]"):
                self.assertIn(token, text)

    def test_limitations_are_explicit(self):
        for path in FILES:
            text = path.read_text().lower()
            for term in ("source polarization", "emission", "absorption", "screen preparation", "receiver", "noise", "covariance", "ell0"):
                self.assertIn(term, text)
            self.assertTrue("basis" in text and "physical" in text)


if __name__ == "__main__":
    unittest.main()
