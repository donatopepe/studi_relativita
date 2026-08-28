import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status_alignment(self):
  e=(R/'audit/finite-window-operator-report-en.md').read_text();i=(R/'audit/finite-window-operator-report-it.md').read_text()
  for s in ['TOY_CONTROL_AND_NEGATIVE_RESULT','NONRADIAL_GEOMETRIC_SHAPE_NOT_ELL0_LANDMARK','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(s,e);self.assertIn(s,i)
 def test_theory_has_scope(self):
  t=(R/'theory/spacetime/finite-window-operator.md').read_text();self.assertIn('does not identify `ell0`',t);self.assertIn('does not trigger core reformulation',t)
if __name__=='__main__':unittest.main()
