import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_joint_quotient.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-joint-quotient-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_joint_quotient", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveJointQuotientTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_reversal_keeps_centered_window(self):
        result = self.module.reversal_control(6000)
        self.assertLess(result["window_reversal_residual"], 2e-10)

    def test_reversal_transposes_vertex_block(self):
        result = self.module.reversal_control(6000)
        self.assertLess(result["jacobi_transpose_residual"], 2e-9)

    def test_raw_vertex_block_retains_order(self):
        result = self.module.reversal_control(6000)
        self.assertGreater(result["raw_jacobi_reversal_residual"], 1e-5)

    def test_individual_quotient_invariants_are_reversal_blind(self):
        result = self.module.reversal_control(6000)
        self.assertLess(result["window_eigenvalue_residual"], 2e-10)
        self.assertLess(result["jacobi_singular_value_residual"], 2e-9)
        self.assertLess(result["jacobi_determinant_residual"], 2e-9)
        self.assertLess(result["jacobi_frobenius_residual"], 2e-9)

    def test_affine_rescaling_preserves_dimensionless_joint_quotient(self):
        result = self.module.affine_rescaling_control(0.8, 1.3, 6000)
        self.assertLess(result["dimensionless_window_spectrum_residual"], 2e-9)
        self.assertLess(result["dimensionless_jacobi_singular_value_residual"], 2e-9)

    def test_ell0_is_absent(self):
        self.assertEqual(
            "JOINT_QUOTIENT_PROFILE_ORDER_AND_ABSOLUTE_SCALE_NOT_ELL0",
            self.module.ell0_gate(["L", "K", "W", "B", "endpoint_frames", "affine_scale"]),
        )

    def test_artifact_is_current_and_scoped(self):
        run = subprocess.run(
            ["python3", str(PROGRAM), "--check"], cwd=ROOT, text=True, capture_output=True
        )
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        artifact = json.loads(ARTIFACT.read_text())
        self.assertEqual(
            "EXACT_PLANE_WAVE_JOINT_QUOTIENT_REVERSAL_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0",
            artifact["status"],
        )
        self.assertEqual("NO_POSITIVE_DETECTION_CLAIM", artifact["conclusion"])
        self.assertEqual("COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN", artifact["open_route"])


if __name__ == "__main__":
    unittest.main()
