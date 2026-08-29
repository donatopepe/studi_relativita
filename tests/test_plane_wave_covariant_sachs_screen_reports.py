import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=ROOT/'studies/spacetime/plane-wave-covariant-sachs-screen-results.json'
FILES=[ROOT/'theory/spacetime/plane-wave-covariant-sachs-screen.md',ROOT/'doc/specs/2026-08-29-plane-wave-covariant-sachs-screen.md',ROOT/'doc/plans/2026-08-29-plane-wave-covariant-sachs-screen.md',ROOT/'audit/plane-wave-covariant-sachs-screen-report-en.md',ROOT/'audit/plane-wave-covariant-sachs-screen-report-it.md']
class Reports(unittest.TestCase):
 def test_files(self):
  for p in [ART,*FILES]:self.assertTrue(p.exists(),p)
 def test_bilingual_authority(self):
  d=json.loads(ART.read_text()); en=FILES[-2].read_text();it=FILES[-1].read_text()
  for token in [d['classification'],d['status'],d['open_gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','Coley','ell0','S_rot','R-A']:
   self.assertIn(token,en);self.assertIn(token,it)
  self.assertIn('Not a structural dead end',en);self.assertIn('Non è un vicolo cieco strutturale',it)
 def test_equations_values_and_prior_ledger(self):
  text='\n'.join(p.read_text() for p in FILES)
  for token in ["R=PX^-1","twist(S_rot)=twist(R)-twist(A)",'2.9466757892120056e-10','0.4101219330881975','0.2899999999999999','twist-area','caustic']:
   self.assertIn(token,text)
if __name__=='__main__':unittest.main()
