import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_common_anchor.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-common-anchor-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_common_anchor", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveCommonAnchorTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_reversal_flips_nonzero_handed_statistic(self):
        result = self.module.reversal_handedness_control(6000)
        self.assertGreater(abs(result["forward_handed_statistic"]), 1e-5)
        self.assertLess(result["reversal_sign_residual"], 2e-9)

    def test_common_oriented_rotations_preserve_statistic(self):
        result = self.module.common_rotation_control(6000)
        self.assertLess(result["maximum_rotation_residual"], 2e-12)

    def test_common_reflection_flips_statistic(self):
        result = self.module.reflection_control(6000)
        self.assertLess(result["reflection_sign_residual"], 2e-12)

    def test_independent_endpoint_frames_remove_transpose_difference(self):
        result = self.module.endpoint_equivalence_control(6000)
        self.assertLess(result["transpose_orbit_residual"], 2e-12)

    def test_affine_rescaling_preserves_dimensionless_handed_statistic(self):
        result = self.module.affine_rescaling_control(0.8, 1.3, 6000)
        self.assertLess(result["dimensionless_handed_residual"], 2e-9)

    def test_ell0_is_absent(self):
        self.assertEqual(
            "ORIENTED_PROFILE_REVERSAL_CONDITIONAL_ABSOLUTE_SCALE_NOT_ELL0",
            self.module.ell0_gate(["L", "K", "B", "common_anchor", "handedness"]),
        )

    def test_artifact_is_current_and_scoped(self):
        run = subprocess.run(
            ["python3", str(PROGRAM), "--check"], cwd=ROOT, text=True, capture_output=True
        )
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        artifact = json.loads(ARTIFACT.read_text())
        self.assertEqual(
            "EXACT_PLANE_WAVE_COMMON_ORIENTED_ANCHOR_RECOVERS_REVERSAL_SIGN_CONDITIONALLY_NOT_ELL0",
            artifact["status"],
        )
        self.assertEqual("PHYSICAL_ORIENTED_ENDPOINT_ANCHOR_NOT_DERIVED", artifact["open_gate"])
        self.assertEqual("NO_POSITIVE_DETECTION_CLAIM", artifact["conclusion"])


if __name__ == "__main__":
    unittest.main()
