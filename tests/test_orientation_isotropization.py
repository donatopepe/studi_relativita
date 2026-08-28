import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/orientation_isotropization.py';O=R/'studies/spacetime/orientation-isotropization-results.json'
def mod():
 s=importlib.util.spec_from_file_location('o',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Orientation(unittest.TestCase):
 def test_half_weight_isotropic(self):self.assertEqual([2,2],mod().eigenvalues(mod().average(.5)))
 def test_shape_changes_with_weights(self):self.assertNotEqual(mod().projective_spectrum(mod().average(1)),mod().projective_spectrum(mod().average(.5)))
 def test_target_scale_movable(self):
  m=mod()
  for target in [1,4,9]:self.assertAlmostEqual(.5,m.weight_profile(target,target))
 def test_mixture_not_conjugate(self):
  m=mod();self.assertNotEqual(m.eigenvalues(m.A),m.eigenvalues(m.average(.5)))
 def test_ell0_absent(self):self.assertEqual('ORIENTATION_PROTOCOL_SCALE_NOT_ELL0',mod().ell0_gate(['ell','weight','A']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('ORIENTATION_WEIGHT_LANDMARK_PROTOCOL_MOVABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
