import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/schwarzschild-orientation-average-report-en.md').read_text();i=(R/'audit/schwarzschild-orientation-average-report-it.md').read_text()
  for x in ['EXACT_PATTERN_CONTROL_AND_NEGATIVE_RESULT','SCHWARZSCHILD_CAP_AVERAGE_SIGN_REVERSAL_ORIENTATION_DOMAIN_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/schwarzschild-orientation-average.md').read_text();self.assertIn('orientation-measure/domain landmark',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
