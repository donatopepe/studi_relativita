import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-12-kerr-estimated-mean-covariance.md';P=R/'doc/plans/2026-09-12-kerr-estimated-mean-covariance.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','nu=N-1','N/(N-1)','[16,64,256]','`54`','J79-J86','estimated_mean','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr estimated-mean covariance penalty MVP',t);self.assertIn('1. [x] Ratify estimated-mean covariance specification.',t);self.assertIn('2. [x] Extend authoritative Kerr scenario matrix and runner.',t);self.assertIn('3. [x] Implement estimated-mean covariance penalty engine.',t);self.assertIn('4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
