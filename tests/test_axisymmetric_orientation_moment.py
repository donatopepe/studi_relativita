import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/axisymmetric_orientation_moment.py';O=R/'studies/spacetime/axisymmetric-orientation-moment-results.json'
def mod():
 s=importlib.util.spec_from_file_location('a',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Moment(unittest.TestCase):
 def test_formula_limits(self):
  m=mod();self.assertEqual([[1,0,0],[0,1,0],[0,0,-2]],m.average(1));self.assertEqual([[-.5,0,0],[0,-.5,0],[0,0,1]],m.average(0))
 def test_isotropic_moment_zero(self):self.assertEqual([[0,0,0],[0,0,0],[0,0,0]],mod().average(1/3))
 def test_signed_projective_sectors(self):
  m=mod();self.assertEqual([-.5,.25,.25],m.projective_spectrum(m.average(.8)));self.assertEqual([-.25,-.25,.5],m.projective_spectrum(m.average(.1)))
 def test_measure_collision(self):
  m=mod();self.assertEqual(m.moment_of_discrete([(1,.5),(0,.5)]),m.moment_of_discrete([(.5,1)]));self.assertEqual(m.average_from_measure([(1,.5),(0,.5)]),m.average_from_measure([(.5,1)]))
 def test_invalid_moment(self):
  m=mod()
  for x in [-.1,1.1]:self.assertRaises(ValueError,m.average,x)
 def test_ell0_absent(self):self.assertEqual('ORIENTATION_SECOND_MOMENT_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['mu2']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('AXISYMMETRIC_ORIENTATION_AVERAGE_SECOND_MOMENT_ONLY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
