import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_sachs_twist_boundary.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-sachs-twist-boundary-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_sachs_twist_boundary", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveSachsTwistBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_nonvertex_boundary_generates_endpoint_twist(self):
        result = self.module.nonvertex_control(n=6000)
        self.assertGreater(abs(result["endpoint"]["twist"]), 1e-2)
        self.assertGreater(result["minimum_abs_det_x"], 1e-2)

    def test_twist_area_product_is_conserved(self):
        result = self.module.twist_area_control(n=6000)
        self.assertLess(result["maximum_residual"], 2e-10)

    def test_boundary_twist_moves_endpoint_twist_at_fixed_profile(self):
        result = self.module.boundary_mobility_control(n=6000)
        self.assertGreater(result["endpoint_twist_difference"], 2e-2)
        self.assertEqual(result["profile_difference"], 0.0)

    def test_orientation_quotient_controls_twist_sign(self):
        result = self.module.orientation_control(n=6000)
        self.assertLess(result["so2_twist_residual"], 3e-12)
        self.assertLess(result["o2_sign_flip_residual"], 3e-12)

    def test_affine_profile_orbit_preserves_dimensionless_raw_optics(self):
        result = self.module.affine_orbit_control(n=6000)
        self.assertLess(result["dimensionless_X_residual"], 5e-11)
        self.assertLess(result["dimensionless_LV_residual"], 5e-11)
        self.assertLess(result["dimensionless_LS_residual"], 5e-11)
        self.assertLess(result["twist_area_residual"], 5e-11)

    def test_profile_sensitivity_remains_conditional(self):
        result = self.module.profile_sensitivity_control(n=6000)
        self.assertGreater(result["raw_endpoint_difference"], 1e-3)

    def test_caustic_guard_and_ell0_gate(self):
        self.assertEqual(self.module.caustic_guard_control()["status"], "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR")
        self.assertEqual(self.module.ell0_gate(["X", "V", "S", "K", "L", "S0", "Q"]), "NONVERTEX_TWIST_BOUNDARY_AND_AFFINE_SCALE_NOT_ELL0")

    def test_artifact_is_deterministic_and_nonconfirmatory(self):
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_NONVERTEX_TWIST_BOUNDARY_PROPAGATED_ORIENTATION_AND_AFFINE_SCALE_CONDITIONAL_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_ROTATING_CONGRUENCE_BOUNDARY_PARITY_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
