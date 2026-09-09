import importlib.util
import json
import math
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kerr_finite_boundary_endpoint_gate.py"
ARTIFACT = ROOT / "studies/spacetime/kerr-finite-boundary-endpoint-gate-results.json"
SPEC = importlib.util.spec_from_file_location("kerr_endpoint", PATH)
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

M, CHI, RHO, RS, RO = 1.0, 0.6, 4.5, 12.0, 12.0
TOL = 2e-9


def max_abs(value):
    if isinstance(value, dict):
        return max((max_abs(item) for item in value.values()), default=0.0)
    if isinstance(value, (list, tuple)):
        return max((max_abs(item) for item in value), default=0.0)
    return abs(value)


class KerrFiniteBoundaryEndpointControls(unittest.TestCase):
    def test_01_signed_turning_roots_satisfy_radial_potential(self):
        for orientation in (-1, 1):
            record = gate.turning_record(M, CHI, RHO, orientation)
            self.assertLess(abs(record["R_turn_residual"]), 1e-11)
            self.assertTrue(math.isfinite(record["xi_over_M"]))
            self.assertEqual(record["orientation"], orientation)

    def test_02_path_first_integrals_and_convergence(self):
        for orientation in (-1, 1):
            record = gate.path_record(M, CHI, RHO, RS, RO, orientation)
            self.assertGreater(record["Delta_t_over_M"], 0.0)
            self.assertGreater(record["affine_length_over_M"], 0.0)
            self.assertGreater(record["minimum_k_t"], 0.0)
            self.assertGreaterEqual(record["minimum_radial_potential"], -1e-11)
            self.assertEqual(record["radial_signs"], [-1, 1])
            self.assertLess(record["convergence_certificate"]["maximum_residual"], 2e-6)

    def test_03_zamo_tetrads_are_orthonormal(self):
        for orientation in (-1, 1):
            record = gate.path_record(M, CHI, RHO, RS, RO, orientation)
            self.assertLess(record["source_endpoint"]["tetrad_orthonormality_residual"], TOL)
            self.assertLess(record["observer_endpoint"]["tetrad_orthonormality_residual"], TOL)

    def test_04_endpoint_local_null_reconstruction(self):
        for orientation in (-1, 1):
            record = gate.path_record(M, CHI, RHO, RS, RO, orientation)
            for endpoint in (record["source_endpoint"], record["observer_endpoint"]):
                self.assertGreater(endpoint["local_frequency"], 0.0)
                self.assertAlmostEqual(math.sqrt(sum(x * x for x in endpoint["local_direction"])), 1.0, places=10)
                self.assertLess(abs(endpoint["coordinate_null_residual"]), TOL)
                self.assertLess(abs(endpoint["local_null_residual"]), TOL)
                self.assertLess(endpoint["reconstruction_residual"], TOL)

    def test_05_orientation_asymmetry_and_simultaneous_reversal(self):
        control = gate.orientation_control(M, CHI, RHO, RS, RO)
        self.assertGreater(control["fixed_spin_shape_difference"], 1e-3)
        self.assertLess(control["simultaneous_reversal_residual"], TOL)
        self.assertEqual(control["classification"], "KERR_ENDPOINT_ORIENTATION_ASYMMETRY_IS_FRAME_DRAGGING_SHAPE_NOT_ABSOLUTE_SCALE")

    def test_06_schwarzschild_unsigned_collision(self):
        control = gate.schwarzschild_control(M, RHO, RS, RO)
        self.assertLess(control["unsigned_collision_residual"], TOL)
        self.assertLess(control["signed_azimuthal_reversal_residual"], TOL)
        self.assertEqual(control["classification"], "KERR_FINITE_BOUNDARY_ORIENTATION_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_UNSIGNED_RECORD")

    def test_07_joint_dilation_preserves_dimensionless_endpoint_record(self):
        control = gate.scale_control(M, CHI, RHO, RS, RO, orientation=1, scale=2.5)
        self.assertLess(control["dimensionless_record_residual"], TOL)
        self.assertLess(control["dimensional_covariance_residual"], TOL)
        self.assertEqual(control["classification"], "KERR_FINITE_BOUNDARY_ZAMO_RECORD_RETAINS_JOINT_GEOMETRIC_SCALE_NULL")

    def test_08_rank_and_no_ell0_gate(self):
        control = gate.rank_control(CHI, RHO, RS, RO)
        self.assertEqual(control["parameters"], ["log_M", "chi", "rho", "R_source_over_M", "R_observer_over_M"])
        self.assertLess(control["log_M_column_norm"], TOL)
        self.assertEqual(control["scale_null_direction"], [1.0, 0.0, 0.0, 0.0, 0.0])
        self.assertGreaterEqual(control["rank"], 2)
        nonclaims = gate.no_ell0_gate()
        self.assertFalse(nonclaims["ell0_identified"])
        self.assertEqual(nonclaims["L_equals_ell0"], "NOT_DERIVED")
        self.assertEqual(nonclaims["Detection"], "NO_POSITIVE_DETECTION_CLAIM")

    def test_stable_artifact_records_eight_controls_and_raw_contract(self):
        expected = json.loads(ARTIFACT.read_text())
        generated = json.loads(subprocess.check_output(["python", str(PATH)], text=True))
        self.assertEqual(generated, expected)
        summary = expected["control_summary"]
        self.assertEqual(summary["controls_passed"], 8)
        self.assertEqual(summary["controls_total"], 8)
        self.assertEqual(len(summary["controls"]), 8)
        self.assertTrue(all(control["passed"] for control in summary["controls"]))
        self.assertEqual([control["threshold"] for control in summary["controls"]], [1e-11, 2e-6, 2e-9, 2e-9, 2e-9, 2e-9, 2e-9, 2e-9])
        raw = expected["raw_output"]
        for key in (
            "geometry", "turning_record", "path_samples", "Delta_t_over_M", "Delta_phi",
            "affine_length_over_M", "source_ZAMO_tetrad", "observer_ZAMO_tetrad",
            "source_local_frequency", "observer_local_frequency", "source_local_direction",
            "observer_local_direction", "coordinate_null_residual", "local_null_residual",
            "reconstruction_residual", "orientation_control", "Schwarzschild_control",
            "scale_control", "rank_control", "convergence_certificate", "source_scope", "limitations",
        ):
            self.assertIn(key, raw)


if __name__ == "__main__":
    unittest.main()
