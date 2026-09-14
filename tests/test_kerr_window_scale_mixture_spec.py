import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-14-kerr-window-scale-mixture.md';P=R/'doc/plans/2026-09-14-kerr-window-scale-mixture.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','E[W]=1','Var(W)=cv^2','MSE_scale(N,cv)','Delta_coefficient=304.907367059628','floor_risk(cv)=0.862883522363*cv^2','[0,0.1,0.2,0.25]','[87,106,292,None]','cv*=0.240718192810','J159-J166','window_scale_mixture','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr window-scale mixture floor MVP',t);self.assertIn('1. [x] Ratify window-scale mixture specification.',t)
if __name__=='__main__':unittest.main()
