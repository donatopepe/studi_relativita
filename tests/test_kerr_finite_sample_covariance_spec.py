import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-11-kerr-finite-sample-covariance.md';P=R/'doc/plans/2026-09-11-kerr-finite-sample-covariance.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','[16,64,256]','0.05','J71-J78','finite_sample','E||S_hat-C||_F^2','Wick','N=16','N=64','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr estimated-mean covariance penalty MVP',t);self.assertIn('finite-sample covariance milestone `686aa2b`',t)
if __name__=='__main__':unittest.main()
