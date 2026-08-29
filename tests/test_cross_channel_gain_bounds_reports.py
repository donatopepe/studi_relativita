import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/cross-channel-gain-bounds-report-en.md').read_text();i=(R/'audit/cross-channel-gain-bounds-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','CROSS_CHANNEL_BOUNDED_GAIN_SHARP_SET_IDENTIFICATION_ONLY','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/cross-channel-gain-bounds.md').read_text();self.assertIn('sharp set identification',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
