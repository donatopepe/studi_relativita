import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-14-kerr-count-dependent-rho-phase.md';P=R/'doc/plans/2026-09-14-kerr-count-dependent-rho-phase.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','rho_low(N)','rho_high(N)','N=[53,54,64,87,128,256]','0.0500676203','0.0491228897','0.084265333564','0.815322224235','0.011608541494','0.000693548809','ALWAYS_UNSAFE_FROM_RHO_ZERO','J151-J158','latent_lag_count_phase','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr count-dependent rho phase MVP',t);self.assertIn('1. [ ] Ratify count-dependent rho phase specification. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
