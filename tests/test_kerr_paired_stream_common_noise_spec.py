import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-12-kerr-paired-stream-common-noise.md';P=R/'doc/plans/2026-09-12-kerr-paired-stream-common-noise.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','Cov(x_t,y_t)=K=N','q(C_S)+q(C_B)-2 q(K)','[0.99,1.0)','`87`','`88`','J95-J102','cross_stream_dependence','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr paired-stream common-noise cancellation MVP: tasks 1–5 completed',t);self.assertIn('scientific `8/8`, scenarios `102/102`, suite `1254/1254`',t)
if __name__=='__main__':unittest.main()
