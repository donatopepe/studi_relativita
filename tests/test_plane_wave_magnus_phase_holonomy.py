import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];PROGRAM=ROOT/'studies/spacetime/plane_wave_magnus_phase_holonomy.py';ART=ROOT/'studies/spacetime/plane-wave-magnus-phase-holonomy-results.json'
def load():
 s=importlib.util.spec_from_file_location('magnus_phase',PROGRAM);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class MagnusPhaseTests(unittest.TestCase):
 def setUp(self):self.m=load()
 def test_commutator_identity(self):
  r=self.m.commutator_control();self.assertLess(r['identity_residual'],2e-12);self.assertGreater(r['noncommuting_norm'],1e-2)
 def test_reversal_separates_second_magnus_not_first(self):
  r=self.m.reversal_control(n=900,samples=17)
  self.assertLess(r['window_difference'],2e-10);self.assertLess(r['omega1_difference'],2e-10)
  self.assertGreater(r['omega2_norm'],1e-3);self.assertLess(r['omega2_sign_reversal_residual'],2e-10)
 def test_raw_map_reversal_obeys_reciprocity_and_spectrum_collides(self):
  r=self.m.reversal_control(n=900,samples=17)
  self.assertGreater(r['raw_full_map_difference'],1e-2);self.assertLess(r['reciprocity_residual'],2e-9);self.assertLess(r['characteristic_difference'],2e-9)
 def test_constant_profile_collapses_second_magnus(self):
  r=self.m.constant_control(n=900);self.assertLess(r['omega2_norm'],2e-12);self.assertLess(r['ordered_exponential_residual'],2e-9)
 def test_orientation_affine_and_profile_controls(self):
  o=self.m.orientation_control(n=900);a=self.m.affine_control(n=900,samples=17);p=self.m.profile_control(n=900,samples=17)
  self.assertLess(o['so2_covariance_residual'],2e-9);self.assertLess(o['o2_characteristic_residual'],2e-9)
  self.assertLess(a['maximum_dimensionless_residual'],2e-8)
  self.assertLess(p['window_difference'],2e-10);self.assertGreater(p['omega2_difference'],1e-3);self.assertGreater(p['full_map_difference'],1e-3)
 def test_artifact_deterministic_and_nonconfirmatory(self):
  d=self.m.build(n=900,samples=17);self.assertEqual(d['umch_status'],'UNPROVEN');self.assertFalse(d['ell0_identified']);self.assertFalse(d['positive_detection_claim']);self.assertEqual(d['structural_dead_end'],'NOT_DECLARED')
  subprocess.run(['python3',str(PROGRAM),'--check'],cwd=ROOT,check=True);self.assertEqual(d,json.loads(ART.read_text()))
if __name__=='__main__':unittest.main()
