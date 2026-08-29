import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/sphere-window-pathscale-report-en.md').read_text();i=(R/'audit/sphere-window-pathscale-report-it.md').read_text()
  for x in ['KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT','SPHERE_WINDOW_NONRADIAL_LANDMARK_CURVATURE_RADIUS_PATH_SHAPE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/sphere-window-pathscale.md').read_text();self.assertIn('exact connection-derived nonradial',t);self.assertIn('does not establish UMCH',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
