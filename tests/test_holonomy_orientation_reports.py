import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/holonomy-orientation-report-en.md').read_text();i=(R/'audit/holonomy-orientation-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','HOLONOMY_TOMOGRAPHY_RANK_CONDITIONAL_ELL0_ABSENT','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/holonomy-orientation-tomography.md').read_text();self.assertIn('not universal-scale identification',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
