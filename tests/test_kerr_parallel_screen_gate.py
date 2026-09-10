import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kerr_parallel_screen_gate.py"
ARTIFACT = ROOT / "studies/spacetime/kerr-parallel-screen-gate-results.json"
SPEC = importlib.util.spec_from_file_location("kerr_screen", PATH)
screen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(screen)

M, CHI, RHO, RS, RO = 1.0, 0.6, 4.5, 12.0, 12.0
TOL = 2e-8


class KerrParallelScreenControls(unittest.TestCase):
    def test_01_connection_is_torsion_free_and_metric_compatible(self):
        for r in (4.5, 7.0, 12.0):
            record = screen.connection_control(M, CHI, r)
            self.assertLess(record["lower_index_symmetry_residual"], 2e-10)
            self.assertLess(record["metric_compatibility_residual"], 2e-10)

    def test_02_transported_tangent_matches_analytic_geodesic(self):
        for orientation in (-1, 1):
            record = screen.transport_record(M, CHI, RHO, RS, RO, orientation)
            self.assertLess(record["geodesic_tangent_residual"], TOL)

    def test_03_parallel_screen_preserves_orthonormality_and_transversality(self):
        for orientation in (-1, 1):
            record = screen.transport_record(M, CHI, RHO, RS, RO, orientation)
            self.assertLess(record["screen_orthonormality_residual"], TOL)
            self.assertLess(record["screen_transversality_residual"], TOL)

    def test_04_endpoint_map_is_proper_orthogonal_and_converged(self):
        for endpoints in ((12.0, 12.0), (12.0, 15.0)):
            record = screen.transport_record(M, CHI, RHO, *endpoints, orientation=1)
            self.assertLess(record["quotient_orthogonality_residual"], TOL)
            self.assertAlmostEqual(record["quotient_determinant"], 1.0, delta=TOL)
            self.assertLess(record["convergence_certificate"]["maximum_residual"], TOL)

    def test_05_reverse_transport_composes_to_identity(self):
        for orientation in (-1, 1):
            record = screen.reversal_control(M, CHI, RHO, RS, 15.0, orientation)
            self.assertLess(record["screen_roundtrip_residual"], TOL)
            self.assertLess(record["quotient_inverse_residual"], TOL)

    def test_06_orientation_convention_and_equatorial_collision(self):
        record = screen.orientation_control(M, CHI, RHO, RS, 15.0)
        self.assertGreater(record["fixed_spin_path_label_difference"], 1e-3)
        self.assertLess(record["simultaneous_reversal_residual"], TOL)
        self.assertLess(record["equatorial_screen_quotient_collision_residual"], TOL)
        self.assertEqual(record["classification"], "KERR_EQUATORIAL_SCREEN_QUOTIENT_COLLIDES_WHILE_PATH_ORIENTATION_LABELS_DIFFER")

    def test_07_schwarzschild_reflection_control(self):
        record = screen.schwarzschild_control(M, RHO, RS, 15.0)
        self.assertLess(record["unsigned_invariant_residual"], TOL)
        self.assertLess(record["screen_map_reflection_residual"], TOL)

    def test_08_scale_rank_and_no_ell0(self):
        scale = screen.scale_control(M, CHI, RHO, RS, 15.0, 1, 2.5)
        self.assertLess(scale["dimensionless_screen_residual"], TOL)
        rank = screen.rank_control(CHI, RHO, RS, 15.0)
        self.assertLess(rank["log_M_column_norm"], TOL)
        self.assertEqual(rank["scale_null_direction"], [1.0, 0.0, 0.0, 0.0, 0.0])
        gate = screen.no_ell0_gate()
        self.assertFalse(gate["ell0_identified"])
        self.assertEqual(gate["Detection"], "NO_POSITIVE_DETECTION_CLAIM")

    def test_stable_artifact_has_eight_controls(self):
        expected = json.loads(ARTIFACT.read_text())
        generated = json.loads(subprocess.check_output(["python", str(PATH)], text=True))
        self.assertEqual(generated, expected)
        summary = expected["control_summary"]
        self.assertEqual(summary["controls_passed"], 8)
        self.assertEqual(summary["controls_total"], 8)
        self.assertTrue(all(control["passed"] for control in summary["controls"]))
        self.assertEqual([control["threshold"] for control in summary["controls"]], [2e-10, 2e-8, 2e-8, 2e-8, 2e-8, 2e-8, 2e-8, 2e-8])
        for key in ("equal_endpoint", "unequal_endpoint", "reversal_control", "orientation_control", "Schwarzschild_control", "scale_control", "rank_control", "source_scope", "limitations"):
            self.assertIn(key, expected["raw_output"])


if __name__ == "__main__":
    unittest.main()
