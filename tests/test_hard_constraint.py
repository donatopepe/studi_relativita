import csv
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
INPUT = STUDY / "hard-constraint-cases.json"
OUTPUT = STUDY / "hard-constraint-results.json"
TOOL = STUDY / "hard_constraint_check.py"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-a-hard-constraint.md"
MATRIX = ROOT / "theory" / "classical-dynamics" / "decision-matrix.csv"


class HardConstraintTests(unittest.TestCase):
    def test_preregistered_cases_cover_kkt_branches_and_limit(self):
        data = json.loads(INPUT.read_text(encoding="utf-8"))
        names = {case["name"] for case in data["cases"]}
        self.assertEqual({"interior", "active-boundary", "infeasible", "zero-limit-geodesic"}, names)
        self.assertEqual("g=kappa0-kappa<=0", data["sign_convention"])

    def test_checker_classifies_declared_algebraic_cases(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        by_name = {case["name"]: case for case in result["cases"]}
        self.assertEqual("FEASIBLE_INACTIVE", by_name["interior"]["classification"])
        self.assertEqual("FEASIBLE_ACTIVE", by_name["active-boundary"]["classification"])
        self.assertEqual("INFEASIBLE", by_name["infeasible"]["classification"])
        self.assertEqual("FEASIBLE_ACTIVE", by_name["zero-limit-geodesic"]["classification"])
        self.assertTrue(all(case["complementarity_residual"] == 0 for case in by_name.values() if case["classification"] != "INFEASIBLE"))

    def test_audit_states_what_is_and_is_not_derived(self):
        text = DOC.read_text(encoding="utf-8")
        for phrase in [
            "g=κ₀-κ≤0", "λ≥0", "λg=0", "FEASIBILITY",
            "ACTIVE-SET", "NO_GO_CONDITIONAL", "No Dirac", "κ₀→0",
            "boundary terms", "initial data",
        ]:
            self.assertIn(phrase, text)
        self.assertIn("does not derive", text)
        self.assertIn("UNPROVEN", text)

    def test_matrix_records_conditional_result_without_overclaim(self):
        with MATRIX.open(encoding="utf-8", newline="") as stream:
            rows = {row["candidate_id"]: row for row in csv.DictReader(stream)}
        row = rows["A"]
        self.assertEqual("INCOMPLETE", row["state"])
        self.assertIn("KINEMATIC", row["analysis_level"])
        self.assertIn("KKT", row["evidence"])
        self.assertNotIn("stable", row["evidence"].lower())


if __name__ == "__main__":
    unittest.main()
