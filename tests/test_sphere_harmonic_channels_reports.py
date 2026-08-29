import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/sphere-harmonic-channels-report-en.md').read_text();i=(R/'audit/sphere-harmonic-channels-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','SPHERE_CROSS_CHANNEL_HARMONIC_ALGEBRAIC_DEPENDENCE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/sphere-harmonic-channels.md').read_text();self.assertIn('rank at most one',t);self.assertIn('not physical channel',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
