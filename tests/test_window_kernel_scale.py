import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/window_kernel_scale.py';O=R/'studies/spacetime/window-kernel-scale-results.json'
def mod():
 s=importlib.util.spec_from_file_location('w',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class KernelScale(unittest.TestCase):
 def test_average_formula(self):self.assertEqual([[1,0],[0,12]],mod().response(2,3))
 def test_crossing_is_isotropic(self):
  m=mod()
  for k in [.5,1,4]:
   r=m.response(m.crossing(k),k);self.assertEqual(1,r[0][0]);self.assertAlmostEqual(1,r[1][1])
 def test_any_target_movable(self):
  m=mod()
  for x in [.5,2,5]:self.assertAlmostEqual(x,m.crossing(m.kappa_for_crossing(x)))
 def test_physical_half_width_constant(self):
  m=mod()
  for k in [.5,1,4]:self.assertAlmostEqual(math.sqrt(3),m.physical_half_width(m.crossing(k),k))
 def test_ell0_absent(self):self.assertEqual('KERNEL_SCALE_CONVENTION_NOT_ELL0',mod().ell0_gate(['ell','kappa']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('FINITE_WINDOW_SPECTRAL_LANDMARK_KERNEL_DILATION_MOVABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
