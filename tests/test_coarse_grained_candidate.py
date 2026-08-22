import csv
import importlib.util
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "coarse_grained_check.py"
INPUT = STUDY / "coarse-grained-cases.json"
OUTPUT = STUDY / "coarse-grained-results.json"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-c-coarse-grained.md"
MATRIX = ROOT / "theory" / "classical-dynamics" / "decision-matrix.csv"


def module():
    spec = importlib.util.spec_from_file_location("coarse", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class CoarseGrainedCandidateTests(unittest.TestCase):
    def test_weighted_rms_is_deterministic_and_dimension_preserving(self):
        coarse = module()
        self.assertAlmostEqual(2.0, coarse.weighted_rms([2.0, 2.0], [1.0, 3.0]))
        self.assertAlmostEqual(5.0 ** 0.5, coarse.weighted_rms([1.0, 3.0], [1.0, 1.0]))
        with self.assertRaises(ValueError):
            coarse.weighted_rms([1.0], [0.0])
        with self.assertRaises(ValueError):
            coarse.weighted_rms([1.0], [-1.0])

    def test_counterexample_proves_non_equivalence(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        cases = {case["name"]: case for case in result["cases"]}
        counterexample = cases["rms-passes-pointwise-fails"]
        self.assertTrue(counterexample["rms_bound_satisfied"])
        self.assertFalse(counterexample["pointwise_bound_satisfied"])
        self.assertTrue(counterexample["contains_zero_curvature"])
        self.assertEqual("NOT_EQUIVALENT", result["equivalence_to_pointwise_umch"])

    def test_input_declares_invariant_window_requirements(self):
        data = json.loads(INPUT.read_text(encoding="utf-8"))
        self.assertEqual("proper_time", data["parameter"])
        self.assertEqual("nonnegative_normalized_weights", data["kernel_requirement"])
        self.assertEqual("L^-1", data["observable_dimension"])
        self.assertEqual("ALTERNATIVE_HYPOTHESIS", data["hypothesis_class"])

    def test_document_marks_operational_unknowns_and_separate_ratification(self):
        text = DOC.read_text(encoding="utf-8")
        for phrase in ["ALTERNATIVE_HYPOTHESIS", "NOT_EQUIVALENT", "proper time", "window", "kernel", "UNPROVEN", "separate ratification", "NON_IDENTIFIABLE"]:
            self.assertIn(phrase, text)
        self.assertIn("instantaneous κ=0", text)

    def test_matrix_does_not_use_candidate_c_to_rescue_pointwise_candidates(self):
        with MATRIX.open(encoding="utf-8", newline="") as stream:
            rows = {row["candidate_id"]: row for row in csv.DictReader(stream)}
        row = rows["C"]
        self.assertEqual("ALTERNATIVE_HYPOTHESIS", row["hypothesis_class"])
        self.assertEqual("NON_IDENTIFIABLE", row["state"])
        self.assertIn("NOT_EQUIVALENT", row["evidence"])
        self.assertNotIn("rescue", " ".join(row.values()).lower())


if __name__ == "__main__":
    unittest.main()
