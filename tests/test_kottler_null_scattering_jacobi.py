import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
P = ROOT / "studies/spacetime/kottler_null_scattering_jacobi.py"
S = importlib.util.spec_from_file_location("kottler_jacobi", P)
k = importlib.util.module_from_spec(S)
S.loader.exec_module(k)

class KottlerNullScatteringJacobiTests(unittest.TestCase):
    def test_domain_requires_static_patch_and_noncritical_turning_point(self):
        with self.assertRaises(ValueError):
            k.profile_control(alpha=0.03, rho=3, R=8, n=30)
        with self.assertRaises(ValueError):
            k.profile_control(alpha=0.03, rho=4, R=12, n=30)
        c = k.profile_control(alpha=0.003, rho=4, R=8, n=35)
        self.assertEqual(c["branches"], ["incoming", "turning", "outgoing"])
        self.assertEqual(c["screen_order"], ["polar", "in-plane"])
        self.assertGreater(len(c["samples"]), 50)

    def test_direct_curvature_record_separates_ricci_from_null_focusing(self):
        c = k.profile_control(alpha=0.003, rho=4, R=8, n=40)
        self.assertGreater(c["maximum_abs_spacetime_Ricci_component"], 1e-6)
        self.assertLess(c["maximum_abs_null_Ricci_trace"], 3e-5)
        self.assertLess(c["maximum_K_symmetry_residual"], 1e-9)
        self.assertLess(c["maximum_screen_residual"], 2e-8)
        self.assertEqual(c["ricci_classification"], "NULL_RICCI_FOCUSING_IN_EINSTEIN_SPACE_NOT_ZERO_SPACETIME_RICCI")

    def test_direct_projection_matches_declared_profile(self):
        c = k.phase_control(alpha=0.003, rho=4, R=8, n=45)
        self.assertLess(c["conformance"]["path_residual"], 1e-12)
        self.assertLess(c["conformance"]["profile_residual"], 4e-5)
        self.assertLess(c["conformance"]["phase_map_residual"], 3e-4)

    def test_schwarzschild_limit_matches_existing_control(self):
        c = k.schwarzschild_limit_control(rho=4, R=8, n=45)
        self.assertLess(c["path_residual"], 1e-11)
        self.assertLess(c["profile_residual"], 4e-5)
        self.assertLess(c["phase_map_residual"], 3e-4)

    def test_pure_de_sitter_null_focusing_is_zero_analytic_control(self):
        c = k.pure_de_sitter_control(Lambda=0.01)
        self.assertGreater(c["maximum_abs_spacetime_Ricci_component"], 0)
        self.assertEqual(c["null_Ricci_contraction"], 0.0)
        self.assertEqual(c["optical_matrix"], [[0.0, 0.0], [0.0, 0.0]])
        self.assertEqual(c["classification"], "PURE_DE_SITTER_NULL_OPTICAL_TIDAL_MATRIX_ZERO_NOT_FLAT_SPACETIME")

    def test_full_phase_map_is_primary_and_controls_hold(self):
        c = k.phase_control(alpha=0.003, rho=4, R=8, n=60)
        self.assertEqual(len(c["P_phase"]), 4)
        self.assertEqual(c["primary_object"], "FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS")
        self.assertLess(c["symplectic_residual"], 5e-4)
        self.assertLess(c["reverse_inverse_residual"], 5e-4)
        self.assertLess(c["composition_residual"], 5e-4)
        self.assertTrue(c["graph"]["B_invertible"])

    def test_zero_window_is_identity(self):
        c = k.zero_window_control(alpha=0.003, rho=4)
        self.assertLess(c["identity_residual"], 1e-13)

    def test_orientation_scope_is_not_endpoint_calibration(self):
        c = k.orientation_control(alpha=0.003, rho=4, R=8, n=45)
        self.assertLess(c["affine_length_residual"], 1e-12)
        self.assertLess(c["profile_set_residual"], 5e-5)
        self.assertEqual(c["classification"], "ORIENTATION_LABEL_CONTROL_NOT_PHYSICAL_ENDPOINT_SCREEN_CALIBRATION")

    def test_effective_schwarzschild_conversion_removes_alpha(self):
        c = k.effective_schwarzschild_control(alpha=0.003, rho=4, R=8, n=50)
        self.assertLess(c["coordinate_path_residual"], 2e-11)
        self.assertLess(c["converted_profile_residual"], 4e-5)
        self.assertLess(c["converted_phase_map_residual"], 3e-4)
        self.assertEqual(c["classification"], "KOTTLER_COORDINATE_ORBIT_AND_CONVERTED_NULL_JACOBI_ALPHA_CANCELLATION_NOT_OPERATOR_SCALE_IDENTIFICATION")

    def test_joint_dilation_preserves_dimensionless_record(self):
        c = k.geometric_scale_control(M=1.2, alpha=0.003, factor=2.5, rho=4, R=8, n=45)
        self.assertLess(c["dimensionless_profile_residual"], 5e-5)
        self.assertLess(c["frequency_converted_phase_map_residual"], 4e-4)
        self.assertEqual(c["classification"], "JOINT_M_LAMBDA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE")

    def test_rank_has_exact_geometric_scale_null_direction(self):
        c = k.rank_control(alpha=0.003, rho=4, R=8, n=40)
        self.assertEqual(c["parameters"], ["log_M", "alpha"])
        self.assertEqual(c["rank_with_log_M_and_alpha"], 0)
        self.assertEqual(c["log_M_column_norm"], 0.0)
        self.assertEqual(c["alpha_column_norm"], 0.0)
        self.assertEqual(c["scale_null_direction"], [1, 0])

    def test_fixed_dimensional_lambda_is_external_standard(self):
        c = k.fixed_lambda_control(M=2, Lambda=0.00075)
        self.assertAlmostEqual(c["alpha"], 0.003)
        self.assertAlmostEqual(c["recovered_M"], 2.0)
        self.assertEqual(c["classification"], "FIXED_EXTERNAL_LAMBDA_IS_IMPORTED_DIMENSIONAL_STANDARD_NOT_ELL0")

if __name__ == "__main__":
    unittest.main()
