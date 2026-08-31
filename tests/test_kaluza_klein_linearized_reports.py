import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kaluza-klein-linearized-report-en.md"
IT = ROOT / "audit/kaluza-klein-linearized-report-it.md"
THEORY = ROOT / "theory/spacetime/kaluza-klein-linearized-tidal.md"

RESULT = "LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE_BUT_UNIFORM_PROFILE_PROJECTION_SOURCE_WINDOW_DEGENERACY_AND_JOINT_5D_DILATION_PREVENT_ABSOLUTE_SCALE_OR_ELL0_IDENTIFICATION"
GATE = "NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"


class KaluzaKleinLinearizedReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_tokens(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (
            RESULT, GATE, "REFORMULATION_CANDIDATE_UNRATIFIED", "UMCH=UNPROVEN_SECONDARY_CANDIDATE",
            "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
            "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM",
            "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE", "DIRECT_REVIEW_NO_SUBAGENT",
            "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE",
        ):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_equations_baseline_and_values_are_aligned(self):
        en, it = EN.read_text(), IT.read_text()
        for token in (
            "M5=R1,3 x S1", "y~y+2*pi*L", "T_ij=partial_i partial_j Phi", "L=1.0", "r=2.0",
            "source_size=0.25", "shell_width=0.3", "T_parallel=-0.74695386", "T_perpendicular=0.25463712",
            "n_used=123", "rank=2", "scale_null_direction=[1.0,0.0,0.0]",
            "dimensionless_point_matrix_residual=0.0", "dimensionless_shell_matrix_residual=0.0",
        ):
            self.assertIn(token, en)
            self.assertIn(token, it)

    def test_theory_classifies_known_project_toy_negative_and_open_scope(self):
        text = THEORY.read_text()
        for token in (
            "KNOWN_RESULT", "PROJECT_DERIVATION", "TOY_CONTROL", "NEGATIVE_RESULT", "OPEN_PROBLEM", "HYPOTHESIS",
            "Liu2003CompactifiedPotential", "FloratosLeontaris1999", "KehagiasSfetsos2000", RESULT, GATE,
            "raw matrix", "not evidence",
        ):
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
