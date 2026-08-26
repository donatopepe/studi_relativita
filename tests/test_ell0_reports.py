import pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'audit'/'ell0-identifiability-report-it.md';EN=R/'audit'/'ell0-identifiability-report-en.md';ROAD=R/'docs'/'roadmap.md'
def ids(p):return re.findall(r'^## (UMCH-ID-\d{4})',p.read_text(),re.M)
class Reports(unittest.TestCase):
 def test_aligned(self):self.assertEqual(ids(IT),ids(EN));self.assertGreaterEqual(len(ids(IT)),6)
 def test_scope(self):
  for p in (IT,EN):
   t=p.read_text()
   for x in ['F_P','F_E','F_PE','F_0','ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES','NO_POSITIVE_DETECTION_CLAIM','external']:self.assertIn(x,t)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Structural ell0 identifiability',t);self.assertIn('exact reparameterization',t)
if __name__=='__main__':unittest.main()
