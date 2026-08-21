import csv
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
THEORY = ROOT / "theory" / "classical-dynamics"
MATRIX = THEORY / "decision-matrix.csv"
CANDIDATES = {
    "A": THEORY / "candidate-a-hard-constraint.md",
    "B": THEORY / "candidate-b-barrier.md",
    "C": THEORY / "candidate-c-coarse-grained.md",
}
FIELDS = [
    "candidate_id", "name", "hypothesis_class", "domain", "action",
    "analysis_level", "differential_order", "constraints", "standard_limit",
    "observable", "evidence", "state", "blocking_issue",
]
STATES = {
    "VIABLE_WITHIN_TESTED_SCOPE", "VIABLE_WITH_CONDITIONS", "INCOMPLETE",
    "NON_IDENTIFIABLE", "CONTRADICTED_UNDER_ASSUMPTIONS", "REJECTED",
}


class ClassicalDynamicsSchemaTests(unittest.TestCase):
    def rows(self):
        with MATRIX.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            self.assertEqual(FIELDS, reader.fieldnames)
            return list(reader)

    def test_candidate_documents_exist_and_state_epistemic_limits(self):
        for identifier, path in CANDIDATES.items():
            self.assertTrue(path.is_file(), identifier)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"Candidate {identifier}", text)
            self.assertIn("UNPROVEN", text)
            self.assertIn("Analysis level", text)
            self.assertIn("Standard limit", text)
        self.assertIn("ALTERNATIVE_HYPOTHESIS", CANDIDATES["C"].read_text(encoding="utf-8"))

    def test_decision_matrix_has_one_reviewed_row_per_candidate(self):
        rows = self.rows()
        self.assertEqual(["A", "B", "C"], [row["candidate_id"] for row in rows])
        self.assertTrue(all(row["state"] in STATES for row in rows))
        self.assertEqual(["INCOMPLETE", "INCOMPLETE", "NON_IDENTIFIABLE"], [row["state"] for row in rows])
        self.assertEqual("POINTWISE_UMCH", rows[0]["hypothesis_class"])
        self.assertEqual("POINTWISE_UMCH", rows[1]["hypothesis_class"])
        self.assertEqual("ALTERNATIVE_HYPOTHESIS", rows[2]["hypothesis_class"])
        for row in rows:
            self.assertTrue(row["domain"])
            self.assertTrue(row["action"])
            self.assertTrue(row["blocking_issue"])

    def test_unevaluated_rows_do_not_claim_stability_or_viability(self):
        for row in self.rows():
            joined = " ".join(row.values()).lower()
            self.assertNotIn("proven stable", joined)
            self.assertNotIn("validated", joined)
            self.assertNotIn("established lower bound", joined)


if __name__ == "__main__":
    unittest.main()
