import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'finite_window_operator.py';O=R/'studies'/'spacetime'/'finite-window-operator-results.json'
def mod():
 s=importlib.util.spec_from_file_location('fw',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Window(unittest.TestCase):
 def test_separable_profile_is_collinear(self):
  m=mod();a=m.response(1,[1,2,3],1);b=m.response(2,[1,2,3],4);self.assertEqual('PROJECTIVE_SCALE_NON_IDENTIFIABLE_SEPARABLE_WINDOW',m.compare(a,b))
 def test_two_profiles_create_nonradial_shape(self):
  m=mod();a=m.response(1,[1,-1,0],1,[0,1,-1],0);b=m.response(2,[1,-1,0],1,[0,1,-1],1);self.assertEqual('NONRADIAL_PROFILE_DEPENDENT_SHAPE_ONLY',m.compare(a,b));self.assertNotEqual(m.project(a),m.project(b))
 def test_reparameterization_blocks_ell0(self):
  m=mod();self.assertEqual('ELL0_NOT_PRESENT_IN_GEOMETRIC_WINDOW_CONTROL',m.identifiability(['ell','profile_coefficients','window']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('NONRADIAL_GEOMETRIC_SHAPE_NOT_ELL0_LANDMARK',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
