import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kaluza-klein-finite-s1-localization-report-en.md"
IT = ROOT / "audit/kaluza-klein-finite-s1-localization-report-it.md"
THEORY = ROOT / "theory/spacetime/kaluza-klein-finite-s1-localization.md"
ROADMAP = ROOT / "docs/roadmap.md"

RESULT = "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE_BUT_STATIC_RESPONSE_IDENTIFIES_ONLY_COMBINED_WIDTH_AND_EVEN_PERIODIC_SEPARATION_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_5D_LOCALIZATION_DYNAMICS_GAUGE_FIXED_TENSOR_COUPLING_RADION_STABILIZATION_SOURCE_PROBE_PREPARATION_PHASE_SENSITIVE_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"


class FiniteS1ReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_tokens(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (
            RESULT, GATE, "10/10", "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
            "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM",
            "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT",
            "BROAD_WRAPPED_GAUSSIAN_APPROACHES_ZERO_MODE_BUT_FINITE_WIDTH_IS_NOT_EXACT_UNIFORM",
            "S1_RELATIVE_ORIENTATION_SIGN_COLLISION_IN_STATIC_REAL_RESPONSE_NOT_COMPACTIFICATION_SCALE",
            "SOURCE_PROBE_LOCALIZATION_WIDTHS_COLLIDE_UNDER_COMBINED_MODE_OVERLAP",
            "JOINT_5D_LOCALIZATION_GEOMETRIC_DILATION_NOT_ABSOLUTE_SCALE",
        ):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_baseline_values_are_identical(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (
            "L=1.0", "r_over_L=2.0", "shell_width_over_L=0.3", "alpha_s=0.25", "alpha_p=0.4", "theta=0.7",
            "equal_u_pair=[0.1,0.46097722]", "T_parallel=-0.48757452", "T_perpendicular=0.19602073",
            "T_shell_parallel=-0.4940744", "T_shell_perpendicular=0.1988726", "rank=2",
            "absolute_scale_null=[1.0,0.0,0.0,0.0]", "combined_width_tangent_null=[0.0,0.4,-0.25,0.0]",
            "dimensionless_point_matrix_residual=0.0", "dimensionless_shell_matrix_residual=0.0",
        ):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_theory_and_roadmap_preserve_source_scope_and_old_result(self):
        text = THEORY.read_text()
        for token in ("KNOWN_RESULT", "PROJECT_DERIVATION", "TOY_CONTROL", "NEGATIVE_RESULT", "OPEN_PROBLEM", "HYPOTHESIS",
                      "NISTDLMF", "raw complex", "static real", RESULT, GATE, "not evidence", "F_0"):
            self.assertIn(token, text)
        roadmap = ROADMAP.read_text()
        self.assertIn(RESULT, roadmap)
        self.assertIn("LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE", roadmap)


if __name__ == "__main__":
    unittest.main()
