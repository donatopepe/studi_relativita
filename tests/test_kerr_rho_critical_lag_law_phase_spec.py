import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-13-kerr-rho-critical-lag-law-phase.md';P=R/'doc/plans/2026-09-13-kerr-rho-critical-lag-law-phase.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','r_unrestricted(rho_low)=0.05','r_uniform(rho_high)=0.05','[0.49,0.51]','rho_low=0.499243438917','rho_high=0.501157235677','FINITE_KAPPA_SENSITIVE','[12.485595532,3.890241565,2.001949812,1.172518080]','J143-J150','latent_lag_rho_phase','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr rho-critical phase window MVP: tasks 1–5 completed',t);self.assertIn('scientific `8/8`, scenarios `150/150`, suite `1332/1332`',t)
if __name__=='__main__':unittest.main()
