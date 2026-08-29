import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_joint_common_spectrum.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-joint-common-spectrum-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_joint_common_spectrum", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveJointCommonSpectrumTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_top_hat_joint_object_collides_under_affine_profile_orbit(self):
        result = self.module.joint_scale_orbit_control("top_hat", n=5000)
        self.assertLess(result["dimensionless_window_residual"], 4e-11)
        self.assertLess(result["characteristic_residual"], 5e-11)
        self.assertLess(result["canonical_similarity_residual"], 5e-11)

    def test_triangular_joint_object_collides_under_affine_profile_orbit(self):
        result = self.module.joint_scale_orbit_control("triangular", n=5000)
        self.assertLess(result["dimensionless_window_residual"], 4e-11)
        self.assertLess(result["characteristic_residual"], 5e-11)

    def test_raw_blocks_follow_declared_dimensions(self):
        result = self.module.block_scaling_control(n=5000)
        for residual in result["residuals"].values():
            self.assertLess(residual, 5e-11)

    def test_joint_object_retains_conditional_profile_information(self):
        result = self.module.profile_sensitivity_control(n=5000)
        self.assertGreater(result["window_difference"], 1e-3)
        self.assertGreater(result["characteristic_difference"], 1e-3)

    def test_same_joint_landmark_has_arbitrarily_rescaled_coordinate(self):
        result = self.module.landmark_reparameterization_control(n=5000)
        self.assertAlmostEqual(result["scaled_coordinate"] / result["base_coordinate"], result["scale_factor"], places=12)
        self.assertLess(result["joint_residual"], 7e-11)
        self.assertEqual(result["interpretation"], "JOINT_LANDMARK_COORDINATE_PROFILE_SCALE_MOVABLE_NOT_ELL0")

    def test_ell0_is_absent_and_artifact_is_deterministic(self):
        self.assertEqual(self.module.ell0_gate(["W", "P", "K", "L", "G", "w"]), "JOINT_AFFINE_PROFILE_ORBIT_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
