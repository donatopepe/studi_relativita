import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/schwarzschild_photon_orbit_holonomy.py'
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-orbit-holonomy-results.json'
def load():
 spec=importlib.util.spec_from_file_location('schwarzschild_photon_orbit_holonomy',MODULE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class SchwarzschildPhotonOrbitHolonomyTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_photon_sphere_boundary_is_null_geodesic_with_exact_duration(self):
  x=self.m.causal_control()
  self.assertAlmostEqual(x['photon_radius'],3.0)
  self.assertLess(x['null_residual'],1e-13)
  self.assertLess(x['maximum_geodesic_residual'],1e-13)
  self.assertLess(abs(x['coordinate_duration']-6*math.pi*math.sqrt(3)),1e-13)
  self.assertLess(abs(x['proper_duration']-6*math.pi),1e-13)
 def test_algebraic_transport_matches_independent_numerical_transport(self):
  x=self.m.transport_control()
  self.assertLess(x['maximum_segment_transport_residual'],2e-9)
  self.assertLess(x['loop_transport_residual'],2e-9)
 def test_loop_is_lorentz_nontrivial_and_reversal_inverts(self):
  g=self.m.geometry_control();r=self.m.reversal_control()
  self.assertLess(g['lorentz_residual'],2e-9)
  self.assertGreater(g['nonidentity_norm'],1e-4)
  self.assertLess(r['inverse_residual'],2e-9)
 def test_segment_order_is_noncommutative_but_not_independent_channel(self):
  x=self.m.ordering_control()
  self.assertGreater(x['segment_commutator_norm'],1e-4)
  self.assertGreater(x['ordered_product_difference'],1e-4)
  self.assertFalse(x['ordering_independent_channel'])
 def test_winding_is_protocol_label_not_continuous_geometric_rank(self):
  x=self.m.winding_control()
  self.assertGreater(x['two_winding_nonidentity_norm'],1e-4)
  self.assertGreater(x['batched_vs_repeated_loop_difference'],1e-4)
  self.assertEqual(x['continuous_geometric_rank_from_winding'],0)
  self.assertEqual(x['winding_role'],'DISCRETE_PROTOCOL_LABEL')
 def test_orientation_is_raw_but_characteristic_quotient_collides(self):
  x=self.m.orientation_control()
  self.assertGreater(x['raw_orientation_difference'],1e-4)
  self.assertLess(x['characteristic_collision'],2e-9)
  self.assertFalse(x['orientation_survives_characteristic_quotient'])
 def test_common_tetrad_conjugacy_preserves_characteristic_data(self):
  x=self.m.anchor_control()
  self.assertGreater(x['raw_conjugacy_difference'],1e-4)
  self.assertLess(x['characteristic_collision'],2e-9)
 def test_geometric_scaling_preserves_dimensionless_record_not_proper_scale(self):
  x=self.m.scale_control()
  self.assertLess(x['dimensionless_duration_residual'],1e-12)
  self.assertLess(x['holonomy_residual'],2e-9)
  self.assertGreater(x['proper_duration_difference'],1.0)
  self.assertFalse(x['ell0_identified'])
 def test_partial_arc_shrinks_to_identity_but_is_not_closed_photon_protocol(self):
  x=self.m.null_control()
  self.assertGreater(x['finite_arc_nonidentity_norm'],1e-5)
  self.assertLess(x['shrinking_arc_nonidentity_norm'],x['finite_arc_nonidentity_norm']/50)
  self.assertEqual(x['partial_arc_scope'],'MATHEMATICAL_NULL_ARC_WITH_STATIC_CLOSURE_NOT_CLOSED_NULL_GEODESIC')
 def test_artifact_contract_and_flags(self):
  d=json.loads(ARTIFACT.read_text())
  for key in ('M','r_ph','f_ph','tetrad','orientation','winding','Delta_phi','Delta_t','Delta_tau','null_tangent','null_residual','geodesic_residual','Gamma_t','Gamma_phi','A_null','A_closure','T_null','T_closure','H_photon','ordered_reverse','H_reverse','characteristic_coefficients','spectrum_or_surrogate','winding_products','Jacobian_joint','scale_factor','scale_orbit','flat_or_large_radius_control'):
   self.assertIn(key,d['raw'])
  self.assertEqual(d['raw']['Jacobian_joint'],'NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN')
  self.assertEqual(d['raw']['flat_or_large_radius_control'],'NO_FINITE_RADIUS_CIRCULAR_NULL_GEODESIC_AT_M_ZERO')
  self.assertEqual(d['classification'],'EXACT_NONRADIAL_NULL_ORBIT_LEVI_CIVITA_HOLONOMY_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL')
  self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim'])
  self.assertEqual(d['structural_dead_end'],'NOT_DECLARED')
 def test_artifact_is_current(self):
  before=ARTIFACT.read_bytes();subprocess.run([sys.executable,str(MODULE),'--output',str(ARTIFACT)],check=True);self.assertEqual(before,ARTIFACT.read_bytes())
if __name__=='__main__':unittest.main()
