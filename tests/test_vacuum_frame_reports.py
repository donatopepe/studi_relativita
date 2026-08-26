import pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'audit'/'vacuum-frame-report-it.md';EN=R/'audit'/'vacuum-frame-report-en.md';ROAD=R/'docs'/'roadmap.md'
def ids(p):return re.findall(r'^## (UMCH-VF-\d{4})',p.read_text(),re.M)
class Reports(unittest.TestCase):
 def test_aligned(self):self.assertEqual(ids(IT),ids(EN));self.assertGreaterEqual(len(ids(IT)),6)
 def test_limits(self):
  for p in (IT,EN):
   t=p.read_text()
   for s in ['FRAME_UNRESOLVED','NON_IDENTIFIABLE','NO_POSITIVE_DETECTION_CLAIM','Schwarzschild','boundary','toy']:self.assertIn(s,t)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Vacuum frame gate',t);self.assertIn('necessary but not sufficient',t)
if __name__=='__main__':unittest.main()
