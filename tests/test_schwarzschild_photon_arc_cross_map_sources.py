import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class PhotonArcCrossMapSourceTests(unittest.TestCase):
 def test_existing_canonical_entries_are_present(self):
  bib=(ROOT/'references/library.bib').read_text()
  self.assertIn('@article{Darwin1959GravityField',bib);self.assertIn('10.1098/rspa.1959.0015',bib)
  self.assertIn('@article{Sachs1961',bib);self.assertIn('10.1098/rspa.1961.0202',bib)
 def test_verification_log_bounds_finite_arc_claims(self):
  text=(ROOT/'references/verification-log.md').read_text()
  for token in ['photon-sphere finite-arc cross-map','Darwin1959GravityField','Sachs1961','critical circular-orbit context','null optical framework','open-arc transport','endpoint tetrads','finite-window selection','affine frequency standard','caustic continuation','vector readout','detector','covariance','`ell0`','UMCH','detection']:
   self.assertIn(token,text)
if __name__=='__main__':unittest.main()
