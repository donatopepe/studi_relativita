import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "studies/spacetime/plane-wave-canonical-screen-phase-results.json"
THEORY = ROOT / "theory/spacetime/plane-wave-canonical-screen-phase.md"
SPEC = ROOT / "doc/specs/2026-08-29-plane-wave-canonical-rotating-screen.md"
PLAN = ROOT / "doc/plans/2026-08-29-plane-wave-canonical-rotating-screen.md"
REPORTS = [ROOT / "audit/plane-wave-canonical-screen-phase-report-en.md", ROOT / "audit/plane-wave-canonical-screen-phase-report-it.md"]


class CanonicalScreenPhaseReportTests(unittest.TestCase):
    def test_authority_files_exist(self):
        for path in [ARTIFACT, THEORY, SPEC, PLAN, *REPORTS]:
            self.assertTrue(path.exists(), path)

    def test_bilingual_status_gate_and_limits(self):
        data = json.loads(ARTIFACT.read_text())
        required = [data["classification"], data["status"], data["open_gate"], "UNPROVEN", "NO_POSITIVE_DETECTION_CLAIM", "Coley", "ell0", "not a structural dead end"]
        en = REPORTS[0].read_text()
        it = REPORTS[1].read_text()
        for token in required[:7]:
            self.assertIn(token, en)
            self.assertIn(token, it)
        self.assertIn("non è un vicolo cieco strutturale", it)

    def test_correction_ledger_and_equations_present(self):
        combined = THEORY.read_text() + SPEC.read_text() + REPORTS[0].read_text() + REPORTS[1].read_text()
        for token in ["p=x'+Ax", "P_c", "H(A_o)", "PR #77", "velocity", "calibrazione", "0.32091041757227023", "0.49508910842587517"]:
            self.assertIn(token, combined)


if __name__ == "__main__":
    unittest.main()
