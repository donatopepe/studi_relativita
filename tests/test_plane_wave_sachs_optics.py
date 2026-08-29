import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_sachs_optics.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-sachs-optics-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_sachs_optics", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveSachsOpticsTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_optical_matrix_is_connection_derived_and_twist_free(self):
        result = self.module.optical_decomposition_control(n=6000)
        self.assertGreater(result["minimum_abs_det_b"], 1e-3)
        self.assertLess(abs(result["twist"]), 2e-12)
        self.assertGreater(result["shear_norm"], 1e-3)

    def test_optical_matrix_satisfies_riccati_equation(self):
        result = self.module.riccati_control(n=5000)
        self.assertLess(result["residual"], 2e-5)

    def test_common_screen_rotation_preserves_scalar_invariants(self):
        result = self.module.rotation_control(n=6000)
        self.assertLess(result["matrix_action_residual"], 3e-12)
        self.assertLess(result["expansion_residual"], 3e-12)
        self.assertLess(result["shear_norm_residual"], 3e-12)
        self.assertLess(result["twist_residual"], 3e-12)

    def test_observer_canonical_shear_moves_expansion_and_shear_not_twist(self):
        result = self.module.calibration_mobility_control(n=6000)
        self.assertLess(result["additive_action_residual"], 3e-12)
        self.assertGreater(result["expansion_shift"], 1e-2)
        self.assertGreater(result["shear_norm_shift"], 1e-2)
        self.assertLess(result["twist_shift"], 3e-12)

    def test_caustic_guard_rejects_singular_vertex_block(self):
        result = self.module.caustic_guard_control()
        self.assertEqual(result["status"], "CAUSTIC_OR_VERTEX_BLOCK_SINGULAR")

    def test_reversal_exchanges_labelled_endpoint_optics(self):
        result = self.module.reversal_exchange_control(n=6000)
        self.assertLess(result["source_observer_exchange_residual"], 5e-11)

    def test_affine_scaling_preserves_dimensionless_optics(self):
        result = self.module.affine_scaling_control(n=6000)
        self.assertLess(result["dimensionless_matrix_residual"], 5e-11)
        self.assertLess(result["dimensionless_scalar_residual"], 5e-11)

    def test_ell0_is_absent_and_artifact_is_deterministic(self):
        self.assertEqual(self.module.ell0_gate(["B", "D", "S", "K", "L", "H", "Q"]), "SACHS_CALIBRATION_AND_AFFINE_SCALE_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_SACHS_EXPANSION_SHEAR_CALIBRATION_MOVABLE_TWIST_ZERO_AFFINE_SCALE_BLIND_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_SACHS_ENDPOINT_CALIBRATION_TWIST_SOURCE_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
