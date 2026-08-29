import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];ART=json.loads((ROOT/'studies/spacetime/schwarzschild-mixed-levi-civita-holonomy-results.json').read_text())
EN=ROOT/'audit/schwarzschild-mixed-levi-civita-holonomy-report-en.md';IT=ROOT/'audit/schwarzschild-mixed-levi-civita-holonomy-report-it.md';THEORY=ROOT/'theory/spacetime/schwarzschild-mixed-levi-civita-holonomy.md'
class Reports(unittest.TestCase):
 def test_reports_exist_and_share_machine_authority(self):
  texts=[EN.read_text(),IT.read_text(),THEORY.read_text()]
  for text in texts:
   for token in (ART['classification'],ART['status'],ART['scope'],ART['gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ell0_identified=false','structural_dead_end=NOT_DECLARED','H_tr','H_rphi','PATH_ORDERED_CONNECTION_HISTORY_REQUIRED','(M,r,T)->(sM,sr,sT)'):
    self.assertIn(token,text)
 def test_reports_share_values_equations_and_limits(self):
  en=EN.read_text();it=IT.read_text()
  values=(ART['controls']['geometry']['tr_nonidentity_norm'],ART['controls']['geometry']['rphi_nonidentity_norm'],ART['controls']['nonabelian']['commutator_nonidentity_norm'],ART['controls']['cross_channel']['finite_naive_flux_residual'],ART['controls']['boundary']['raw_holonomy_difference'],ART['controls']['scale']['maximum_holonomy_residual'])
  for text in (en,it):
   for value in values:self.assertIn(str(value),text)
   for token in ('dV/ds=-Gamma_mu dz^mu/ds V','H_reverse=H^-1','H is not assumed equal to exp(integral R)','mathematical piecewise-coordinate loops','not geodesic','not causal','not detector-derived','non-Abelianity does not imply independent rank'):
    self.assertIn(token,text)
if __name__=='__main__':unittest.main()
