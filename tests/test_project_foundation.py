import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ProjectFoundationTests(unittest.TestCase):
    def test_required_public_files_exist(self):
        required = {
            ".gitignore",
            "README.md",
            "README.en.md",
            "LICENSE",
            "CITATION.cff",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
            "docs/ai-assistance.md",
        }
        missing = sorted(path for path in required if not (ROOT / path).is_file())
        self.assertEqual([], missing, f"Missing public project files: {missing}")

    def test_readmes_are_linked_and_describe_falsifiable_hypothesis(self):
        italian = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")

        self.assertIn("README.en.md", italian)
        self.assertIn("README.md", english)
        self.assertIn("κ₀", italian)
        self.assertIn("κ₀", english)
        self.assertIn("falsificabile", italian.lower())
        self.assertIn("falsifiable", english.lower())
        self.assertIn("non è un risultato acquisito", italian.lower())
        self.assertIn("is not an established result", english.lower())

    def test_author_and_license_metadata_are_consistent(self):
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("Pepe", citation)
        self.assertIn("Donato", citation)
        self.assertIn("donato.pepe.it@gmail.com", citation)
        self.assertIn("CC-BY-4.0", citation)
        self.assertIn("Creative Commons Attribution 4.0 International", license_text)
        self.assertIn("CC BY 4.0", readme)

    def test_ai_policy_rejects_ai_as_source_or_author(self):
        policy = (ROOT / "docs/ai-assistance.md").read_text(encoding="utf-8").lower()
        self.assertIn("non è una fonte scientifica", policy)
        self.assertIn("non è coautrice", policy)
        self.assertIn("verifica umana", policy)


if __name__ == "__main__":
    unittest.main()
