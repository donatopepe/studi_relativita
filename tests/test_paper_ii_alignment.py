import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
IT = ROOT / "papers" / "classical-dynamics" / "it" / "main.tex"
EN = ROOT / "papers" / "classical-dynamics" / "en" / "main.tex"
README = ROOT / "papers" / "classical-dynamics" / "README.md"
CI = ROOT / ".github" / "workflows" / "verify.yml"


def labels(text):
    return set(re.findall(r"\\label\{([^}]+)\}", text))


def citations(text):
    found = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        found.update(item.strip() for item in group.split(","))
    return found


class PaperIIAlignmentTests(unittest.TestCase):
    def test_sources_have_aligned_labels_and_citations(self):
        italian = IT.read_text(encoding="utf-8")
        english = EN.read_text(encoding="utf-8")
        self.assertEqual(labels(italian), labels(english))
        self.assertGreaterEqual(len(labels(italian)), 12)
        self.assertEqual(citations(italian), citations(english))
        self.assertTrue({"ArreagaCapovillaGuven2001", "CapovillaGuvenRojas2002", "NesterenkoEtAl1995"} <= citations(italian))

    def test_both_versions_preserve_candidate_states_and_gate(self):
        for path in (IT, EN):
            text = path.read_text(encoding="utf-8")
            for token in ["UNPROVEN", "INCOMPLETE", "NON\\_IDENTIFIABLE", "ALTERNATIVE\\_HYPOTHESIS", "NO\\_GO\\_NOT\\_ESTABLISHED"]:
                self.assertIn(token, text)
            self.assertIn(r"\kappa_0", text)
            self.assertIn("Paper III", text)
            self.assertNotRegex(text, r"(?i)(we prove|dimostriamo).*\\kappa_0>0")

    def test_required_sections_are_aligned(self):
        required = {
            "sec:p2-status", "sec:p2-method", "sec:p2-a", "sec:p2-b", "sec:p2-c",
            "sec:p2-dimensions", "sec:p2-stability", "sec:p2-limits",
            "sec:p2-observables", "sec:p2-decision", "sec:p2-limitations", "sec:p2-ai",
        }
        self.assertTrue(required <= labels(IT.read_text(encoding="utf-8")))
        self.assertTrue(required <= labels(EN.read_text(encoding="utf-8")))

    def test_readme_and_ci_compile_both_languages(self):
        readme = README.read_text(encoding="utf-8")
        workflow = CI.read_text(encoding="utf-8")
        self.assertIn("NOT COMPILED LOCALLY", readme)
        self.assertIn("papers/classical-dynamics/it", workflow)
        self.assertIn("papers/classical-dynamics/en", workflow)
        self.assertGreaterEqual(workflow.count("bibtex main"), 4)
        self.assertIn("papers/classical-dynamics/it/main.pdf", workflow)
        self.assertIn("papers/classical-dynamics/en/main.pdf", workflow)


if __name__ == "__main__":
    unittest.main()
