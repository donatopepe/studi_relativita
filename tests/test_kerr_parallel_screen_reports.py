import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kerr-parallel-screen-gate-report-en.md"
IT = ROOT / "audit/kerr-parallel-screen-gate-report-it.md"
THEORY = ROOT / "theory/spacetime/kerr-parallel-screen-gate.md"
ROADMAP = ROOT / "docs/roadmap.md"
LEDGER = ROOT / "audit/kaluza-klein-reformulation-change-ledger.md"
ARTIFACT = ROOT / "studies/spacetime/kerr-parallel-screen-gate-results.json"
RESULT = "KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT_IS_METRIC_COMPATIBLE_BUT_ENDPOINT_SCREEN_QUOTIENT_COLLIDES_UNDER_EQUATORIAL_SYMMETRY_WHILE_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_KERR_SCREEN_PREPARATION_POLARIZATION_SOURCE_ANALYZER_JACOBI_TIDAL_MAP_CAUSTICS_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED"


class KerrParallelScreenReportTests(unittest.TestCase):
    def test_bilingual_reports_share_result_and_nonclaims(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (RESULT, GATE, "8/8", "DIRECT_REVIEW_NO_SUBAGENT", "UMCH=UNPROVEN_SECONDARY_CANDIDATE", "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED", "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED", "NO_POSITIVE_DETECTION_CLAIM", "MODEL_LEVEL_KERR_PARALLEL_SCREEN_CONFORMANCE_NOT_EVIDENCE"):
                self.assertIn(token, text)

    def test_reports_match_identity_collision_artifact(self):
        self.assertEqual(json.loads(ARTIFACT.read_text())["control_summary"]["controls_passed"], 8)
        for text in (EN.read_text(), IT.read_text()):
            for token in ("equal_Q=[[1.0,0.0],[0.0,1.0]]", "unequal_Q=[[1.0,0.0],[0.0,1.0]]", "screen_quotient_rank=0", "path_orientation_difference=7.7337185", "geodesic_residual=0.0", "screen_residual=0.0", "scale_residual=0.0", "scale_null_direction=[1.0,0.0,0.0,0.0,0.0]"):
                self.assertIn(token, text)

    def test_theory_explains_collision_and_next_solution(self):
        text = THEORY.read_text()
        for token in ("Dolan2018GeometricalOptics", "GrallaLupsasca2020KerrNullGeodesics", "s_1=e_theta", "s_2=n_phi e_r-n_r e_phi", "equatorial symmetry", "not a detector Jones matrix", "Jacobi tidal map", RESULT, GATE):
            self.assertIn(token, text)

    def test_roadmap_and_ledger_preserve_previous_chain(self):
        for text in (ROADMAP.read_text(), LEDGER.read_text()):
            for token in (RESULT, GATE, "KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS", "KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE", "DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J", "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE", "F_0"):
                self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
