import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/sphere_window_pathscale.py';O=R/'studies/spacetime/sphere-window-pathscale-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class WindowPath(unittest.TestCase):
 def test_first_isotropy(self):
  m=mod();e=m.first_isotropy(2,.5);self.assertAlmostEqual(2*math.sqrt(math.pi),e);self.assertAlmostEqual(0,m.gap(e,2,.5,2))
 def test_eta_moves_landmark(self):
  m=mod();target=3;r=2;eta=math.pi*r*r/(2*target*target);self.assertAlmostEqual(target,m.first_isotropy(r,eta))
 def test_area_landmark_fixed(self):
  m=mod();r=2
  for eta in [.2,1,3]:self.assertAlmostEqual(math.pi*r*r/2,eta*m.first_isotropy(r,eta)**2)
 def test_ratio_confounding(self):
  m=mod()
  for e in [.3,1,2]:self.assertAlmostEqual(m.gap(e,2,.5,2),m.gap(e,4,2,2))
 def test_branch_alias(self):
  m=mod();r=1;eta=1;a=m.first_isotropy(r,eta);b=math.sqrt((3*math.pi/2)*r*r/eta);self.assertAlmostEqual(0,m.gap(a,r,eta,2));self.assertAlmostEqual(0,m.gap(b,r,eta,2))
 def test_ell0_absent(self):self.assertEqual('CURVATURE_RADIUS_PATH_LANDMARK_NOT_ELL0',mod().ell0_gate(['r','eta','ell']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SPHERE_WINDOW_NONRADIAL_LANDMARK_CURVATURE_RADIUS_PATH_SHAPE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
