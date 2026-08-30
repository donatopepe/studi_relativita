import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/schwarzschild_photon_arc_cross_map.py'
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-arc-cross-map-results.json'
def load():
 spec=importlib.util.spec_from_file_location('schwarzschild_photon_arc_cross_map',MODULE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class SchwarzschildPhotonArcCrossMapTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_open_arc_geometry_uses_declared_affine_anchor(self):
  x=self.m.geometry_control(math.pi/3)
  self.assertAlmostEqual(x['r_ph'],3.0);self.assertEqual(x['k_tetrad'],[1.0,0.0,0.0,1.0])
  self.assertLess(x['null_residual'],1e-13);self.assertLess(x['geodesic_residual'],1e-12)
  self.assertLess(abs(x['L']-math.pi),1e-12);self.assertLess(abs(x['delta_phi']-math.pi/3),1e-12)
  self.assertFalse(x['closed_arc'])
 def test_raw_connection_and_phase_maps_match_numerical_propagation(self):
  for alpha in [0.0,math.pi/3,math.pi,3*math.pi/2,2*math.pi]:
   x=self.m.raw_map_control(alpha)
   self.assertEqual(len(x['T_arc']),4);self.assertEqual(len(x['P_arc']),4)
   self.assertLess(x['connection_exact_numerical_residual'],3e-8)
   self.assertLess(x['phase_exact_numerical_residual'],3e-8)
   self.assertLess(x['lorentz_residual'],3e-9);self.assertLess(x['symplectic_residual'],3e-9)
   self.assertLess(abs(x['phase_determinant']-1),3e-9)
 def test_zero_window_is_identity_with_correct_generators(self):
  x=self.m.zero_window_control()
  self.assertLess(x['connection_identity_residual'],1e-14);self.assertLess(x['phase_identity_residual'],1e-14)
  self.assertLess(x['connection_generator_residual'],2e-6);self.assertLess(x['phase_generator_residual'],2e-6)
 def test_constant_generators_obey_semigroup_composition(self):
  x=self.m.composition_control(.7,1.1)
  self.assertLess(x['connection_composition_residual'],2e-11);self.assertLess(x['phase_composition_residual'],2e-11)
 def test_caustics_gate_graph_not_full_phase_map(self):
  x=self.m.caustic_control()
  self.assertEqual(x['conjugate_angles'],[math.pi,2*math.pi])
  for c in x['controls']:
   self.assertEqual(c['S_vertex']['status'],'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR')
   self.assertLess(c['endpoint_X_determinant_abs'],2e-9);self.assertLess(c['full_map_inverse_residual'],2e-8)
  self.assertEqual(x['nonvertex']['S_nonvertex']['status'],'REGULAR')
 def test_orientation_and_endpoint_actions_are_not_extra_physical_rank(self):
  x=self.m.orientation_endpoint_control(math.pi/3)
  self.assertGreater(x['connection_raw_orientation_difference'],1e-3)
  self.assertLess(x['connection_characteristic_orientation_collision'],2e-9)
  self.assertLess(x['phase_orientation_collision'],2e-12)
  self.assertGreater(x['connection_endpoint_raw_difference'],1e-3)
  self.assertLess(x['connection_endpoint_characteristic_collision'],2e-9)
  self.assertGreater(x['phase_endpoint_raw_difference'],1e-3)
  self.assertLess(x['phase_endpoint_symplectic_residual'],2e-9)
 def test_affine_and_geometric_scale_blindness_are_separate(self):
  a=self.m.affine_scale_control(math.pi/3,1.7);g=self.m.geometric_scale_control(math.pi/3,2.4)
  self.assertLess(a['phase_dimensionless_residual'],2e-9);self.assertGreater(a['raw_rate_block_difference'],.01)
  self.assertLess(g['connection_dimensionless_residual'],2e-9);self.assertLess(g['phase_dimensionless_residual'],2e-9)
  self.assertGreater(g['affine_length_difference'],1.0);self.assertGreater(g['coordinate_duration_difference'],1.0)
 def test_joint_dimensionless_map_has_one_shape_direction_and_scale_null(self):
  x=self.m.joint_rank_control(math.pi/3)
  self.assertEqual(x['parameters'],['alpha','log_M']);self.assertEqual(x['rank_joint'],1)
  self.assertGreater(x['singular_values_joint'][0],1e-3);self.assertLess(x['singular_values_joint'][1],2e-7)
  self.assertLess(x['scale_column_norm'],2e-7);self.assertLess(x['jacobian_step_convergence'],2e-5)
  self.assertEqual(x['independent_channels'],False);self.assertEqual(x['scale_null_direction'],[0.0,1.0])
 def test_optical_periodicity_does_not_create_joint_global_collision(self):
  x=self.m.collision_control(.45)
  self.assertLess(x['phase_elliptic_periodic_collision'],2e-9)
  self.assertGreater(x['phase_full_map_difference'],.1);self.assertGreater(x['joint_feature_difference'],1e-3)
  self.assertFalse(x['global_joint_collision'])
 def test_full_winding_matches_existing_segment_and_separate_closure(self):
  x=self.m.closed_loop_cross_check()
  self.assertLess(x['future_null_segment_residual'],2e-9);self.assertLess(x['closed_loop_residual'],2e-9)
  self.assertEqual(x['primary_object'],'OPEN_ARC_ENDPOINT_TRANSPORT_NOT_HOLONOMY')
  self.assertEqual(x['closure_role'],'DERIVED_PAST_DIRECTED_STATIC_CLOSURE_CROSS_CHECK_ONLY')
 def test_artifact_is_canonical_and_preserves_state(self):
  art=json.loads(ARTIFACT.read_text());self.assertEqual(art['status'],'SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_CONNECTION_JACOBI_CROSS_MAP_CAUSTIC_LANDMARKED_LOCALLY_ONE_SHAPE_DIRECTION_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0')
  self.assertEqual(art['scope'],'FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_CONNECTION_AND_SCREEN_PHASE_MAP_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_ENDPOINT_BASES_AND_NO_DETECTOR_READOUT')
  self.assertEqual(art['gate'],'PHYSICAL_FINITE_ARC_WINDOW_SELECTION_SOURCE_OBSERVER_TETRADS_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED')
  self.assertFalse(art['ell0_identified']);self.assertEqual(art['structural_dead_end'],'NOT_DECLARED');self.assertEqual(art['detection'],'NO_POSITIVE_DETECTION_CLAIM')
  subprocess.run([sys.executable,str(MODULE),'--check'],check=True,cwd=ROOT)
if __name__=='__main__':unittest.main()
