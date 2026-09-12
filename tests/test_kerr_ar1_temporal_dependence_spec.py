import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-12-kerr-ar1-temporal-dependence.md';P=R/'doc/plans/2026-09-12-kerr-ar1-temporal-dependence.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','T_rho[t,s]=rho^|t-s|','alpha=tr(H T_rho H T_rho)','[0,0.25,0.5,0.75]','`88`','0.99','J87-J94','temporal_dependence','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr AR(1) temporal-dependence penalty MVP',t);self.assertIn('1. [x] Ratify AR(1) temporal-dependence specification.',t);self.assertIn('2. [x] Extend authoritative Kerr scenario matrix and runner.',t);self.assertIn('3. [x] Implement AR(1) covariance-penalty engine.',t);self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',t);self.assertIn('5. [ ] Closure and publication. **ACTIVE**',t)
if __name__=='__main__':unittest.main()
