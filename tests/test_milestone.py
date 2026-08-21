import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class InitialMilestoneTests(unittest.TestCase):
    def test_ci_workflow_runs_required_checks_and_latex(self):
        workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
        for command in [
            "python3 -m unittest discover -s tests -v",
            "python3 tools/extract_docx.py --check",
            "python3 tools/inventory_source.py --check",
            "python3 studies/free-fall-identifiability/analysis.py --check",
            "pdflatex",
            "bibtex",
        ]:
            self.assertIn(command, workflow)
        self.assertIn("ubuntu-latest", workflow)

    def test_bilingual_overviews_have_matching_section_keys(self):
        pattern = re.compile(r"^## (UMCH-OV-\d{4})", re.MULTILINE)
        italian = (ROOT / "docs" / "overview-it.md").read_text(encoding="utf-8")
        english = (ROOT / "docs" / "overview-en.md").read_text(encoding="utf-8")
        self.assertEqual(pattern.findall(italian), pattern.findall(english))
        self.assertGreaterEqual(len(pattern.findall(italian)), 6)
        for text in (italian, english):
            self.assertIn("UNPROVEN", text)
            self.assertIn("NO_BOUND_DERIVABLE", text)

    def test_roadmap_and_falsification_are_concrete(self):
        roadmap = (ROOT / "docs" / "roadmap.md").read_text(encoding="utf-8")
        falsification = (ROOT / "docs" / "falsification.md").read_text(encoding="utf-8")
        for phase in ["Paper II", "Paper III", "Paper IV", "Paper V", "Paper VI", "Paper VII"]:
            self.assertIn(phase, roadmap)
        self.assertIn("Completed initial milestone", roadmap)
        for criterion in ["covariance", "instability", "κ₀ → 0", "observational", "no new observable"]:
            self.assertIn(criterion.lower(), falsification.lower())

    def test_readme_links_resolve(self):
        for filename in ("README.md", "README.en.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                self.assertTrue((ROOT / target).exists(), f"Broken link in {filename}: {target}")


if __name__ == "__main__":
    unittest.main()
