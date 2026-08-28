import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/cross-channel-nuisance-report-en.md').read_text();i=(R/'audit/cross-channel-nuisance-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','CROSS_CHANNEL_IDENTIFIABILITY_REQUIRES_CALIBRATION_QUOTIENT','NO_POSITIVE_DETECTION_CLAIM','X_STRUCTURALLY_NON_IDENTIFIABLE_FREE_GAIN_RATIO']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/cross-channel-nuisance-quotient.md').read_text();self.assertIn('not channel-wise calibration group',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
