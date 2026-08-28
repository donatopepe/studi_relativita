import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'operator_exact_cases.py';O=R/'studies'/'spacetime'/'operator-exact-results.json'
def m():
 s=importlib.util.spec_from_file_location('oe',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Exact(unittest.TestCase):
 def test_minkowski(self):
  r=m().analyze([0,0,0]);self.assertEqual(0,r['rank']);self.assertIsNone(r['projective_spectrum'])
 def test_flrw_isotropic(self):
  r=m().analyze([-2,-2,-2]);self.assertEqual([-1,-1,-1],r['projective_spectrum']);self.assertEqual(1,r['distinct_eigenvalues'])
 def test_schwarzschild_ratio(self):
  r=m().analyze([-4,2,2]);self.assertEqual([-1,.5,.5],r['projective_spectrum']);self.assertEqual(2,r['distinct_eigenvalues'])
 def test_scale_collinearity(self):
  x=m();self.assertEqual(x.analyze([-2,1,1])['projective_spectrum'],x.analyze([-8,4,4])['projective_spectrum']);self.assertEqual('PROJECTIVE_SCALE_NON_IDENTIFIABLE',x.compare_scales([-2,1,1],[-8,4,4]))
 def test_output(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('PROJECTIVE_SCALE_NON_IDENTIFIABLE_IN_CURRENT_EXACT_CONTROLS',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
