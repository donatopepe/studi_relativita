import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-scattering-coherent-readout-report-en.md",
    ROOT / "audit/schwarzschild-scattering-coherent-readout-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-scattering-coherent-readout.md",
]
STATUS = "SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildScatteringCoherentReadoutReportTests(unittest.TestCase):
    def test_authoritative_contract_is_aligned(self):
        for path in FILES:
            text = path.read_text()
            for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT"):
                self.assertIn(token, text)
            self.assertIn("R_readout=(y_IQ,Phi_clock,P_frequency_converted)", text)
            self.assertIn("relative phase=Phi_clock+phi_s-phi_LO", text)
            self.assertIn("(polar,in-plane)", text)

    def test_exact_diagnostics_are_bilingual(self):
        for path in FILES[:2]:
            text = path.read_text()
            for token in ("1.8457457784393227e-15", "nuisance_jacobian_rank=2", "5.9117155615240335e-12", "iq_difference=1.1246427723525296", "rank_raw_with_log_M=2", "rank_quotient_with_log_M=2", "[0,0,1]"):
                self.assertIn(token, text)

    def test_limitations_are_explicit(self):
        for path in FILES:
            text = path.read_text().lower()
            for term in ("coherence", "emission", "absorption", "receiver", "covariance", "ell0"):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
