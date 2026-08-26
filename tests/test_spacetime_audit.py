import csv,pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];CSV=ROOT/'audit'/'spacetime-claims.csv';IT=ROOT/'audit'/'spacetime-foundation-report-it.md';EN=ROOT/'audit'/'spacetime-foundation-report-en.md'
class Audit(unittest.TestCase):
 def test_claim_schema(self):
  with CSV.open(newline='') as f:r=list(csv.DictReader(f));self.assertEqual(['claim_id','statement','level','status','evidence','limitation'],list(r[0].keys()));self.assertGreaterEqual(len(r),8)
  self.assertTrue(all(x['status'] in {'SUPPORTED_WITH_CONDITIONS','UNPROVEN','NON_IDENTIFIABLE','FRAME_UNRESOLVED'} for x in r))
 def test_reports_align(self):
  h=lambda p:re.findall(r'^## (UMCH-ST-\d{4})',p.read_text(),re.M);self.assertEqual(h(IT),h(EN));self.assertGreaterEqual(len(h(IT)),7)
  for p in (IT,EN):
   t=p.read_text();
   for x in ['Minkowski','FLRW','Schwarzschild','VSI','NO_POSITIVE_DETECTION_CLAIM','UNPROVEN','FRAME_UNRESOLVED']:self.assertIn(x,t)
if __name__=='__main__':unittest.main()
