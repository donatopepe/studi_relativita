import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-arc-cross-map-results.json'
FILES=[ROOT/'theory/spacetime/schwarzschild-photon-arc-cross-map.md',ROOT/'audit/schwarzschild-photon-arc-cross-map-report-en.md',ROOT/'audit/schwarzschild-photon-arc-cross-map-report-it.md']
class PhotonArcCrossMapReportTests(unittest.TestCase):
 def test_reports_and_theory_exist(self):
  for p in FILES:self.assertTrue(p.exists(),p)
 def test_machine_stable_contract_is_bilingual(self):
  art=json.loads(ARTIFACT.read_text())
  tokens=[art['classification'],art['status'],art['scope'],art['gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ell0_identified=false','structural_dead_end=NOT_DECLARED','OPEN_ARC_ENDPOINT_TRANSPORT_NOT_HOLONOMY','CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR','CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','Darwin1959GravityField','Sachs1961','rank_joint=1','independent_channels=false']
  for p in FILES:
   text=p.read_text()
   for token in tokens:self.assertIn(token,text,f'{token} missing from {p}')
 def test_limitations_and_direct_review_exception_are_bilingual(self):
  en=FILES[1].read_text().lower();it=FILES[2].read_text().lower()
  for token in ['detector','covariance','readout','ell0','evidence','detection','endpoint','affine','caustic','holonomy','subagent','direct review','generic scattering','freely falling']:
   self.assertIn(token,en);self.assertIn(token,it)
 def test_core_values_are_identical(self):
  en=FILES[1].read_text();it=FILES[2].read_text()
  for token in ['alpha=pi','alpha=2*pi','r_ph=3M','L=3M alpha','rank_joint=1']:
   self.assertIn(token,en);self.assertIn(token,it)
if __name__=='__main__':unittest.main()
