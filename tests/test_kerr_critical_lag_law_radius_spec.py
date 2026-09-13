import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-13-kerr-critical-lag-law-radius.md';P=R/'doc/plans/2026-09-13-kerr-critical-lag-law-radius.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','N=87','m=floor(n/(kappa+1))','beta_min(kappa)=A_m*kappa+B_m/kappa+C_m','[2,4]','kappa*=3.89024156496','m=35','J135-J142','latent_lag_critical_radius','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr critical lag-law radius MVP',t);self.assertIn('1. [ ] Ratify critical density-ratio specification. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
