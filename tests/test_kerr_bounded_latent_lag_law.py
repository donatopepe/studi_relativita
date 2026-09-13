import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_bounded_latent_lag_law.py';A=R/'studies/spacetime/kerr-bounded-latent-lag-law-results.json';S=importlib.util.spec_from_file_location('laglaw',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertLess(x['probability_sum_residual'],2e-10);self.assertLess(x['bound_residual'],2e-10);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases'])
 def test_02_extrema(self):self.assertLess(c.extrema_identity_control()['residual'],2e-10)
 def test_03_uniform(self):
  x=c.uniform_control();self.assertLess(x['residual'],2e-10);self.assertEqual(x['counts'],[87,87,87,87])
 def test_04_envelope(self):self.assertTrue(c.envelope_control()['all_ordered'])
 def test_05_widening(self):self.assertTrue(c.widening_control()['all_nondecreasing'])
 def test_06_count_transition(self):
  x=c.count_transition_control();self.assertEqual(x['kappas']['2']['worst_counts'],[87,87,87,87]);self.assertEqual(x['kappas']['4']['worst_counts'],[87,87,87,88]);self.assertEqual(x['kappas']['2']['best_counts'],[87,87,87,87]);self.assertEqual(x['kappas']['4']['best_counts'],[87,87,87,87]);self.assertTrue(x['kappas']['4']['all_predecessors_fail']);self.assertTrue(x['kappas']['4']['all_N64_unsafe'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM');self.assertTrue(x['lag_law_bounds'].startswith('TOY_'))
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
