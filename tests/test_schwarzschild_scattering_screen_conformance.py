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


if __name__ == "__main__":
    unittest.main()
