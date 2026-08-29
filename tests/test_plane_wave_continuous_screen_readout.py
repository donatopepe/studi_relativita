import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];PROGRAM=ROOT/'studies/spacetime/plane_wave_continuous_screen_readout.py';ART=ROOT/'studies/spacetime/plane-wave-continuous-screen-readout-results.json'
def load():
 s=importlib.util.spec_from_file_location('continuous_readout',PROGRAM);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ContinuousReadoutTests(unittest.TestCase):
 def setUp(self):self.m=load()
 def test_raw_histories_move_but_endpoint_collides(self):
  r=self.m.history_control(n=4000,samples=13)
  self.assertGreater(r['maximum_intermediate_canonical_difference'],1e-2);self.assertGreater(r['maximum_intermediate_velocity_difference'],1e-2)
  self.assertLess(r['endpoint_canonical_difference'],3e-10);self.assertLess(r['endpoint_velocity_difference'],3e-10)
 def test_local_gauge_and_inertial_reconstruction(self):
  r=self.m.history_control(n=4000,samples=13)
  self.assertLess(r['maximum_local_gauge_residual'],3e-10);self.assertLess(r['maximum_inertial_reconstruction_difference'],3e-10)
 def test_zero_path_orientation_and_affine(self):
  z=self.m.zero_path_control(n=4000,samples=13);o=self.m.orientation_control(n=4000,samples=13);a=self.m.affine_control(n=4000,samples=13)
  self.assertLess(z['maximum_raw_history_difference'],3e-10);self.assertLess(o['so2_history_covariance_residual'],3e-10);self.assertLess(o['reflection_signed_component_residual'],3e-10);self.assertLess(a['maximum_dimensionless_residual'],5e-10)
 def test_artifact(self):
  d=self.m.build(n=4000,samples=13);self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim']);self.assertEqual(d['structural_dead_end'],'NOT_DECLARED');self.assertEqual(len(d['history']['samples']),13)
  subprocess.run(['python3',str(PROGRAM),'--check'],cwd=ROOT,check=True);self.assertEqual(d,json.loads(ART.read_text()))
if __name__=='__main__':unittest.main()
