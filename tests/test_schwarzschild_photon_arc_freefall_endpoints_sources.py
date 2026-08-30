import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class PhotonArcFreefallEndpointSourceTests(unittest.TestCase):
 def test_existing_canonical_context_entries_are_present(self):
  bib=(ROOT/'references/library.bib').read_text()
  self.assertIn('@article{Schwarzschild2003Translation',bib);self.assertIn('10.1023/A:1022971926521',bib)
  self.assertIn('@article{Darwin1959GravityField',bib);self.assertIn('10.1098/rspa.1959.0015',bib)
  self.assertIn('@article{Sachs1961',bib);self.assertIn('10.1098/rspa.1961.0202',bib)
 def test_verification_log_bounds_freefall_endpoint_claims(self):
  text=(ROOT/'references/verification-log.md').read_text()
  for token in ['photon-sphere finite arc with freely falling endpoint frames','Schwarzschild2003Translation','Darwin1959GravityField','Sachs1961','radial timelike geodesic','project derivation','release history','endpoint synchronization','screen preparation','frequency standard','vector readout','detector','covariance','`ell0`','UMCH','detection']:
   self.assertIn(token,text)
if __name__=='__main__':unittest.main()
