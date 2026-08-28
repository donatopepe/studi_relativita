import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/boundary_spectral_landmark.py';O=R/'studies/spacetime/boundary-spectral-landmark-results.json'
def mod():
 s=importlib.util.spec_from_file_location('b',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Boundary(unittest.TestCase):
 def test_crossing(self):self.assertAlmostEqual(2,mod().crossing(1,2,4))
 def test_free_boundary_moves_crossing(self):
  m=mod()
  for x in [1,3,7]:self.assertAlmostEqual(x,m.crossing(1,2,m.beta_for_crossing(1,2,x)))
 def test_no_real_positive_crossing(self):self.assertIsNone(mod().crossing(2,1,4))
 def test_additive_channel_boundary_changes_projective_shape(self):
  m=mod();self.assertNotEqual(m.project(m.operator(1,1,2,4)),m.project(m.operator(2,1,2,4)))
 def test_ell0_absent(self):self.assertEqual('BOUNDARY_GEOMETRIC_SCALE_NOT_ELL0',mod().ell0_gate(['ell','a','c','beta']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('BOUNDARY_SPECTRAL_LANDMARK_MOVABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
