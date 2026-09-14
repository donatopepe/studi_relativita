import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_window_scale_mixture.py';A=R/'studies/spacetime/kerr-window-scale-mixture-results.json';S=importlib.util.spec_from_file_location('scalemixture',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertLess(x['mean_residual'],2e-10);self.assertLess(x['second_moment_residual'],2e-10);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases'])
 def test_02_identity(self):self.assertLess(c.identity_control()['residual'],2e-10)
 def test_03_zero_variance(self):
  x=c.zero_variance_control();self.assertLess(x['residual'],2e-10);self.assertEqual(x['minimum_count'],87)
 def test_04_floor(self):
  x=c.floor_control();self.assertLess(x['residual'],2e-10);self.assertTrue(x['all_decrease_to_floor'])
 def test_05_counts(self):
  x=c.count_control();self.assertEqual(x['minimum_counts'],[87,106,292,None]);self.assertTrue(x['finite_predecessors_fail']);self.assertTrue(x['all_N64_unsafe'])
 def test_06_critical(self):
  x=c.critical_control();self.assertTrue(x['in_fixed_window']);self.assertLess(x['floor_residual'],2e-10);self.assertTrue(x['below_has_finite_count']);self.assertFalse(x['at_finite_count_passes']);self.assertFalse(x['above_finite_count_passes'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['basis_delta_residual'],2e-10);self.assertLess(x['scale_risk_residual'],2e-10);self.assertLess(x['critical_cv_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['scale_mixture_interpretation'].startswith('TOY_'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
