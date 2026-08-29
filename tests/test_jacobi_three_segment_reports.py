import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/jacobi-three-segment-report-en.md').read_text();i=(R/'audit/jacobi-three-segment-report-it.md').read_text()
  for x in ['EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT','JACOBI_THREE_SEGMENT_SPECTRUM_PERMUTATION_BLIND_VERTEX_ENDPOINT_MIDDLE_ONLY_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-three-segment.md').read_text();self.assertIn('all six',t);self.assertIn('not smooth matrix Sachs',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
