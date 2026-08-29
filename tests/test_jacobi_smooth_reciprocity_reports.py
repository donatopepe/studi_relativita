import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status_scope(self):
  e=(R/'audit/jacobi-smooth-reciprocity-report-en.md').read_text();i=(R/'audit/jacobi-smooth-reciprocity-report-it.md').read_text();t=(R/'theory/spacetime/jacobi-smooth-reciprocity.md').read_text();s='JACOBI_CONTINUOUS_SYMMETRIC_PROFILE_REVERSAL_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0'
  for x in (e,i,t):self.assertIn(s,x);self.assertIn('NO_POSITIVE_DETECTION_CLAIM',x);self.assertIn('ell0',x)
 def test_open_exact_spacetime_route(self):
  s=(R/'doc/specs/2026-08-28-jacobi-smooth-reciprocity.md').read_text();self.assertIn('connection-derived',s);self.assertIn('no structural dead end',s)
if __name__=='__main__':unittest.main()
