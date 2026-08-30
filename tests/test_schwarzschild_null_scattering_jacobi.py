import importlib.util,math,pathlib,unittest
P=pathlib.Path(__file__).parents[1]/'studies/spacetime/schwarzschild_null_scattering_jacobi.py'
S=importlib.util.spec_from_file_location('scattering_jacobi',P);s=importlib.util.module_from_spec(S);S.loader.exec_module(s)

class SchwarzschildNullScatteringJacobiTests(unittest.TestCase):
 def test_profile_preserves_branches_screen_and_vacuum_tidal_structure(self):
  c=s.profile_control(M=1.,rho=4.,R=12.,orientation=1,n=120)
  self.assertEqual(c['branches'],['incoming','turning','outgoing'])
  self.assertGreater(len(c['samples']),100)
  self.assertLess(c['maximum_screen_orthonormality_residual'],2e-8)
  self.assertLess(c['maximum_screen_transport_residual'],2e-5)
  self.assertLess(c['maximum_K_symmetry_residual'],2e-8)
  self.assertLess(c['maximum_vacuum_trace_residual'],2e-5)
  turn=next(z for z in c['samples'] if z['branch']=='turning')
  expected=3*c['M']*(c['M']*c['beta'])**2/turn['r']**5
  self.assertAlmostEqual(turn['K'][0][0],expected,12)
  self.assertAlmostEqual(turn['K'][1][1],-expected,12)
  self.assertEqual(c['affine_normalization'],'UNIT_KILLING_ENERGY_PROJECT_ANCHOR_NOT_DETECTOR_FREQUENCY')
 def test_phase_map_is_primary_symplectic_reversible_and_composes_at_turning(self):
  c=s.phase_control(M=1.,rho=4.,R=12.,orientation=1,n=160)
  self.assertEqual(len(c['P_phase']),4)
  self.assertLess(c['symplectic_residual'],3e-6)
  self.assertLess(c['reverse_inverse_residual'],3e-6)
  self.assertLess(c['turning_composition_residual'],3e-6)
  self.assertEqual(c['primary_object'],'FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS')
 def test_zero_window_and_source_preparations(self):
  z=s.zero_window_control()
  self.assertLess(z['identity_residual'],1e-12)
  c=s.phase_control(n=120)
  self.assertEqual(c['vertex_preparation']['X_source'],[[0.,0.],[0.,0.]])
  self.assertEqual(c['parallel_preparation']['V_source'],[[0.,0.],[0.,0.]])
  self.assertGreater(s.maxabs(s.sub(c['vertex_preparation']['X_observer'],c['parallel_preparation']['X_observer'])),1e-3)
 def test_graph_is_guarded_and_full_map_survives_caustic_search(self):
  c=s.caustic_control(n=180)
  self.assertTrue(c['full_map_available_at_all_samples'])
  self.assertGreaterEqual(len(c['vertex_caustic_brackets']),0)
  self.assertIn(c['observer_graph']['status'],('REGULAR','CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'))
  self.assertEqual(c['global_caustic_count'],'NOT_ESTABLISHED')
 def test_endpoint_actions_change_raw_map_but_reconstruct(self):
  c=s.endpoint_action_control(n=120)
  self.assertGreater(c['raw_map_difference'],1e-3)
  self.assertLess(c['reconstruction_residual'],2e-8)
  self.assertEqual(c['classification'],'TOY_ORIENTED_SCREEN_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION')
 def test_affine_and_geometric_scale_conversions(self):
  a=s.affine_scale_control(factor=1.7,n=120)
  self.assertGreater(a['raw_rate_map_difference'],1e-3)
  self.assertLess(a['converted_phase_map_residual'],3e-5)
  g=s.geometric_scale_control(factor=2.5,n=120)
  self.assertGreater(g['raw_rate_map_difference'],1e-3)
  self.assertLess(g['dimensionless_profile_residual'],3e-5)
  self.assertLess(g['converted_phase_map_residual'],3e-5)
  self.assertEqual(g['classification'],'GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_PHASE_RATE_AND_ENDPOINT_CONVERSION')
 def test_rank_keeps_log_M_null_and_does_not_claim_global_injectivity(self):
  c=s.rank_control(n=100)
  self.assertGreaterEqual(c['rank_shape_boundary'],1)
  self.assertEqual(c['rank_with_log_M'],c['rank_shape_boundary'])
  self.assertLess(c['log_M_column_norm'],2e-4)
  self.assertEqual(c['scale_null_direction'],[0,0,1])
  self.assertFalse(c['independent_channels'])
  self.assertEqual(c['global_injectivity'],'NOT_ESTABLISHED')
  self.assertIn('log_M',c['jacobian_columns'])
 def test_result_contract_is_conservative(self):
  r=s.build_result(n=100)
  self.assertEqual(r['UMCH'],'UNPROVEN')
  self.assertFalse(r['ell0_identified'])
  self.assertEqual(r['detection'],'NO_POSITIVE_DETECTION_CLAIM')
  self.assertEqual(r['maximum_interpretation'],'CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE')
  self.assertIn('NOT_ELL0',r['status'])
  self.assertEqual(r['structural_dead_end'],'NOT_DECLARED')

if __name__=='__main__':unittest.main()
