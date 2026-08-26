import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'ell0_turnover.py';O=R/'studies'/'spacetime'/'ell0-turnover-results.json'
def m():
 s=importlib.util.spec_from_file_location('et',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Turnover(unittest.TestCase):
 def test_two_scale_exact_inversion(self):
  x=m();A,e0,p,q=0.3,2.,3.,1.;e1,e2=2.5,5.;y1=x.response(e1,A,e0,p,q);y2=x.response(e2,A,e0,p,q);self.assertAlmostEqual(e0,x.infer(e1,y1,e2,y2,p,q),12)
 def test_amplitude_cancels(self):
  x=m()
  vals=[]
  for A in (.1,10.):vals.append(x.infer(2.5,x.response(2.5,A,2,3,1),5,x.response(5,A,2,3,1),3,1))
  for value in vals:self.assertAlmostEqual(value,2.,14)
 def test_peak_landmark(self):self.assertEqual(6.,m().peak(2,3,1))
 def test_invalid(self):
  x=m()
  for args in [(1,1,2,8,3,1),(1,0,2,1,3,1)]:
   with self.assertRaises(ValueError):x.infer(*args)
  self.assertEqual('NON_IDENTIFIABLE_IF_SHAPE_FREE',x.gate(False,True,True));self.assertEqual('PRACTICALLY_UNRESOLVED_NO_TURNOVER_COVERAGE',x.gate(True,False,True));self.assertEqual('FRAME_UNRESOLVED',x.gate(True,True,False));self.assertEqual('IDENTIFIABLE_IN_PRINCIPLE',x.gate(True,True,True))
 def test_output(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
