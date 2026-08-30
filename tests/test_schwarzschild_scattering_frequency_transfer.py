import importlib.util
import json
import math
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE = ROOT / "studies/spacetime/schwarzschild_scattering_frequency_transfer.py"
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-scattering-frequency-transfer-results.json"

spec = importlib.util.spec_from_file_location("frequency_transfer", MODULE)
frequency_transfer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frequency_transfer)


class FrequencyTransferTests(unittest.TestCase):
    def test_static_frequency_transfer_and_consistency_gate(self):
        control = frequency_transfer.static_frequency_transfer(1.0, 12.0, 9.0, 2.0)
        expected = math.sqrt((1.0 - 2.0 / 12.0) / (1.0 - 2.0 / 9.0))
        self.assertAlmostEqual(control["omega_observer"] / 2.0, expected, places=13)
        self.assertAlmostEqual(control["source_killing_energy"], control["observer_killing_energy"], places=13)
        self.assertEqual(control["classification"], "STATIC_TETRAD_FREQUENCY_TRANSFER_KNOWN_GEOMETRIC_RELATION")
        with self.assertRaises(ValueError):
            frequency_transfer.validate_endpoint_frequencies(1.0, 12.0, 9.0, 2.0, 2.0)

    def test_equal_endpoint_primary_path_has_equal_local_frequencies(self):
        control = frequency_transfer.static_frequency_transfer(1.0, 12.0, 12.0, 2.0)
        self.assertAlmostEqual(control["omega_observer"], 2.0, places=13)
        self.assertAlmostEqual(control["transfer_ratio"], 1.0, places=13)

    def test_affine_tangent_rescaling_and_full_map_similarity(self):
        control = frequency_transfer.affine_frequency_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, n=80)
        a = 0.2 * math.sqrt(1.0 - 2.0 / 12.0)
        self.assertAlmostEqual(control["tangent_scale"], a, places=13)
        self.assertAlmostEqual(control["profile_quadratic_ratio"], a * a, places=10)
        self.assertLess(control["profile_scaling_residual"], 1e-12)
        self.assertGreater(control["raw_rate_map_difference"], 1e-3)
        self.assertLess(control["converted_phase_map_residual"], 2e-10)
        self.assertEqual(control["classification"], "SOURCE_LOCAL_FREQUENCY_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK")

    def test_fixed_dimensionless_frequency_scale_orbit_remains_blind(self):
        control = frequency_transfer.geometric_scale_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, factor=1.7, n=80)
        self.assertAlmostEqual(control["nu_source"], 0.2, places=13)
        self.assertLess(control["dimensionless_frequency_transfer_residual"], 1e-13)
        self.assertLess(control["converted_phase_map_residual"], 3e-9)
        self.assertEqual(control["classification"], "GEOMETRIC_SCALE_BLIND_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY")

    def test_dimensional_frequency_is_external_standard_not_interior_scale(self):
        control = frequency_transfer.external_frequency_standard_control(M=1.0, rho=4.0, R=12.0, omega_source=0.2, factor=1.7, n=60)
        self.assertGreater(control["raw_output_difference"], 1e-3)
        self.assertEqual(control["varying_product"], "M_TIMES_OMEGA_SOURCE")
        self.assertEqual(control["classification"], "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE")
        self.assertFalse(control["ell0_identified"])

    def test_rank_keeps_geometric_scale_null_after_declared_conversion(self):
        control = frequency_transfer.rank_control(M=1.0, rho=4.0, R=12.0, nu_source=0.2, n=60)
        self.assertEqual(control["parameters"], ["rho", "R", "log_M"])
        self.assertEqual(control["rank_shape_boundary"], 2)
        self.assertEqual(control["rank_with_log_M"], 2)
        self.assertLess(control["log_M_column_norm"], 2e-7)
        self.assertEqual(control["scale_null_direction"], [0, 0, 1])
        self.assertEqual(control["global_injectivity"], "NOT_ESTABLISHED")

    def test_result_contract_and_artifact(self):
        result = frequency_transfer.build_result(n=80)
        self.assertEqual(result["UMCH"], "UNPROVEN")
        self.assertEqual(result["status"], "SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0")
        self.assertEqual(result["gate"], "PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(result["primary_object"], "FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY")
        self.assertEqual(result["screen_order"], ["polar", "in-plane"])
        self.assertFalse(result["ell0_identified"])
        self.assertEqual(result["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(result["detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(result["maximum_interpretation"], "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE")
        self.assertEqual(result["review"], "DIRECT_REVIEW_NO_SUBAGENT")
        self.assertEqual(json.loads(ARTIFACT.read_text()), result)
        check = subprocess.run([sys.executable, str(MODULE), "--check"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)


if __name__ == "__main__":
    unittest.main()
