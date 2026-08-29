import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=ROOT/'studies/spacetime/plane-wave-connection-path-cross-channel-results.json'
THEORY=ROOT/'theory/spacetime/plane-wave-connection-path-cross-channel.md'
EN=ROOT/'audit/plane-wave-connection-path-cross-channel-report-en.md';IT=ROOT/'audit/plane-wave-connection-path-cross-channel-report-it.md'
class Reports(unittest.TestCase):
 def test_bilingual_authority(self):
  d=json.loads(ART.read_text());en=EN.read_text();it=IT.read_text()
  for token in [d['classification'],d['status'],d['open_gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','Coley','ell0','0.015157779434373101','0.017400310040274355','3.95516952522712e-16']:
   self.assertIn(token,en);self.assertIn(token,it)
  self.assertIn('Not a structural dead end',en);self.assertIn('Non è un vicolo cieco strutturale',it)
 def test_equations_and_scope(self):
  text='\n'.join(p.read_text() for p in [THEORY,EN,IT])
  for token in ['W_i=(1/L) int Q_i^T K Q_i du','P_c=C_o^-1 P_inertial C_s','P_v=H(A_o)^-1 P_c H(A_s)','S_rot=R-A_o','cross-channel','caustic']:
   self.assertIn(token,text)
if __name__=='__main__':unittest.main()
