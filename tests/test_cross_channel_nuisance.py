import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/cross_channel_nuisance.py';O=R/'studies/spacetime/cross-channel-nuisance-results.json'
def mod():
 s=importlib.util.spec_from_file_location('c',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Cross(unittest.TestCase):
 def test_common_gain_cancels(self):
  m=mod();obs=m.observe(3,2,2,1,2,1,5,5);self.assertAlmostEqual(3,m.infer_x(obs,2,1,2,1,1))
 def test_independent_gain_can_mimic_any_x(self):
  m=mod();obs=m.observe(3,2,2,1,2,1,1,4);self.assertAlmostEqual(obs[0]/obs[1],m.required_gain_ratio(obs,2,1,2,1,7)*(2/1)*7)
  self.assertEqual('X_STRUCTURALLY_NON_IDENTIFIABLE_FREE_GAIN_RATIO',m.gate(2,1,None))
 def test_bounded_gain_yields_interval(self):
  m=mod();lo,hi=m.x_interval(6,2,1,2,1,.5,2);self.assertAlmostEqual(1.5,lo);self.assertAlmostEqual(6,hi)
 def test_equal_exponents(self):self.assertEqual('X_NON_IDENTIFIABLE_EQUAL_EXPONENTS',mod().gate(1,1,1))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('CROSS_CHANNEL_IDENTIFIABILITY_REQUIRES_CALIBRATION_QUOTIENT',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
