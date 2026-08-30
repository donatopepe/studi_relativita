import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
STATUS = "KOTTLER_LAMBDA_ADDS_STATIC_BOUNDARY_NORMALIZATION_BUT_NULL_RICCI_FOCUSING_AND_CONVERTED_NULL_JACOBI_SHAPE_CANCEL_WHILE_JOINT_MLAMBDA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_COSMOLOGICAL_MATCHING_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"

class KottlerNullScatteringReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_tokens(self):
        en = (ROOT / "audit/kottler-null-scattering-jacobi-report-en.md").read_text()
        it = (ROOT / "audit/kottler-null-scattering-jacobi-report-it.md").read_text()
        for token in (STATUS, GATE, "UMCH=UNPROVEN", "ell0_identified=false", "structural_dead_end=NOT_DECLARED",
                      "NO_POSITIVE_DETECTION_CLAIM", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
                      "NULL_RICCI_FOCUSING_IN_EINSTEIN_SPACE_NOT_ZERO_SPACETIME_RICCI",
                      "FIXED_EXTERNAL_LAMBDA_IS_IMPORTED_DIMENSIONAL_STANDARD_NOT_ELL0",
                      "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE", "DIRECT_REVIEW_NO_SUBAGENT"):
            self.assertIn(token, en); self.assertIn(token, it)

    def test_equations_baseline_and_controls_are_aligned(self):
        en = (ROOT / "audit/kottler-null-scattering-jacobi-report-en.md").read_text()
        it = (ROOT / "audit/kottler-null-scattering-jacobi-report-it.md").read_text()
        for token in ("f(r)=1-2M/r-Lambda*r^2/3", "alpha=Lambda*M^2", "u''+u=3M*u^2", "rho=4", "R=8",
                      "alpha=0.003", "beta=5.7495957", "maximum_abs_null_Ricci_trace=0.0",
                      "rank_with_log_M_and_alpha=0", "scale_null_direction=[1,0]", "phase_map_residual=1.0249681e-05"):
            self.assertIn(token, en); self.assertIn(token, it)

    def test_theory_and_roadmap_preserve_negative_scope(self):
        theory = (ROOT / "theory/spacetime/kottler-null-scattering-jacobi.md").read_text()
        roadmap = (ROOT / "docs/roadmap.md").read_text()
        for token in (STATUS, GATE, "ell0_identified=false", "NO_POSITIVE_DETECTION_CLAIM"):
            self.assertIn(token, theory); self.assertIn(token, roadmap)
        self.assertIn("RindlerIshak2007", theory)
        self.assertIn("not an asymptotically measured impact parameter", theory)

if __name__ == "__main__": unittest.main()
