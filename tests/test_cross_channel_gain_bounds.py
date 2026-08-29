import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/cross_channel_gain_bounds.py';O=R/'studies/spacetime/cross-channel-gain-bounds-results.json'
def mod():
 s=importlib.util.spec_from_file_location('g',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class GainBounds(unittest.TestCase):
 def test_positive_delta_interval(self):self.assertEqual((1,2),mod().feasible_interval(4,1,2,4,1))
 def test_negative_delta_sorted(self):self.assertEqual((.5,1),mod().feasible_interval(4,1,2,4,-1))
 def test_every_candidate_attainable(self):
  m=mod();R=9;C=1;lo,hi=m.feasible_interval(R,C,1,9,2)
  for x in [lo,(lo+hi)/2,hi]:
   g=m.required_gain(R,C,x,2);self.assertGreaterEqual(g,1);self.assertLessEqual(g,9);self.assertAlmostEqual(R,g*C*x**2)
 def test_collapsed_bound_point(self):self.assertEqual((4,4),mod().feasible_interval(8,1,2,2,1))
 def test_equal_delta_gate(self):self.assertEqual('X_ABSENT_EQUAL_HOMOGENEITY',mod().equal_delta_gate(4,2,1,3));self.assertEqual('GAIN_BOUNDS_INCONSISTENT',mod().equal_delta_gate(8,2,1,3))
 def test_invalid(self):
  m=mod();self.assertRaises(ValueError,m.feasible_interval,1,1,1,2,0);self.assertRaises(ValueError,m.feasible_interval,1,1,2,1,1)
 def test_ell0_absent(self):self.assertEqual('BOUNDED_GAIN_SET_NOT_ELL0',mod().ell0_gate(['x','gamma']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('CROSS_CHANNEL_BOUNDED_GAIN_SHARP_SET_IDENTIFICATION_ONLY',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
