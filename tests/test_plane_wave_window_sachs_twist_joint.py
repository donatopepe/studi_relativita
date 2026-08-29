import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_window_sachs_twist_joint.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-window-sachs-twist-joint-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_window_sachs_twist_joint", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveWindowSachsTwistJointTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_top_hat_and_triangular_full_joint_affine_collisions(self):
        for kernel in ("top_hat", "triangular"):
            result = self.module.affine_joint_control(kernel=kernel, n=6000)
            for key in ("LW", "X", "LV", "LS", "LS0"):
                self.assertLess(result["residuals"][key], 5e-11, (kernel, key))

    def test_boundary_mobility_leaves_window_fixed(self):
        result = self.module.boundary_mobility_control(n=6000)
        self.assertLess(result["window_residual"], 1e-14)
        self.assertGreater(result["sachs_joint_difference"], 1e-2)
        self.assertGreater(result["endpoint_twist_difference"], 2e-2)

    def test_landmark_coordinate_moves_with_identical_full_joint_object(self):
        result = self.module.landmark_reparameterization_control(n=6000)
        self.assertNotEqual(result["base_coordinate"], result["scaled_coordinate"])
        self.assertLess(result["full_joint_residual"], 8e-11)

    def test_profile_shape_remains_conditionally_informative(self):
        result = self.module.profile_sensitivity_control(n=6000)
        self.assertGreater(result["window_difference"], 1e-3)
        self.assertGreater(result["sachs_difference"], 1e-3)

    def test_ell0_absent_and_artifact_deterministic(self):
        self.assertEqual(self.module.ell0_gate(["W", "X", "V", "S", "S0", "K", "L"]), "WINDOW_SACHS_TWIST_JOINT_AFFINE_AND_BOUNDARY_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_WINDOW_SACHS_TWIST_JOINT_PROFILE_AND_BOUNDARY_CONDITIONAL_AFFINE_ORBIT_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_CAUSAL_WINDOW_ROTATING_BOUNDARY_COMMON_SCREEN_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
