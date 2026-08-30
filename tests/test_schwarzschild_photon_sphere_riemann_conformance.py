import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE = ROOT / "studies/spacetime/schwarzschild_photon_sphere_riemann_conformance.py"


def load():
    spec = importlib.util.spec_from_file_location("schwarzschild_photon_sphere_riemann_conformance", MODULE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class SchwarzschildPhotonSphereRiemannConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load()

    def test_explicit_circular_screen_and_tangent_are_orthonormal_and_null(self):
        result = self.m.circular_screen_control(M=1.0, orientation=1)
        self.assertEqual(result["screen_order"], ["polar", "radial"])
        self.assertLess(result["null_residual"], 1e-13)
        self.assertLess(result["screen_metric_residual"], 1e-13)
        self.assertLess(result["screen_tangent_residual"], 1e-13)

    def test_full_riemann_projection_refines_and_falsifies_legacy_profile(self):
        result = self.m.full_riemann_control(M=1.0, coarse_step=4e-4, fine_step=1e-4)
        self.assertLess(result["fine_projection_mismatch"], result["coarse_projection_mismatch"])
        self.assertLess(result["fine_projection_mismatch"], 5e-8)
        self.assertLess(result["symmetry_residual"], 1e-9)
        self.assertLess(result["vacuum_trace_residual"], 1e-8)
        self.assertGreater(result["legacy_profile_mismatch"], 0.2)
        self.assertEqual(result["legacy_profile_status"], "FALSIFIED_BY_FULL_FOUR_DIMENSIONAL_RIEMANN_PROJECTION")

    def test_projection_computes_both_channels_not_trace_inference(self):
        result = self.m.full_riemann_control(M=1.0)
        self.assertEqual(result["derivative_coordinates"], ["r", "theta"])
        self.assertEqual(result["polar_channel_origin"], "DIRECT_RIEMANN_PROJECTION")
        self.assertEqual(result["radial_channel_origin"], "DIRECT_RIEMANN_PROJECTION")
        self.assertAlmostEqual(result["K_analytic"][0][0], -1.0 / 9.0, places=12)
        self.assertAlmostEqual(result["K_analytic"][1][1], 1.0 / 9.0, places=12)


if __name__ == "__main__":
    unittest.main()
