import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-13-kerr-bounded-latent-lag-law.md';P=R/'doc/plans/2026-09-13-kerr-bounded-latent-lag-law.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','u/kappa <= p_d <= kappa*u','kappa in [1,2,4]','greedily allocating','[87,87,87,87]','[87,87,87,88]','J127-J134','latent_lag_law_robustness','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr bounded latent-lag law robustness MVP',t);self.assertIn('1. [ ] Ratify bounded latent-lag law specification. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
