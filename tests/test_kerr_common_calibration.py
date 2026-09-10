import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_common_calibration.py';A=R/'studies/spacetime/kerr-common-calibration-results.json';S=importlib.util.spec_from_file_location('common',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_identity_and_noncollision(self):
  x=c.common_difference_control(.8,1.1,.25);self.assertLess(x['identity_residual'],2e-10);self.assertGreater(x['difference_norm'],1e-3)
 def test_02_domain(self):
  for bad in ((0,.8,.2),(.8,.8,0),(.4,.8,.2),(.8,1.6,.2),(.8,.8,1.1)):
   with self.assertRaises(ValueError):c.bounded_receiver(*bad)
 def test_03_positive_bounded_minimum(self):
  x=c.grid_minimum(17);self.assertGreater(x['minimum_symmetric_KL'],1e-3);self.assertEqual(x['anchor'],[.5,.5,1.])
 def test_04_refinement(self):
  x=c.refinement_control();self.assertTrue(x['nonincreasing']);self.assertLess(x['fine_anchor_residual'],2e-10)
 def test_05_boundary(self):
  x=c.boundary_control();self.assertLess(x['direct_residual'],2e-10);self.assertEqual(x['boundary'],['gain_1_min','gain_2_min','noise_max'])
 def test_06_attenuation(self):
  x=c.attenuation_control();self.assertTrue(x['strictly_decreasing']);self.assertLess(x['last_value'],1e-3)
 def test_07_noise(self):
  x=c.unbounded_noise_control();self.assertTrue(x['strictly_decreasing']);self.assertLess(x['last_value'],1e-3);self.assertLess(x['SNR_duality_residual'],2e-10)
 def test_08_basis_scale_nonclaims(self):
  x=c.basis_scale_control(.37,2.5);self.assertLess(x['basis_KL_residual'],2e-10);self.assertLess(x['scale_KL_residual'],2e-10);self.assertEqual(x['scale_null_direction'],[1.,0.,0.,0.,0.]);g=c.no_ell0_gate();self.assertFalse(g['ell0_identified']);self.assertEqual(g['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):
  a=json.loads(A.read_text());b=json.loads(subprocess.check_output(['python',str(P)],text=True));self.assertEqual(a,b);s=a['control_summary'];self.assertEqual((s['controls_passed'],s['controls_total']),(8,8));self.assertEqual([x['threshold']for x in s['controls']],[2e-10,1.,1e-3,2e-10,2e-10,1e-3,1e-3,2e-10])
if __name__=='__main__':unittest.main()
