import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/holonomy_path_shape.py';O=R/'studies/spacetime/holonomy-path-shape-results.json'
def mod():
 s=importlib.util.spec_from_file_location('h',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class PathShape(unittest.TestCase):
 def test_trace_formula(self):self.assertAlmostEqual(2-3*4,mod().loop_trace(2,3))
 def test_target_crossing(self):
  m=mod();tau=1
  for x in [1,2,5]:
   rho=m.rho_for_crossing(tau,x);self.assertAlmostEqual(x,m.crossing(tau,rho));self.assertAlmostEqual(tau,m.loop_trace(x,rho))
 def test_zero_shape_no_crossing(self):self.assertIsNone(mod().crossing(1,0))
 def test_trace_similarity_invariant(self):
  m=mod();h=m.loop(2,3);s=[[1,1],[0,1]];self.assertAlmostEqual(m.trace(h),m.trace(m.mm(m.mm(m.inv(s),h),s)))
 def test_ell0_absent(self):self.assertEqual('PATH_SHAPE_GEOMETRIC_SCALE_NOT_ELL0',mod().ell0_gate(['ell','rho','tau']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('HOLONOMY_TRACE_LANDMARK_PATH_SHAPE_MOVABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
