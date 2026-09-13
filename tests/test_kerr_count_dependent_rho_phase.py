import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_count_dependent_rho_phase.py';A=R/'studies/spacetime/kerr-count-dependent-rho-phase-results.json';S=importlib.util.spec_from_file_location('countphase',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['accepted']);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases']);self.assertTrue(x['N53_nonroot_rejected'])
 def test_02_iid_threshold(self):
  x=c.iid_threshold_control();self.assertTrue(x['N53_unsafe']);self.assertTrue(x['N54_safe']);self.assertEqual(x['first_safe_count'],54)
 def test_03_root_identity(self):
  x=c.root_identity_control();self.assertLess(x['residual'],2e-10);self.assertTrue(x['all_sides_classify'])
 def test_04_boundaries(self):
  x=c.boundaries_control();self.assertLess(x['residual'],2e-10);self.assertTrue(x['N53_no_window']);self.assertTrue(x['all_sides_classify'])
 def test_05_ordering(self):
  x=c.ordering_control();self.assertTrue(x['all_strictly_ordered']);self.assertTrue(x['within_case_order'])
 def test_06_width(self):
  x=c.width_control();self.assertLess(x['residual'],2e-10);self.assertTrue(x['strictly_decreasing'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['scale_boundary_residual'],2e-10);self.assertLess(x['basis_risk_residual'],2e-10);self.assertLess(x['N87_prior_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['count_phase_interpretation'].startswith('TOY_'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
