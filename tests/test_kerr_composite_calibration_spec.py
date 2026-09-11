import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-11-kerr-composite-calibration-profile.md';P=R/'doc/plans/2026-09-11-kerr-composite-calibration-profile.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','J31-J38','profiling','g1,g2 in [0.5,1.5]','n in [0.1,1.0]','Composite-hypothesis profiling','MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr composite common-calibration profile gate MVP',t);self.assertIn('1. [x] Ratify composite-hypothesis profile specification.',t);self.assertIn('2. [ ] Extend authoritative Kerr scenario matrix and runner. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
