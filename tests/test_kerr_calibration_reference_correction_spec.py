import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-11-kerr-calibration-reference-placement-correction.md';P=R/'doc/plans/2026-09-11-kerr-calibration-reference-placement-correction.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_CORRECTION_FOR_IMMEDIATE_IMPLEMENTATION','exactly `8/8`','reversed collision polarity','R_inside=[0.1,10.0]','R_outside=[0.02,0.02]','J47-J54','reference_placement','KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr finite-sample covariance uncertainty MVP',t);self.assertIn('correlated-noise mismatch milestone `bba10b3`',t)
if __name__=='__main__':unittest.main()
