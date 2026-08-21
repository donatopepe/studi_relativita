import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references" / "library.bib"
LOG = ROOT / "references" / "verification-log.md"


class BibliographyTests(unittest.TestCase):
    def entries(self):
        text = BIB.read_text(encoding="utf-8")
        matches = list(re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n\})", text, re.DOTALL))
        return [(match.group(1), match.group(2)) for match in matches]

    def test_starter_bibliography_has_unique_entries_and_required_fields(self):
        entries = self.entries()
        self.assertGreaterEqual(len(entries), 5)
        keys = [key for key, _ in entries]
        self.assertEqual(len(keys), len(set(keys)))
        for key, body in entries:
            for field in ("author", "title", "year", "doi", "url"):
                self.assertRegex(body, rf"\b{field}\s*=", f"{key} missing {field}")

    def test_doi_and_arxiv_identifiers_have_valid_syntax(self):
        text = BIB.read_text(encoding="utf-8")
        dois = re.findall(r"\bdoi\s*=\s*\{([^}]+)\}", text)
        self.assertGreaterEqual(len(dois), 5)
        for doi in dois:
            self.assertRegex(doi, r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
        arxiv_ids = re.findall(r"\beprint\s*=\s*\{([^}]+)\}", text)
        for identifier in arxiv_ids:
            self.assertRegex(identifier, r"^(?:[a-z-]+/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?$")

    def test_every_entry_has_verified_log_record(self):
        log = LOG.read_text(encoding="utf-8")
        for key, _ in self.entries():
            self.assertIn(f"## {key}", log)
        self.assertNotIn("VERIFIED: pending", log)
        self.assertGreaterEqual(log.count("Canonical metadata:"), 5)
        self.assertGreaterEqual(log.count("Exact supported topic:"), 5)
        self.assertGreaterEqual(log.count("Access date:"), 5)


if __name__ == "__main__":
    unittest.main()
