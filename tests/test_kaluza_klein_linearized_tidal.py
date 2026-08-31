import importlib.util
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kaluza_klein_linearized_tidal.py"
SPEC = importlib.util.spec_from_file_location("kk_tidal", PATH)
kk = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kk)

NULL_PROJECTION = "UNIFORM_S1_SOURCE_OR_PROBE_PROJECTS_NONZERO_KK_MODES_NOT_ABSENCE_OF_EXTRA_DIMENSION"


class KaluzaKleinCircleAndPointTidalTests(unittest.TestCase):
    def test_domain_rejects_nonpositive_scale_and_singular_radius(self):
        with self.assertRaises(ValueError):
            kk.point_response(r=1.0, L=0.0)
        with self.assertRaises(ValueError):
            kk.point_response(r=0.0, L=1.0)

    def test_circle_mode_weights_preserve_relative_position(self):
        weights = kk.circle_mode_weights("localized", "localized", n_max=3, delta_y=0.4, L=2.0)
        self.assertEqual(weights[0], 1.0)
        self.assertAlmostEqual(weights[1], math.cos(0.2))
        self.assertAlmostEqual(weights[2], math.cos(0.4))
        self.assertAlmostEqual(weights[3], math.cos(0.6))

    def test_uniform_source_or_probe_projects_nonzero_modes(self):
        for source, probe in (("localized", "uniform"), ("uniform", "localized"), ("uniform", "uniform")):
            control = kk.circle_projection_control(source, probe, n_max=8, delta_y=0.3, L=1.2)
            self.assertEqual(control["weights"][0], 1.0)
            self.assertEqual(control["weights"][1:], [0.0] * 8)
            self.assertEqual(control["classification"], NULL_PROJECTION)

    def test_mode_sum_matches_exact_same_circle_shape(self):
        for x in (0.35, 1.0, 4.0):
            exact = kk.point_shape_exact(r=x, L=1.0, delta_y=0.0)
            summed = kk.point_shape_modes(r=x, L=1.0, delta_y=0.0, n_max=200)
            self.assertLess(abs(exact - summed), 1e-10)

    def test_point_tidal_matrix_is_symmetric_and_reconstructs(self):
        result = kk.point_response(r=1.3, L=0.7, direction=(1.0, 2.0, -1.0))
        matrix = result["T_matrix"]
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(matrix[i][j], matrix[j][i], places=12)
        self.assertLess(result["reconstruction_residual"], 1e-12)
        self.assertEqual(result["primary_object"], "FULL_SPATIAL_TIDAL_HESSIAN")

    def test_long_distance_recovers_four_dimensional_shape(self):
        control = kk.asymptotic_control(r=20.0, L=1.0)
        self.assertLess(control["long_distance_relative_residual"], 1e-6)

    def test_short_distance_recovers_inverse_square_potential_shape(self):
        control = kk.asymptotic_control(r=0.01, L=1.0)
        self.assertLess(control["short_distance_scaled_residual"], 3e-5)

    def test_tower_convergence_is_certified(self):
        control = kk.convergence_control(r=0.2, L=1.0, delta_y=0.0, tolerance=1e-9)
        self.assertTrue(control["converged"])
        self.assertLess(control["residual"], 1e-9)
        self.assertGreater(control["n_used"], 5)


