import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/jacobi-thin-lens-report-en.md').read_text();i=(R/'audit/jacobi-thin-lens-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','JACOBI_INTEGRATED_FOCUSING_INSUFFICIENT_PROFILE_LOCATION_REQUIRED','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-thin-lens.md').read_text();self.assertIn('insufficient statistic',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
