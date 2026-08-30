import json
import pathlib
import subprocess
import sys
import unittest

from studies.spacetime import schwarzschild_scattering_source_coherence as sc

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-scattering-source-coherence-results.json"


class SchwarzschildScatteringSourceCoherenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = sc.build_result()

    def test_raw_record_preserves_vector_visibility_clock_and_full_map(self):
        raw = self.result["raw_coherence_record"]
        self.assertEqual(len(raw["y_coh"]), 2)
        self.assertGreater(raw["visibility"], 0.0)
        self.assertLessEqual(raw["visibility"], 1.0)
        self.assertEqual(len(raw["P_frequency_converted"]), 4)
        self.assertEqual(len(raw["P_frequency_converted"][0]), 4)
        norm = sum(value * value for value in raw["y_coh"]) ** 0.5
        self.assertAlmostEqual(norm, raw["amplitude"] * raw["visibility"], places=12)

    def test_source_lo_and_amplitude_nuisances_are_explicit(self):
        control = self.result["nuisance_controls"]
        self.assertLess(control["common_phase_residual"], 1e-12)
        self.assertLess(control["source_gain_compensation_residual"], 1e-12)
        self.assertEqual(control["phase_null_direction"], [0.0, 1.0, 0.0, 1.0])
        self.assertEqual(control["amplitude_null_direction"], [1.0, 0.0, -1.0, 0.0])
        self.assertEqual(control["nuisance_jacobian_rank"], 2)

    def test_zero_window_has_unit_visibility_and_trivial_geometry(self):
        control = self.result["zero_window_control"]
        self.assertLess(control["visibility_difference_from_one"], 1e-7)
        self.assertLess(control["clock_phase"], 1e-7)
        self.assertLess(control["phase_map_identity_residual"], 1e-6)
        self.assertEqual(control["interpretation"], "ZERO_WINDOW_RAW_COHERENCE_PHASE_CAN_REMAIN_SOURCE_LO_NUISANCE_NOT_GEOMETRY")

    def test_fixed_dimensionless_coherence_width_retains_dilation_blindness(self):
        control = self.result["geometric_scale_control"]
        self.assertAlmostEqual(control["scale_factor"], 1.7)
        self.assertLess(control["coherence_iq_residual"], 1e-9)
        self.assertLess(control["visibility_residual"], 1e-12)
        self.assertLess(control["clock_phase_residual"], 1e-12)
        self.assertLess(control["converted_phase_map_residual"], 1e-8)

    def test_fixed_dimensional_coherence_time_is_external_standard(self):
        control = self.result["external_coherence_standard_control"]
        self.assertGreater(abs(control["visibility_difference"]), 1e-4)
        self.assertGreater(control["coherence_iq_difference"], 1e-4)
        self.assertEqual(control["classification"], "EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE")

    def test_rank_audit_retains_log_mass_null_direction(self):
        rank = self.result["rank_control"]
        self.assertEqual(rank["parameters"], ["rho", "R", "log_M"])
        self.assertEqual(rank["rank_raw_shape_boundary"], 2)
        self.assertEqual(rank["rank_raw_with_log_M"], 2)
        self.assertEqual(rank["rank_quotient_shape_boundary"], 2)
        self.assertEqual(rank["rank_quotient_with_log_M"], 2)
        self.assertLess(rank["raw_log_M_column_norm"], 1e-7)
        self.assertLess(rank["quotient_log_M_column_norm"], 1e-7)
        self.assertEqual(rank["scale_null_direction"], [0.0, 0.0, 1.0])
        self.assertEqual(rank["statistical_independence"], "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE")

    def test_status_scope_and_gate_remain_bounded(self):
        self.assertEqual(self.result["status"], sc.STATUS)
        self.assertEqual(self.result["gate"], sc.GATE)
        self.assertEqual(self.result["UMCH"], "UNPROVEN")
        self.assertFalse(self.result["ell0_identified"])
        self.assertEqual(self.result["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(self.result["detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(self.result["maximum_interpretation"], "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE")

    def test_committed_artifact_is_current(self):
        committed = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(committed, self.result)
        subprocess.run(
            [sys.executable, str(ROOT / "studies/spacetime/schwarzschild_scattering_source_coherence.py"), "--check"],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
