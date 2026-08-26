import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];S=ROOT/'studies'/'spacetime';P=S/'vacuum_frame_gate.py';O=S/'vacuum-frame-results.json'
def m():
 s=importlib.util.spec_from_file_location('vf',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class FrameGate(unittest.TestCase):
 def test_matter_wins(self):self.assertEqual(('MATTER_FRAME_RESOLVED','UNIQUE_TIMELIKE_TMUNU_EIGENVECTOR'),m().resolve(True,False,False,False,False,False))
 def test_missing_anchor(self):self.assertEqual(('FRAME_UNRESOLVED','MISSING_COSMOLOGICAL_ANCHOR'),m().resolve(False,False,True,True,True,True))
 def test_competing_paths(self):self.assertEqual(('FRAME_UNRESOLVED','CONTINUATION_NONUNIQUE'),m().resolve(False,True,True,True,False,True))
 def test_insufficient_coverage(self):self.assertEqual(('FRAME_UNRESOLVED','TARGET_NOT_COVERED'),m().resolve(False,True,True,True,True,False))
 def test_certified_toy(self):self.assertEqual(('CMB_CONTINUATION_RESOLVED','PREREGISTERED_UNIQUE_CONTINUATION'),m().resolve(False,True,True,True,True,True))
 def test_deterministic_and_nonconfirmatory(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=ROOT,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion']);self.assertEqual('NON_IDENTIFIABLE',d['ell0_status'])
if __name__=='__main__':unittest.main()
