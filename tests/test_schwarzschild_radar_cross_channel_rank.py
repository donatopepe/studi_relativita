import importlib.util,json,pathlib,subprocess,sys,unittest
R=pathlib.Path(__file__).resolve().parents[1];M=R/'studies/spacetime/schwarzschild_radar_cross_channel_rank.py';A=R/'studies/spacetime/schwarzschild-radar-cross-channel-rank-results.json'
def load():s=importlib.util.spec_from_file_location('rank',M);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class RadarRank(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.m=load()
 def test_rapidity_is_exact_coordinate_for_raw_boost_block(self):
  x=self.m.boost_control();self.assertLess(x['reconstruction_residual'],2e-8);self.assertLess(x['transport_repeat_residual'],1e-12);self.assertGreater(abs(x['signed_rapidity']),.01)
 def test_duration_collision_tangent_changes_holonomy(self):
  x=self.m.tangent_control();self.assertLess(abs(x['duration_directional_derivative']),2e-7);self.assertGreater(abs(x['rapidity_directional_derivative']),1e-3);self.assertEqual(x['duration_only_rank'],1)
 def test_anchored_dimensionless_joint_map_is_locally_rank_two(self):
  x=self.m.rank_control();self.assertEqual(x['rank_raw'],2);self.assertGreater(abs(x['determinant_raw']),1e-4);self.assertGreater(x['singular_values_raw'][1],1e-4);self.assertLess(x['jacobian_step_convergence'],2e-5)
 def test_orientation_quotient_has_local_rank_but_global_collision(self):
  x=self.m.quotient_control();self.assertEqual(x['rank_even_quotient'],2);self.assertLess(x['duration_collision'],1e-14);self.assertLess(x['even_holonomy_collision'],1e-12);self.assertGreater(x['raw_orientation_difference'],.01);self.assertTrue(x['global_orientation_collision'])
 def test_anchor_and_absolute_scale_nuisance(self):
  a=self.m.anchor_control();s=self.m.scale_control();self.assertLess(a['common_conjugacy_residual'],1e-12);self.assertLess(a['characteristic_collision'],2e-8);self.assertGreater(a['raw_anchor_difference'],.01)
  self.assertLess(s['dimensionless_joint_residual'],2e-8);self.assertGreater(s['proper_time_difference'],.1);self.assertEqual(s['three_parameter_rank'],2);self.assertLess(s['scale_null_residual'],2e-6)
 def test_scan_and_null_limits(self):
  q=self.m.scan_control();n=self.m.null_control();self.assertGreater(q['minimum_interior_singular_value'],1e-5);self.assertGreater(q['sample_count'],10);self.assertLess(n['shrinking_second_singular_value'],1e-3);self.assertLess(n['flat_rapidity'],2e-8)
 def test_artifact_raw_record_and_nonclaims(self):
  subprocess.run([sys.executable,str(M),'--check'],cwd=R,check=True);d=json.loads(A.read_text());self.assertEqual(d,self.m.build())
  self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim']);self.assertEqual(d['structural_dead_end'],'NOT_DECLARED')
  for k in ('M','r_o','r_m','rho_o','rho_m','r_star','Delta_t','Delta_tau','H_radar','eta_radar','orientation','transport_residual','Jacobian_raw','singular_values_raw','determinant_raw','fixed_duration_tangent','holonomy_derivative_along_collision','quotient_maps','scale_factor','scale_orbit'):self.assertIn(k,d['raw_record'])
if __name__=='__main__':unittest.main()
