import importlib.util,json,math,pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];MODULE=ROOT/'studies/spacetime/schwarzschild_radar_holonomy.py';ART=ROOT/'studies/spacetime/schwarzschild-radar-holonomy-results.json'
def load():
 s=importlib.util.spec_from_file_location('radar',MODULE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class RadarHolonomy(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_exact_radar_time_and_causal_segments(self):
  x=self.m.causal_control()
  self.assertLess(x['travel_time_formula_residual'],1e-14)
  self.assertLess(x['maximum_null_residual'],2e-12)
  self.assertGreater(x['round_trip_proper_time'],0)
 def test_transport_is_lorentz_nontrivial_reversible_and_convergent(self):
  g=self.m.geometry_control();r=self.m.reversal_control();q=self.m.refinement_control()
  self.assertLess(g['lorentz_residual'],2e-8);self.assertGreater(g['nonidentity_norm'],1e-4)
  self.assertLess(r['inverse_residual'],3e-8);self.assertLess(q['fine_difference'],q['coarse_difference']/8)
 def test_causal_boundary_differs_from_matched_coordinate_rectangle(self):
  x=self.m.rectangle_control()
  self.assertLess(x['radial_endpoint_collision'],1e-14);self.assertLess(x['coordinate_duration_collision'],1e-14)
  self.assertGreater(x['raw_holonomy_difference'],1e-4)
 def test_fixed_duration_does_not_fix_boundary_but_joint_raw_separates_toy_pair(self):
  x=self.m.endpoint_control()
  self.assertLess(x['duration_ratio_collision'],2e-10);self.assertGreater(x['mirror_radius_difference'],.1)
  self.assertGreater(x['anchored_raw_holonomy_difference'],1e-4)
  self.assertEqual(x['duration_only_identifies_boundary'],False)
  self.assertEqual(x['joint_raw_toy_pair_collision'],False)
 def test_quotients_lose_orientation_anchor_information(self):
  s=self.m.spectrum_control();a=self.m.anchor_control()
  self.assertGreater(s['raw_reversal_difference'],1e-4);self.assertLess(s['characteristic_collision'],2e-8)
  self.assertLess(a['common_conjugacy_residual'],2e-8);self.assertLess(a['characteristic_collision'],2e-8)
 def test_scaling_and_null_controls(self):
  s=self.m.scale_control();n=self.m.null_control()
  self.assertLess(s['dimensionless_time_residual'],2e-12);self.assertLess(s['holonomy_residual'],3e-8)
  self.assertGreater(s['proper_time_difference'],.1);self.assertLess(n['flat_identity_residual'],2e-8);self.assertLess(n['shrinking_identity_residual'],3e-4)
 def test_artifact_and_nonclaims(self):
  subprocess.run([sys.executable,str(MODULE),'--check'],cwd=ROOT,check=True)
  d=json.loads(ART.read_text());self.assertEqual(d,self.m.build())
  self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim']);self.assertEqual(d['structural_dead_end'],'NOT_DECLARED')
  for k in ('M','r_o','r_m','f','r_star','Delta_t','Delta_tau','tetrads','vertices','segment_labels','null_residuals','segment_transports','H_radar','orientation','characteristic_coefficients','curvature_window','refinement_history','endpoint_control','scale_factor','null_control'):self.assertIn(k,d['raw_record'])
if __name__=='__main__':unittest.main()
