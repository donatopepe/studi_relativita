import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/sphere-path-measure-report-en.md').read_text();i=(R/'audit/sphere-path-measure-report-it.md').read_text()
  for x in ['KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT','SPHERE_PATH_MEASURE_SECOND_CIRCULAR_MOMENT_ONLY_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/sphere-path-measure.md').read_text();self.assertIn("statistic's null space",t);self.assertIn('does not establish UMCH',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
