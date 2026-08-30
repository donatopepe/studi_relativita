import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-scattering-clock-phase-report-en.md",
    ROOT / "audit/schwarzschild-scattering-clock-phase-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-scattering-clock-phase.md",
]
STATUS = "SCHWARZSCHILD_STATIC_ENDPOINT_CLOCK_PHASE_ADDS_CROSS_CHANNEL_SHAPE_BUT_RETAINS_EXTERNAL_FREQUENCY_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_CLOCK_REALIZATION_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildScatteringClockPhaseReportTests(unittest.TestCase):
    def test_authoritative_contract_is_aligned(self):
        for path in FILES:
            text = path.read_text()
            for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT"):
                self.assertIn(token, text)
            self.assertIn("Phi_clock=nu_s Delta_tau_R/M", text)
            self.assertIn("R_joint=(Phi_clock,P_frequency_converted)", text)
            self.assertIn("(polar,in-plane)", text)

    def test_exact_diagnostics_are_bilingual(self):
        for path in FILES[:2]:
            text = path.read_text()
            for token in ("40.223422979930845", "36.718793510299655", "7.343803420273261", "5.9117155615240335e-12", "rank_shape_boundary=2", "rank_with_log_M=2", "5.730937517383603e-09", "[0,0,1]"):
                self.assertIn(token, text)

    def test_limitations_are_explicit(self):
        for path in FILES:
            text = path.read_text().lower()
            for term in ("source", "absorber", "detector", "covariance", "ell0"):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
