import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/plane_wave_finite_window.py';O=R/'studies/spacetime/plane-wave-finite-window-results.json'
def mod():
 s=importlib.util.spec_from_file_location('pww',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class PlaneWaveWindow(unittest.TestCase):
 def setUp(self):self.m=mod()
 def test_fixed_polarization_is_projectively_radial(self):self.assertLess(self.m.projective_distance(self.m.window(.4,'fixed'),self.m.window(1.1,'fixed')),1e-10)
 def test_centered_odd_rotation_is_symmetry_collapsed(self):self.assertLess(self.m.projective_distance(self.m.window(.4,'odd'),self.m.window(1.1,'odd')),1e-10)
 def test_asymmetric_rotation_is_nonradial(self):self.assertGreater(self.m.projective_distance(self.m.window(.4,'asymmetric'),self.m.window(1.1,'asymmetric')),1e-3)
 def test_window_center_changes_direction(self):self.assertGreater(self.m.projective_distance(self.m.window(.9,'odd',center=0),self.m.window(.9,'odd',center=.25)),1e-3)
 def test_kernel_changes_direction(self):self.assertGreater(self.m.projective_distance(self.m.window(1.0,'asymmetric',kernel='top_hat'),self.m.window(1.0,'asymmetric',kernel='triangular')),1e-4)
 def test_tracefree(self):
  for mode in ('fixed','odd','asymmetric'):self.assertAlmostEqual(0,self.m.trace(self.m.profile(.31,mode)),places=12)
 def test_ell0_absent(self):self.assertEqual('EXACT_PLANE_WAVE_NONRADIALITY_NOT_ELL0',self.m.ell0_gate(['L','omega','phase','center','kernel']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('EXACT_PLANE_WAVE_FINITE_WINDOW_NONRADIAL_GEOMETRY_PROTOCOL_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
