import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_full_jacobi.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-full-jacobi-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_full_jacobi", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveFullJacobiTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_full_map_is_symplectic(self):
        result = self.module.symplectic_control(6000)
        self.assertLess(result["symplectic_residual"], 3e-12)

    def test_reversal_obeys_all_block_reciprocity_identities(self):
        result = self.module.reversal_control(6000)
        for key in ("a_to_dt_residual", "b_to_bt_residual", "c_to_ct_residual", "d_to_at_residual"):
            self.assertLess(result[key], 3e-12, key)

    def test_labelled_endpoint_optical_spectra_are_swapped(self):
        result = self.module.endpoint_optical_control(6000)
        self.assertGreater(result["forward_endpoint_spectrum_difference"], 1e-3)
        self.assertLess(result["reversal_source_to_forward_observer_residual"], 3e-11)
        self.assertLess(result["reversal_observer_to_forward_source_residual"], 3e-11)

    def test_endpoint_swap_quotient_erases_reversal(self):
        result = self.module.endpoint_swap_quotient_control(6000)
        self.assertLess(result["quotient_reversal_residual"], 3e-12)

    def test_affine_profile_rescaling_preserves_dimensionless_full_map(self):
        result = self.module.affine_rescaling_control(0.8, 1.3, 6000)
        self.assertLess(result["dimensionless_full_map_residual"], 3e-11)

    def test_ell0_is_absent(self):
        self.assertEqual(
            "FULL_JACOBI_LABELLED_ENDPOINT_ORIENTATION_CONDITIONAL_AFFINE_SCALE_NOT_ELL0",
            self.module.ell0_gate(["L", "K", "A", "B", "C", "D", "endpoint_labels"]),
        )

    def test_artifact_is_current_and_scoped(self):
        run = subprocess.run(["python3", str(PROGRAM), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        artifact = json.loads(ARTIFACT.read_text())
        self.assertEqual(
            "EXACT_PLANE_WAVE_FULL_JACOBI_LABELLED_ENDPOINT_ORDER_CONDITIONAL_SWAP_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0",
            artifact["status"],
        )
        self.assertEqual("PHYSICAL_ENDPOINT_LABELS_AND_CALIBRATION_NOT_DERIVED", artifact["open_gate"])
        self.assertEqual("NO_POSITIVE_DETECTION_CLAIM", artifact["conclusion"])
        for block in ("A", "B", "C", "D"):
            self.assertIn(block, artifact["raw_forward_blocks"])


if __name__ == "__main__":
    unittest.main()
