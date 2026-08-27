import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'audit'/'unified-assumptions.csv'
REQ={'UMCH-A-0001','UMCH-A-0002','UMCH-A-0003','UMCH-A-0004','UMCH-A-0005','UMCH-A-0006','UMCH-A-0007','UMCH-A-0008','UMCH-A-0009','UMCH-A-0010','UMCH-A-0011','UMCH-A-0012'}
class Assumptions(unittest.TestCase):
 def rows(self):
  with P.open() as f:return list(csv.DictReader(f))
 def test_complete(self):self.assertEqual(REQ,{r['assumption_id'] for r in self.rows()})
 def test_fields(self):
  for r in self.rows():
   for k in ['scope','status','dependency','failure_effect','resolution_gate']:self.assertTrue(r[k].strip(),(r['assumption_id'],k))
 def test_no_hidden_resolution(self):
  rows={r['assumption_id']:r for r in self.rows()};self.assertEqual('OPEN',rows['UMCH-A-0007']['status']);self.assertIn('double counting',rows['UMCH-A-0007']['scope']);self.assertEqual('EXTERNAL_EVIDENCE_REQUIRED',rows['UMCH-A-0011']['status']);self.assertEqual('HUMAN_REVIEW_REQUIRED',rows['UMCH-A-0012']['status'])
if __name__=='__main__':unittest.main()
