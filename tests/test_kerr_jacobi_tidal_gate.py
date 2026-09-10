import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kerr_jacobi_tidal_gate.py"
ARTIFACT = ROOT / "studies/spacetime/kerr-jacobi-tidal-gate-results.json"
SPEC = importlib.util.spec_from_file_location("kerr_jacobi", PATH)
jacobi = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(jacobi)
M, CHI, RHO, RS, RO = 1.0, 0.6, 4.5, 12.0, 15.0


def matrix_residual(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[i])))


class KerrJacobiTidalControls(unittest.TestCase):
    def test_01_tidal_profile_matches_equatorial_source_formula(self):
        for orientation in (-1, 1):
            sample = jacobi.tidal_sample(M, CHI, RHO, orientation, r=7.0)
            expected = 3.0 * M * (sample["xi"] - CHI * M) ** 2 / 7.0**5
            self.assertAlmostEqual(sample["K"][0][0], -expected, places=13)
            self.assertAlmostEqual(sample["K"][1][1], expected, places=13)

    def test_02_tidal_matrix_is_symmetric_and_vacuum_trace_free(self):
        control = jacobi.profile_control(M, CHI, RHO, RS, RO, orientation=1)
        self.assertLess(control["maximum_symmetry_residual"], 2e-12)
        self.assertLess(control["maximum_vacuum_trace_residual"], 2e-12)
        self.assertEqual(control["branches"], ["incoming", "turning", "outgoing"])

    def test_03_schwarzschild_profile_and_phase_conform(self):
        control = jacobi.schwarzschild_conformance(M, RHO, RS, RO)
        self.assertLess(control["profile_residual"], 2e-12)
        self.assertLess(control["phase_map_residual"], 3e-6)

    def test_04_full_phase_map_is_symplectic(self):
        for orientation in (-1, 1):
            phase = jacobi.phase_control(M, CHI, RHO, RS, RO, orientation)
            self.assertEqual(len(phase["P_phase"]), 4)
            self.assertLess(phase["symplectic_residual"], 3e-7)
            self.assertEqual(phase["primary_object"], "FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS")

    def test_05_reversal_turning_composition_and_convergence(self):
        control = jacobi.reversal_composition_control(M, CHI, RHO, RS, RO, orientation=1)
        self.assertLess(control["reverse_inverse_residual"], 3e-6)
        self.assertLess(control["turning_composition_residual"], 3e-6)
        self.assertLess(control["coarse_fine_residual"], 3e-6)

    def test_06_orientation_adds_phase_map_shape(self):
        control = jacobi.orientation_control(M, CHI, RHO, RS, RO)
        self.assertGreater(control["fixed_spin_phase_difference"], 1e-3)
        self.assertLess(control["simultaneous_reversal_residual"], 3e-6)
        self.assertEqual(control["classification"], "KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_IDENTITY_SCREEN_QUOTIENT")

    def test_07_source_preparations_and_caustic_gate(self):
        control = jacobi.preparation_control(M, CHI, RHO, RS, RO, orientation=1)
        self.assertGreater(control["preparation_difference"], 1e-3)
        self.assertIn(control["graph"]["status"], {"REGULAR", "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR"})
        self.assertEqual(control["full_phase_map_status"], "FINITE_AND_PRIMARY")

    def test_08_scale_rank_and_no_ell0(self):
        scale = jacobi.scale_control(M, CHI, RHO, RS, RO, orientation=1, scale=2.5)
        self.assertLess(scale["converted_phase_map_residual"], 3e-6)
        rank = jacobi.rank_control(CHI, RHO, RS, RO)
        self.assertLess(rank["log_M_column_norm"], 2e-8)
        self.assertEqual(rank["scale_null_direction"], [1.0, 0.0, 0.0, 0.0, 0.0])
        gate = jacobi.no_ell0_gate()
        self.assertFalse(gate["ell0_identified"])
        self.assertEqual(gate["Detection"], "NO_POSITIVE_DETECTION_CLAIM")

    def test_stable_artifact_has_eight_controls(self):
        expected = json.loads(ARTIFACT.read_text())
        generated = json.loads(subprocess.check_output(["python", str(PATH)], text=True))
        self.assertEqual(generated, expected)
        summary = expected["control_summary"]
        self.assertEqual(summary["controls_passed"], 8)
        self.assertEqual(summary["controls_total"], 8)
        self.assertTrue(all(item["passed"] for item in summary["controls"]))
        self.assertEqual([item["threshold"] for item in summary["controls"]], [2e-12, 2e-12, 3e-6, 3e-7, 3e-6, 3e-6, 1e-3, 3e-6])


if __name__ == "__main__":
    unittest.main()
