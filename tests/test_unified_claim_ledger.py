import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'audit'/'unified-claims.csv';IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex'
class Ledger(unittest.TestCase):
 def rows(self):
  with P.open() as f:return list(csv.DictReader(f))
 def test_all_paper_claims_atomic(self):
  rows=self.rows();ids={r['claim_id'] for r in rows};expected={f'UMCH-U-{i:04d}' for i in range(1,19)};self.assertEqual(expected,ids)
  for r in rows:
   for k in ['classification','status','evidence','limitation','falsifier']:self.assertTrue(r[k].strip(),(r['claim_id'],k))
 def test_bilingual_claim_coverage(self):
  for p in (IT,EN):
   t=p.read_text()
   for r in self.rows():self.assertIn(r['claim_id'],t)
 def test_required_statuses(self):
  statuses={r['status'] for r in self.rows()}
  for x in ['UNPROVEN','SUPERSEDED_AS_CORE','CONTRADICTED_UNDER_ASSUMPTIONS','FRAME_UNRESOLVED','ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES','MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY','BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM','NO_POSITIVE_DETECTION_CLAIM']:self.assertIn(x,statuses)
if __name__=='__main__':unittest.main()
