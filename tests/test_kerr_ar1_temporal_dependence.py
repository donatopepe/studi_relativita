import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_ar1_temporal_dependence.py';A=R/'studies/spacetime/kerr-ar1-temporal-dependence-results.json';S=importlib.util.spec_from_file_location('ar1',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  for N,rho in ((1,.5),(1.5,.5),(16,-.1),(16,1.),(16,float('nan'))):
   with self.assertRaises(ValueError):c.alpha(N,rho)
 def test_02_identity(self):self.assertLess(c.trace_identity_control()['residual'],2e-10)
 def test_03_iid(self):self.assertLess(c.iid_limit_control()['residual'],2e-10)
 def test_04_rms(self):self.assertTrue(c.rms_control(.5)['strictly_decreasing'])
 def test_05_monotonicity(self):self.assertTrue(c.rho_monotonicity_control()['strictly_increasing'])
 def test_06_safe_count(self):
  x=c.safe_count_control(.5);self.assertEqual(x['minimum_count'],88);self.assertLessEqual(x['risk_at_count'],.05);self.assertGreater(x['risk_at_predecessor'],.05);self.assertFalse(x['N64_passes'])
 def test_07_basis_scale_limit(self):
  x=c.basis_scale_limit_control(.37,2.5);self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10);self.assertLess(x['near_unit_effective_df_64'],4.)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
