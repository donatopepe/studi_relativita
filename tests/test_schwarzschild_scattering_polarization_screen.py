import json
import pathlib
import subprocess
import sys
import unittest

from studies.spacetime import schwarzschild_scattering_polarization_screen as ps

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-scattering-polarization-screen-results.json"


class SchwarzschildScatteringPolarizationScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = ps.build_result()

    def test_raw_record_preserves_jones_coherency_clock_and_full_map(self):
        raw = self.result["raw_polarization_record"]
        self.assertEqual(len(raw["j_R"]), 2)
        self.assertEqual(len(raw["J_R"]), 2)
        self.assertEqual(len(raw["J_R"][0]), 2)
        self.assertEqual(len(raw["P_frequency_converted"]), 4)
        self.assertEqual(len(raw["P_frequency_converted"][0]), 4)
        self.assertLess(raw["jones_norm_residual"], 1e-12)
        self.assertLess(raw["coherency_hermiticity_residual"], 1e-12)
        self.assertLess(raw["coherency_outer_product_residual"], 1e-12)
        self.assertLess(raw["coherency_determinant_abs"], 1e-12)

    def test_screen_transfer_is_identity_only_in_parallel_screen_quotient(self):
        control = self.result["screen_transport_control"]
        self.assertGreater(control["coarse"]["max_interior_raw_covariant_derivative"], 1e-4)
        self.assertLess(control["fine"]["max_interior_screen_quotient_residual"], control["coarse"]["max_interior_screen_quotient_residual"])
        self.assertLess(control["fine"]["max_interior_screen_rotation_residual"], control["coarse"]["max_interior_screen_rotation_residual"])
        self.assertLess(control["U_screen_identity_residual"], 1e-12)
        self.assertEqual(control["interpretation"], "POLARIZATION_CONSTANT_IN_DECLARED_PARALLEL_SCREEN_MODULO_NULL_GAUGE_NOT_ENDPOINT_HARDWARE")

    def test_common_basis_rotation_leaves_analyzer_projection_invariant(self):
        control = self.result["basis_rotation_control"]
        self.assertLess(control["jones_covariance_residual"], 1e-12)
        self.assertLess(control["coherency_covariance_residual"], 1e-12)
        self.assertLess(control["analyzer_amplitude_residual"], 1e-12)
        self.assertLess(control["analyzer_power_residual"], 1e-12)
        self.assertEqual(control["interpretation"], "COMMON_SCREEN_ROTATION_IS_BASIS_QUOTIENT_NOT_PHYSICAL_CALIBRATION")

    def test_analyzer_is_secondary_nuisance_not_raw_record(self):
        control = self.result["analyzer_control"]
        self.assertGreater(abs(control["power_difference"]), 1e-3)
        self.assertLess(control["raw_jones_difference"], 1e-12)
        self.assertLess(control["raw_coherency_difference"], 1e-12)
        self.assertEqual(control["interpretation"], "ANALYZER_LABEL_CHANGES_PROJECTED_POWER_NOT_RAW_POLARIZATION_RECORD")

    def test_orientation_reversal_is_a_scoped_symmetry(self):
        control = self.result["orientation_control"]
        self.assertLess(control["jones_residual"], 1e-12)
        self.assertLess(control["coherency_residual"], 1e-12)
        self.assertLess(control["clock_phase_residual"], 1e-12)
        self.assertLess(control["converted_phase_map_residual"], 1e-9)
        self.assertEqual(control["interpretation"], "EQUATORIAL_ORIENTATION_REVERSAL_SYMMETRY_IN_DECLARED_SCREEN_NOT_STATISTICAL_INDEPENDENCE")

    def test_zero_window_has_identity_transfer_and_trivial_geometry(self):
        control = self.result["zero_window_control"]
        self.assertLess(control["polarization_transfer_identity_residual"], 1e-12)
        self.assertLess(control["clock_phase"], 1e-7)
        self.assertLess(control["phase_map_identity_residual"], 1e-6)
        self.assertEqual(control["interpretation"], "ZERO_WINDOW_SOURCE_POLARIZATION_CAN_REMAIN_BOUNDARY_DATA_NOT_GEOMETRY")

    def test_fixed_dimensionless_dilation_retains_scale_blindness(self):
        control = self.result["geometric_scale_control"]
        self.assertAlmostEqual(control["scale_factor"], 1.7)
        self.assertLess(control["jones_residual"], 1e-12)
        self.assertLess(control["coherency_residual"], 1e-12)
        self.assertLess(control["clock_phase_residual"], 1e-12)
        self.assertLess(control["converted_phase_map_residual"], 1e-9)
        self.assertEqual(control["interpretation"], "FIXED_DIMENSIONLESS_CONTROLS_RETAIN_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0")

    def test_rank_has_direct_log_M_null_direction(self):
        control = self.result["rank_control"]
        self.assertEqual(control["parameter_order"], ["rho", "R", "log_M"])
        self.assertEqual(control["rank_raw_shape_boundary"], 2)
        self.assertEqual(control["rank_raw_with_log_M"], 2)
        self.assertEqual(control["rank_quotient_shape_boundary"], 2)
        self.assertEqual(control["rank_quotient_with_log_M"], 2)
        self.assertLess(control["raw_log_M_column_norm"], 1e-7)
        self.assertLess(control["quotient_log_M_column_norm"], 1e-7)
        self.assertEqual(control["scale_null_direction"], [0.0, 0.0, 1.0])
        self.assertEqual(control["global_injectivity"], "NOT_ESTABLISHED")
        self.assertEqual(control["statistical_independence"], "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE")

    def test_result_keeps_conservative_status(self):
        self.assertEqual(ps.STATUS, "SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0")
        self.assertEqual(ps.GATE, "PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(self.result["UMCH"], "UNPROVEN")
        self.assertFalse(self.result["ell0_identified"])
        self.assertEqual(self.result["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(self.result["detection_claim"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(self.result["maximum_interpretation"], "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE")

    def test_artifact_is_deterministic(self):
        on_disk = json.loads(ARTIFACT.read_text())
        self.assertEqual(on_disk, self.result)
        subprocess.run(
            [sys.executable, str(ROOT / "studies/spacetime/schwarzschild_scattering_polarization_screen.py"), "--check"],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
