import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-10-kerr-common-calibration-robustness.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  text=S.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','[0.5,1.5]','[0.1,1.0]','J23','J30','30/30','common-map difference identity','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,text)
  todo=T.read_text();self.assertIn('Kerr correlated-noise mismatch threshold MVP',todo);self.assertIn('bounded reference-drift milestone `b1ca8a8`',todo)
if __name__=='__main__':unittest.main()
