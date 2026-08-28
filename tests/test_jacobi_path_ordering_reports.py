import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/jacobi-path-ordering-report-en.md').read_text();i=(R/'audit/jacobi-path-ordering-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','JACOBI_PATH_ORDER_REQUIRED_LOCAL_SPECTRA_INSUFFICIENT','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-path-ordering.md').read_text();self.assertIn('not sufficient statistic',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
