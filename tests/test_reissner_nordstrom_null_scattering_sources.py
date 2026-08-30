import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class ReissnerNordstromNullScatteringSourceTests(unittest.TestCase):
    def test_canonical_rn_source_is_registered_and_verified(self):
        bib = (ROOT / "references/library.bib").read_text()
        log = (ROOT / "references/verification-log.md").read_text()
        self.assertIn("@article{EiroaRomeroTorres2002", bib)
        self.assertIn("10.1103/PhysRevD.66.024010", bib)
        self.assertIn("gr-qc/0203049", bib)
        self.assertIn("## EiroaRomeroTorres2002", log)
        self.assertIn("equations (6), (8), (10), and (11)", log)

    def test_source_scope_excludes_project_inference(self):
        log = (ROOT / "references/verification-log.md").read_text()
        section = log.split("## EiroaRomeroTorres2002", 1)[1]
        self.assertIn("does not establish", section)
        for term in ("finite-boundary", "Jacobi", "covariance", "ell0", "UMCH", "detection"):
            self.assertIn(term, section)


if __name__ == "__main__":
    unittest.main()
