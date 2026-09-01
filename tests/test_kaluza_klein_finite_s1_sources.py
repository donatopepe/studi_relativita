import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"


class FiniteS1SourceTests(unittest.TestCase):
    def test_dlmf_metadata_and_exact_equations_are_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        self.assertIn("@misc{NISTDLMF", bib)
        self.assertIn("10.18434/M3167", bib)
        self.assertIn("Release 1.2.7", bib)
        self.assertIn("## NISTDLMF", log)
        section = log.split("## NISTDLMF", 1)[1].split("\n## ", 1)[0]
        for token in (
            "section 1.8(iv), equation (1.8.14)",
            "section 20.2(i), equation (20.2.3)",
            "https://dlmf.nist.gov/1.8.E14",
            "https://dlmf.nist.gov/20.2.E3",
            "Poisson summation",
            "theta-3 Fourier series",
        ):
            self.assertIn(token, section)

    def test_source_scope_excludes_physical_localization_and_inference(self):
        section = LOG.read_text().split("## NISTDLMF", 1)[1].split("\n## ", 1)[0]
        self.assertIn("does not establish", section)
        for token in (
            "Kaluza-Klein matter-localization mechanism",
            "source preparation",
            "probe preparation",
            "gravitational coupling",
            "finite-window",
            "covariance",
            "data",
            "ell0",
            "UMCH",
            "evidence",
            "detection",
        ):
            self.assertIn(token, section)


if __name__ == "__main__":
    unittest.main()
