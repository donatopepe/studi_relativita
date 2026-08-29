import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_covariant_screen_phase.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-covariant-screen-phase-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_covariant_screen_phase", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CovariantScreenPhaseTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_zero_connection_collapses_all_maps(self):
        result = self.module.zero_connection_control(n=5000)
        self.assertLess(result["covariant_vs_inertial_residual"], 3e-12)
        self.assertLess(result["naive_vs_inertial_residual"], 3e-12)

    def test_direct_generator_matches_endpoint_graph_law(self):
        result = self.module.endpoint_graph_control(n=5000)
        self.assertLess(result["phase_map_residual"], 3e-10)

    def test_naive_conjugated_profile_is_not_rotating_phase_map(self):
        result = self.module.naive_counterexample(n=5000)
        self.assertGreater(result["raw_map_difference"], 1e-2)
        self.assertGreater(result["characteristic_difference"], 1e-4)
        self.assertEqual(result["disposition"], "NAIVE_CONJUGATED_PROFILE_MAP_NOT_ROTATING_COORDINATE_PROPAGATOR")

    def test_common_basis_and_anchor_covariance(self):
        common = self.module.common_basis_control(n=5000)
        anchor = self.module.right_anchor_control(n=5000)
        self.assertLess(common["map_similarity_residual"], 3e-10)
        self.assertLess(common["characteristic_residual"], 3e-10)
        self.assertLess(anchor["map_similarity_residual"], 3e-10)
        self.assertLess(anchor["characteristic_residual"], 3e-10)

    def test_affine_profile_connection_orbit_remains_scale_blind(self):
        result = self.module.affine_orbit_control(n=5000)
        self.assertLess(result["endpoint_graph_scaling_residual"], 5e-10)
        self.assertLess(result["characteristic_residual"], 5e-10)

    def test_deterministic_artifact_and_ell0_gate(self):
        self.assertEqual(self.module.ell0_gate(["K", "omega", "A", "G", "P", "L"]), "COVARIANT_SCREEN_PHASE_MAP_AFFINE_ORBIT_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_ROTATING_SCREEN_CONNECTION_TERMS_REQUIRED_NAIVE_TRANSPORTED_JACOBI_MAP_SUPERSEDED_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_SCREEN_CONNECTION_ENDPOINT_ANGULAR_VELOCITY_AND_DETECTOR_PHASE_VARIABLES_NOT_DERIVED")
        self.assertFalse(data["structural_dead_end"])
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")


if __name__ == "__main__":
    unittest.main()
