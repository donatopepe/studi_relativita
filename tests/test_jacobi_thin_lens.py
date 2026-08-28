import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_thin_lens.py';O=R/'studies/spacetime/jacobi-thin-lens-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ThinLens(unittest.TestCase):
 def test_continuity_and_jump(self):
  m=mod();k=2;a=1
  self.assertEqual(a,m.solution(a,k,a));self.assertEqual(1-k*a,m.post_slope(k,a))
 def test_endpoint_depends_on_location(self):
  m=mod();self.assertNotEqual(m.endpoint(5,2,1),m.endpoint(5,2,2))
 def test_caustic_formula(self):
  m=mod()
  for k,a in [(2,1),(3,1),(1,2)]:
   c=m.caustic(k,a);self.assertAlmostEqual(0,m.solution(c,k,a));self.assertGreater(c,a)
 def test_no_caustic_below_threshold(self):
  m=mod();self.assertIsNone(m.caustic(1,.5));self.assertIsNone(m.caustic(1,1))
 def test_same_strength_different_caustic(self):
  m=mod();self.assertNotEqual(m.caustic(2,.75),m.caustic(2,2))
 def test_ell0_absent(self):self.assertEqual('ORDERED_OPTICAL_PROFILE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['k','a','S']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_INTEGRATED_FOCUSING_INSUFFICIENT_PROFILE_LOCATION_REQUIRED',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
