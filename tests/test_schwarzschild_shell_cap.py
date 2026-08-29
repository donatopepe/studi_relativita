import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/schwarzschild_shell_cap.py';O=R/'studies/spacetime/schwarzschild-shell-cap-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ShellCap(unittest.TestCase):
 def test_uniform_shell_moment(self):
  m=mod();self.assertAlmostEqual((1/4-1/16)/(2*(4-2)),m.uniform_radial_moment(2,4))
 def test_factorization(self):
  m=mod();moment=.02;c=.6;self.assertEqual(tuple(moment*x for x in m.cap_pattern(c)),m.shell_cap(moment,c))
 def test_radial_profiles_same_projective_shape(self):
  m=mod();a=m.shell_cap(.02,.4);b=m.shell_cap(.07,.4)
  for x,y in zip(a,b):self.assertAlmostEqual(x/a[0],y/b[0])
 def test_hemisphere_zero_for_all_shells(self):
  m=mod()
  for moment in [.001,.1,3]:self.assertEqual((0,0,0),m.shell_cap(moment,0))
 def test_sign_reversal_cap_only(self):
  m=mod();a=m.shell_cap(.02,.4);b=m.shell_cap(.02,-.4)
  for x,y in zip(a,b):self.assertAlmostEqual(x/a[0],y/b[0]);self.assertLess(a[0]*b[0],0)
 def test_cap_law_moves_crossing(self):
  m=mod()
  for target in [.3,1,4]:self.assertAlmostEqual(target,m.hemisphere_crossing(math.pi/(2*target)))
 def test_ell0_absent(self):self.assertEqual('SCHWARZSCHILD_SHELL_CAP_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['r','theta','m']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SCHWARZSCHILD_PRODUCT_SHELL_CAP_REMAINS_FACTORABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
