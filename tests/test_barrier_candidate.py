import csv
import importlib.util
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "barrier_check.py"
INPUT = STUDY / "barrier-cases.json"
OUTPUT = STUDY / "barrier-results.json"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-b-barrier.md"
MATRIX = ROOT / "theory" / "classical-dynamics" / "decision-matrix.csv"


def module():
    spec = importlib.util.spec_from_file_location("barrier", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class BarrierCandidateTests(unittest.TestCase):
    def test_preregistered_barrier_and_scalings(self):
        data = json.loads(INPUT.read_text(encoding="utf-8"))
        self.assertEqual("f(z)=1/(z-1)", data["barrier"])
        self.assertEqual("z=kappa/kappa0", data["dimensionless_ratio"])
        self.assertEqual("epsilon*m*c", data["coefficient"])
        self.assertEqual({"fixed-kappa", "proportional-kappa", "geodesic"}, {case["name"] for case in data["limit_cases"]})

    def test_exact_barrier_properties(self):
        barrier = module()
        self.assertEqual(1.0, barrier.f(2.0))
        self.assertGreater(barrier.f(1.0001), 9999.0)
        self.assertLess(barrier.f(1000000.0), 1.1e-6)
        self.assertLess(barrier.first_derivative(2.0), 0)
        self.assertGreater(barrier.second_derivative(2.0), 0)
        with self.assertRaises(ValueError):
            barrier.f(1.0)
        with self.assertRaises(ValueError):
            barrier.f(0.0)

    def test_limit_cases_distinguish_pointwise_and_nonuniform_limit(self):
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        cases = {case["name"]: case for case in result["limit_cases"]}
        self.assertEqual("VANISHES_POINTWISE", cases["fixed-kappa"]["classification"])
        self.assertEqual("FINITE_NONZERO", cases["proportional-kappa"]["classification"])
        self.assertEqual("OUTSIDE_DOMAIN", cases["geodesic"]["classification"])
        self.assertEqual("NONUNIFORM", result["standard_limit_classification"])

    def test_committed_result_is_deterministic(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)

    def test_document_does_not_overclaim_higher_derivative_result(self):
        text = DOC.read_text(encoding="utf-8")
        for phrase in ["f(z)=1/(z-1)", "εmc", "LENGTH", "NONUNIFORM", "fourth-order", "No Ostrogradsky", "UNPROVEN", "κ₀→0"]:
            self.assertIn(phrase, text)
        self.assertIn("constraint analysis remains incomplete", text)
        self.assertIn("no stability conclusion", text)

    def test_matrix_records_checked_barrier_but_incomplete_dynamics(self):
        with MATRIX.open(encoding="utf-8", newline="") as stream:
            row = {item["candidate_id"]: item for item in csv.DictReader(stream)}["B"]
        self.assertEqual("INCOMPLETE", row["state"])
        self.assertIn("SYMBOLIC", row["analysis_level"])
        self.assertIn("nonuniform", row["standard_limit"].lower())
        self.assertNotIn("proven stable", " ".join(row.values()).lower())


if __name__ == "__main__":
    unittest.main()
