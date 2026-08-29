import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PROGRAM=ROOT/'studies/spacetime/plane_wave_connection_path_cross_channel.py'
ARTIFACT=ROOT/'studies/spacetime/plane-wave-connection-path-cross-channel-results.json'
def load():
 spec=importlib.util.spec_from_file_location('connection_path_cross',PROGRAM);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class ConnectionPathCrossChannelTests(unittest.TestCase):
 def setUp(self):self.m=load()
 def test_endpoint_matched_internal_paths_move_window(self):
  r=self.m.path_counterexample(n=5000)
  self.assertLess(r['source_q_difference'],3e-10);self.assertLess(r['observer_q_difference'],3e-10)
  self.assertLess(r['source_a_difference'],3e-10);self.assertLess(r['observer_a_difference'],3e-10)
  self.assertGreater(r['internal_q_difference'],1e-2);self.assertGreater(r['transported_window_difference'],1e-3)
 def test_covariant_endpoint_channels_collide(self):
  r=self.m.path_counterexample(n=5000)
  self.assertLess(r['canonical_map_difference'],3e-10);self.assertLess(r['velocity_map_difference'],3e-10)
  self.assertLess(r['canonical_sachs_difference'],3e-10);self.assertLess(r['velocity_sachs_difference'],3e-10)
  self.assertGreater(r['naive_map_difference'],1e-3)
 def test_orientation_and_affine(self):
  o=self.m.orientation_control(n=5000);a=self.m.affine_control(n=5000)
  self.assertLess(o['so2_window_covariance_residual'],3e-10);self.assertLess(o['so2_map_covariance_residual'],3e-10)
  self.assertLess(o['reflection_oriented_component_sign_residual'],3e-10)
  self.assertLess(a['maximum_dimensionless_residual'],5e-10)
 def test_caustic_and_artifact(self):
  self.assertEqual(self.m.safe_graph([[1,0],[0,0]],[[0,0],[0,0]])['status'],'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR')
  data=self.m.build(n=5000);self.assertEqual(data['umch_status'],'UNPROVEN');self.assertFalse(data['ell0_identified']);self.assertFalse(data['positive_detection_claim'])
  self.assertEqual(data['structural_dead_end'],'NOT_DECLARED')
  subprocess.run(['python3',str(PROGRAM),'--check'],cwd=ROOT,check=True)
  self.assertEqual(data,json.loads(ARTIFACT.read_text()))
if __name__=='__main__':unittest.main()
