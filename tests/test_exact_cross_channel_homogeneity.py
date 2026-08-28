import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/exact_cross_channel_homogeneity.py';O=R/'studies/spacetime/exact-cross-channel-homogeneity-results.json'
def mod():
 s=importlib.util.spec_from_file_location('x',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ExactCross(unittest.TestCase):
 def test_equal_homogeneity_ratio_scale_free(self):
  m=mod();self.assertEqual(m.ratio(m.observe(1,2,3,4,5),m.observe(1,7,11,13,17)),m.ratio(m.observe(9,2,3,4,5),m.observe(9,7,11,13,17)))
 def test_zero_channel_undefined(self):self.assertIsNone(mod().ratio(3,0))
 def test_gain_geometry_confounding(self):
  m=mod();target=6;self.assertEqual(target,m.ratio(m.observe(2,1,1,3,2),m.observe(2,1,1,1,1)))
 def test_ell0_absent(self):self.assertEqual('EQUAL_HOMOGENEITY_RATIO_NOT_ELL0',mod().ell0_gate(['ell','g','c','k']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('EXACT_CROSS_CHANNEL_EQUAL_HOMOGENEITY_SCALE_CANCELS',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
