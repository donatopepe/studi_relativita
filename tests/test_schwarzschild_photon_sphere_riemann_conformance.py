import importlib.util
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE = ROOT / "studies/spacetime/schwarzschild_photon_sphere_riemann_conformance.py"
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-photon-sphere-riemann-conformance-results.json"


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

    def test_full_riemann_projection_refines_and_confirms_legacy_profile(self):
        result = self.m.full_riemann_control(M=1.0, coarse_step=4e-4, fine_step=1e-4)
        self.assertLess(result["fine_projection_mismatch"], result["coarse_projection_mismatch"])
        self.assertLess(result["fine_projection_mismatch"], 5e-8)
        self.assertLess(result["symmetry_residual"], 1e-9)
        self.assertLess(result["vacuum_trace_residual"], 1e-8)
        self.assertLess(result["legacy_profile_mismatch"], 5e-8)
        self.assertEqual(result["legacy_profile_status"], "CONFIRMED_AFTER_EXPLICIT_SCREEN_ORDER_AND_AFFINE_NORMALIZATION")

    def test_scattering_limit_requires_affine_frequency_conversion(self):
        result = self.m.affine_normalization_control(M=1.0)
        self.assertAlmostEqual(result["scattering_to_circular_frequency_ratio"], 3.0 ** 0.5, places=12)
        self.assertAlmostEqual(result["tidal_matrix_quadratic_ratio"], 3.0, places=12)
        self.assertLess(result["converted_profile_residual"], 1e-12)
        self.assertGreater(result["unconverted_profile_residual"], 0.2)
        self.assertEqual(result["naive_comparison_status"], "FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON")

    def test_projection_computes_both_channels_not_trace_inference(self):
        result = self.m.full_riemann_control(M=1.0)
        self.assertEqual(result["derivative_coordinates"], ["r", "theta"])
        self.assertEqual(result["polar_channel_origin"], "DIRECT_RIEMANN_PROJECTION")
        self.assertEqual(result["radial_channel_origin"], "DIRECT_RIEMANN_PROJECTION")
        self.assertAlmostEqual(result["K_analytic"][0][0], -1.0 / 9.0, places=12)
        self.assertAlmostEqual(result["K_analytic"][1][1], 1.0 / 9.0, places=12)

    def test_result_preserves_negative_identifiability_and_history(self):
        result = self.m.build_result()
        self.assertEqual(result["status"], "SCHWARZSCHILD_PHOTON_SPHERE_FULL_RIEMANN_CONFIRMS_LEGACY_PROFILE_AFTER_SCREEN_ORDER_AND_AFFINE_NORMALIZATION_NOT_ELL0")
        self.assertEqual(result["naive_cross_control"], "FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON")
        self.assertEqual(result["legacy_result"], "CONFIRMED_NOT_FALSIFIED")
        self.assertEqual(result["scattering_result"], "CONFIRMED_AFTER_AFFINE_FREQUENCY_CONVERSION")
        self.assertFalse(result["ell0_identified"])
        self.assertEqual(result["detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(result["review"], "DIRECT_REVIEW_NO_SUBAGENT")

    def test_artifact_is_current(self):
        expected = self.m.build_result()
        self.assertEqual(json.loads(ARTIFACT.read_text()), expected)
        subprocess.run([sys.executable, str(MODULE), "--check"], cwd=ROOT, check=True)


if __name__ == "__main__":
    unittest.main()
