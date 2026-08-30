import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/schwarzschild_photon_sphere_jacobi.py'
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-sphere-jacobi-results.json'
def load():
 spec=importlib.util.spec_from_file_location('schwarzschild_photon_sphere_jacobi',MODULE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class SchwarzschildPhotonSphereJacobiTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_affine_boundary_is_normalized_null_photon_orbit(self):
  x=self.m.boundary_control()
  self.assertAlmostEqual(x['r_ph'],3.0)
  self.assertEqual(x['k_tetrad'],[1.0,0.0,0.0,1.0])
  self.assertLess(x['null_residual'],1e-13)
  self.assertLess(x['geodesic_residual'],1e-12)
  self.assertLess(abs(x['L']-6*math.pi),1e-12)
 def test_screen_and_curvature_derive_tracefree_optical_tidal_matrix(self):
  x=self.m.curvature_control()
  self.assertLess(x['screen_metric_residual'],1e-12)
  self.assertLess(abs(x['trace']),1e-10)
  self.assertLess(x['finite_difference_residual'],2e-6)
  self.assertLess(abs(max(abs(v) for row in x['K'] for v in row)-1/9),2e-7)
 def test_exact_phase_map_matches_numerical_and_is_symplectic(self):
  x=self.m.phase_control()
  self.assertLess(x['exact_numerical_residual'],2e-8)
  self.assertLess(x['symplectic_residual'],2e-10)
  self.assertLess(abs(x['determinant']-1),2e-10)
 def test_vertex_endpoint_is_caustic_but_full_map_survives(self):
  x=self.m.vertex_control()
  self.assertEqual(x['S_vertex']['status'],'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR')
  self.assertTrue(x['caustic_flags']['endpoint'])
  self.assertGreaterEqual(len(x['conjugate_locations']),2)
  self.assertLess(x['endpoint_X_determinant_abs'],2e-9)
  self.assertLess(x['full_map_inverse_residual'],2e-9)
 def test_nonvertex_boundary_is_separate_and_regular(self):
  x=self.m.nonvertex_control()
  self.assertEqual(x['S_nonvertex']['status'],'REGULAR')
  self.assertGreater(abs(x['X_determinant']),1e-5)
 def test_zero_window_has_identity_and_generator_derivative(self):
  x=self.m.zero_window_control()
  self.assertLess(x['identity_residual'],1e-14)
  self.assertLess(x['generator_derivative_residual'],2e-7)
 def test_orientation_and_endpoint_quotient_do_not_create_scale_rank(self):
  o=self.m.orientation_control();q=self.m.endpoint_quotient_control()
  self.assertLess(o['raw_orientation_difference'],2e-9)
  self.assertLess(o['spectrum_collision'],2e-9)
  self.assertFalse(o['raw_orientation_survives'])
  self.assertLess(q['endpoint_action_residual'],2e-10)
  self.assertGreater(q['raw_entry_difference'],1e-5)
  self.assertFalse(q['raw_entries_are_calibration_invariant'])
 def test_affine_and_geometric_scale_orbits_preserve_dimensionless_map(self):
  a=self.m.affine_scale_control();g=self.m.geometric_scale_control()
  self.assertLess(a['phase_rate_converted_residual'],2e-9)
  self.assertLess(g['phase_rate_converted_residual'],2e-9)
  self.assertGreater(g['affine_length_difference'],1e-3)
  self.assertFalse(g['ell0_identified'])
 def test_holonomy_cross_map_is_dependent_and_winding_discrete(self):
  x=self.m.holonomy_cross_map()
  self.assertFalse(x['independent_channel'])
  self.assertEqual(x['winding_role'],'DISCRETE_PROTOCOL_LABEL')
  self.assertEqual(x['Jacobian_joint'],'NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN')
 def test_raw_contract_and_bounded_status(self):
  x=self.m.build();raw=x['raw']
  required={'M','r_ph','orientation','winding','affine_normalization','k_tetrad','screen_classes','screen_metric','screen_transport','optical_tidal_K','L','A','B','C','D','P_phase','characteristic_coefficients','spectrum_or_surrogate','vertex_X','vertex_V','nonvertex_S0','nonvertex_X','nonvertex_V','S_vertex','S_nonvertex','caustic_flags','conjugate_locations','orientation_controls','endpoint_quotient_controls','affine_scale_controls','geometric_scale_controls','holonomy_cross_map','Jacobian_joint','scale_factor','scale_orbit'}
  self.assertTrue(required.issubset(raw))
  self.assertEqual(x['status'],'SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0')
  self.assertEqual(x['umch_status'],'UNPROVEN');self.assertFalse(x['positive_detection_claim'])
  self.assertFalse(x['ell0_identified']);self.assertEqual(x['structural_dead_end'],'NOT_DECLARED')
 def test_artifact_is_current(self):
  expected=self.m.canonical(self.m.build());actual=json.loads(ARTIFACT.read_text())
  self.assertEqual(expected,actual)
  subprocess.run([sys.executable,str(MODULE),'--check'],check=True,cwd=ROOT)
if __name__=='__main__':unittest.main()
