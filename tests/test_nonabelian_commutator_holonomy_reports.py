import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/nonabelian-commutator-holonomy-report-en.md').read_text();i=(R/'audit/nonabelian-commutator-holonomy-report-it.md').read_text()
  for x in ['EXACT_GROUP_TOY_CONTROL_AND_NEGATIVE_RESULT','NONABELIAN_COMMUTATOR_TRACE_PRODUCT_DEGENERACY_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/nonabelian-commutator-holonomy.md').read_text();self.assertIn('do not by themselves',t);self.assertIn('No four-dimensional spacetime connection',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
