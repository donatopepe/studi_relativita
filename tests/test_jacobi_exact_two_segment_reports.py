import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/jacobi-exact-two-segment-report-en.md').read_text();i=(R/'audit/jacobi-exact-two-segment-report-it.md').read_text()
  for x in ['EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT','JACOBI_EXACT_SPECTRUM_AND_VERTEX_DISPLACEMENT_ORDER_BLIND_FULL_MAP_ORDER_SENSITIVE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-exact-two-segment.md').read_text();self.assertIn('Vertex source',t);self.assertIn('not smooth matrix Sachs',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
