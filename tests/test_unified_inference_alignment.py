import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex';ROAD=R/'docs'/'roadmap.md';CLAIMS=R/'audit'/'unified-claims.csv'
STAT=['FRAME_UNRESOLVED','DOMAIN_INCONSISTENT','EXPLORATORY_FAMILY_SELECTION','DEPENDENCE_UNRESOLVED','LIKELIHOOD_UNRESOLVED','NUISANCE_UNBOUNDED','NON_IDENTIFIABLE','REPLICATION_MISSING','CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE']
class Align(unittest.TestCase):
 def test_papers(self):
  for p in (IT,EN):
   t=p.read_text()
   for x in STAT:self.assertIn(x,t)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Inference protocol gate',t);self.assertIn('CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE',t)
 def test_claim_gate(self):
  with CLAIMS.open() as f:rows={r['claim_id']:r for r in csv.DictReader(f)}
  s=rows['UMCH-U-0014'];self.assertIn('ordered inference gate',s['evidence']);self.assertIn('eligibility is not evidence',s['limitation'])
if __name__=='__main__':unittest.main()
