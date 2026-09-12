import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_bounded_pairing_lag.py';A=R/'studies/spacetime/kerr-bounded-pairing-lag-results.json';S=importlib.util.spec_from_file_location('lag',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['accepted']);self.assertEqual(x['invalid_cases_rejected'],x['invalid_cases']);self.assertEqual(x['round_half_up_example'],2)
 def test_02_identity(self):self.assertLess(c.identity_control()['residual'],2e-10)
 def test_03_synchronous(self):
  x=c.synchronous_control();self.assertLess(x['residual'],2e-10);self.assertEqual(x['minimum_count'],87)
 def test_04_risk(self):self.assertTrue(c.risk_control()['all_strictly_decreasing'])
 def test_05_monotonicity(self):self.assertTrue(c.monotonicity_control()['all_monotonic'])
 def test_06_count_transition(self):
  x=c.count_transition_control();self.assertEqual(x['minimum_counts'],[87,87,87,88]);self.assertTrue(x['all_predecessors_fail']);self.assertTrue(x['all_N64_unsafe'])
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
