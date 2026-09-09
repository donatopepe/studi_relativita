import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"


class KerrPhotonRingSourceTests(unittest.TestCase):
    def test_teo_source_metadata_and_equations_are_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        self.assertIn("@article{Teo2003SphericalPhotonOrbits", bib)
        self.assertIn("10.1023/A:1026286607562", bib)
        self.assertIn("General Relativity and Gravitation", bib)
        self.assertIn("1909--1926", bib)
        self.assertIn("https://phyweb.physics.nus.edu.sg/~phyteoe/kerr/paper.pdf", bib)
        self.assertIn("## Teo2003SphericalPhotonOrbits", log)
        section = log.split("## Teo2003SphericalPhotonOrbits", 1)[1]
        for token in (
            "equations (1a,b), (2)-(5a-d), and (10)",
            "constant-radius conditions",
            "prograde and retrograde equatorial circular photon radii",
            "Boyer-Lindquist",
            "radial-potential conformance",
        ):
            self.assertIn(token, section)

    def test_source_scope_excludes_project_inference(self):
        section = LOG.read_text().split("## Teo2003SphericalPhotonOrbits", 1)[1]
        for token in (
            "transported screen",
            "Jacobi",
            "detector",
            "physical clock",
            "covariance",
            "ell0",
            "UMCH",
            "evidence",
            "detection",
        ):
            self.assertIn(token, section)


if __name__ == "__main__":
    unittest.main()
