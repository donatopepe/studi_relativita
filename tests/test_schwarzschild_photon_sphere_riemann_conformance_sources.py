import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "audit/schwarzschild-photon-sphere-riemann-conformance-report-en.md",
    ROOT / "audit/schwarzschild-photon-sphere-riemann-conformance-report-it.md",
    ROOT / "theory/spacetime/schwarzschild-photon-sphere-riemann-conformance.md",
]


class SchwarzschildPhotonSphereRiemannConformanceSourceTests(unittest.TestCase):
    def test_only_bounded_canonical_keys_are_used(self):
        for path in FILES:
            text = path.read_text()
            for key in ("Schwarzschild2003Translation", "Darwin1959GravityField", "Sachs1961"):
                self.assertIn(key, text)
            self.assertIn("detector", text.lower())
            self.assertTrue("do not establish" in text.lower() or "non stabiliscono" in text.lower())

    def test_reports_do_not_turn_sources_into_umch_support(self):
        for path in FILES:
            text = path.read_text().lower()
            for forbidden in ("source establishes umch", "source proves umch", "fonte dimostra umch", "fonte stabilisce umch"):
                self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
