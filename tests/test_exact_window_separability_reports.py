import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/exact-window-separability-report-en.md').read_text();i=(R/'audit/exact-window-separability-report-it.md').read_text()
  for x in ['EXACT_PATTERN_CONTROL_AND_NEGATIVE_RESULT','EXACT_PATTERN_WINDOW_AVERAGING_REMAINS_PROJECTIVELY_RADIAL','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/exact-window-separability.md').read_text();self.assertIn('exact-pattern counterexample',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
