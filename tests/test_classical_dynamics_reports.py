import csv
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
IT = ROOT / "audit" / "classical-dynamics-report-it.md"
EN = ROOT / "audit" / "classical-dynamics-report-en.md"
DIM = ROOT / "audit" / "dimensional-analysis" / "classical-dynamics.md"
MATRIX = ROOT / "theory" / "classical-dynamics" / "decision-matrix.csv"


def keys(path):
    return re.findall(r"^## (UMCH-P2-\d{4})", path.read_text(encoding="utf-8"), re.MULTILINE)


class ClassicalDynamicsReportTests(unittest.TestCase):
    def test_bilingual_reports_have_matching_keys_and_candidate_states(self):
        self.assertEqual(keys(IT), keys(EN))
        self.assertGreaterEqual(len(keys(IT)), 7)
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            for token in ["Candidate A", "Candidate B", "Candidate C", "INCOMPLETE", "NON_IDENTIFIABLE", "UNPROVEN", "ALTERNATIVE_HYPOTHESIS"]:
                self.assertIn(token, text)
            self.assertIn("Paper III", text)
            self.assertIn("not blocked", text.lower())

    def test_reports_do_not_claim_pointwise_no_go_yet(self):
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            self.assertIn("NO_GO_NOT_ESTABLISHED", text)
            self.assertNotIn("both pointwise candidates are rejected", text.lower())
            self.assertNotIn("entrambi i candidati pointwise sono respinti", text.lower())

    def test_dimensional_report_covers_all_actions_and_observables(self):
        text = DIM.read_text(encoding="utf-8")
        for token in ["[κ₀] = L⁻¹", "[λ] = M L T⁻¹", "[ε] = 1", "[κRMS] = L⁻¹", "[S] = M L² T⁻¹"]:
            self.assertIn(token, text)
        self.assertIn("dimensionally consistent", text)
        self.assertIn("does not establish", text)

    def test_report_states_match_decision_matrix(self):
        with MATRIX.open(encoding="utf-8", newline="") as stream:
            rows = {row["candidate_id"]: row["state"] for row in csv.DictReader(stream)}
        self.assertEqual({"A": "INCOMPLETE", "B": "INCOMPLETE", "C": "NON_IDENTIFIABLE"}, rows)
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            for identifier, state in rows.items():
                self.assertRegex(text, rf"Candidate {identifier}[^\n]*`{state}`")


if __name__ == "__main__":
    unittest.main()
