import importlib.util
import json
import math
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "studies/spacetime/kerr_photon_ring_orientation_scale.py"
ARTIFACT = ROOT / "studies/spacetime/kerr-photon-ring-orientation-scale-results.json"
SPEC = importlib.util.spec_from_file_location("kerr_ring", PATH)
ring = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ring)

CHIS = (0.0, 0.2, 0.6, 0.9, 0.99)
TOL = 1e-10


class KerrPhotonRingOrientationScaleControls(unittest.TestCase):
    def test_01_radius_formula_and_range(self):
        for chi in CHIS:
            pro = ring.orbit_record(1.0, chi, "prograde")
            retro = ring.orbit_record(1.0, chi, "retrograde")
            self.assertTrue(math.isfinite(pro["x_ph"]))
            self.assertTrue(math.isfinite(retro["x_ph"]))
            self.assertGreaterEqual(pro["x_ph"], 1.0)
            self.assertLessEqual(pro["x_ph"], 3.0)
            self.assertGreaterEqual(retro["x_ph"], 3.0)
            self.assertLessEqual(retro["x_ph"], 4.0)

    def test_02_branch_ordering(self):
        for chi in CHIS[1:]:
            self.assertLess(
                ring.orbit_record(1.0, chi, "prograde")["x_ph"],
                ring.orbit_record(1.0, chi, "retrograde")["x_ph"],
            )

    def test_03_schwarzschild_collision(self):
        pro = ring.orbit_record(2.0, 0.0, "prograde")
        retro = ring.orbit_record(2.0, 0.0, "retrograde")
        self.assertAlmostEqual(pro["x_ph"], 3.0)
        self.assertAlmostEqual(retro["x_ph"], 3.0)
        self.assertAlmostEqual(pro["r_ph"], retro["r_ph"])
        self.assertAlmostEqual(abs(pro["xi_over_M"]), 3.0 * math.sqrt(3.0))
        self.assertEqual(pro["collision_classification"], "KERR_PROGRADE_RETROGRADE_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_LIMIT")

    def test_04_radial_potential_conformance(self):
        for chi in CHIS:
            for branch in ("prograde", "retrograde"):
                record = ring.orbit_record(1.7, chi, branch)
                self.assertLess(abs(record["R_residual"]), TOL)
                self.assertLess(abs(record["R_prime_residual"]), TOL)
                self.assertLess(abs(record["null_angular_rate_residual"]), TOL)

    def test_05_signed_spin_orientation_collision(self):
        for relative in (-1, 1):
            forward = ring.signed_convention_record(1.0, 0.6, 1, relative)
            reversed_both = ring.signed_convention_record(1.0, 0.6, -1, -relative)
            self.assertEqual(forward["relative_orientation"], reversed_both["relative_orientation"])
            self.assertAlmostEqual(forward["x_ph"], reversed_both["x_ph"])
            self.assertAlmostEqual(forward["unsigned_period_over_M"], reversed_both["unsigned_period_over_M"])
            self.assertAlmostEqual(forward["Omega_phi_M"], -reversed_both["Omega_phi_M"])
        fixed_spin_pro = ring.signed_convention_record(1.0, 0.6, 1, 1)
        fixed_spin_retro = ring.signed_convention_record(1.0, 0.6, 1, -1)
        self.assertNotAlmostEqual(fixed_spin_pro["x_ph"], fixed_spin_retro["x_ph"])

    def test_06_joint_geometric_dilation(self):
        control = ring.joint_dilation_control(M=1.3, chi=0.6, scale=2.5)
        self.assertLess(control["dimensionless_residual"], TOL)
        self.assertLess(control["dimensional_covariance_residual"], TOL)
        self.assertEqual(control["classification"], "JOINT_MA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE")

    def test_07_rank_retains_exact_scale_null_direction(self):
        control = ring.rank_control(chi=0.6)
        self.assertEqual(control["parameters"], ["log_M", "chi"])
        self.assertEqual(control["rank"], 1)
        self.assertEqual(control["scale_null_direction"], [1.0, 0.0])
        self.assertLess(control["log_M_column_norm"], TOL)
        self.assertGreater(control["chi_column_norm"], 1e-3)

    def test_08_no_ell0_identification(self):
        gate = ring.no_ell0_gate()
        self.assertFalse(gate["M_identified_internally"])
        self.assertFalse(gate["a_identified_internally"])
        self.assertFalse(gate["ell0_identified"])
        self.assertEqual(gate["L_equals_ell0"], "NOT_DERIVED")
        self.assertEqual(gate["Detection"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertEqual(gate["result"], "KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0")

    def test_stable_artifact_records_exactly_eight_passing_controls(self):
        expected = json.loads(ARTIFACT.read_text())
        generated = json.loads(subprocess.check_output(["python", str(PATH)], text=True))
        self.assertEqual(generated, expected)
        summary = expected["control_summary"]
        self.assertEqual(summary["controls_passed"], 8)
        self.assertEqual(summary["controls_total"], 8)
        self.assertEqual(len(summary["controls"]), 8)
        self.assertTrue(all(control["passed"] for control in summary["controls"]))
        self.assertEqual([control["threshold"] for control in summary["controls"]], [1e-12, 1e-8, 1e-12, 1e-10, 1e-10, 1e-10, 1e-10, 1.0])
        for key, value in (
            ("L_identified", False), ("ell0_identified", False),
            ("L_equals_ell0", "NOT_DERIVED"), ("extra_dimension_detected", False),
            ("structural_dead_end", "NOT_DECLARED"),
            ("Detection", "NO_POSITIVE_DETECTION_CLAIM"),
            ("Maximum_interpretation", "MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE"),
        ):
            self.assertEqual(summary[key], value)


if __name__ == "__main__":
    unittest.main()
