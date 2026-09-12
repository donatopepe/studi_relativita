import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-12-kerr-bounded-pairing-lag.md';P=R/'doc/plans/2026-09-12-kerr-bounded-pairing-lag.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','K_L[t,s]=rho^|t-s-L|','beta=tr(H K_L H K_L^T)','round_half_up','[0,0.25,0.5,1.0]','[87,87,87,88]','J103-J110','pairing_lag','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr bounded pairing-lag erosion MVP',t);self.assertIn('1. [ ] Ratify bounded pairing-lag specification. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