class KaluzaKleinFiniteSourceTests(unittest.TestCase):
    def test_source_profiles_are_normalized_with_declared_width(self):
        sphere = kk.source_profile_control("uniform_sphere", size=0.4)
        gaussian = kk.source_profile_control("gaussian", size=0.4)
        self.assertLess(abs(sphere["normalization"] - 1.0), 1e-8)
        self.assertLess(abs(gaussian["normalization"] - 1.0), 1e-8)
        self.assertEqual(gaussian["width_convention"], "ONE_DIMENSIONAL_COMPONENT_STANDARD_DEVIATION_SIGMA")

    def test_uniform_circle_finite_sources_remain_zero_mode_only(self):
        for profile in ("uniform_sphere", "gaussian"):
            result = kk.finite_source_response(r=2.0, L=1.0, source_profile_3d=profile, source_size=0.3,
                                               source_S1_profile="uniform", probe_S1_profile="localized")
            point = kk.point_response(r=2.0, L=1.0, source_profile="uniform", probe_profile="localized")
            self.assertLess(kk.matrix_residual(result["T_matrix"], point["T_matrix"]), 2e-5)
            self.assertEqual(result["circle_projection"]["classification"], NULL_PROJECTION)

    def test_finite_sources_converge_to_point_source(self):
        point = kk.point_response(r=1.5, L=0.8)
        sphere = kk.finite_source_response(r=1.5, L=0.8, source_profile_3d="uniform_sphere", source_size=0.01)
        gaussian = kk.finite_source_response(r=1.5, L=0.8, source_profile_3d="gaussian", source_size=0.01)
        self.assertLess(kk.matrix_residual(sphere["T_matrix"], point["T_matrix"]), 2e-3)
        self.assertLess(kk.matrix_residual(gaussian["T_matrix"], point["T_matrix"]), 2e-3)

    def test_finite_size_changes_localized_kk_shape(self):
        small = kk.finite_source_response(r=1.4, L=1.0, source_profile_3d="gaussian", source_size=0.1)
        large = kk.finite_source_response(r=1.4, L=1.0, source_profile_3d="gaussian", source_size=0.5)
        self.assertGreater(kk.matrix_residual(small["T_matrix"], large["T_matrix"]), 1e-4)
        self.assertEqual(large["classification"], "SOURCE_PROFILE_AND_WINDOW_SHAPE_ARE_PREPARATION_NUISANCES_NOT_INTRINSIC_GEOMETRY")

    def test_quadrature_refinement_is_certified(self):
        result = kk.finite_source_response(r=1.8, L=0.9, source_profile_3d="uniform_sphere", source_size=0.35)
        self.assertTrue(result["quadrature_certificate"]["converged"])
        self.assertLess(result["quadrature_certificate"]["residual"], 3e-4)


class KaluzaKleinFiniteWindowTests(unittest.TestCase):
    def test_radial_shell_zero_window_recovers_pointwise_matrix(self):
        point = kk.point_response(r=2.0, L=0.8)
        shell = kk.radial_shell_window(r_center=2.0, width=0.002, L=0.8, n=80)
        self.assertLess(kk.matrix_residual(shell["T_window_matrix"], point["T_matrix"]), 2e-5)
        self.assertEqual(shell["window_family"], "radial_shell")
        self.assertAlmostEqual(shell["kernel_normalization"], 1.0)

    def test_radial_shell_rejects_singular_support(self):
        with self.assertRaises(ValueError):
            kk.radial_shell_window(r_center=0.2, width=0.5, L=1.0)

    def test_oriented_region_matrix_is_symmetric(self):
        region = kk.oriented_box_window(center=(2.0, 0.0, 0.0), dimensions=(0.4, 0.2, 0.1), L=0.9,
                                        angle=0.3, n_per_axis=6)
        matrix = region["T_window_matrix"]
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(matrix[i][j], matrix[j][i], places=12)
        self.assertEqual(region["transport_convention"], "FLAT_BACKGROUND_CARTESIAN_IDENTITY")

    def test_oriented_region_is_rotation_covariant(self):
        base = kk.oriented_box_window(center=(2.0, 0.0, 0.0), dimensions=(0.5, 0.2, 0.1), L=1.0,
                                      angle=0.0, n_per_axis=7)
        rotated = kk.oriented_box_window(center=(0.0, 2.0, 0.0), dimensions=(0.5, 0.2, 0.1), L=1.0,
                                         angle=math.pi / 2.0, n_per_axis=7)
        expected = kk.rotate_matrix_z(base["T_window_matrix"], math.pi / 2.0)
        self.assertLess(kk.matrix_residual(rotated["T_window_matrix"], expected), 2e-10)

    def test_oriented_region_zero_window_recovers_pointwise_matrix(self):
        region = kk.oriented_box_window(center=(2.0, 0.0, 0.0), dimensions=(0.002, 0.001, 0.001), L=0.8,
                                        angle=0.4, n_per_axis=5)
        point = kk.point_response(r=2.0, L=0.8)
        self.assertLess(kk.matrix_residual(region["T_window_matrix"], point["T_matrix"]), 2e-5)


if __name__ == "__main__":
    unittest.main()
