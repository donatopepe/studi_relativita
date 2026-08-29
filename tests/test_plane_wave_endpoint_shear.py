import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_endpoint_shear.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-endpoint-shear-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_endpoint_shear", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveEndpointShearTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_endpoint_shears_are_symplectic_and_keep_labels(self):
        result = self.module.symplectic_shear_control()
        self.assertLess(result["source_shear_symplectic_residual"], 1e-14)
        self.assertLess(result["observer_shear_symplectic_residual"], 1e-14)
        self.assertEqual(result["endpoint_labels"], ["source", "observer"])

    def test_direct_map_matches_exact_block_action(self):
        result = self.module.block_action_control(6000)
        for key in ("A", "B", "C", "D"):
            self.assertLess(result[f"{key.lower()}_formula_residual"], 2e-13, key)
        self.assertLess(result["b_unchanged_residual"], 2e-13)
        self.assertLess(result["calibrated_map_symplectic_residual"], 2e-12)

    def test_optical_matrices_follow_additive_endpoint_nuisance(self):
        result = self.module.optical_additive_control(6000)
        self.assertLess(result["source_additive_residual"], 2e-13)
        self.assertLess(result["observer_additive_residual"], 2e-13)

    def test_general_shears_move_endpoint_spectra_and_gaps(self):
        result = self.module.spectral_mobility_control(6000)
        self.assertGreater(result["source_spectrum_shift"], 0.1)
        self.assertGreater(result["observer_spectrum_shift"], 0.1)
        self.assertGreater(result["source_gap_shift"], 0.05)
        self.assertGreater(result["observer_gap_shift"], 0.05)

    def test_scalar_shears_shift_spectra_but_preserve_gaps(self):
        result = self.module.scalar_shear_control(6000)
        self.assertGreater(result["source_spectrum_shift"], 0.1)
        self.assertGreater(result["observer_spectrum_shift"], 0.1)
        self.assertLess(result["source_gap_residual"], 2e-13)
        self.assertLess(result["observer_gap_residual"], 2e-13)

    def test_affine_scale_and_ell0_gates_remain_negative(self):
        result = self.module.affine_rescaling_control(6000)
        self.assertLess(result["dimensionless_calibrated_map_residual"], 5e-11)
        self.assertEqual(
            self.module.ell0_gate(["A", "B", "C", "D", "Hs", "Ho", "L"]),
            "LABELLED_ENDPOINT_SHEAR_CALIBRATION_NONIDENTIFIABLE_AFFINE_SCALE_NOT_ELL0",
        )

    def test_artifact_is_deterministic_and_scoped(self):
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
