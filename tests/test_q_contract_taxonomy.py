import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];T=R/'audit'/'q-theory-contract.csv';D=R/'theory'/'spacetime'/'q-theory-contract.md';B=R/'references'/'library.bib';L=R/'references'/'verification-log.md'
CLASSES={'mass_gap','spectral_gap','compactification','screening','higher_derivative_poles','entire_form_factor','covariant_form_factor','causal_set_nonlocality','asymptotic_safety','stochastic_correlation','cosmological_horizon','boundary_topology','critical_rg','fractional_operator','quasinormal_resonance'}
class Contract(unittest.TestCase):
 def rows(self):
  with T.open() as f:return list(csv.DictReader(f))
 def test_taxonomy(self):self.assertEqual(CLASSES,{r['scenario'] for r in self.rows()})
 def test_gates(self):
  for r in self.rows():
   for k in ['independent_input','profile_issue','degeneracy','decision','required_contract']:self.assertTrue(r[k].strip(),(r['scenario'],k))
  self.assertFalse(any(r['decision']=='Q_DERIVED' for r in self.rows()))
 def test_contract(self):
  t=D.read_text()
  for x in ['action/operator','degrees of freedom','state/boundary','channel map','no free-scale degeneracy','predictions beyond turnover','NO_MODEL_INDEPENDENT_Q_DERIVATION_FOUND']:self.assertIn(x,t)
 def test_sources(self):
  b=B.read_text();l=L.read_text()
  for k,d in [('HastingsKoma2006','10.1007/s00220-006-0030-4'),('Brax2013','10.1088/0264-9381/30/21/214005'),('BelenchiaEtAl2016','10.1103/PhysRevD.93.044017'),('BurrageSakstein2018','10.1007/s41114-018-0011-x')]:self.assertIn('@article{'+k+',',b);self.assertIn('doi = {'+d+'}',b);self.assertIn('## '+k,l)
if __name__=='__main__':unittest.main()
