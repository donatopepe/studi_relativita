import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"


class KerrFiniteBoundarySourceTests(unittest.TestCase):
    def test_gralla_lupsasca_source_is_registered(self):
        bib, log = BIB.read_text(), LOG.read_text()
        self.assertIn("@article{GrallaLupsasca2020KerrNullGeodesics", bib)
        self.assertIn("10.1103/PhysRevD.101.044032", bib)
        self.assertIn("1910.12881", bib)
        self.assertIn("## GrallaLupsasca2020KerrNullGeodesics", log)
        section = log.split("## GrallaLupsasca2020KerrNullGeodesics", 1)[1]
        for token in (
            "v3", "equations (1)-(13f)", "conserved quantities",
            "radial and angular potentials", "turning points",
            "source and observer integral form", "explicit parameterized solutions",
        ):
            self.assertIn(token, section)

    def test_source_does_not_define_project_endpoint_protocol(self):
        section = LOG.read_text().split("## GrallaLupsasca2020KerrNullGeodesics", 1)[1]
        for token in (
            "ZAMO endpoint tetrad", "physical emitter", "physical observer",
            "detector", "absolute clock", "screen transport", "covariance",
            "5D comparator", "ell0", "UMCH", "evidence", "detection",
        ):
            self.assertIn(token, section)


if __name__ == "__main__":
    unittest.main()
