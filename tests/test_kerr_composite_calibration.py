import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_composite_calibration.py';A=R/'studies/spacetime/kerr-composite-calibration-results.json';S=importlib.util.spec_from_file_location('profile',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_analytic_overlap(self):
  x=c.bounded_overlap_control();self.assertFalse(x['sets_overlap']);self.assertGreater(x['second_channel_gap'],1.)
 def test_02_domain(self):
  for bad in ((0,.8,.2),(.8,.8,0),(.4,.8,.2),(.8,1.6,.2),(.8,.8,1.1),(float('nan'),.8,.2)):
   with self.assertRaises(ValueError):c.bounded_profile_covariance(1,*bad)
 def test_03_positive_profile_minimum(self):
  x=c.profile_minimum(9);self.assertGreater(x['minimum_symmetric_KL'],1e-3)
 def test_04_refinement(self):
  x=c.refinement_control();self.assertTrue(x['nonincreasing']);self.assertEqual(x['grid_sizes'],[3,5,9])
 def test_05_boundary(self):
  x=c.boundary_control();self.assertTrue(x['on_declared_boundary']);self.assertLess(x['direct_residual'],2e-10)
 def test_06_relaxed_collision(self):
  x=c.relaxed_collision_control();self.assertLess(x['covariance_residual'],2e-10);self.assertGreater(min(x['plus_gains']+x['minus_gains']),0.)
 def test_07_basis_scale(self):
  x=c.basis_scale_control(.37,2.5);self.assertLess(x['basis_KL_residual'],2e-10);self.assertLess(x['scale_KL_residual'],2e-10);self.assertEqual(x['scale_null_direction'],[1.,0.,0.,0.,0.])
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertFalse(x['extra_dimension_detected']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):
  self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
