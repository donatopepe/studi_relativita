import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_reference_drift.py';A=R/'studies/spacetime/kerr-reference-drift-results.json';S=importlib.util.spec_from_file_location('drift',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_geometry(self):self.assertLess(c.interval_geometry_control()['endpoint_residual'],2e-10)
 def test_02_box(self):
  x=c.drift_box_control();self.assertTrue(x['strictly_inside']);self.assertEqual(x['drift_fraction'],.8)
 def test_03_robust_margin(self):self.assertGreater(c.robust_obstruction_control()['minimum_margin'],1e-3)
 def test_04_endpoint(self):
  x=c.endpoint_loss_control();self.assertLess(x['placement_product_residual'],2e-10);self.assertLess(x['fisher_determinant_residual'],2e-10)
 def test_05_outside_collision(self):
  x=c.outside_collision_control();self.assertLess(x['joint_residual'],2e-10);self.assertGreater(min(x['plus_gains']+x['minus_gains']+x['plus_noise']+x['minus_noise']),0.)
 def test_06_fisher_margin(self):self.assertGreater(c.fisher_margin_control()['minimum_determinant'],1e-8)
 def test_07_scale(self):self.assertLess(c.scale_control(2.5)['normalized_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
