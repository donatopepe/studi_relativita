import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'inference_protocol_gate.py';O=R/'studies'/'spacetime'/'inference-protocol-results.json'
def m():
 s=importlib.util.spec_from_file_location('ip',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Gate(unittest.TestCase):
 def test_domain(self):
  x=m();self.assertEqual('DOMAIN_CONSISTENT',x.domain([1,2,4],.5));self.assertEqual('DOMAIN_INCONSISTENT',x.domain([1,2,4],1.1))
 def test_decision_order(self):
  x=m();base=dict(frame=True,domain_ok=True,family_fixed=True,dependence=True,likelihood=True,nuisance=True,identifiable=True,replicated=True)
  self.assertEqual('FRAME_UNRESOLVED',x.gate(**{**base,'frame':False}));self.assertEqual('DEPENDENCE_UNRESOLVED',x.gate(**{**base,'dependence':False}));self.assertEqual('NON_IDENTIFIABLE',x.gate(**{**base,'identifiable':False}));self.assertEqual('CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE',x.gate(**base))
 def test_no_detection(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
