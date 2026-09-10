import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = ROOT / "references/verification-log.md"
BIB = ROOT / "references/library.bib"


class KerrParallelScreenSourceTests(unittest.TestCase):
    def test_existing_sources_are_scoped_to_path_and_parallel_screen(self):
        bib, log = BIB.read_text(), LOG.read_text()
        for key in ("GrallaLupsasca2020KerrNullGeodesics", "Dolan2018GeometricalOptics"):
            self.assertIn("@article{" + key, bib)
            self.assertIn("## " + key, log)
        section = log.split("## Dolan2018GeometricalOptics", 1)[1]
        for token in (
            "sections 3.1-3.3 and 4.1", "equations (20)-(28)",
            "parallel transport", "transversality", "null tetrad",
            "does not establish the Kerr ZAMO endpoint joining",
            "Jacobi tidal map", "detector", "5D comparator", "ell0", "detection",
        ):
            self.assertIn(token, section)


if __name__ == "__main__":
    unittest.main()
