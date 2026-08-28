import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/exact_window_separability.py';O=R/'studies/spacetime/exact-window-separability-results.json'
def mod():
 s=importlib.util.spec_from_file_location('e',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ExactWindow(unittest.TestCase):
 def test_flrw_windows_same_ray(self):
  m=mod();a=m.response(1,[1,2,3],[1,1,1],m.I);b=m.response(2,[4,5],[1,3],m.I);self.assertEqual(m.project(a),m.project(b))
 def test_schwarzschild_radial_windows_same_ray(self):
  m=mod();a=m.response(1,[m.schwarzschild_amp(r) for r in [2,3]],[1,1],m.S);b=m.response(3,[m.schwarzschild_amp(r) for r in [4,5]],[2,1],m.S);self.assertEqual(m.project(a),m.project(b))
 def test_zero_average_undefined(self):self.assertIsNone(mod().project(mod().response(1,[1,-1],[1,1],mod().I)))
 def test_ell0_absent(self):self.assertEqual('SEPARABLE_EXACT_PATTERN_NOT_ELL0',mod().ell0_gate(['ell','window','curvature']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('EXACT_PATTERN_WINDOW_AVERAGING_REMAINS_PROJECTIVELY_RADIAL',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
