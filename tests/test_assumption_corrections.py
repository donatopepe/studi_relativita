import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];A=R/'audit'/'unified-assumptions.csv';D=R/'theory'/'spacetime'/'admissible-regions.md';V=R/'theory'/'spacetime'/'response-vector.md';H=R/'theory'/'spacetime'/'hypothesis.md';IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex'
class Correct(unittest.TestCase):
 def rows(self):
  with A.open() as f:return {r['assumption_id']:r for r in csv.DictReader(f)}
 def test_domain_non_circular(self):
  for p in (D,H,IT,EN):
   t=p.read_text().replace('D_{\\rm survey}','D_survey').replace('\\ell_{\\min}','ell_min');self.assertIn('D_survey',t);self.assertIn('DOMAIN_INCONSISTENT',t);self.assertIn('ell_min',t)
 def test_dependence_contract(self):
  for p in (V,IT,EN):
   t=p.read_text();self.assertIn('DEPENDENCE_UNRESOLVED',t);self.assertIn('joint covariance',t);self.assertIn('not',t.lower())
 def test_assumption_statuses(self):
  r=self.rows();self.assertEqual('CORRECTED_PROTOCOL_RULE',r['UMCH-A-0002']['status']);self.assertEqual('CORRECTED_PROTOCOL_RULE',r['UMCH-A-0006']['status']);self.assertEqual('CORRECTED_NO_INDEPENDENCE_ASSUMPTION',r['UMCH-A-0007']['status']);self.assertEqual('CORRECTED_PROTOCOL_RULE',r['UMCH-A-0009']['status']);self.assertEqual('EXTERNAL_EVIDENCE_REQUIRED',r['UMCH-A-0011']['status']);self.assertEqual('HUMAN_REVIEW_REQUIRED',r['UMCH-A-0012']['status'])
if __name__=='__main__':unittest.main()
