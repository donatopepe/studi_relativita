import cmath
import importlib.util
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kaluza_klein_finite_s1_localization.py"
SPEC = importlib.util.spec_from_file_location("kk_finite_s1", PATH)
kk = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kk)

RESULT = "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE_BUT_STATIC_RESPONSE_IDENTIFIES_ONLY_COMBINED_WIDTH_AND_EVEN_PERIODIC_SEPARATION_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"


def midpoint_integral(function, start, stop, n=8000):
    step = (stop - start) / n
    return step * sum(function(start + (index + 0.5) * step) for index in range(n))


class FiniteS1LocalizationControls(unittest.TestCase):
    def test_01_wrapped_profiles_are_normalized_across_boundary(self):
        L = 1.0
        for width, center in ((0.2, 0.0), (0.45, 2.0 * math.pi - 0.08), (1.5, 1.7)):
            value = midpoint_integral(lambda y: kk.wrapped_density(y, center, width, L), 0.0, 2.0 * math.pi * L)
            self.assertLess(abs(value - 1.0), 2e-8)

    def test_02_direct_quadrature_matches_analytic_complex_coefficients(self):
        L, width, center = 1.2, 0.37, 0.81
        circumference = 2.0 * math.pi * L
        for n in range(4):
            direct = midpoint_integral(
                lambda y: kk.wrapped_density(y, center, width, L) * cmath.exp(-1j * n * y / L),
                0.0,
                circumference,
            )
            analytic = kk.mode_coefficient("wrapped_gaussian", n, L, center=center, width=width)
            self.assertLess(abs(direct - analytic), 3e-8)

    def test_03_zero_width_limit_recovers_localized_response(self):
        finite = kk.point_response(r=2.0, L=1.0, w_s=1e-5, w_p=1e-5, delta_y=0.4)
        localized = kk.point_response(r=2.0, L=1.0, source_profile="localized", probe_profile="localized", delta_y=0.4)
        self.assertLess(kk.matrix_residual(finite["T_point_matrix"], localized["T_point_matrix"]), 2e-8)
        self.assertTrue(finite["convergence_certificate"]["converged"])

    def test_04_broad_finite_profile_approaches_but_is_not_exact_uniform(self):
        broad = kk.point_response(r=2.0, L=1.0, w_s=5.0, w_p=0.3)
        uniform = kk.point_response(r=2.0, L=1.0, source_profile="uniform", probe_profile="wrapped_gaussian", w_p=0.3)
        self.assertLess(kk.matrix_residual(broad["T_point_matrix"], uniform["T_point_matrix"]), 2e-5)
        self.assertNotEqual(broad["source_profile"], "uniform")
        self.assertEqual(broad["broad_width_classification"], "BROAD_WRAPPED_GAUSSIAN_APPROACHES_ZERO_MODE_BUT_FINITE_WIDTH_IS_NOT_EXACT_UNIFORM")
        exact = kk.mode_records(5, 1.0, source_profile="uniform", probe_profile="wrapped_gaussian", w_p=0.3)
        self.assertEqual([record["static_real_mode_weight"] for record in exact[1:]], [0.0] * 5)

    def test_05_periodicity_preserves_complete_static_record(self):
        first = kk.point_response(r=1.7, L=0.9, w_s=0.2, w_p=0.35, delta_y=0.44)
        periodic = kk.point_response(r=1.7, L=0.9, w_s=0.2, w_p=0.35, delta_y=0.44 + 2.0 * math.pi * 0.9)
        self.assertLess(kk.matrix_residual(first["T_point_matrix"], periodic["T_point_matrix"]), 2e-12)
        for left, right in zip(first["mode_records"], periodic["mode_records"]):
            self.assertLess(abs(complex(*left["combined_complex_overlap"]) - complex(*right["combined_complex_overlap"])), 2e-12)

    def test_06_orientation_reversal_conjugates_complex_record_but_collides_statically(self):
        positive = kk.point_response(r=1.8, L=1.0, w_s=0.25, w_p=0.4, delta_y=0.7)
        negative = kk.point_response(r=1.8, L=1.0, w_s=0.25, w_p=0.4, delta_y=-0.7)
        for left, right in zip(positive["mode_records"], negative["mode_records"]):
            self.assertLess(abs(complex(*left["combined_complex_overlap"]).conjugate() - complex(*right["combined_complex_overlap"])), 2e-12)
            self.assertAlmostEqual(left["static_real_mode_weight"], right["static_real_mode_weight"], places=12)
        self.assertLess(kk.matrix_residual(positive["T_point_matrix"], negative["T_point_matrix"]), 2e-12)
        self.assertEqual(positive["orientation_classification"], "S1_RELATIVE_ORIENTATION_SIGN_COLLISION_IN_STATIC_REAL_RESPONSE_NOT_COMPACTIFICATION_SCALE")

    def test_07_source_probe_exchange_conjugates_overlap_and_preserves_static_matrix(self):
        original = kk.point_response(r=1.9, L=1.1, w_s=0.2, w_p=0.5, delta_y=0.6)
        exchanged = kk.point_response(r=1.9, L=1.1, w_s=0.5, w_p=0.2, delta_y=-0.6)
        for left, right in zip(original["mode_records"], exchanged["mode_records"]):
            self.assertLess(abs(complex(*left["combined_complex_overlap"]).conjugate() - complex(*right["combined_complex_overlap"])), 2e-12)
        self.assertLess(kk.matrix_residual(original["T_point_matrix"], exchanged["T_point_matrix"]), 2e-12)

    def test_08_equal_combined_width_pairs_collide_for_point_and_shell(self):
        alpha_s, alpha_p = 0.25, 0.4
        other_s = 0.1
        other_p = math.sqrt(alpha_s**2 + alpha_p**2 - other_s**2)
        first = kk.point_response(r=2.0, L=1.0, w_s=alpha_s, w_p=alpha_p, delta_y=0.7)
        second = kk.point_response(r=2.0, L=1.0, w_s=other_s, w_p=other_p, delta_y=0.7)
        self.assertLess(kk.matrix_residual(first["T_point_matrix"], second["T_point_matrix"]), 2e-12)
        shell_first = kk.radial_shell_response(2.0, 0.3, 1.0, alpha_s, alpha_p, 0.7)
        shell_second = kk.radial_shell_response(2.0, 0.3, 1.0, other_s, other_p, 0.7)
        self.assertLess(kk.matrix_residual(shell_first["T_shell_matrix"], shell_second["T_shell_matrix"]), 2e-12)
        self.assertEqual(first["width_classification"], "SOURCE_PROBE_LOCALIZATION_WIDTHS_COLLIDE_UNDER_COMBINED_MODE_OVERLAP")

    def test_09_joint_dilation_and_zero_shell_width_conform(self):
        control = kk.geometric_scale_control(scale=2.5, L=1.0, r=2.0, shell_width=0.3, w_s=0.25, w_p=0.4, delta_y=0.7)
        self.assertLess(control["dimensionless_point_matrix_residual"], 2e-11)
        self.assertLess(control["dimensionless_shell_matrix_residual"], 2e-9)
        self.assertEqual(control["classification"], "JOINT_5D_LOCALIZATION_GEOMETRIC_DILATION_NOT_ABSOLUTE_SCALE")
        shell = kk.radial_shell_response(2.0, 0.002, 1.0, 0.25, 0.4, 0.7, n=120)
        point = kk.point_response(2.0, 1.0, 0.25, 0.4, 0.7)
        self.assertLess(kk.matrix_residual(shell["T_shell_matrix"], point["T_point_matrix"]), 2e-5)

    def test_10_rank_nulls_global_collisions_and_metric_gate(self):
        rank = kk.rank_control(alpha_s=0.25, alpha_p=0.4, theta=0.7)
        self.assertEqual(rank["rank"], 2)
        self.assertLess(rank["absolute_scale_null_residual"], 2e-8)
        self.assertLess(rank["combined_width_tangent_null_residual"], 2e-8)
        self.assertEqual(rank["absolute_scale_null"], [1.0, 0.0, 0.0, 0.0])
        self.assertEqual(rank["combined_width_tangent_null"], [0.0, 0.4, -0.25, 0.0])
        summary = kk.ten_control_summary()
        self.assertEqual(summary["controls_passed"], 10)
        self.assertEqual(summary["controls_total"], 10)
        self.assertEqual(summary["metric"], "10/10")
        self.assertEqual(summary["result"], RESULT)
        self.assertFalse(summary["L_identified"])
        self.assertFalse(summary["ell0_identified"])
        self.assertEqual(summary["L_equals_ell0"], "NOT_DERIVED")
        self.assertFalse(summary["extra_dimension_detected"])
        self.assertEqual(summary["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(summary["Detection"], "NO_POSITIVE_DETECTION_CLAIM")


if __name__ == "__main__":
    unittest.main()
