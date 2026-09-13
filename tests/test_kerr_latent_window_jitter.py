import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_latent_window_jitter.py';A=R/'studies/spacetime/kerr-latent-window-jitter-results.json';S=importlib.util.spec_from_file_location('latent',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['accepted']);self.assertLess(x['weight_residual'],2e-10);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases'])
 def test_02_conditional_identity(self):self.assertLess(c.conditional_identity_control()['residual'],2e-10)
 def test_03_zero_support(self):
  x=c.zero_support_control();self.assertLess(x['residual'],2e-10);self.assertEqual(x['minimum_count'],87)
 def test_04_jensen(self):
  x=c.jensen_control();self.assertLess(x['zero_support_residual'],2e-10);self.assertGreater(x['minimum_positive_gap'],0);self.assertTrue(x['latent_risk_not_greater'])
 def test_05_risk(self):
  x=c.risk_control();self.assertTrue(x['all_count_decreasing']);self.assertTrue(x['all_fraction_increasing'])
 def test_06_count_contrast(self):
  x=c.count_contrast_control();self.assertEqual(x['latent_counts'],[87,87,87,87]);self.assertEqual(x['kernel_counts'],[87,88,88,88]);self.assertTrue(x['all_predecessors_fail']);self.assertTrue(x['all_N64_unsafe'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['unconditional_sample_law'].startswith('NON_GAUSSIAN'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
