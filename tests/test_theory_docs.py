import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class TheoryDocumentationTests(unittest.TestCase):
    def test_required_theory_and_audit_documents_exist(self):
        paths = [
            "theory/definitions.md", "theory/assumptions.md", "theory/notation.md",
            "theory/limiting-cases.md", "theory/open-problems.md",
            "audit/contradiction-log.md", "docs/glossary-it.md", "docs/glossary-en.md",
        ]
        self.assertEqual([], [path for path in paths if not (ROOT / path).is_file()])

    def test_definitions_keep_distinct_geometric_objects(self):
        text = (ROOT / "theory" / "definitions.md").read_text(encoding="utf-8").lower()
        for term in ["spacetime curvature", "geodesic curvature", "proper acceleration", "timelike", "null curve", "field observable", "vacuum observable"]:
            self.assertIn(term, text)
        self.assertIn("not identified", text)
        self.assertIn("conjecture", text)

    def test_notation_declares_units_and_standard_limit(self):
        notation = (ROOT / "theory" / "notation.md").read_text(encoding="utf-8")
        limits = (ROOT / "theory" / "limiting-cases.md").read_text(encoding="utf-8")
        self.assertIn("[κ₀] = L⁻¹", notation)
        self.assertIn("[c] = L T⁻¹", notation)
        self.assertIn("κ₀ → 0", limits)
        self.assertIn("general relativity", limits.lower())
        self.assertIn("special relativity", limits.lower())

    def test_bilingual_glossaries_have_matching_keys(self):
        pattern = re.compile(r"^## (UMCH-TERM-\d{4})", re.MULTILINE)
        italian = pattern.findall((ROOT / "docs" / "glossary-it.md").read_text(encoding="utf-8"))
        english = pattern.findall((ROOT / "docs" / "glossary-en.md").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(italian), 8)
        self.assertEqual(italian, english)


if __name__ == "__main__":
    unittest.main()
