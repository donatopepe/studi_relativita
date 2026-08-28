import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/cross-channel-mixing-report-en.md').read_text();i=(R/'audit/cross-channel-mixing-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','CROSS_CHANNEL_INJECTIVITY_DESTROYED_BY_FREE_MIXING_GROUP','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/cross-channel-mixing.md').read_text();self.assertIn('group choice matters',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
