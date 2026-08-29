import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/sphere_transport_mixture.py';O=R/'studies/spacetime/sphere-transport-mixture-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class SphereTransport(unittest.TestCase):
 def test_holonomy_angle(self):self.assertAlmostEqual(math.pi/2,mod().holonomy_angle(1,math.pi/2))
 def test_mixed_eigenvalues(self):
  m=mod();self.assertEqual((1,3),m.mixed_eigenvalues(3,1,0));self.assertAlmostEqual(2-math.sqrt(2)/2,m.mixed_eigenvalues(3,1,math.pi/4)[0]);self.assertAlmostEqual(2+math.sqrt(2)/2,m.mixed_eigenvalues(3,1,math.pi/4)[1])
 def test_isotropy_at_quarter_turn(self):self.assertEqual((2,2),mod().mixed_eigenvalues(3,1,math.pi/2))
 def test_area_aliasing(self):
  m=mod();self.assertEqual(m.mixed_eigenvalues(3,1,.3),m.mixed_eigenvalues(3,1,math.pi-.3))
 def test_signed_path_invisible(self):
  m=mod();self.assertEqual(m.mixed_eigenvalues(3,1,.7),m.mixed_eigenvalues(3,1,-.7))
 def test_ell0_absent(self):self.assertEqual('SPHERE_TRANSPORT_MIXTURE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['K','area']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SPHERE_HOLONOMY_MIXTURE_SPECTRAL_SHAPE_PATH_AREA_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
