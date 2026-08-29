import importlib.util,json,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/schwarzschild_mixed_levi_civita_holonomy.py'
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-mixed-levi-civita-holonomy-results.json'
def load():
 spec=importlib.util.spec_from_file_location('schwarzschild_mixed_levi_civita_holonomy',MODULE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class SchwarzschildMixedHolonomyTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_connection_and_loop_preserve_metric(self):
  c=self.m.connection_control();g=self.m.geometry_control()
  self.assertLess(c['maximum_metric_connection_residual'],2e-7)
  self.assertLess(g['maximum_lorentz_residual'],2e-8)
  self.assertGreater(g['tr_nonidentity_norm'],1e-3)
  self.assertGreater(g['rphi_nonidentity_norm'],1e-3)
 def test_reversal_inverts_and_refinement_converges(self):
  r=self.m.reversal_control();q=self.m.refinement_control()
  self.assertLess(r['maximum_inverse_residual'],3e-8)
  self.assertLess(q['fine_difference'],q['coarse_difference']/8)
  self.assertLess(q['fine_difference'],2e-8)
 def test_mixed_planes_are_noncommuting(self):
  n=self.m.nonabelian_control()
  self.assertGreater(n['commutator_nonidentity_norm'],1e-3)
  self.assertGreater(n['ordered_product_difference'],1e-3)
 def test_shrinking_loop_recovers_local_curvature_but_finite_flux_is_incomplete(self):
  x=self.m.cross_channel_control()
  self.assertLess(x['small_loop_log_flux_residual'],2e-4)
  self.assertGreater(x['finite_naive_flux_residual'],1e-3)
  self.assertFalse(x['holonomy_independent_channel'])
  self.assertEqual(x['finite_map_gate'],'PATH_ORDERED_CONNECTION_HISTORY_REQUIRED')
 def test_equal_coordinate_area_boundary_placement_changes_holonomy(self):
  b=self.m.boundary_control()
  self.assertLess(b['coordinate_area_collision'],1e-14)
  self.assertGreater(b['radial_boundary_difference'],.1)
  self.assertGreater(b['raw_holonomy_difference'],1e-3)
 def test_spectrum_and_conjugacy_lose_anchored_raw_information(self):
  s=self.m.spectrum_control();a=self.m.anchor_control()
  self.assertGreater(s['raw_reversal_difference'],1e-3)
  self.assertLess(s['reversal_characteristic_collision'],2e-8)
  self.assertLess(a['common_conjugacy_residual'],2e-8)
  self.assertLess(a['characteristic_collision'],2e-8)
 def test_geometric_scale_orbit_and_null_limits(self):
  s=self.m.scale_control();n=self.m.null_control()
  self.assertLess(s['maximum_holonomy_residual'],3e-8)
  self.assertGreater(s['proper_scale_difference'],.1)
  self.assertLess(n['flat_identity_residual'],2e-8)
  self.assertLess(n['shrinking_loop_identity_residual'],2e-4)
 def test_artifact_is_deterministic_and_nonconfirmatory(self):
  subprocess.run([sys.executable,str(MODULE),'--check'],cwd=ROOT,check=True)
  data=json.loads(ARTIFACT.read_text());self.assertEqual(data,self.m.build())
  self.assertFalse(data['ell0_identified']);self.assertFalse(data['positive_detection_claim'])
  self.assertEqual(data['umch_status'],'UNPROVEN');self.assertEqual(data['structural_dead_end'],'NOT_DECLARED')
  for key in ('M','metric','tetrad','Gamma_mu','loop_vertices','orientations','segment_transports','H_tr','H_rphi','ordered_products','commutator','spectrum','characteristic_coefficients','curvature_flux','refinement_history','boundary_control','scale_factor','null_control'):
   self.assertIn(key,data['raw_record'])
if __name__=='__main__':unittest.main()
