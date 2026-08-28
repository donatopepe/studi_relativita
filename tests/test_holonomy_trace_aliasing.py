import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/holonomy_trace_aliasing.py';O=R/'studies/spacetime/holonomy-trace-aliasing-results.json'
def mod():
 s=importlib.util.spec_from_file_location('h',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Aliasing(unittest.TestCase):
 def test_even_periodic_collisions(self):
  m=mod()
  for p in [.2,1,2.5]:self.assertAlmostEqual(m.trace(p),m.trace(-p));self.assertAlmostEqual(m.trace(p),m.trace(p+2*math.pi))
 def test_principal_branch_inverse(self):
  m=mod()
  for p in [0,.2,1,math.pi]:self.assertAlmostEqual(p,m.principal_phase(m.trace(p)))
 def test_all_branches_reproduce_trace(self):
  m=mod();t=m.trace(.7)
  for p in m.branches(t,2):self.assertAlmostEqual(t,m.trace(p))
 def test_area_curvature_collision(self):
  m=mod();self.assertAlmostEqual(m.phase(2,3),m.phase(1,6));self.assertAlmostEqual(m.trace(m.phase(2,3)),m.trace(m.phase(1,6)))
 def test_ell0_absent(self):self.assertEqual('HOLONOMY_PHASE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['phi','k','area']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('FINITE_HOLONOMY_TRACE_PERIODIC_BRANCH_NONIDENTIFIABLE',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
