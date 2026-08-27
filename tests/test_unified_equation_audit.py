import csv,pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'audit'/'unified-equations.csv';IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex'
def labels(p):return set(re.findall(r'\\label\{(eq:u-[^}]+)\}',p.read_text()))
class Equations(unittest.TestCase):
 def rows(self):
  with P.open() as f:return list(csv.DictReader(f))
 def test_complete(self):
  paper=labels(IT);self.assertEqual(paper,labels(EN));self.assertEqual(paper,{r['equation_label'] for r in self.rows()});self.assertEqual(7,len(paper))
 def test_fields(self):
  for r in self.rows():
   for k in ['classification','symbols_dimensions','domain_assumptions','status','limitation','failure_gate']:self.assertTrue(r[k].strip(),(r['equation_label'],k))
 def test_sensitive_gates(self):
  rows={r['equation_label']:r for r in self.rows()};self.assertEqual('EXACT_REPARAMETERIZATION_IDENTITY',rows['eq:u-degeneracy']['status']);self.assertEqual('MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY',rows['eq:u-turnover']['status']);self.assertIn('denominator',rows['eq:u-inversion']['failure_gate']);self.assertIn('ell>=ell0',rows['eq:u-inversion']['domain_assumptions'])
if __name__=='__main__':unittest.main()
