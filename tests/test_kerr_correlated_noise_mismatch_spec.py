import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-11-kerr-correlated-noise-mismatch.md';P=R/'doc/plans/2026-09-11-kerr-correlated-noise-mismatch.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','N=[[0.4,0.12],[0.12,0.7]]','0.8*tau','J63-J70','calibration_mismatch','spectral/operator norm','KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr estimated-mean covariance penalty MVP',t);self.assertIn('finite-sample covariance milestone `686aa2b`',t)
if __name__=='__main__':unittest.main()
