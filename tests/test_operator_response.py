import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'operator_response.py';O=R/'studies'/'spacetime'/'operator-response-results.json'
def m():
 s=importlib.util.spec_from_file_location('o',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Operator(unittest.TestCase):
 def test_projective_identification(self):
  x=m();r=x.channels(3,2,2,1,2,1);self.assertAlmostEqual(3,x.infer_x_from_ratio(r[0],r[1],2,1,2,1));self.assertAlmostEqual(4/3,x.infer_ell0(4,r[0],r[1],2,1,2,1))
 def test_amplitude_cancels(self):
  x=m();a=x.channels(3,.2,2,1,2,1);b=x.channels(3,20,2,1,2,1);self.assertAlmostEqual(a[0]/a[1],b[0]/b[1],14)
 def test_collinear_counterexample(self):
  self.assertEqual('PROJECTIVE_NON_IDENTIFIABLE_COLLINEAR',m().identifiability([1,2],[2,4]))
 def test_noncollinear(self):self.assertEqual('PROJECTIVE_IDENTIFIABLE_IN_PRINCIPLE_TOY',m().identifiability([1,1],[2,4]))
 def test_output(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('OPERATOR_IDENTIFIABILITY_NOT_YET_PHYSICALLY_DERIVED',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
