import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-scattering-polarization-screen-report-en.md",
    ROOT / "audit/schwarzschild-scattering-polarization-screen-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-scattering-polarization-screen.md",
]


class SchwarzschildScatteringPolarizationScreenSourceTests(unittest.TestCase):
    def test_source_scope_is_bounded(self):
        for path in FILES:
            text = path.read_text()
            for key in ("Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961", "Dolan2018GeometricalOptics"):
                self.assertIn(key, text)
            self.assertTrue("do not establish" in text.lower() or "non stabiliscono" in text.lower())

    def test_sources_are_not_promoted(self):
        for path in FILES:
            text = path.read_text().lower()
            for forbidden in ("source proves umch", "source establishes umch", "source derives ell0", "fonte dimostra umch", "fonte stabilisce umch", "fonte deriva ell0"):
                self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
