import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_critical_lag_law_radius.py';A=R/'studies/spacetime/kerr-critical-lag-law-radius-results.json';S=importlib.util.spec_from_file_location('critical',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['accepted']);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases']);self.assertTrue(x['outside_active_root_rejected'])
 def test_02_active_set(self):
  x=c.active_set_control();self.assertLess(x['residual'],2e-10);self.assertTrue(x['counts_match'])
 def test_03_bracket(self):
  x=c.bracket_control();self.assertTrue(x['lower_passes']);self.assertTrue(x['upper_fails']);self.assertTrue(x['strictly_increasing'])
 def test_04_root(self):
  x=c.root_control();self.assertLess(x['residual'],2e-10);self.assertLess(x['risk_residual'],2e-10);self.assertTrue(x['in_fixed_window']);self.assertEqual(x['active_count'],35)
 def test_05_sides(self):
  x=c.side_control();self.assertLess(x['risk_87_below'],.05);self.assertGreater(x['risk_87_above'],.05);self.assertEqual(x['below_count'],87);self.assertEqual(x['above_count'],88);self.assertLess(x['risk_88_above'],.05)
 def test_06_support(self):
  x=c.support_control();self.assertTrue(x['subfull_all_pass']);self.assertTrue(x['full_fails'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['scale_root_residual'],2e-10);self.assertLess(x['basis_target_residual'],2e-10);self.assertLess(x['basis_risk_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['critical_kappa_interpretation'].startswith('TOY_'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
