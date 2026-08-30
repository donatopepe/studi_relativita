import json
import pathlib
import subprocess
import sys
import unittest

from studies.spacetime import schwarzschild_scattering_coherent_readout as cr

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-scattering-coherent-readout-results.json"


class SchwarzschildScatteringCoherentReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = cr.build_result()

    def test_iq_norm_matches_declared_amplitude(self):
        raw = self.result["raw_readout"]
        norm = (raw["y_IQ"][0] ** 2 + raw["y_IQ"][1] ** 2) ** 0.5
        self.assertAlmostEqual(norm, raw["amplitude"], places=12)
        self.assertEqual(len(raw["P_frequency_converted"]), 4)
        self.assertEqual(len(raw["P_frequency_converted"][0]), 4)

    def test_common_source_lo_phase_is_exact_nuisance(self):
        control = self.result["nuisance_controls"]
        self.assertLess(control["common_phase_residual"], 1e-12)
        self.assertLess(control["source_gain_compensation_residual"], 1e-12)
        self.assertEqual(control["phase_null_direction"], [0.0, 1.0, 0.0, 1.0])
        self.assertEqual(control["amplitude_null_direction"], [1.0, 0.0, -1.0, 0.0])
        self.assertLess(control["phase_null_residual"], 1e-8)
        self.assertLess(control["amplitude_null_residual"], 1e-8)
        self.assertEqual(control["nuisance_jacobian_rank"], 2)

    def test_unrestricted_gain_phase_quotient_collapses_nonzero_iq(self):
        control = self.result["quotient_control"]
        self.assertLess(control["representative_residual"], 1e-12)
        self.assertEqual(control["reference_representative"], [1.0, 0.0])
        self.assertEqual(control["transformed_representative"], [1.0, 0.0])
        self.assertEqual(control["classification"], "UNRESTRICTED_POSITIVE_GAIN_AND_PHASE_QUOTIENT_REMOVES_SCALAR_CARRIER_IQ_CONTENT")

    def test_zero_window_separates_carrier_nuisance_from_geometry(self):
        control = self.result["zero_window_control"]
        self.assertLess(control["fine_clock_phase"], control["coarse_clock_phase"])
        self.assertLess(control["fine_map_identity_residual"], control["coarse_map_identity_residual"])
        self.assertGreater(control["fine_raw_iq_norm"], 0.0)
        self.assertEqual(control["classification"], "ZERO_WINDOW_GEOMETRY_LIMIT_DOES_NOT_REMOVE_ARBITRARY_SOURCE_LO_CARRIER_PHASE")

    def test_fixed_dimensionless_frequency_preserves_dilation(self):
        control = self.result["geometric_scale_control"]
        self.assertLess(control["iq_residual"], 1e-10)
        self.assertLess(control["clock_phase_residual"], 1e-10)
        self.assertLess(control["converted_phase_map_residual"], 3e-8)
        self.assertLess(control["quotient_residual"], 1e-12)
        self.assertEqual(control["classification"], "GEOMETRIC_DILATION_NULL_DIRECTION_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY")

    def test_fixed_dimensional_frequency_is_external_standard(self):
        control = self.result["external_frequency_standard_control"]
        self.assertGreater(abs(control["iq_difference"]), 1e-3)
        self.assertGreater(abs(control["clock_phase_difference"]), 1e-3)
        self.assertEqual(control["classification"], "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE")

    def test_rank_retains_log_m_null_direction(self):
        control = self.result["rank_control"]
        self.assertEqual(control["parameters"], ["rho", "R", "log_M"])
        self.assertEqual(control["rank_raw_shape_boundary"], 2)
        self.assertEqual(control["rank_raw_with_log_M"], 2)
        self.assertEqual(control["rank_quotient_shape_boundary"], 2)
        self.assertEqual(control["rank_quotient_with_log_M"], 2)
        self.assertLess(control["raw_log_M_column_norm"], 1e-6)
        self.assertLess(control["quotient_log_M_column_norm"], 1e-6)
        self.assertEqual(control["scale_null_direction"], [0, 0, 1])
        self.assertEqual(control["global_injectivity"], "NOT_ESTABLISHED")
        self.assertEqual(control["statistical_independence"], "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE")

    def test_authority_and_gate_remain_negative(self):
        result = self.result
        self.assertEqual(result["status"], "SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0")
        self.assertEqual(result["gate"], "PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(result["UMCH"], "UNPROVEN")
        self.assertFalse(result["ell0_identified"])
        self.assertEqual(result["detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(result["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(result["maximum_interpretation"], "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE")

    def test_artifact_is_deterministic(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "studies/spacetime/schwarzschild_scattering_coherent_readout.py"), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(ARTIFACT.read_text()), self.result)


if __name__ == "__main__":
    unittest.main()
