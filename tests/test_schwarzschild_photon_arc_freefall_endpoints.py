import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/schwarzschild_photon_arc_freefall_endpoints.py'
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-arc-freefall-endpoints-results.json'
def load():
 spec=importlib.util.spec_from_file_location('schwarzschild_photon_arc_freefall_endpoints',MODULE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class SchwarzschildPhotonArcFreefallEndpointTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_radial_endpoint_state_is_timelike_geodesic_and_orthonormal(self):
  for energy,sign in [(1.,-1),(1.,1),(0.8,-1)]:
   x=self.m.endpoint_frame_control(1.,energy,sign)
   self.assertLess(x['normalization_residual'],2e-12)
   self.assertLess(x['geodesic_residual'],2e-8)
   self.assertLess(x['orthonormal_residual'],2e-12)
   self.assertLess(x['lorentz_residual'],2e-12)
 def test_static_limit_recovers_static_endpoint_basis(self):
  x=self.m.endpoint_frame_control(1.,1/math.sqrt(3),1)
  self.assertLess(x['beta_abs'],1e-12);self.assertLess(x['boost_identity_residual'],2e-12)
 def test_raw_endpoint_actions_and_static_reconstruction(self):
  x=self.m.raw_freefall_control(math.pi/3,1.,-1,.8,1)
  self.assertEqual(len(x['T_ff']),4);self.assertEqual(len(x['P_ff']),4)
  self.assertLess(x['connection_action_residual'],1e-12)
  self.assertLess(x['phase_action_residual'],1e-12)
  self.assertLess(x['connection_reconstruction_residual'],2e-10)
  self.assertLess(x['phase_reconstruction_residual'],2e-10)
 def test_zero_window_is_endpoint_comparison_not_interior_transport(self):
  x=self.m.zero_window_control(1.,-1,.8,1)
  self.assertLess(x['static_interior_identity_residual'],1e-14)
  self.assertGreater(x['freefall_endpoint_comparison_nonidentity'],1e-3)
  self.assertEqual(x['classification'],'ENDPOINT_FRAME_COMPARISON_NOT_HOLONOMY_OR_INTERIOR_CURVATURE_RESPONSE')
 def test_composition_requires_matched_intermediate_frame(self):
  x=self.m.composition_control(.7,1.1)
  self.assertLess(x['matched_connection_residual'],2e-10)
  self.assertLess(x['matched_phase_residual'],2e-10)
  self.assertGreater(x['mismatched_connection_residual'],1e-4)
  self.assertGreater(x['mismatched_phase_residual'],1e-4)
  self.assertLess(x['transition_corrected_connection_residual'],2e-10)
  self.assertLess(x['transition_corrected_phase_residual'],2e-10)
 def test_endpoint_actions_do_not_remove_caustics(self):
  for alpha in [math.pi,2*math.pi]:
   x=self.m.caustic_control(alpha)
   self.assertLess(x['endpoint_X_determinant_abs'],2e-8)
   self.assertLess(x['full_map_inverse_residual'],5e-8)
   self.assertEqual(x['graph_status'],'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR')
 def test_endpoint_quotient_removes_preparation_from_interior_map(self):
  x=self.m.endpoint_quotient_control(math.pi/3)
  self.assertGreater(x['raw_connection_difference'],1e-3)
  self.assertGreater(x['raw_phase_difference'],1e-3)
  self.assertLess(x['static_reconstructed_connection_difference'],2e-10)
  self.assertLess(x['static_reconstructed_phase_difference'],2e-10)
 def test_affine_and_geometric_scale_blindness_remain_separate(self):
  x=self.m.scale_control(math.pi/3)
  self.assertGreater(x['raw_affine_rate_difference'],1e-3)
  self.assertLess(x['affine_converted_residual'],2e-10)
  self.assertLess(x['geometric_connection_residual'],2e-10)
  self.assertLess(x['geometric_phase_residual'],2e-10)
 def test_fixed_preparation_joint_map_has_one_interior_shape_direction(self):
  x=self.m.rank_control(math.pi/3)
  self.assertEqual(x['rank_fixed_preparation'],1)
  self.assertLess(x['log_M_column_norm'],1e-7)
  self.assertGreater(x['alpha_column_norm'],1e-4)
  self.assertEqual(x['scale_null_direction'],[0.0,1.0])
  self.assertFalse(x['independent_channels'])
 def test_preparation_direction_is_not_interior_scale(self):
  x=self.m.rank_control(math.pi/3)
  self.assertGreater(x['endpoint_energy_column_norm'],1e-4)
  self.assertEqual(x['endpoint_energy_column_classification'],'ENDPOINT_PREPARATION_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE')
 def test_collisions_and_full_winding_provenance_remain_bounded(self):
  x=self.m.collision_and_provenance_control(.45)
  self.assertLess(x['elliptic_periodic_subblock_collision'],2e-10)
  self.assertFalse(x['global_joint_collision'])
  self.assertLess(x['full_winding_static_segment_residual'],2e-10)
  self.assertEqual(x['closure_status'],'NO_PHYSICAL_FREEFALL_CLOSURE_DERIVED')
 def test_artifact_is_canonical_and_preserves_negative_state(self):
  result=self.m.build_result();stored=json.loads(ARTIFACT.read_text())
  self.assertEqual(result,stored)
  self.assertEqual(stored['status'],self.m.STATUS);self.assertEqual(stored['scope'],self.m.SCOPE);self.assertEqual(stored['gate'],self.m.GATE)
  self.assertFalse(stored['ell0_identified']);self.assertFalse(stored['independent_channels'])
  self.assertEqual(stored['UMCH'],'UNPROVEN');self.assertEqual(stored['detection'],'NO_POSITIVE_DETECTION_CLAIM')
  self.assertEqual(stored['structural_dead_end'],'NOT_DECLARED')
  subprocess.run([sys.executable,str(MODULE),'--check'],check=True,cwd=ROOT)
if __name__=='__main__':unittest.main()
