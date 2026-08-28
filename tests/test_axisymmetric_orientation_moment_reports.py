import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/axisymmetric-orientation-moment-report-en.md').read_text();i=(R/'audit/axisymmetric-orientation-moment-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','AXISYMMETRIC_ORIENTATION_AVERAGE_SECOND_MOMENT_ONLY_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/axisymmetric-orientation-moment.md').read_text();self.assertIn('null space',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
