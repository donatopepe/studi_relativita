import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/'studies/spacetime/schwarzschild-photon-sphere-jacobi-results.json').read_text())
FILES=[ROOT/'theory/spacetime/schwarzschild-photon-sphere-jacobi.md',ROOT/'audit/schwarzschild-photon-sphere-jacobi-report-en.md',ROOT/'audit/schwarzschild-photon-sphere-jacobi-report-it.md']
class PhotonSphereJacobiReportTests(unittest.TestCase):
 def test_reports_and_theory_exist(self):
  for p in FILES:self.assertTrue(p.exists(),p)
 def test_machine_stable_contract_is_bilingual(self):
  tokens=[ART['classification'],ART['status'],ART['scope'],ART['gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ell0_identified=false','structural_dead_end=NOT_DECLARED','STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR','CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR','DISCRETE_PROTOCOL_LABEL','NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN','CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','Darwin1959GravityField','Sachs1961']
  for p in FILES:
   text=p.read_text()
   for token in tokens:self.assertIn(token,text,f'{token} missing from {p}')
 def test_limitations_are_present_in_both_languages(self):
  en=FILES[1].read_text().lower();it=FILES[2].read_text().lower()
  for token in ['detector','covariance','readout','ell0','evidence','detection','endpoint','affine','caustic','holonomy']:
   self.assertIn(token,en);self.assertIn(token,it)
if __name__=='__main__':unittest.main()
