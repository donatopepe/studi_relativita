import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/finite-holonomy-ordering-report-en.md').read_text();i=(R/'audit/finite-holonomy-ordering-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','FINITE_HOLONOMY_RAW_ORDER_DIFF_CONJUGACY_AMBIGUOUS','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/finite-holonomy-ordering.md').read_text();self.assertIn('cyclic re-anchoring',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
