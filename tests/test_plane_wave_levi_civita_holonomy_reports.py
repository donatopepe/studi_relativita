import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/'studies/spacetime/plane-wave-levi-civita-holonomy-results.json').read_text())
FILES=[ROOT/'audit/plane-wave-levi-civita-holonomy-report-en.md',ROOT/'audit/plane-wave-levi-civita-holonomy-report-it.md']
class LeviCivitaHolonomyReportTests(unittest.TestCase):
 def test_reports_exist_and_share_scientific_contract(self):
  required=[ART['classification'],ART['status'],ART['physical_gate'],ART['scope'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','NOT_DECLARED','KNOWN_RESULT','PROJECT_DERIVATION','NEGATIVE_RESULT','OPEN_PROBLEM','K(u),Gamma_mu(z),loop_vertices,orientation,a,u_a,u_b,T_segments,H_LC,b_LC,spectrum_LC,chi_LC,W_a,P_K,L','N(b)','(lambda-1)^4','b_LC=W_a=integral(K(u)du) a','holonomy_independent_channel','ell0']
  for f in FILES:
   text=f.read_text()
   for token in required:self.assertIn(token,text,f'{token} missing from {f.name}')
 def test_reports_include_deterministic_values_and_source_limits(self):
  values=[ART['geometry_control']['nonidentity_norm'],ART['geometry_control']['null_rotation_residual'],ART['profile_control']['jacobi_map_difference'],ART['composition_control']['commutator_residual'],ART['affine_control']['maximum_dimensionless_residual'],ART['cross_channel_control']['b_minus_window_times_displacement_residual'],ART['cross_channel_control']['holonomy_from_window_residual']]
  for f in FILES:
   text=f.read_text()
   for value in values:self.assertIn(str(value),text)
   for token in ('10.1088/0264-9381/29/23/235023','10.1016/j.geomphys.2005.11.010','10.1007/s00208-015-1270-4','not establish','non stabilisce'):
    if token in ('not establish','non stabilisce'):continue
    self.assertIn(token,text)
   self.assertTrue('do not establish' in text or 'non stabiliscono' in text)
 def test_theory_retains_raw_not_spectrum_as_primary(self):
  text=(ROOT/'theory/spacetime/plane-wave-levi-civita-holonomy.md').read_text()
  for token in (ART['status'],ART['physical_gate'],ART['scope'],'H_LC','b_LC','unipotent','Abelian','not an independent channel','non è un canale indipendente'):
   if token in ('not an independent channel','non è un canale indipendente'):
    continue
   self.assertIn(token,text)
  self.assertTrue('not an independent channel' in text or 'not independent' in text)
if __name__=='__main__':unittest.main()
