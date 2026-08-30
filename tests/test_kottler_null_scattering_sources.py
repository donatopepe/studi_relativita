import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class KottlerNullScatteringSourceTests(unittest.TestCase):
    def test_canonical_kottler_source_is_registered_and_verified(self):
        bib = (ROOT / "references/library.bib").read_text()
        log = (ROOT / "references/verification-log.md").read_text()
        self.assertIn("@article{RindlerIshak2007", bib)
        self.assertIn("10.1103/PhysRevD.76.043006", bib)
        self.assertIn("0709.2948", bib)
        self.assertIn("## RindlerIshak2007", log)
        self.assertIn("equations (1), (2), and (7)", log)

    def test_source_scope_excludes_project_inference(self):
        log = (ROOT / "references/verification-log.md").read_text()
        section = log.split("## RindlerIshak2007", 1)[1]
        self.assertIn("does not establish", section)
        for term in ("finite-window", "screen", "Jacobi", "receiver", "covariance", "ell0", "UMCH", "detection"):
            self.assertIn(term, section)

if __name__ == "__main__":
    unittest.main()
