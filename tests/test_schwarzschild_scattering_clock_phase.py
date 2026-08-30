import json
import pathlib
import subprocess
import sys
import unittest

from studies.spacetime import schwarzschild_scattering_clock_phase as cp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "studies/spacetime/schwarzschild-scattering-clock-phase-results.json"


class SchwarzschildScatteringClockPhaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = cp.build_result()

    def test_regularized_elapsed_time_is_finite_and_convergent(self):
        coarse = cp.elapsed_time_control(n=200)
        fine = cp.elapsed_time_control(n=400)
        self.assertGreater(fine["delta_t_over_M"], 0.0)
        self.assertGreater(fine["delta_tau_over_M"], 0.0)
        self.assertLess(fine["mesh_doubling_residual"], coarse["mesh_doubling_residual"])
        self.assertLess(fine["mesh_doubling_residual"], 2e-4)
        self.assertGreater(fine["direct_cutoff_residual"], 0.0)
        self.assertLess(fine["direct_cutoff_residual"], 0.05)

    def test_clock_phase_is_linear_and_orientation_even(self):
        controls = self.result["clock_controls"]
        self.assertLess(controls["frequency_linearity_residual"], 1e-12)
        self.assertLess(controls["orientation_phase_residual"], 1e-12)
        self.assertEqual(controls["optical_orientation_labels"], [1, -1])

    def test_zero_window_tends_to_zero_and_identity(self):
        control = self.result["zero_window_control"]
        self.assertLess(control["fine_phase"], control["coarse_phase"])
        self.assertLess(control["fine_map_identity_residual"], control["coarse_map_identity_residual"])

    def test_fixed_dimensionless_frequency_preserves_dilation(self):
        control = self.result["geometric_scale_control"]
        self.assertLess(control["dimensionless_time_residual"], 1e-10)
        self.assertLess(control["clock_phase_residual"], 1e-10)
        self.assertLess(control["converted_phase_map_residual"], 3e-8)
        self.assertEqual(control["classification"], "GEOMETRIC_DILATION_NULL_DIRECTION_AT_FIXED_DIMENSIONLESS_SOURCE_FREQUENCY")

    def test_fixed_dimensional_frequency_is_external_standard(self):
        control = self.result["external_frequency_standard_control"]
        self.assertGreater(control["clock_phase_difference"], 0.1)
        self.assertEqual(control["classification"], "EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE")

    def test_joint_rank_retains_log_M_null_direction(self):
        rank = self.result["rank_control"]
        self.assertEqual(rank["parameters"], ["rho", "R", "log_M"])
        self.assertEqual(rank["rank_shape_boundary"], 2)
        self.assertEqual(rank["rank_with_log_M"], 2)
        self.assertLess(rank["log_M_column_norm"], 1e-6)
        self.assertEqual(rank["scale_null_direction"], [0.0, 0.0, 1.0])
        self.assertEqual(rank["global_injectivity"], "NOT_ESTABLISHED")

    def test_artifact_labels_preserve_no_evidence_contract(self):
        r = self.result
        self.assertEqual(r["status"], cp.STATUS)
        self.assertEqual(r["gate"], cp.GATE)
        self.assertFalse(r["ell0_identified"])
        self.assertEqual(r["UMCH"], "UNPROVEN")
        self.assertEqual(r["detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(r["maximum_interpretation"], "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE")
        self.assertEqual(r["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(r["joint_record"]["screen_order"], ["polar", "in-plane"])
        self.assertEqual(len(r["joint_record"]["P_frequency_converted"]), 4)

    def test_artifact_is_deterministic(self):
        self.assertEqual(json.loads(ARTIFACT.read_text()), self.result)
        proc = subprocess.run(
            [sys.executable, str(ROOT / "studies/spacetime/schwarzschild_scattering_clock_phase.py"), "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
