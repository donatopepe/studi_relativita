import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_estimated_mean_covariance.py';A=R/'studies/spacetime/kerr-estimated-mean-covariance-results.json';S=importlib.util.spec_from_file_location('estimated',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_identity(self):self.assertLess(c.centered_wishart_control()['residual'],2e-10)
 def test_02_domain(self):
  for C,N in (([[1.,0.],[0.,1.]],1),([[1.,0.],[0.,1.]],1.5),([[1.,2.],[2.,1.]],16)):
   with self.assertRaises(ValueError):c.estimated_mse(C,N)
 def test_03_penalty(self):self.assertLess(c.penalty_control()['residual'],2e-10)
 def test_04_rms(self):self.assertTrue(c.rms_control()['strictly_decreasing'])
 def test_05_safe_count(self):
  x=c.safe_count_control();self.assertEqual(x['minimum_count'],54);self.assertLessEqual(x['risk_at_count'],.05);self.assertGreater(x['risk_at_predecessor'],.05)
 def test_06_safe_unsafe(self):
  x=c.safe_unsafe_control();self.assertFalse(x['N16_passes']);self.assertTrue(x['N64_passes'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control(.37,2.5);self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
