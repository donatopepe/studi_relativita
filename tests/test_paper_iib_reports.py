import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
IT = ROOT / "audit" / "paper-iib-report-it.md"
EN = ROOT / "audit" / "paper-iib-report-en.md"
PIT = ROOT / "papers" / "classical-dynamics" / "it" / "barrier-appendix.tex"
PEN = ROOT / "papers" / "classical-dynamics" / "en" / "barrier-appendix.tex"
CI = ROOT / ".github" / "workflows" / "verify.yml"


def headings(path):
    return re.findall(r"^## (UMCH-P2B-\d{4})", path.read_text(encoding="utf-8"), re.MULTILINE)


def labels(path):
    return set(re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")))


class PaperIIBReportTests(unittest.TestCase):
    def test_bilingual_audit_reports_align_and_preserve_scope(self):
        self.assertEqual(headings(IT), headings(EN))
        self.assertGreaterEqual(len(headings(IT)), 8)
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            for token in ["CONTRADICTED_UNDER_ASSUMPTIONS", "BLOCKED", "UNPROVEN", "Lκκ", "two first-class", "local planar", "nonuniform"]:
                self.assertIn(token, text)
            self.assertIn("not a full", text.lower())

    def test_bilingual_latex_appendices_align(self):
        self.assertEqual(labels(PIT), labels(PEN))
        required = {"sec:p2b-model", "sec:p2b-canonical", "sec:p2b-stationary", "sec:p2b-limit", "sec:p2b-gate", "sec:p2b-limits", "sec:p2b-ai"}
        self.assertTrue(required <= labels(PIT))
        for path in (PIT, PEN):
            text = path.read_text(encoding="utf-8")
            self.assertIn(r"\kappa_0", text)
            self.assertIn(r"\texttt{BLOCKED}", text)
            self.assertIn(r"\texttt{CONTRADICTED\_UNDER\_ASSUMPTIONS}", text)
            self.assertIn("ArreagaCapovillaGuven2001", text)
            self.assertIn("CapovillaGuvenRojas2002", text)

    def test_ci_compiles_appendices(self):
        workflow = CI.read_text(encoding="utf-8")
        self.assertIn("barrier-appendix.tex", workflow)
        self.assertIn("barrier-appendix-it.pdf", workflow)
        self.assertIn("barrier-appendix-en.pdf", workflow)


if __name__ == "__main__":
    unittest.main()
