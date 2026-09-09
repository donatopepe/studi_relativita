import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kerr-finite-boundary-endpoint-gate-report-en.md"
IT = ROOT / "audit/kerr-finite-boundary-endpoint-gate-report-it.md"
THEORY = ROOT / "theory/spacetime/kerr-finite-boundary-endpoint-gate.md"
ROADMAP = ROOT / "docs/roadmap.md"
LEDGER = ROOT / "audit/kaluza-klein-reformulation-change-ledger.md"
ARTIFACT = ROOT / "studies/spacetime/kerr-finite-boundary-endpoint-gate-results.json"
RESULT = "KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS_TO_LOCAL_DIRECTION_AND_RELATIVE_FREQUENCY_SHAPE_BUT_WITHOUT_PHYSICAL_ENDPOINT_STANDARDS_OR_SCREEN_TRANSPORT_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_KERR_EMITTER_ABSORBER_WORLDLINES_CLOCKS_AFFINE_FREQUENCY_STANDARD_PARALLEL_SCREEN_JACOBI_PREPARATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED"


class KerrFiniteBoundaryEndpointReportTests(unittest.TestCase):
    def test_bilingual_reports_share_status(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                RESULT, GATE, "8/8", "DIRECT_REVIEW_NO_SUBAGENT",
                "MODEL=KERR_EQUATORIAL_FINITE_BOUNDARY_4D_CONTROL",
                "UMCH=UNPROVEN_SECONDARY_CANDIDATE", "L_identified=false",
                "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED",
                "NO_POSITIVE_DETECTION_CLAIM", "MODEL_LEVEL_KERR_ENDPOINT_CONFORMANCE_NOT_EVIDENCE",
            ):
                self.assertIn(token, text)

    def test_reports_match_artifact_anchor(self):
        self.assertEqual(json.loads(ARTIFACT.read_text())["control_summary"]["controls_passed"], 8)
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                "chi=0.6", "rho=4.5", "R_source/M=12.0", "R_observer/M=12.0",
                "Delta_t_plus/M=33.987089", "Delta_t_minus/M=41.551191",
                "Delta_phi_plus=3.4663312", "Delta_phi_minus=-4.2673873",
                "omega_plus=1.0911117", "omega_minus=1.1004156",
                "orientation_shape_difference=7.7337185", "rank=4",
                "scale_null_direction=[1.0,0.0,0.0,0.0,0.0]",
                "dimensionless_scale_residual=0.0",
            ):
                self.assertIn(token, text)

    def test_theory_preserves_zamo_and_screen_boundary(self):
        text = THEORY.read_text()
        for token in (
            "GrallaLupsasca2020KerrNullGeodesics", "ZAMO",
            "R(r_turn)=0", "r=r_turn+y^2", "local_frequency=-g(k,e_(0))",
            "declared mathematical endpoint observer", "not a physical emitter",
            "parallel screen transport", RESULT, GATE,
        ):
            self.assertIn(token, text)

    def test_roadmap_and_ledger_preserve_prior_results(self):
        for text in (ROADMAP.read_text(), LEDGER.read_text()):
            for token in (
                RESULT, GATE, "8/8", "KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE",
                "DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J",
                "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE", "F_0",
                "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "NO_POSITIVE_DETECTION_CLAIM",
            ):
                self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
