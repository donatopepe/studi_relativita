import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_correlated_noise_mismatch.py';A=R/'studies/spacetime/kerr-correlated-noise-mismatch-results.json';S=importlib.util.spec_from_file_location('mismatch',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_spd(self):
  x=c.spd_control();self.assertTrue(x['anchor_spd']);self.assertGreater(x['minimum_eigenvalue'],0.);self.assertTrue(x['invalid_rejected'])
 def test_02_cancellation(self):self.assertLess(c.shared_noise_cancellation_control()['residual'],2e-10)
 def test_03_sign_cones(self):
  x=c.sign_cone_control();self.assertTrue(x['opposite_definite']);self.assertFalse(x['exact_collision_possible'])
 def test_04_threshold(self):
  x=c.threshold_control();self.assertGreater(x['tau'],1e-3);self.assertLess(x['boundary_residual'],2e-10)
 def test_05_safe_bound(self):self.assertGreater(c.safe_mismatch_control()['remaining_margin'],1e-3)
 def test_06_threshold_collision(self):self.assertLess(c.threshold_collision_control()['zero_eigenvalue_residual'],2e-10)
 def test_07_basis_scale(self):
  x=c.basis_scale_control(.37,2.5);self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
