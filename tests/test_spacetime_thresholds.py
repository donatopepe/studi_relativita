import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];S=ROOT/'studies'/'spacetime';T=S/'thresholds.py';I=S/'threshold-cases.json';O=S/'threshold-results.json'
def mod():
 s=importlib.util.spec_from_file_location('th',T);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Threshold(unittest.TestCase):
 def test_families(self):
  m=mod();self.assertEqual(0,m.threshold('F_0',2,{}));self.assertAlmostEqual(.25,m.threshold('F_P',2,{'A':1,'p':2}));self.assertAlmostEqual(1,m.threshold('F_E',1,{'A':1,'q':3}));self.assertAlmostEqual(.6,m.threshold('F_PE',2,{'A_inf':.1,'A_1':1,'p':1}))
 def test_domain(self):
  with self.assertRaises(ValueError):mod().threshold('F_P',.9,{'A':1,'p':1})
 def test_identifiability(self):
  m=mod();self.assertEqual('FRAME_UNRESOLVED',m.classify(1,.1,'FRAME_UNRESOLVED',True));self.assertEqual('NON_IDENTIFIABLE',m.classify(1,.1,'FRAME_RESOLVED',False));self.assertEqual('CONTRADICTED',m.classify(0,.1,'FRAME_RESOLVED',True));self.assertEqual('SUPPORTED_WITHIN_DATA_RANGE',m.classify(1,.1,'FRAME_RESOLVED',True));self.assertEqual('UPPER_BOUND_ONLY',m.classify(.05,.1,'FRAME_RESOLVED',True))
 def test_deterministic(self):
  r=subprocess.run(['python3',str(T),'--check'],cwd=ROOT,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertIn('F_0',d['families']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
