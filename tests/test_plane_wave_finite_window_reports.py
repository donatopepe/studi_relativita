import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status_scope(self):
  e=(R/'audit/plane-wave-finite-window-report-en.md').read_text();i=(R/'audit/plane-wave-finite-window-report-it.md').read_text();t=(R/'theory/spacetime/plane-wave-finite-window.md').read_text();s='EXACT_PLANE_WAVE_FINITE_WINDOW_NONRADIAL_GEOMETRY_PROTOCOL_NOT_ELL0'
  for x in (e,i,t):self.assertIn(s,x);self.assertIn('NO_POSITIVE_DETECTION_CLAIM',x);self.assertIn('ell0',x);self.assertIn('10.1088/0264-9381/29/23/235023',x)
 def test_source_scope(self):
  b=(R/'references/library.bib').read_text();v=(R/'references/verification-log.md').read_text();self.assertIn('ColeyMcNuttMilson2012',b);self.assertIn('ColeyMcNuttMilson2012',v);self.assertIn('does not establish finite-window protocol',v)
 def test_open_route(self):
  s=(R/'doc/specs/2026-08-28-plane-wave-finite-window.md').read_text();self.assertIn('physically selected windows',s);self.assertIn('no structural dead end',s)
if __name__=='__main__':unittest.main()
