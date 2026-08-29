import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_smooth_profile.py';O=R/'studies/spacetime/jacobi-smooth-profile-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class SmoothProfile(unittest.TestCase):
 def test_equal_integral(self):
  m=mod();self.assertAlmostEqual(1,m.integrate(lambda t:m.uniform(t,2),2));self.assertAlmostEqual(1,m.integrate(lambda t:m.beta22(t,2),2))
 def test_weighted_moments_exact(self):
  m=mod();self.assertAlmostEqual(4/6,m.weighted(lambda t:m.uniform(t,2),2),places=8);self.assertAlmostEqual(4/5,m.weighted(lambda t:m.beta22(t,2),2),places=8)
 def test_endpoint_difference(self):
  m=mod();self.assertAlmostEqual(.1*4/30,m.first_endpoint(lambda t:m.uniform(t,2),2,.1)-m.first_endpoint(lambda t:m.beta22(t,2),2,.1),places=8)
 def test_reflection_collision(self):
  m=mod();S=2;f=lambda t:2*t/S**2;rf=lambda t:f(S-t);self.assertAlmostEqual(m.integrate(f,S),m.integrate(rf,S));self.assertAlmostEqual(m.weighted(f,S),m.weighted(rf,S))
 def test_ell0_absent(self):self.assertEqual('SMOOTH_OPTICAL_PROFILE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['epsilon','f','S']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_SMOOTH_EQUAL_INTEGRAL_DIFFERENT_WEIGHTED_ENDPOINT_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
