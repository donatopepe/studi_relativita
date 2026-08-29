import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/schwarzschild-shell-cap-report-en.md').read_text();i=(R/'audit/schwarzschild-shell-cap-report-it.md').read_text()
  for x in ['EXACT_PATTERN_WINDOW_CONTROL_AND_NEGATIVE_RESULT','SCHWARZSCHILD_PRODUCT_SHELL_CAP_REMAINS_FACTORABLE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/schwarzschild-shell-cap.md').read_text();self.assertIn('factor',t);self.assertIn('not Schwarzschild bitensor',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
