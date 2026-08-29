import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_sachs_shear_transfer.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-sachs-shear-transfer-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_sachs_shear_transfer", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveSachsShearTransferTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_source_shear_is_absorbed_by_boundary_graph(self):
        result = self.module.source_absorption_control(n=6000)
        self.assertLess(result["X_residual"], 2e-12)
        self.assertLess(result["V_residual"], 2e-12)
        self.assertLess(result["S_residual"], 2e-12)
        self.assertLess(result["graph_residual"], 2e-12)

    def test_observer_shear_moves_symmetric_optics_not_twist(self):
        result = self.module.observer_shift_control(n=6000)
        self.assertLess(result["X_residual"], 2e-12)
        self.assertLess(result["V_shift_residual"], 2e-12)
        self.assertLess(result["S_shift_residual"], 2e-12)
        self.assertGreater(abs(result["expansion_shift"]), 1e-2)
        self.assertGreater(abs(result["shear_norm_shift"]), 1e-2)
        self.assertLess(abs(result["twist_shift"]), 2e-12)

    def test_uncompensated_source_shear_changes_endpoint(self):
        result = self.module.uncompensated_source_control(n=6000)
        self.assertGreater(result["X_difference"], 1e-2)
        self.assertGreater(result["V_difference"], 1e-2)
        self.assertGreater(result["S_difference"], 1e-2)

    def test_affine_profile_orbit_preserves_dimensionless_transfer(self):
        result = self.module.affine_transfer_control(n=6000)
        for key, residual in result["residuals"].items():
            self.assertLess(residual, 8e-11, key)

    def test_profile_sensitivity_and_caustic_guard(self):
        result = self.module.profile_sensitivity_control(n=6000)
        self.assertGreater(result["raw_difference"], 1e-2)
        self.assertEqual(self.module.caustic_guard_control()["status"], "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR")

    def test_ell0_absent_and_artifact_deterministic(self):
        self.assertEqual(self.module.ell0_gate(["P", "X", "V", "S", "S0", "Hs", "Ho", "K", "L"]), "SACHS_SHEAR_TRANSFER_BOUNDARY_AND_AFFINE_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_SACHS_SOURCE_SHEAR_ABSORBED_BY_BOUNDARY_OBSERVER_SHEAR_MOVES_OPTICS_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_SACHS_SOURCE_BOUNDARY_AND_OBSERVER_CALIBRATION_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
