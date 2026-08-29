import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status_scope(self):
  fs=['audit/plane-wave-window-jacobi-cross-channel-report-en.md','audit/plane-wave-window-jacobi-cross-channel-report-it.md','theory/spacetime/plane-wave-window-jacobi-cross-channel.md'];s='EXACT_PLANE_WAVE_WINDOW_JACOBI_MAP_CONDITIONAL_SUPPORT_IDENTIFIABILITY_NOT_ELL0'
  for f in fs:
   x=(R/f).read_text();self.assertIn(s,x);self.assertIn('NO_POSITIVE_DETECTION_CLAIM',x);self.assertIn('ell0',x)
 def test_raw_projection_limit_and_open_route(self):
  e=(R/'audit/plane-wave-window-jacobi-cross-channel-report-en.md').read_text();i=(R/'audit/plane-wave-window-jacobi-cross-channel-report-it.md').read_text();s=(R/'doc/specs/2026-08-28-plane-wave-window-jacobi-cross-channel.md').read_text();self.assertIn('not raw-matrix equivalence',e);self.assertIn('non è equivalenza delle matrici raw',i);self.assertIn('no structural dead end',s)
if __name__=='__main__':unittest.main()
