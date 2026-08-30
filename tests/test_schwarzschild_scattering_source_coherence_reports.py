import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-scattering-source-coherence-report-en.md",
    ROOT / "audit/schwarzschild-scattering-source-coherence-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-scattering-source-coherence.md",
]
STATUS = "SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildScatteringSourceCoherenceReportTests(unittest.TestCase):
    def test_authoritative_contract_is_aligned(self):
        for path in FILES:
            text = path.read_text()
            for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT"):
                self.assertIn(token, text)
            self.assertIn("R_coherence=(y_coh,V,Phi_clock,P_frequency_converted)", text)
            self.assertIn("V=exp[-(Delta_tau_R/tau_c)^2/2]", text)
            self.assertIn("(polar,in-plane)", text)

    def test_exact_diagnostics_are_bilingual(self):
        for path in FILES[:2]:
            text = path.read_text()
            for token in ("1.6653345369377348e-16", "visibility=2.9462060018828695e-33", "visibility_difference=-0.17770997834344382", "coherence_iq_difference=0.18481837747718158", "converted_phase_map_residual=5.9117155615240335e-12", "rank_raw_with_log_M=2", "rank_quotient_with_log_M=2", "[0,0,1]"):
                self.assertIn(token, text)

    def test_limitations_are_explicit(self):
        for path in FILES:
            text = path.read_text().lower()
            for term in ("spectrum", "coherence dynamics", "emission", "absorption", "polarization", "receiver", "noise", "covariance", "ell0"):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
