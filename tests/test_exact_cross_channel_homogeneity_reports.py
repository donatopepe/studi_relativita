import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/exact-cross-channel-homogeneity-report-en.md').read_text();i=(R/'audit/exact-cross-channel-homogeneity-report-it.md').read_text()
  for x in ['EXACT_PATTERN_CONTROL_AND_NEGATIVE_RESULT','EXACT_CROSS_CHANNEL_EQUAL_HOMOGENEITY_SCALE_CANCELS','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/exact-cross-channel-homogeneity.md').read_text();self.assertIn('operational scale cancels',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
