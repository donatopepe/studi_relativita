import importlib.util
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kaluza_klein_linearized_tensor.py"
SPEC = importlib.util.spec_from_file_location("kk_tensor", PATH)
kk = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kk)

L = 1.0
R = 2.0
Y = 0.7
SHELL_WIDTH = 0.3
SCALE = 2.5
TOL = 1e-10


def max_abs(values):
    if isinstance(values, dict):
        return max((max_abs(value) for value in values.values()), default=0.0)
    if isinstance(values, (list, tuple)):
        return max((max_abs(value) for value in values), default=0.0)
    return abs(values)


def matrix_residual(left, right):
    return max(abs(left[i][j] - right[i][j]) for i in range(len(left)) for j in range(len(left[i])))


class KaluzaKleinTensorConformanceControls(unittest.TestCase):
    def test_01_d5_dust_trace_reversal_ratios(self):
        record = kk.trace_reversal_from_bar([[3.0 if i == j == 0 else 0.0 for j in range(5)] for i in range(5)])
        self.assertLess(matrix_residual(record["h"], [
            [2.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0],
        ]), TOL)
        self.assertLess(matrix_residual(record["bar_h_roundtrip"], record["bar_h"]), TOL)

    def test_02_harmonic_gauge_residual(self):
        localized = kk.point_tensor_response(R, L, delta_y=Y, profile="localized")
        uniform = kk.point_tensor_response(R, L, delta_y=Y, profile="uniform")
        self.assertLess(max_abs(localized["harmonic_gauge_residual"]), TOL)
        self.assertLess(max_abs(uniform["harmonic_gauge_residual"]), TOL)

    def test_03_riemann_contractions_match_einstein_operator_and_vacuum(self):
        for profile in ("localized", "uniform"):
            record = kk.point_tensor_response(R, L, delta_y=Y, profile=profile)
            self.assertLess(max_abs(record["einstein_conformance_residual"]), TOL)
            self.assertLess(max_abs(record["Ricci_5D"]), TOL)
            self.assertLess(abs(record["Ricci_scalar_5D"]), TOL)
            self.assertLess(max_abs(record["Einstein_5D"]), TOL)
            self.assertGreater(max_abs(record["Riemann_5D"]), 1e-4)

    def test_04_r0i0j_matches_point_and_shell_scalar_hessian(self):
        point = kk.point_tensor_response(R, L, delta_y=Y, profile="localized")
        shell = kk.shell_tensor_response(R, SHELL_WIDTH, L, delta_y=Y, profile="localized")
        self.assertLess(matrix_residual(point["R_0i0j"], point["scalar_Hessian_reference"]), TOL)
        self.assertLess(matrix_residual(shell["shell_R_0i0j"], shell["shell_Hessian_reference"]), TOL)
        self.assertLess(point["point_conformance_residual"], TOL)
        self.assertLess(shell["shell_conformance_residual"], TOL)

    def test_05_localized_compact_index_curvature_separates_y_derivatives(self):
        record = kk.point_tensor_response(R, L, delta_y=Y, profile="localized")
        self.assertGreater(abs(record["R_0404"]), 1e-4)
        self.assertGreater(max_abs(record["R_0i04"]), 1e-4)
        self.assertGreater(max_abs(record["R_i4j4"]), 1e-4)
        self.assertEqual(record["compact_classification"], "ORDINARY_SPACE_TIDAL_BLOCK_OMITS_COMPACT_INDEX_CURVATURE_NOT_EXTRA_OBSERVATIONAL_RANK")

    def test_06_exact_uniform_removes_y_derivatives_not_all_index4_curvature(self):
        record = kk.point_tensor_response(R, L, delta_y=Y, profile="uniform")
        self.assertLess(abs(record["R_0404"]), TOL)
        self.assertLess(max_abs(record["R_0i04"]), TOL)
        self.assertGreater(max_abs(record["R_i4j4"]), 1e-4)
        self.assertLess(matrix_residual(record["R_0i0j"], record["scalar_Hessian_reference"]), TOL)
        self.assertEqual(record["mode_or_exact_expression"], "EXACT_UNIFORM_ZERO_MODE")

    def test_07_tensor_completion_depends_on_source_stress(self):
        control = kk.source_stress_dependence_control()
        self.assertEqual(control["alternative_label"], "SYMBOLIC_DIAGONAL_STRESS_COUNTEREXAMPLE_NOT_PHYSICAL_EOS")
        self.assertAlmostEqual(control["dust_h00"], control["alternative_h00"])
        self.assertGreater(control["spatial_ratio_residual"], 0.1)
        self.assertEqual(control["classification"], "TENSOR_COMPLETION_DEPENDS_ON_SOURCE_STRESS_AND_DECLARED_LINEARIZED_CONVENTIONS_NOT_SCALAR_POTENTIAL_ALONE")

    def test_08_joint_scaling_preserves_dimensionless_tensor_and_scale_null(self):
        control = kk.joint_scaling_control(R, SHELL_WIDTH, L, Y, SCALE)
        self.assertLess(control["dimensionless_full_curvature_residual"], TOL)
        self.assertLess(control["dimensionless_R_0i0j_residual"], TOL)
        self.assertEqual(control["rank"], 0)
        self.assertEqual(control["scale_null_direction"], [1.0])
        self.assertEqual(control["classification"], "LINEARIZED_5D_TENSOR_COMPLETION_RETAINS_JOINT_GEOMETRIC_SCALE_NULL_NOT_ELL0")


if __name__ == "__main__":
    unittest.main()
