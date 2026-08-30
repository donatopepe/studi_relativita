import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
P = ROOT / "studies/spacetime/reissner_nordstrom_null_scattering_jacobi.py"
S = importlib.util.spec_from_file_location("rn_jacobi", P)
rn = importlib.util.module_from_spec(S)
S.loader.exec_module(rn)


class ReissnerNordstromNullScatteringJacobiTests(unittest.TestCase):
    def test_domain_and_path_contract(self):
        with self.assertRaises(ValueError):
            rn.profile_control(epsilon=0.8, rho=rn.photon_radius(0.8), R=12, n=30)
        c = rn.profile_control(M=1, epsilon=0.8, rho=4, R=12, n=40)
        self.assertEqual(c["branches"], ["incoming", "turning", "outgoing"])
        self.assertEqual(c["screen_order"], ["polar", "in-plane"])
        self.assertGreater(len(c["samples"]), 50)
        self.assertLess(c["maximum_K_symmetry_residual"], 1e-9)
        self.assertGreater(c["maximum_abs_Ricci_trace"], 1e-6)

    def test_schwarzschild_limit_matches_existing_control(self):
        c = rn.schwarzschild_limit_control(rho=4, R=12, n=50)
        self.assertLess(c["path_residual"], 1e-11)
        self.assertLess(c["profile_residual"], 3e-5)
        self.assertLess(c["phase_map_residual"], 2e-4)

    def test_charge_sign_is_exact_collision(self):
        c = rn.charge_sign_control(epsilon=0.8, n=45)
        self.assertLess(c["path_residual"], 1e-13)
        self.assertLess(c["profile_residual"], 1e-13)
        self.assertLess(c["phase_map_residual"], 1e-13)
        self.assertEqual(c["classification"], "Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0")

    def test_full_phase_map_is_primary_and_well_conditioned(self):
        c = rn.phase_control(epsilon=0.8, n=60)
        self.assertEqual(len(c["P_phase"]), 4)
        self.assertEqual(c["primary_object"], "FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS")
        self.assertLess(c["symplectic_residual"], 4e-4)
        self.assertLess(c["reverse_inverse_residual"], 4e-4)
        self.assertLess(c["turning_composition_residual"], 4e-4)

    def test_orientation_reversal_is_scoped_similarity(self):
        c = rn.orientation_control(epsilon=0.8, n=45)
        self.assertLess(c["phase_similarity_residual"], 2e-5)
        self.assertEqual(c["scope"], "DECLARED_EQUATORIAL_SCREEN_ONLY_NOT_STATISTICAL_INDEPENDENCE")

    def test_zero_window_graph_guard_and_scale_gate(self):
        self.assertLess(rn.zero_window_control()["identity_residual"], 1e-14)
        self.assertEqual(rn.graph([[1, 0], [0, 1]], [[0, 0], [0, 0]])["status"], "CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR")
        c = rn.geometric_scale_control(epsilon=0.8, n=45)
        self.assertLess(c["frequency_converted_phase_map_residual"], 3e-4)
        self.assertLess(c["dimensionless_profile_residual"], 3e-5)
        self.assertEqual(c["classification"], "JOINT_MQ_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE")

    def test_rank_retains_shape_but_loses_absolute_scale(self):
        c = rn.rank_control(epsilon=0.8, n=35)
        self.assertGreaterEqual(c["rank_with_log_M_and_epsilon"], 1)
        self.assertLess(c["log_M_column_norm"], 3e-4)
        self.assertEqual(c["scale_null_direction"], [1, 0])
        self.assertEqual(c["dependence_status"], "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE")

    def test_artifact_is_deterministic_and_negative(self):
        expected = json.loads((ROOT / "studies/spacetime/reissner-nordstrom-null-scattering-jacobi-results.json").read_text())
        self.assertEqual(rn.build_result(), expected)
        self.assertEqual(expected["status"], rn.STATUS)
        self.assertFalse(expected["ell0_identified"])
        self.assertEqual(expected["structural_dead_end"], "NOT_DECLARED")
        self.assertEqual(expected["detection"], "NO_POSITIVE_DETECTION_CLAIM")


if __name__ == "__main__":
    unittest.main()
