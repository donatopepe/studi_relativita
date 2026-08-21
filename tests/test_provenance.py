import hashlib
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "original"
SOURCE_NAME = "Dimostrazione e Prove Relatività Einstein.docx"


class ProvenanceTests(unittest.TestCase):
    def test_original_is_archived_once(self):
        sources = list(ARCHIVE.glob("*.docx")) if ARCHIVE.exists() else []
        self.assertEqual([SOURCE_NAME], [path.name for path in sources])
        self.assertFalse((ROOT / SOURCE_NAME).exists())

    def test_checksum_matches_original(self):
        source = ARCHIVE / SOURCE_NAME
        checksum_file = ARCHIVE / "SHA256SUMS"
        self.assertTrue(checksum_file.is_file())
        line = checksum_file.read_text(encoding="utf-8").strip()
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        self.assertIsNotNone(match)
        expected, filename = match.groups()
        self.assertEqual(SOURCE_NAME, filename)
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        self.assertEqual(expected, actual)

    def test_provenance_records_origin_and_limitations(self):
        provenance = (ROOT / "archive" / "provenance.md").read_text(encoding="utf-8")
        self.assertIn("b438381", provenance)
        self.assertIn("SHA-256", provenance)
        self.assertIn("AI-assisted", provenance)
        self.assertIn("equation", provenance.lower())
        self.assertIn("historical source", provenance.lower())
        self.assertIn(SOURCE_NAME, provenance)


if __name__ == "__main__":
    unittest.main()
