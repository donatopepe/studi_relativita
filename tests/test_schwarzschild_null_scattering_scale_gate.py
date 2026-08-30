import importlib.util,math,pathlib,unittest
P=pathlib.Path(__file__).parents[1]/'studies/spacetime/schwarzschild_null_scattering_scale_gate.py'
S=importlib.util.spec_from_file_location('scattering_gate',P);s=importlib.util.module_from_spec(S);S.loader.exec_module(s)

class SchwarzschildNullScatteringScaleGateTests(unittest.TestCase):
 def test_domain_and_turning_relation(self):
  beta=s.turning_beta(4.)
  self.assertAlmostEqual(beta,4/math.sqrt(.5),12)
  self.assertAlmostEqual(1-beta*beta*(1-2/4)/16,0.,12)
  for args in ((0,4,12),(1,3,12),(1,4,4),(1,5,4)):
   with self.assertRaises(ValueError):s.path_samples(*args)
 def test_path_branches_and_first_integrals(self):
  c=s.raw_control(M=1.,rho=4.,R=12.,orientation=1,n=600)
  self.assertEqual(c['branches'],['incoming','turning','outgoing'])
  self.assertLess(c['turning_residual'],1e-12)
  self.assertLess(c['maximum_null_residual'],2e-10)
  self.assertLess(c['maximum_energy_residual'],2e-10)
  self.assertLess(c['maximum_angular_momentum_residual'],2e-10)
  self.assertLess(c['turning_match_residual'],1e-12)
  self.assertGreater(c['delta_t'],0)
  self.assertGreater(c['delta_phi'],0)
 def test_open_transport_is_metric_compatible_and_reversible(self):
  c=s.raw_control(M=1.,rho=4.,R=12.,orientation=1,n=800)
  self.assertEqual(len(c['T_coordinate']),4)
  self.assertEqual(len(c['T_tetrad']),4)
  self.assertLess(c['endpoint_metric_residual'],2e-8)
  self.assertLess(c['reverse_inverse_residual'],2e-8)
  self.assertEqual(c['map_classification'],'OPEN_PATH_ENDPOINT_TRANSPORT_NOT_HOLONOMY')
 def test_boundary_and_orientation_are_not_interior_scale(self):
  b=s.boundary_control()
  self.assertGreater(b['delta_t_over_M_difference'],1e-2)
  self.assertGreater(b['transport_difference'],1e-3)
  self.assertEqual(b['classification'],'FINITE_BOUNDARY_PROTOCOL_DIRECTION')
  o=s.orientation_control()
  self.assertLess(o['time_even_residual'],2e-8)
  self.assertLess(o['phi_odd_residual'],2e-8)
  self.assertGreater(o['raw_transport_difference'],1e-3)
  self.assertEqual(o['norm_alias_classification'],'PROJECTED_NORM_ALIAS_NOT_RAW_MAP_EQUALITY')
 def test_endpoint_actions_reconstruct_raw_static_map(self):
  c=s.endpoint_control()
  self.assertGreater(c['acted_map_difference'],1e-3)
  self.assertLess(c['reconstruction_residual'],2e-10)
  self.assertEqual(c['classification'],'TOY_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION')
 def test_geometric_scale_symmetry_is_explicit(self):
  c=s.scale_control(scale=2.5)
  self.assertLess(c['dimensionless_path_residual'],2e-8)
  self.assertLess(c['delta_t_over_M_residual'],2e-8)
  self.assertLess(c['tetrad_transport_residual'],2e-8)
  self.assertLess(c['delta_t_scaling_residual'],2e-8)
  self.assertGreater(c['coordinate_transport_difference'],1e-3)
  self.assertEqual(c['classification'],'GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_ENDPOINT_CONVERSION')
 def test_rank_retains_scale_null_direction(self):
  c=s.rank_control()
  self.assertEqual(c['rank_shape_boundary'],2)
  self.assertEqual(c['rank_with_log_M'],2)
  self.assertLess(c['log_M_column_norm'],2e-6)
  self.assertEqual(c['scale_null_direction'],[0,0,1])
  self.assertFalse(c['independent_channels'])
 def test_collision_and_status_envelope(self):
  c=s.collision_control()
  self.assertEqual(c['global_injectivity'],'NOT_ESTABLISHED')
  r=s.build_result()
  self.assertEqual(r['umch'],'UNPROVEN')
  self.assertEqual(r['detection'],'NO_POSITIVE_DETECTION_CLAIM')
  self.assertFalse(r['ell0_identified'])
  self.assertEqual(r['structural_dead_end'],'NOT_DECLARED')
  self.assertIn('GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0',r['status'])
  self.assertIn('PHYSICAL_SCATTERING_WINDOW',r['gate'])

if __name__=='__main__':unittest.main()
