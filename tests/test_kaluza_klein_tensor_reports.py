import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kaluza-klein-linearized-tensor-report-en.md"
IT = ROOT / "audit/kaluza-klein-linearized-tensor-report-it.md"
THEORY = ROOT / "theory/spacetime/kaluza-klein-linearized-tensor.md"
ROADMAP = ROOT / "docs/roadmap.md"
LEDGER = ROOT / "audit/kaluza-klein-reformulation-change-ledger.md"
ARTIFACT = ROOT / "studies/spacetime/kaluza-klein-linearized-tensor-results.json"

RESULT = "DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J_BUT_ADDS_COMPACT_INDEX_CURVATURE_WHILE_TENSOR_COMPLETION_REMAINS_SOURCE_DEPENDENT_AND_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_5D_SOURCE_STRESS_LOCALIZATION_DYNAMICS_GAUGE_INVARIANT_OBSERVABLE_RADION_STABILIZATION_COUPLING_CALIBRATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"


class KaluzaKleinTensorReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_tokens(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                RESULT, GATE, "8/8", "DIRECT_REVIEW_NO_SUBAGENT",
                "HIGHER_DIMENSIONAL_GRAVITY_DIRECTION=HUMAN_RATIFIED_RESEARCH_DIRECTION",
                "MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL",
                "UMCH=UNPROVEN_SECONDARY_CANDIDATE", "L_identified=false",
                "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED",
                "NO_POSITIVE_DETECTION_CLAIM", "MODEL_LEVEL_LINEARIZED_TENSOR_CONFORMANCE_NOT_EVIDENCE",
            ):
                self.assertIn(token, text)

    def test_reports_match_artifact_baseline_and_primary_values(self):
        artifact = json.loads(ARTIFACT.read_text())
        self.assertEqual(artifact["control_summary"]["controls_passed"], 8)
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                "L=1.0", "r/L=2.0", "y/L=0.7", "shell_width/L=0.3", "scale_factor=2.5",
                "R_0101=-0.50548011", "R_0202=0.20349714", "R_0404=0.098485837",
                "R_0104=-0.24481889", "shell_R_0101=-0.51149219",
                "point_conformance_residual=0.0", "shell_conformance_residual=0.0",
                "uniform_R_0404=0.0", "uniform_R_1414=-0.125",
                "source_ratio_residual=0.5", "dimensionless_full_curvature_residual=0.0",
            ):
                self.assertIn(token, text)

    def test_theory_note_states_equations_and_uniform_compact_index_caveat(self):
        text = THEORY.read_text()
        for token in (
            "h_00=-2 Phi", "h_11=h_22=h_33=h_44=-Phi",
            "R_0i0j=partial_i partial_j Phi",
            "R_i4j4", "ordinary-space derivatives", "exact uniform zero mode",
            "Robinson2006Normalization", "AtondoRubio2008Linearized5D",
            "equations (21)-(23)", "must not be imported", RESULT, GATE,
        ):
            self.assertIn(token, text)

    def test_roadmap_and_ledger_preserve_prior_results_and_record_tensor_gate(self):
        roadmap, ledger = ROADMAP.read_text(), LEDGER.read_text()
        for text in (roadmap, ledger):
            for token in (
                RESULT, GATE, "8/8", "F_0", "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE",
                "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "NO_POSITIVE_DETECTION_CLAIM",
            ):
                self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
