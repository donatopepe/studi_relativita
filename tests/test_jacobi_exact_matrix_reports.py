import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/jacobi-exact-matrix-report-en.md').read_text();i=(R/'audit/jacobi-exact-matrix-report-it.md').read_text()
  for x in ['EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT','JACOBI_EXACT_MATRIX_SPECTRUM_AND_VERTEX_SINGULAR_VALUES_ORDER_BLIND_BLOCK_TRANSPOSE_SENSITIVE_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-exact-matrix.md').read_text();self.assertIn('transpose',t);self.assertIn('singular values coincide',t);self.assertIn('not smooth Sachs',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
