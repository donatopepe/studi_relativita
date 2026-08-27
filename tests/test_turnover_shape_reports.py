import pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'audit'/'turnover-shape-report-it.md';EN=R/'audit'/'turnover-shape-report-en.md';T=R/'theory'/'spacetime'/'turnover-shape-gate.md';ROAD=R/'docs'/'roadmap.md'
def ids(p):return re.findall(r'^## (UMCH-SG-\d{4})',p.read_text(),re.M)
class Reports(unittest.TestCase):
 def test_aligned(self):self.assertEqual(ids(IT),ids(EN));self.assertGreaterEqual(len(ids(IT)),7)
 def test_limits(self):
  for f in (IT,EN,T):
   t=f.read_text()
   lower=t.lower()
   for x in ['p=2','q','BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM','NO_POSITIVE_DETECTION_CLAIM']:self.assertIn(x,t)
   for x in ['holonomy','clock','null','congruence']:self.assertIn(x,lower)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Turnover shape derivation gate',t);self.assertIn('nonlocal mechanism',t)
if __name__=='__main__':unittest.main()
