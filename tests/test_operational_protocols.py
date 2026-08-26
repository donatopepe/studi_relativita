import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];S=ROOT/'studies'/'spacetime';T=S/'operational_protocols.py';O=S/'operational-protocol-results.json'
def mod():
 s=importlib.util.spec_from_file_location('op',T);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Op(unittest.TestCase):
 def test_minkowski_all_zero(self):
  r=mod().responses(curvature_scale=0,ell=2,clock_fraction=0,null_shear=0,congruence_residual=0);self.assertEqual([0.]*6,r['raw_vector'])
 def test_protocol_scaling(self):
  r=mod().responses(curvature_scale=.25,ell=2,clock_fraction=.01,null_shear=.02,congruence_residual=.03);self.assertEqual(1,r['R_hol']);self.assertEqual(.01,r['R_clock']);self.assertEqual(.02,r['R_null']);self.assertEqual(.03,r['R_cong'])
 def test_frame(self):
  m=mod();self.assertEqual('MATTER_FRAME_RESOLVED',m.frame(True,False));self.assertEqual('CMB_CONTINUATION_RESOLVED',m.frame(False,True));self.assertEqual('FRAME_UNRESOLVED',m.frame(False,False))
 def test_identifiability(self):
  m=mod();self.assertEqual('NON_IDENTIFIABLE',m.identifiability('FRAME_UNRESOLVED',True,True,True,True));self.assertEqual('NON_IDENTIFIABLE',m.identifiability('MATTER_FRAME_RESOLVED',False,True,True,True));self.assertEqual('IDENTIFIABLE_IN_PRINCIPLE',m.identifiability('MATTER_FRAME_RESOLVED',True,True,True,True))
 def test_deterministic(self):
  r=subprocess.run(['python3',str(T),'--check'],cwd=ROOT,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
