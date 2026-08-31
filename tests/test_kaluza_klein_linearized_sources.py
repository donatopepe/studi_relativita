import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"


class KaluzaKleinLinearizedSourceTests(unittest.TestCase):
    def test_exact_compact_circle_potential_source_is_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        self.assertIn("@article{Liu2003CompactifiedPotential", bib)
        self.assertIn("hep-ph/0312200", bib)
        self.assertIn("## Liu2003CompactifiedPotential", log)
        section = log.split("## Liu2003CompactifiedPotential", 1)[1]
        for token in (
            "equations (3), (6), (7), (8), (13), and (14)",
            "L=2*pi*R",
            "G4=G5/(4*R)",
            "exact compact-circle point potential",
            "large-distance expansion",
        ):
            self.assertIn(token, section)

    def test_fourier_tower_and_asymptotic_sources_are_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        for key, doi, arxiv in (
            ("FloratosLeontaris1999", "10.1016/S0370-2693(99)01019-9", "hep-ph/9906238"),
            ("KehagiasSfetsos2000", "10.1016/S0370-2693(99)01421-5", "hep-ph/9905417"),
        ):
            self.assertIn("@article{" + key, bib)
            self.assertIn(doi, bib)
            self.assertIn(arxiv, bib)
            self.assertIn("## " + key, log)
        floratos = log.split("## FloratosLeontaris1999", 1)[1]
        for token in ("equations (6), (7), (10), (11), (14), and (15)", "full KK tower", "short-distance", "long-distance Yukawa"):
            self.assertIn(token, floratos)
        kehagias = log.split("## KehagiasSfetsos2000", 1)[1]
        for token in ("equations (1), (9), (10), (11), (12), (13), and (19)", "lightest KK", "degeneracy", "range"):
            self.assertIn(token, kehagias)

    def test_source_scope_excludes_project_inference(self):
        log = LOG.read_text()
        for key in ("Liu2003CompactifiedPotential", "FloratosLeontaris1999", "KehagiasSfetsos2000"):
            section = log.split("## " + key, 1)[1].split("\n## ", 1)[0]
            self.assertIn("does not establish", section)
            for token in (
                "finite-window",
                "source preparation",
                "probe preparation",
                "identifiability",
                "receiver",
                "covariance",
                "ell0",
                "UMCH",
                "detection",
            ):
                self.assertIn(token, section)

    def test_tensor_interpretation_remains_bounded(self):
        section = LOG.read_text().split("## Liu2003CompactifiedPotential", 1)[1].split("\n## ", 1)[0]
        self.assertIn("Newtonian scalar potential", section)
        self.assertIn("does not establish a complete five-dimensional tensor perturbation", section)
        self.assertIn("tidal Hessian is a project weak-field derivation", section)


if __name__ == "__main__":
    unittest.main()
