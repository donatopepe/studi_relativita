import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Authority(unittest.TestCase):
 def test_readmes(self):
  for p in (R/'README.md',R/'README.en.md'):
   t=p.read_text()
   for x in ['papers/umch','ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES','MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY','BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM','NO_POSITIVE_DETECTION_CLAIM']:self.assertIn(x,t)
 def test_roadmap_authority(self):
  t=(R/'docs'/'roadmap.md').read_text();self.assertIn('Unified authoritative paper',t);self.assertIn('papers/umch',t);self.assertNotIn('ell0 remains `NON_IDENTIFIABLE`',t)
if __name__=='__main__':unittest.main()
