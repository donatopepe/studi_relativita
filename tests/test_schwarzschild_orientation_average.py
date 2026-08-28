import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/schwarzschild_orientation_average.py';O=R/'studies/spacetime/schwarzschild-orientation-average-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class CapAverage(unittest.TestCase):
 def test_axis_limit(self):self.assertEqual([.25,.25,-.5],mod().projective(mod().average(0)))
 def test_caps_same_projective_spectrum_within_sign_sector(self):
  m=mod()
  for t in [.2,.7,1.2]:self.assertEqual([-.5,.25,.25],m.projective_spectrum(m.average(t)))
  for t in [2.0,2.8]:self.assertEqual([-.25,-.25,.5],m.projective_spectrum(m.average(t)))
 def test_hemisphere_zero(self):self.assertEqual([[0,0,0],[0,0,0],[0,0,0]],mod().average(math.pi/2))
 def test_full_sphere_zero(self):self.assertEqual([[0,0,0],[0,0,0],[0,0,0]],mod().average(math.pi))
 def test_trace_free(self):
  m=mod()
  for t in [0,.7,1.2,2.8,math.pi]:self.assertAlmostEqual(0,m.trace(m.average(t)))
 def test_ell0_absent(self):self.assertEqual('ORIENTATION_MEASURE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['Theta','n']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SCHWARZSCHILD_CAP_AVERAGE_SIGN_REVERSAL_ORIENTATION_DOMAIN_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
