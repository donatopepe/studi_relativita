import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"


class KaluzaKleinTensorSourceTests(unittest.TestCase):
    def test_arbitrary_dimension_linearized_source_is_narrowly_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        self.assertIn("@article{Robinson2006Normalization", bib)
        self.assertIn("gr-qc/0609060", bib)
        self.assertIn("10.48550/arXiv.gr-qc/0609060", bib)
        self.assertIn("## Robinson2006Normalization", log)
        section = log.split("## Robinson2006Normalization", 1)[1]
        for token in (
            "equations (1), (2a,b), (4), (5a,b), (6a,b), (7a-c), and (9)-(15)",
            "d=5 trace-reversal ratios",
            "harmonic gauge",
            "Newtonian potential",
            "geodesic-deviation sign convention",
            "does not establish the compact-circle profile",
        ):
            self.assertIn(token, section)

    def test_five_dimensional_curvature_context_is_narrowly_registered(self):
        bib = BIB.read_text()
        log = LOG.read_text()
        self.assertIn("@article{AtondoRubio2008Linearized5D", bib)
        self.assertIn("hep-th/0609133", bib)
        self.assertIn("Revista Mexicana de Fisica", bib)
        self.assertIn("## AtondoRubio2008Linearized5D", log)
        section = log.split("## AtondoRubio2008Linearized5D", 1)[1]
        for token in (
            "equations (4)-(19)",
            "linearized metric, connection, Riemann, Ricci, and Einstein equations",
            "equations (21)-(23)",
            "cylinder ansatz",
            "h_44=0",
            "must not be imported",
            "localized compact-circle calculation",
        ):
            self.assertIn(token, section)

    def test_sources_do_not_authorize_physical_inference(self):
        log = LOG.read_text()
        for heading in ("Robinson2006Normalization", "AtondoRubio2008Linearized5D"):
            section = log.split("## " + heading, 1)[1]
            for token in (
                "radion stabilization",
                "L=ell0",
                "UMCH",
                "evidence",
                "detection",
            ):
                self.assertIn(token, section)


if __name__ == "__main__":
    unittest.main()
