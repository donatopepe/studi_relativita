import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/orientation-isotropization-report-en.md').read_text();i=(R/'audit/orientation-isotropization-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','ORIENTATION_WEIGHT_LANDMARK_PROTOCOL_MOVABLE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/orientation-isotropization.md').read_text();self.assertIn('protocol-movable',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
