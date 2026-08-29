import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status_and_limits(self):
  e=(R/'audit/jacobi-endpoint-gauge-report-en.md').read_text();i=(R/'audit/jacobi-endpoint-gauge-report-it.md').read_text();t=(R/'theory/spacetime/jacobi-endpoint-gauge.md').read_text();s='JACOBI_TRANSPOSE_REVERSAL_NONIDENTIFIABLE_UNDER_INDEPENDENT_ENDPOINT_FRAME_QUOTIENT'
  for x in (e,i,t):self.assertIn(s,x);self.assertIn('NO_POSITIVE_DETECTION_CLAIM',x);self.assertIn('ell0',x)
 def test_spec_preserves_open_route(self):
  s=(R/'doc/specs/2026-08-28-jacobi-endpoint-gauge.md').read_text();self.assertIn('physically linked',s);self.assertIn('no structural dead end',s)
if __name__=='__main__':unittest.main()
