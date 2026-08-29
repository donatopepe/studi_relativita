import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/'studies/spacetime/einstein_static_spatial_holonomy.py'
ARTIFACT=ROOT/'studies/spacetime/einstein-static-spatial-holonomy-results.json'

def load_module():
 spec=importlib.util.spec_from_file_location('einstein_static_spatial_holonomy',MODULE)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class EinsteinStaticSpatialHolonomyTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load_module()
 def test_right_spherical_triangle_closes_and_has_positive_excess(self):
  t=self.m.right_triangle(.43,.71,3.2)
  self.assertAlmostEqual(math.cos(t['c_angle']),math.cos(.43)*math.cos(.71),places=13)
  self.assertAlmostEqual(t['excess'],t['area']/3.2**2,places=13)
  self.assertGreater(t['excess'],0)
  self.assertEqual(len(t['proper_side_lengths']),3)
 def test_loop_is_lorentz_and_fixes_time_leg(self):
  g=self.m.geometry_control()
  self.assertLess(g['metric_compatibility_residual'],1e-13)
  self.assertLess(g['fixed_time_residual'],1e-15)
  self.assertGreater(g['nonidentity_norm'],1e-3)
 def test_reversal_inverts_and_distinct_planes_do_not_commute(self):
  r=self.m.reversal_control();n=self.m.nonabelian_control()
  self.assertLess(r['inverse_residual'],1e-13)
  self.assertLess(r['signed_excess_residual'],1e-15)
  self.assertGreater(n['commutator_residual'],1e-3)
  self.assertGreater(n['ordered_product_difference'],1e-3)
 def test_holonomy_is_exponential_of_window_not_independent_channel(self):
  x=self.m.cross_channel_control()
  self.assertLess(x['holonomy_from_window_residual'],1e-13)
  self.assertLess(x['excess_minus_area_curvature_residual'],1e-14)
  self.assertFalse(x['holonomy_independent_channel'])
 def test_trace_aliases_sign_and_common_anchor_conjugacy(self):
  s=self.m.spectrum_control();a=self.m.anchor_control()
  self.assertLess(s['sign_trace_collision'],1e-14)
  self.assertGreater(s['raw_sign_difference'],1e-3)
  self.assertLess(a['common_conjugacy_residual'],1e-13)
  self.assertLess(a['characteristic_collision'],1e-12)
 def test_equal_excess_shapes_collide_in_holonomy_but_not_labelled_jacobi(self):
  c=self.m.shape_collision_control()
  self.assertLess(c['excess_collision'],2e-13)
  self.assertLess(c['holonomy_collision'],2e-13)
  self.assertGreater(c['boundary_length_difference'],1e-2)
  self.assertGreater(c['labelled_jacobi_difference'],1e-2)
 def test_curvature_radius_scale_orbit_and_flat_limit(self):
  s=self.m.scale_control();f=self.m.flat_control()
  self.assertLess(s['maximum_dimensionless_residual'],2e-13)
  self.assertGreater(s['proper_length_difference'],1e-2)
  self.assertLess(f['large_radius_nonidentity_norm'],2e-4)
  self.assertGreater(f['finite_radius_nonidentity_norm'],1e-3)
 def test_artifact_is_deterministic_complete_and_nonconfirmatory(self):
  subprocess.run([sys.executable,str(MODULE),'--check'],check=True,cwd=ROOT)
  stored=json.loads(ARTIFACT.read_text());self.assertEqual(stored,self.m.build())
  self.assertFalse(stored['ell0_identified']);self.assertEqual(stored['umch_status'],'UNPROVEN')
  self.assertFalse(stored['positive_detection_claim']);self.assertEqual(stored['structural_dead_end'],'NOT_DECLARED')
  self.assertFalse(stored['cross_channel_control']['holonomy_independent_channel'])
  for key in ('R','eta','tetrad','loop_planes','orientation','alpha_i','beta_i','c_i','proper_side_lengths','area_i','E_i','W_T_i','H_i','ordered_products','commutator','spectrum_i','chi_i','segment_Jacobi_i','shape_collision','scale_factor','flat_control'):
   self.assertIn(key,stored['raw_record'])

if __name__=='__main__':unittest.main()
