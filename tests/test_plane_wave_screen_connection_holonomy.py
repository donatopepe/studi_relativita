import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];PROGRAM=ROOT/'studies/spacetime/plane_wave_screen_connection_holonomy.py';ART=ROOT/'studies/spacetime/plane-wave-screen-connection-holonomy-results.json'
def load():
 s=importlib.util.spec_from_file_location('screen_holonomy',PROGRAM);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ScreenHolonomyTests(unittest.TestCase):
 def setUp(self):self.m=load()
 def test_ordered_product_matches_so2_exponential(self):
  r=self.m.endpoint_matched_control(n=6000,samples=15)
  self.assertLess(r['maximum_ordered_analytic_residual'],2e-10)
 def test_partial_history_moves_but_endpoint_collides(self):
  r=self.m.endpoint_matched_control(n=6000,samples=15)
  self.assertGreater(r['maximum_intermediate_holonomy_difference'],1e-2)
  self.assertLess(r['endpoint_holonomy_difference'],2e-10)
  self.assertLess(r['relative_endpoint_identity_residual'],2e-10)
  self.assertLess(r['canonical_endpoint_loop_identity_residual'],2e-10)
 def test_trace_aliases_sign_and_winding(self):
  r=self.m.alias_control()
  self.assertGreater(r['raw_sign_matrix_difference'],1e-2)
  self.assertLess(r['sign_trace_residual'],2e-12)
  self.assertLess(r['winding_matrix_residual'],2e-12)
  self.assertLess(r['winding_trace_residual'],2e-12)
 def test_zero_orientation_and_affine_controls(self):
  z=self.m.zero_connection_control(n=6000,samples=15);o=self.m.orientation_control(n=6000,samples=15);a=self.m.affine_control(n=6000,samples=15)
  self.assertLess(z['maximum_identity_residual'],2e-10)
  self.assertLess(o['so2_covariance_residual'],2e-10)
  self.assertLess(o['reflection_matrix_residual'],2e-10)
  self.assertLess(o['reflection_trace_residual'],2e-12)
  self.assertLess(a['maximum_dimensionless_residual'],2e-10)
 def test_artifact_is_deterministic_and_nonconfirmatory(self):
  d=self.m.build(n=6000,samples=15)
  self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim']);self.assertEqual(d['structural_dead_end'],'NOT_DECLARED')
  subprocess.run(['python3',str(PROGRAM),'--check'],cwd=ROOT,check=True);self.assertEqual(d,json.loads(ART.read_text()))
if __name__=='__main__':unittest.main()
