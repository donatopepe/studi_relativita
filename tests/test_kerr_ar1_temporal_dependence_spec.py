import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-12-kerr-ar1-temporal-dependence.md';P=R/'doc/plans/2026-09-12-kerr-ar1-temporal-dependence.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','T_rho[t,s]=rho^|t-s|','alpha=tr(H T_rho H T_rho)','[0,0.25,0.5,0.75]','`88`','0.99','J87-J94','temporal_dependence','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr AR(1) temporal-dependence penalty MVP: tasks 1–5 completed',t);self.assertIn('scientific `8/8`, scenarios `94/94`, suite `1241/1241`',t);self.assertIn('estimated-mean milestone `4a84c16`',t)
if __name__=='__main__':unittest.main()
