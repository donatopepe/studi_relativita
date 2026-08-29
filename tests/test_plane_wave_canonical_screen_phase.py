import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_canonical_screen_phase.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-canonical-screen-phase-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_canonical_screen_phase", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CanonicalScreenPhaseTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_zero_connection_collapses_velocity_and_canonical_maps(self):
        result = self.module.zero_connection_control(n=5000)
        self.assertLess(result["velocity_canonical_residual"], 3e-12)
        self.assertLess(result["canonical_inertial_residual"], 3e-12)

    def test_canonical_generator_matches_endpoint_and_velocity_conversion(self):
        result = self.module.canonical_equivalence_control(n=5000)
        self.assertLess(result["direct_endpoint_residual"], 3e-10)
        self.assertLess(result["velocity_conversion_residual"], 3e-10)

    def test_standard_symplecticity_requires_canonical_variables(self):
        result = self.module.symplectic_structure_control(n=5000)
        self.assertLess(result["canonical_standard_residual"], 3e-10)
        self.assertGreater(result["velocity_standard_residual"], 1e-2)
        self.assertLess(result["velocity_pulled_back_residual"], 3e-10)

    def test_velocity_and_canonical_characteristics_differ(self):
        result = self.module.spectral_counterexample(n=5000)
        self.assertGreater(result["characteristic_difference"], 1e-2)
        self.assertEqual(result["disposition"], "VELOCITY_CHARACTERISTIC_NOT_CANONICAL_SCREEN_INVARIANT")

    def test_endpoint_angular_velocity_moves_only_velocity_diagnostic(self):
        result = self.module.endpoint_calibration_mobility_control(n=5000)
        self.assertEqual(result["canonical_map_difference"], 0.0)
        self.assertGreater(result["velocity_map_difference"], 1e-2)
        self.assertGreater(result["velocity_characteristic_difference"], 1e-3)

    def test_common_basis_and_affine_orbit(self):
        common = self.module.common_basis_control(n=5000)
        affine = self.module.affine_orbit_control(n=5000)
        self.assertLess(common["map_similarity_residual"], 3e-10)
        self.assertLess(common["characteristic_residual"], 3e-10)
        self.assertLess(affine["map_scaling_residual"], 5e-10)
        self.assertLess(affine["characteristic_residual"], 5e-10)

    def test_deterministic_artifact_and_gate(self):
        self.assertEqual(self.module.ell0_gate(["K", "Q", "A", "x", "p", "P_c", "L"]), "CANONICAL_SCREEN_PHASE_AFFINE_ORBIT_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_ROTATING_SCREEN_VELOCITY_SPECTRUM_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_MAP_AFFINE_SCALE_BLIND_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_SCREEN_CANONICAL_MOMENTUM_ENDPOINT_ANGULAR_VELOCITY_AND_UNIT_CALIBRATION_NOT_DERIVED")
        self.assertFalse(data["structural_dead_end"])
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")


if __name__ == "__main__":
    unittest.main()
