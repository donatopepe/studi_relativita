import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-13-kerr-latent-window-jitter.md';P=R/'doc/plans/2026-09-13-kerr-latent-window-jitter.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','One latent integer lag `D`','law of total covariance','beta_latent=E_D','beta_latent>=beta_kernel','[87,87,87,87]','[87,88,88,88]','J119-J126','latent_pairing_jitter','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr latent window-jitter mixture MVP',t);self.assertIn('1. [ ] Ratify latent window-jitter specification. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
