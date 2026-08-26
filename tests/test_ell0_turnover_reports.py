import pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'audit'/'ell0-turnover-report-it.md';EN=R/'audit'/'ell0-turnover-report-en.md';T=R/'theory'/'spacetime'/'ell0-turnover-candidate.md';ROAD=R/'docs'/'roadmap.md'
def ids(p):return re.findall(r'^## (UMCH-TI-\d{4})',p.read_text(),re.M)
class Reports(unittest.TestCase):
 def test_aligned(self):self.assertEqual(ids(IT),ids(EN));self.assertGreaterEqual(len(ids(IT)),7)
 def test_limits(self):
  for p in (IT,EN,T):
   t=p.read_text()
   for x in ['MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY','NO_POSITIVE_DETECTION_CLAIM','F_T','F_0','p','q','ell0']:self.assertIn(x,t)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Turnover identifiability candidate',t);self.assertIn('not adopted',t)
if __name__=='__main__':unittest.main()
