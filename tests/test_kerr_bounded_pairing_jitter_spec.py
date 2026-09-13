import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-13-kerr-bounded-pairing-jitter.md';P=R/'doc/plans/2026-09-13-kerr-bounded-pairing-jitter.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','P(D=d)=1/(2J+1)','K_J[t,s]','beta_J=tr(H K_J H K_J^T)','J=[0,1,2,4,8,16]','[87,87,87,87,87,88]','J111-J118','pairing_jitter','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr bounded pairing-jitter erosion MVP: tasks 1–5 completed',t);self.assertIn('scientific `8/8`, scenarios `118/118`, suite `1280/1280`',t)
if __name__=='__main__':unittest.main()
