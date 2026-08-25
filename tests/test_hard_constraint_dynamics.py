import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "hard_constraint_dynamics_check.py"
INPUT = STUDY / "hard-constraint-dynamics-cases.json"
OUTPUT = STUDY / "hard-constraint-dynamics-results.json"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-a-dynamics.md"


def module():
    spec = importlib.util.spec_from_file_location("harddyn", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class HardConstraintDynamicsTests(unittest.TestCase):
    def test_fixed_normalized_action_dimensions_and_branches(self):
        data = json.loads(INPUT.read_text(encoding="utf-8"))
        self.assertEqual("g=1-kappa/kappa0<=0", data["constraint"])
        self.assertEqual("dimensionless", data["lambda_dimension"])
        self.assertEqual("S0+mc*integral(ds*lambda*g)", data["action"])
        hard = module()
        self.assertEqual("INACTIVE_FREE_BRANCH", hard.classify(kappa=2, kappa0=1, multiplier=0)["classification"])
        self.assertEqual("ACTIVE_BOUNDARY_BRANCH", hard.classify(kappa=1, kappa0=1, multiplier=0.5)["classification"])
        self.assertEqual("KKT_INFEASIBLE", hard.classify(kappa=0, kappa0=1, multiplier=0)["classification"])

    def test_active_interval_effective_lagrangian_is_linear_in_curvature(self):
        hard = module()
        active = hard.effective_lagrangian_coefficients(multiplier=0.5, kappa0=2.0)
        self.assertEqual(-0.5, active["constant_mc_coefficient"])
        self.assertEqual(-0.25, active["kappa_mc_length_coefficient"])
        self.assertEqual(0.0, active["L_kappakappa"])
        self.assertEqual("LINEAR_CURVATURE_DEGENERATE_SECTOR", active["classification"])

    def test_transition_jump_audit(self):
        hard = module()
        smooth = hard.transition_audit(lambda_left=0, lambda_right=0, lambda_prime_left=0, lambda_prime_right=0)
        jump = hard.transition_audit(lambda_left=0, lambda_right=1, lambda_prime_left=0, lambda_prime_right=0)
        self.assertEqual("NO_MULTIPLIER_JUMP_DETECTED", smooth["classification"])
        self.assertEqual("DISTRIBUTIONAL_MATCHING_REQUIRED", jump["classification"])
        self.assertFalse(jump["matching_rule_derived"])

    def test_deterministic_output_and_document_scope(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual("SMOOTH_BRANCHES_ONLY", result["derived_scope"])
        self.assertFalse(result["global_well_posedness_derived"])
        text = DOC.read_text(encoding="utf-8")
        for token in ["INACTIVE_FREE_BRANCH", "ACTIVE_BOUNDARY_BRANCH", "LINEAR_CURVATURE_DEGENERATE_SECTOR", "DISTRIBUTIONAL_MATCHING_REQUIRED", "UNPROVEN", "not derived"]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
