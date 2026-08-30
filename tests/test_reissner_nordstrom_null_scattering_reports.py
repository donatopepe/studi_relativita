import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
STATUS = "REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE_BUT_Q_SQUARED_DEGENERACY_AND_JOINT_MQ_DILATION_RETAIN_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_CHARGE_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class ReissnerNordstromNullScatteringReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_tokens(self):
        en = (ROOT / "audit/reissner-nordstrom-null-scattering-jacobi-report-en.md").read_text()
        it = (ROOT / "audit/reissner-nordstrom-null-scattering-jacobi-report-it.md").read_text()
        for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED",
                      "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
                      "Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0", "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
                      "DIRECT_REVIEW_NO_SUBAGENT"):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_equations_baseline_and_limits_are_aligned(self):
        en = (ROOT / "audit/reissner-nordstrom-null-scattering-jacobi-report-en.md").read_text()
        it = (ROOT / "audit/reissner-nordstrom-null-scattering-jacobi-report-it.md").read_text()
        for token in ("f(r)=1-2M/r+Q^2/r^2", "epsilon=Q/M", "rho=4", "R=12", "epsilon=0.8",
                      "beta=5.4433105", "maximum_abs_Ricci_trace=0.0092592465", "rank_with_log_M_and_epsilon=1",
                      "scale_null_direction=[1,0]", "phase_map_residual=8.0925039e-06"):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_theory_and_roadmap_preserve_negative_scope(self):
        theory = (ROOT / "theory/spacetime/reissner-nordstrom-null-scattering-jacobi.md").read_text()
        roadmap = (ROOT / "docs/roadmap.md").read_text()
        for token in (STATUS, GATE, "Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0"):
            self.assertIn(token, theory)
            self.assertIn(token, roadmap)
        self.assertIn("full `4x4` phase map", theory)
        self.assertIn("not `ell0`", theory)


if __name__ == "__main__":
    unittest.main()
