import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_status(self):
  e=(R/'audit/jacobi-matrix-reciprocity-report-en.md').read_text();i=(R/'audit/jacobi-matrix-reciprocity-report-it.md').read_text()
  for x in ['EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT','JACOBI_MATRIX_PROFILE_REVERSAL_TRANSPOSE_RECIPROCITY_SINGULAR_VALUES_BLIND_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-matrix-reciprocity.md').read_text();self.assertIn('two-, three-, and four-segment',t);self.assertIn('not a proof for every smooth matrix profile',t);self.assertIn('No structural dead end',t)
if __name__=='__main__':unittest.main()
