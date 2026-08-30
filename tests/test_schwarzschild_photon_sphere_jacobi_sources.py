import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class PhotonSphereJacobiSourceTests(unittest.TestCase):
 def test_existing_canonical_entries_are_present(self):
  bib=(ROOT/'references/library.bib').read_text()
  self.assertIn('@article{Darwin1959GravityField',bib);self.assertIn('10.1098/rspa.1959.0015',bib)
  self.assertIn('@article{Sachs1961',bib);self.assertIn('10.1098/rspa.1961.0202',bib)
 def test_verification_log_bounds_project_specific_claims(self):
  text=(ROOT/'references/verification-log.md').read_text()
  for token in ['Darwin1959GravityField','Sachs1961','photon-sphere Jacobi','project affine normalization','endpoint screen','finite-window phase map','caustic readout','detector','covariance','`ell0`','UMCH','detection']:
   self.assertIn(token,text)
if __name__=='__main__':unittest.main()
