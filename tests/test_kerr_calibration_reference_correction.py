import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_calibration_reference_correction.py';A=R/'studies/spacetime/kerr-calibration-reference-correction-results.json';S=importlib.util.spec_from_file_location('correction',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_criterion(self):
  x=c.collision_criterion_control();self.assertLess(x['algebra_residual'],2e-10);self.assertEqual(x['positive_collision_condition'],'product_positive')
 def test_02_inside_domain(self):
  x=c.inside_reference_control();self.assertTrue(x['strictly_inside']);self.assertLess(max(x['products']),0.)
 def test_03_inside_noncollision(self):self.assertFalse(c.inside_reference_control()['positive_collision_possible'])
 def test_04_outside_collision(self):
  x=c.outside_reference_collision_control();self.assertLess(x['joint_residual'],2e-10);self.assertGreater(min(x['plus_gains']+x['minus_gains']+x['plus_noise']+x['minus_noise']),0.)
 def test_05_fisher(self):self.assertEqual(c.fisher_rank_control()['joint_ranks'],[2,2])
 def test_06_unknown_reference(self):self.assertLess(c.unknown_reference_collision_control()['joint_residual'],2e-10)
 def test_07_weak_precision(self):
  x=c.weak_precision_control();self.assertTrue(x['precision_decreasing']);self.assertTrue(x['information_decreasing'])
 def test_08_scale_nonclaims(self):
  x=c.scale_nonclaim_control(2.5);self.assertLess(x['scale_residual'],2e-10);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
