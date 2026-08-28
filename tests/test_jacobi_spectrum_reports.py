import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_alignment(self):
  e=(R/'audit/jacobi-spectrum-report-en.md').read_text();i=(R/'audit/jacobi-spectrum-report-it.md').read_text()
  for x in ['PROJECT_DERIVATION_AND_NEGATIVE_RESULT','JACOBI_CAUSTIC_GEOMETRIC_LANDMARK_NOT_ELL0','NO_POSITIVE_DETECTION_CLAIM','AFFINE_OPTICAL_SCALE_DEGENERACY','10.1098/rspa.1961.0202']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/jacobi-spectrum-caustic-gate.md').read_text();self.assertIn('not `ell0`',t);self.assertIn('No core reformulation',t)
if __name__=='__main__':unittest.main()
