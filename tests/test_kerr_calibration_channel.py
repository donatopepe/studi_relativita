import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_calibration_channel.py';A=R/'studies/spacetime/kerr-calibration-channel-results.json';S=importlib.util.spec_from_file_location('calchannel',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_joint_map(self):
  x=c.joint_map_control();self.assertLess(x['formula_residual'],2e-10)
 def test_02_domain(self):
  for bad in ((0,.8,1.1,.25,.35,.02,.02,10),(1,0,1.1,.25,.35,.02,.02,10),(1,.8,1.1,0,.35,.02,.02,10),(1,.8,1.1,.25,.35,0,.02,10),(1,.8,1.1,.25,.35,.02,.02,0)):
   with self.assertRaises(ValueError):c.joint_covariance(*bad)
 def test_03_known_reference(self):
  x=c.known_reference_control();self.assertEqual(x['reference'],[.1,10.]);self.assertFalse(x['positive_collision_possible']);self.assertLess(max(x['placement_products']),0.);self.assertGreater(min(x['obstruction_margins']),0.)
 def test_04_fisher_rank(self):
  x=c.fisher_rank_control();self.assertEqual(x['calibration_only_ranks'],[1,1]);self.assertEqual(x['joint_ranks'],[2,2]);self.assertGreater(min(x['joint_determinants']),1e-8)
 def test_05_finite_precision(self):
  x=c.finite_precision_control();self.assertEqual(x['sample_counts'],[1.,10.,100.]);self.assertTrue(x['strictly_decreasing']);self.assertLess(x['formula_residual'],2e-10)
 def test_06_weak_limit(self):
  x=c.weak_channel_control();self.assertTrue(x['strictly_decreasing']);self.assertLess(x['last_information'],.1)
 def test_07_unknown_reference_collision(self):
  x=c.unknown_reference_collision_control();self.assertLess(x['joint_residual'],2e-10);self.assertGreater(min(x['plus_gains']+x['minus_gains']+x['plus_reference']+x['minus_reference']),0.)
 def test_08_scale_nonclaims(self):
  x=c.scale_nonclaim_control(2.5);self.assertLess(x['dimensionless_joint_residual'],2e-10);self.assertEqual(x['scale_null_direction'],[1.,0.,0.,0.,0.]);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
