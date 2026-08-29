import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_screen_transport.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-screen-transport-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_screen_transport", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveScreenTransportTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_zero_connection_collapses_orderings(self):
        result = self.module.zero_connection_control(n=5000)
        self.assertLess(result["window_residual"], 2e-13)
        self.assertLess(result["map_residual"], 2e-12)

    def test_nonconstant_connection_makes_orderings_differ(self):
        result = self.module.order_control(n=5000)
        self.assertGreater(result["window_difference"], 1e-3)
        self.assertGreater(result["map_difference"], 1e-3)
        self.assertGreater(result["characteristic_difference"], 1e-5)

    def test_pointwise_invariants_preserved_but_insufficient(self):
        result = self.module.invariant_average_control(n=5000)
        self.assertLess(result["pointwise_max_residual"], 2e-12)
        self.assertLess(result["average_invariant_residual"], 2e-12)
        self.assertGreater(result["transported_window_vs_invariant_reconstruction_gap"], 1e-3)
        self.assertGreater(result["transported_map_vs_invariant_reconstruction_gap"], 1e-3)

    def test_common_screen_basis_covariance(self):
        result = self.module.common_basis_control(n=5000)
        self.assertLess(result["window_conjugation_residual"], 2e-11)
        self.assertLess(result["map_similarity_residual"], 2e-10)
        self.assertLess(result["characteristic_residual"], 2e-10)

    def test_affine_profile_connection_orbit_is_scale_blind(self):
        for kernel in ("top_hat", "triangular"):
            result = self.module.affine_orbit_control(kernel=kernel, n=5000)
            self.assertLess(result["dimensionless_window_residual"], 3e-11)
            self.assertLess(result["characteristic_residual"], 3e-10)

    def test_transport_profile_moves_outputs_at_fixed_curvature(self):
        result = self.module.transport_profile_mobility_control(n=5000)
        self.assertEqual(result["curvature_profile_difference"], 0.0)
        self.assertGreater(result["window_difference"], 1e-3)
        self.assertGreater(result["map_difference"], 1e-3)

    def test_ell0_absent_and_artifact_deterministic(self):
        self.assertEqual(self.module.ell0_gate(["K", "omega", "Q", "W", "P", "L"]), "SCREEN_TRANSPORT_WINDOW_JACOBI_PROTOCOL_AND_AFFINE_NOT_ELL0")
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_SCREEN_TRANSPORT_AVERAGE_ORDER_OPERATOR_AND_JACOBI_PROTOCOL_DEPENDENT_AFFINE_SCALE_BLIND_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_SCREEN_CONNECTION_PATH_KERNEL_AND_COMMON_ENDPOINT_STANDARD_NOT_DERIVED")
        self.assertFalse(data["structural_dead_end"])
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")


if __name__ == "__main__":
    unittest.main()
