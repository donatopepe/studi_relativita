import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'ell0_identifiability.py';O=R/'studies'/'spacetime'/'ell0-identifiability-results.json'
def m():
 s=importlib.util.spec_from_file_location('ei',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Ell0(unittest.TestCase):
 def test_power_reparameterization(self):
  x=m();ells=[1,2,7];self.assertEqual(x.power(ells,2,3,2),x.power(ells,8,1.5,2))
 def test_exponential_reparameterization(self):
  x=m();ells=[1,2,7];a,q,l=2,3,4;q2,l2=6,8;a2=a*x.math.exp(q-q2)
  for left,right in zip(x.exponential(ells,a,q,l),x.exponential(ells,a2,q2,l2)):self.assertAlmostEqual(left,right,14)
 def test_plateau_power_reparameterization(self):
  x=m();ells=[1,3];self.assertEqual(x.plateau_power(ells,.2,2,3,2),x.plateau_power(ells,.2,8,1.5,2))
 def test_gate(self):
  x=m();self.assertEqual('ELL0_STRUCTURALLY_NON_IDENTIFIABLE',x.gate('F_P',False,False));self.assertEqual('IDENTIFIABLE_IN_PRINCIPLE_WITH_EXTERNAL_CALIBRATION',x.gate('F_P',True,True));self.assertEqual('ELL0_ABSENT_FROM_NULL_MODEL',x.gate('F_0',True,True))
 def test_output(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
