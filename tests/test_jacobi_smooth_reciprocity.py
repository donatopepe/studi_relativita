import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_smooth_reciprocity.py';O=R/'studies/spacetime/jacobi-smooth-reciprocity-results.json'
def mod():
 s=importlib.util.spec_from_file_location('jsr',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class SmoothReciprocity(unittest.TestCase):
 def setUp(self):self.m=mod()
 def test_symmetric_smooth_reversal_transposes_vertex_block(self):
  d=self.m.symmetric_control(4000);self.assertLess(d['block_transpose_residual'],2e-10)
 def test_full_anti_involution(self):self.assertLess(self.m.symmetric_control(4000)['full_involution_residual'],3e-10)
 def test_singular_values_reversal_blind(self):
  d=self.m.symmetric_control(4000);self.assertLess(max(abs(x-y) for x,y in zip(d['forward_singular_values'],d['reverse_singular_values'])),2e-10)
 def test_nonsymmetric_profile_breaks_identity(self):self.assertGreater(self.m.nonsymmetric_counterexample(4000)['block_transpose_residual'],1e-4)
 def test_convergence(self):
  ref=self.m.integrate(self.m.sym_k,4000);a=self.m.norm(self.m.sub(self.m.integrate(self.m.sym_k,250),ref));b=self.m.norm(self.m.sub(self.m.integrate(self.m.sym_k,500),ref));self.assertLess(b,a)
 def test_ell0_absent(self):self.assertEqual('SMOOTH_RECIPROCITY_NOT_ELL0',self.m.ell0_gate(['K','S','affine','screen']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_CONTINUOUS_SYMMETRIC_PROFILE_REVERSAL_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
