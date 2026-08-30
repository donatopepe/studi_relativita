import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "theory/spacetime/schwarzschild-scattering-screen-conformance.md",
    ROOT / "audit/schwarzschild-scattering-screen-conformance-report-en.md",
    ROOT / "audit/schwarzschild-scattering-screen-conformance-report-it.md",
]
KEYS = ["Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961"]


class SchwarzschildScatteringScreenConformanceSourceTests(unittest.TestCase):
    def test_source_scope_is_bounded(self):
        for path in FILES:
            text = path.read_text()
            for key in KEYS:
                self.assertIn(key, text)
            self.assertIn("KNOWN_RESULT", text)
            self.assertIn("PROJECT_DERIVATION", text)
            self.assertIn("TOY_CONTROL", text)
            self.assertIn("NEGATIVE_RESULT", text)
            self.assertIn("OPEN_PROBLEM", text)
            self.assertIn("detector", text.lower())
            self.assertIn("covariance", text.lower())
            self.assertIn("ell0", text)
            self.assertIn("do not establish", text.lower())


if __name__ == "__main__":
    unittest.main()
