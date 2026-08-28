import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/boundary-spectral-landmark-report-en.md').read_text();i=(R/'audit/boundary-spectral-landmark-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','BOUNDARY_SPECTRAL_LANDMARK_MOVABLE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/boundary-spectral-landmark.md').read_text();self.assertIn('movable boundary nuisance',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
