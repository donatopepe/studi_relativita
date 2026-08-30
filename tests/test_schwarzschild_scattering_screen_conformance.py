import importlib.util
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "studies" / "spacetime" / "schwarzschild_scattering_screen_conformance.py"
SPEC = importlib.util.spec_from_file_location("schwarzschild_scattering_screen_conformance", MODULE_PATH)
ssc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ssc)


class SchwarzschildScatteringScreenConformanceTests(unittest.TestCase):
    def test_coordinate_ray_and_screen_are_metric_orthonormal(self):
        samples = ssc.screen_transport_control(M=1.0, rho=4.0, R=12.0, orientation=1, n=120)
        self.assertLess(samples["max_null_residual"], 2e-12)
        self.assertLess(samples["max_screen_metric_residual"], 2e-12)
        self.assertLess(samples["max_k_screen_residual"], 2e-12)
        self.assertEqual(samples["screen_handedness"], 1)
        self.assertEqual({row["branch"] for row in samples["checkpoints"]}, {"incoming", "turning", "outgoing"})

    def test_screen_transport_is_parallel_modulo_explicit_null_gauge(self):
        control = ssc.screen_transport_control(M=1.0, rho=4.0, R=12.0, orientation=-1, n=120)
        self.assertLess(control["interior_max_quotient_residual"], 2e-5)
        self.assertLess(control["interior_max_screen_rotation"], 2e-5)
        self.assertGreater(control["interior_max_raw_covariant_derivative"], 1e-4)
        self.assertTrue(any(abs(row["null_gauge_coefficient"][1]) > 1e-4 for row in control["samples"]))
        for row in control["samples"]:
            self.assertEqual(len(row["raw_covariant_derivative"]), 2)
            self.assertEqual(len(row["quotient_covariant_derivative"]), 2)
            self.assertEqual(len(row["screen_rotation"]), 2)

    def test_transport_residual_refines(self):
        coarse = ssc.screen_transport_control(M=1.0, rho=4.0, R=12.0, orientation=1, n=60)
        fine = ssc.screen_transport_control(M=1.0, rho=4.0, R=12.0, orientation=1, n=120)
        self.assertLessEqual(fine["interior_max_quotient_residual"], coarse["interior_max_quotient_residual"] + 1e-10)
        self.assertLessEqual(fine["interior_max_screen_rotation"], coarse["interior_max_screen_rotation"] + 1e-10)
        self.assertGreater(fine["endpoint_max_quotient_residual"], 0.0)

    def test_four_dimensional_riemann_reconstruction_matches_full_profile(self):
        control = ssc.riemann_projection_control(M=1.0, rho=4.0, R=12.0, orientation=1)
        self.assertTrue(control["uses_radial_metric_derivatives"])
        self.assertTrue(control["uses_polar_metric_derivatives"])
        self.assertLess(control["fine_max_profile_mismatch"], 5e-5)
        self.assertLess(control["fine_max_symmetry_residual"], 5e-5)
        self.assertLess(control["fine_max_vacuum_trace_residual"], 5e-5)
        self.assertLess(control["fine_max_profile_mismatch"], control["coarse_max_profile_mismatch"])
        for row in control["fine_checkpoints"]:
            self.assertEqual(len(row["K_fd"]), 2)
            self.assertEqual(len(row["K_fd"][0]), 2)

    def test_riemann_projection_is_orientation_even_but_raw_screen_is_not(self):
        plus = ssc.riemann_projection_control(orientation=1)
        minus = ssc.riemann_projection_control(orientation=-1)
        self.assertLess(ssc.matrix_distance(plus["fine_checkpoints"][1]["K_fd"], minus["fine_checkpoints"][1]["K_fd"]), 5e-5)
        self.assertNotEqual(plus["fine_checkpoints"][0]["screen"], minus["fine_checkpoints"][0]["screen"])

    def test_photon_sphere_profile_anchor(self):
        anchor = ssc.photon_sphere_anchor(rho=3.000001)
        self.assertAlmostEqual(anchor["turning_M2_K_polar"], -1.0 / 3.0, places=6)
        self.assertAlmostEqual(anchor["turning_M2_K_in_plane"], 1.0 / 3.0, places=6)
        self.assertEqual(anchor["limit"], "diag(-1,+1)/3 in (polar,in-plane) order")

    def test_existing_jacobi_profile_uses_corrected_screen_order_and_normalization(self):
        sample = ssc.base.profile_control(M=1.0, rho=4.0, R=12.0, orientation=1, n=24)["samples"][24]
        expected = 3.0 * 1.0 * (ssc.base.sc.turning_beta(4.0)) ** 2 / 4.0 ** 5
        self.assertAlmostEqual(sample["K"][0][0], -expected, places=12)
        self.assertAlmostEqual(sample["K"][1][1], expected, places=12)


if __name__ == "__main__":
    unittest.main()
