import importlib.util,json,math,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];PATH=ROOT/'studies/spacetime/kerr_receiver_likelihood.py';ART=ROOT/'studies/spacetime/kerr-receiver-likelihood-results.json';SPEC=importlib.util.spec_from_file_location('receiver',PATH);r=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(r)
class ReceiverTests(unittest.TestCase):
 def test_01_receiver_covariance(self):
  for o in (-1,1):
   c=r.receiver_covariance(o,.8,.25);self.assertTrue(c['positive_definite']);self.assertLess(c['symmetry_residual'],2e-10);self.assertLess(c['expanded_formula_residual'],2e-10)
  with self.assertRaises(ValueError):r.receiver_covariance(1,0,.25)
 def test_02_likelihood_normalization(self):
  c=r.likelihood_normalization_control();self.assertLess(c['normalization_residual'],2e-7);self.assertLess(c['log_density_residual'],2e-10)
 def test_03_kl_conformance(self):
  c=r.kl_control();self.assertGreater(c['plus_to_minus'],0);self.assertGreater(c['minus_to_plus'],0);self.assertLess(c['self_residual'],2e-10);self.assertLess(c['quadrature_residual'],2e-5)
 def test_04_noise_monotonicity(self):
  c=r.noise_control();self.assertTrue(c['strictly_decreasing']);self.assertEqual(c['noise_sigmas'],[.1,.25,.5,1.,2.])
 def test_05_expected_llr(self):
  c=r.expected_llr_control(25);self.assertGreater(c['plus_expected_llr'],0);self.assertGreater(c['minus_expected_llr'],0);self.assertLess(c['sum_residual'],2e-10)
 def test_06_basis_covariance(self):
  c=r.basis_control(.37);self.assertLess(c['KL_residual'],2e-10);self.assertLess(c['eigenvalue_residual'],2e-10)
 def test_07_calibration_collision(self):
  c=r.calibration_collision_control();self.assertLess(c['covariance_collision_residual'],2e-10);self.assertGreater(c['underlying_signal_difference'],1e-3);self.assertTrue(c['positive_calibrations'])
 def test_08_scale_rank_nonclaims(self):
  c=r.scale_rank_control(2.5);self.assertLess(c['receiver_covariance_residual'],2e-10);self.assertLess(c['KL_residual'],2e-10);self.assertEqual(c['scale_null_direction'],[1.,0.,0.,0.,0.]);g=r.no_ell0_gate();self.assertFalse(g['ell0_identified']);self.assertEqual(g['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):
  a=json.loads(ART.read_text());b=json.loads(subprocess.check_output(['python',str(PATH)],text=True));self.assertEqual(a,b);s=a['control_summary'];self.assertEqual((s['controls_passed'],s['controls_total']),(8,8));self.assertEqual([x['threshold']for x in s['controls']],[2e-10,2e-7,2e-5,1.,2e-10,2e-10,2e-10,2e-10])
if __name__=='__main__':unittest.main()
