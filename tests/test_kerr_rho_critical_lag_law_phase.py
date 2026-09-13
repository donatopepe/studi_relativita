import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_rho_critical_lag_law_phase.py';A=R/'studies/spacetime/kerr-rho-critical-lag-law-phase-results.json';S=importlib.util.spec_from_file_location('rhophase',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['accepted']);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases']);self.assertTrue(x['non_straddling_rejected'])
 def test_02_monotonicity(self):
  x=c.monotonicity_control();self.assertTrue(x['uniform_strictly_increasing']);self.assertTrue(x['unrestricted_strictly_increasing']);self.assertTrue(x['ordered'])
 def test_03_lower_root(self):
  x=c.lower_root_control();self.assertLess(x['risk_residual'],2e-10);self.assertTrue(x['in_fixed_window']);self.assertTrue(x['sides_classify'])
 def test_04_upper_root(self):
  x=c.upper_root_control();self.assertLess(x['risk_residual'],2e-10);self.assertTrue(x['in_fixed_window']);self.assertTrue(x['sides_classify'])
 def test_05_classification(self):
  x=c.classification_control();self.assertTrue(x['strict_order']);self.assertTrue(x['matches'])
 def test_06_kappa_path(self):
  x=c.kappa_path_control();self.assertLess(x['residual'],2e-9);self.assertTrue(x['strictly_decreasing']);self.assertLess(x['rho_half_recovery'],2e-10)
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['lower_scale_residual'],2e-10);self.assertLess(x['upper_scale_residual'],2e-10);self.assertLess(x['kappa_basis_risk_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['rho_window_interpretation'].startswith('TOY_'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
