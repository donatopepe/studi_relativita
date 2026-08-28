import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/transport-gauge-report-en.md').read_text();i=(R/'audit/transport-gauge-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','TRANSPORT_GAUGE_QUOTIENT_REQUIRED_FOR_NONRADIALITY','NO_POSITIVE_DETECTION_CLAIM','APPARENT_NONRADIALITY_PURE_CONJUGATION','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/transport-gauge-quotient.md').read_text();self.assertIn('pure conjugation',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
