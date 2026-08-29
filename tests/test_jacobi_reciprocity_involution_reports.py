import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status(self):
  e=(R/'audit/jacobi-reciprocity-involution-report-en.md').read_text();i=(R/'audit/jacobi-reciprocity-involution-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_EXACT_MATRIX_CONTROL','JACOBI_FINITE_SYMMETRIC_PROFILE_REVERSAL_EXACT_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_exact_scope(self):
  t=(R/'theory/spacetime/jacobi-reciprocity-involution.md').read_text();self.assertIn('any finite ordered product',t);self.assertIn('does not claim smooth covariant Sachs reciprocity',t);self.assertIn('no structural dead end',t)
if __name__=='__main__':unittest.main()
