import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PROGRAM=ROOT/'studies/spacetime/plane_wave_levi_civita_holonomy.py'
ART=ROOT/'studies/spacetime/plane-wave-levi-civita-holonomy-results.json'
def load():
 s=importlib.util.spec_from_file_location('lc_holonomy',PROGRAM);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class LeviCivitaHolonomyTests(unittest.TestCase):
 def setUp(self):self.m=load()
 def test_connection_derived_transport_is_lorentz_and_fixes_parallel_null_vector(self):
  r=self.m.geometry_control()
  self.assertLess(r['metric_compatibility_residual'],2e-9)
  self.assertLess(r['parallel_null_residual'],2e-11)
  self.assertGreater(r['nonidentity_norm'],1e-3)
  self.assertLess(r['null_rotation_residual'],2e-9)
 def test_nontrivial_raw_holonomies_have_colliding_unipotent_spectra(self):
  r=self.m.spectrum_control()
  self.assertGreater(r['raw_matrix_difference'],1e-3)
  self.assertLess(r['unit_eigenvalue_residual'],2e-9)
  self.assertLess(r['characteristic_collision_residual'],2e-9)
  self.assertGreater(r['raw_b_difference'],1e-3)
 def test_reversal_inverts_raw_holonomy_but_not_spectrum(self):
  r=self.m.reversal_control()
  self.assertLess(r['inverse_residual'],2e-9)
  self.assertLess(r['b_sign_residual'],2e-9)
  self.assertLess(r['characteristic_residual'],2e-9)
 def test_based_loop_composition_is_abelian_and_additive(self):
  r=self.m.composition_control()
  self.assertLess(r['commutator_residual'],2e-9)
  self.assertLess(r['parameter_addition_residual'],2e-9)
  self.assertGreater(r['separate_loop_parameter_norm'],1e-3)
 def test_rectangle_holonomy_is_fixed_by_tidal_window_cross_channel_map(self):
  r=self.m.cross_channel_control()
  self.assertLess(r['b_minus_window_times_displacement_residual'],2e-8)
  self.assertLess(r['holonomy_from_window_residual'],2e-8)
  self.assertLess(r['reversed_profile_window_collision'],2e-10)
  self.assertGreater(r['reversed_profile_jacobi_difference'],1e-4)
  self.assertFalse(r['holonomy_independent_channel'])
 def test_profile_anchor_affine_and_null_controls(self):
  p=self.m.profile_control();a=self.m.anchor_control();s=self.m.affine_control();n=self.m.null_control()
  self.assertGreater(p['profile_sample_difference'],1e-3)
  self.assertLess(p['holonomy_collision_residual'],2e-8)
  self.assertGreater(p['jacobi_map_difference'],1e-4)
  self.assertLess(a['so2_conjugacy_residual'],2e-9)
  self.assertLess(a['screen_norm_residual'],2e-9)
  self.assertGreater(a['boost_parameter_difference'],1e-3)
  self.assertLess(a['boost_conjugacy_residual'],2e-9)
  self.assertLess(s['maximum_dimensionless_residual'],2e-8)
  self.assertLess(n['identity_residual'],2e-11)
 def test_artifact_deterministic_and_nonconfirmatory(self):
  subprocess.run(['python3',str(PROGRAM),'--check'],check=True)
  generated=self.m.build();stored=json.loads(ART.read_text())
  self.assertEqual(generated,stored)
  self.assertEqual(stored['status'],'EXACT_PLANE_WAVE_LEVI_CIVITA_NULL_ROTATION_HOLONOMY_RAW_LOOP_VECTOR_NONTRIVIAL_SPECTRUM_UNIPOTENT_ABELIAN_AND_AFFINE_SCALE_BLIND_NOT_ELL0')
  self.assertEqual(stored['physical_gate'],'PHYSICAL_CAUSAL_SPACETIME_LOOP_FAMILY_TETRAD_ANCHOR_NULL_NORMALIZATION_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED')
  self.assertEqual(stored['scope'],'FOUR_DIMENSIONAL_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_BRINKMANN_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED')
  self.assertFalse(stored['ell0_identified']);self.assertEqual(stored['umch_status'],'UNPROVEN')
  self.assertFalse(stored['positive_detection_claim']);self.assertEqual(stored['structural_dead_end'],'NOT_DECLARED')
  self.assertFalse(stored['cross_channel_control']['holonomy_independent_channel'])
  for key in ('K(u)','Gamma_mu(z)','loop_vertices','orientation','a','u_a','u_b','T_segments','H_LC','b_LC','spectrum_LC','chi_LC','W_a','P_K','L'):
   self.assertIn(key,stored['raw_record'])
if __name__=='__main__':unittest.main()
