import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
ARTIFACT=ROOT/'studies/spacetime/schwarzschild-photon-arc-freefall-endpoints-results.json'
FILES=[ROOT/'theory/spacetime/schwarzschild-photon-arc-freefall-endpoints.md',ROOT/'audit/schwarzschild-photon-arc-freefall-endpoints-report-en.md',ROOT/'audit/schwarzschild-photon-arc-freefall-endpoints-report-it.md']
class PhotonArcFreefallEndpointReportTests(unittest.TestCase):
 def test_reports_and_theory_exist(self):
  for p in FILES:self.assertTrue(p.exists(),p)
 def test_machine_stable_contract_is_bilingual(self):
  art=json.loads(ARTIFACT.read_text())
  tokens=[art['classification'],art['status'],art['scope'],art['gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ell0_identified=false','structural_dead_end=NOT_DECLARED','ENDPOINT_FRAME_COMPARISON_NOT_HOLONOMY_OR_INTERIOR_CURVATURE_RESPONSE','ENDPOINT_PREPARATION_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE','CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR','CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','rank_fixed_preparation=1','independent_channels=false']
  for p in FILES:
   text=p.read_text()
   for token in tokens:self.assertIn(token,text,f'{token} missing from {p}')
 def test_limitations_and_direct_review_exception_are_bilingual(self):
  en=FILES[1].read_text().lower();it=FILES[2].read_text().lower()
  for token in ['detector','covariance','readout','ell0','evidence','detection','release','synchronization','endpoint','frequency','screen','caustic','holonomy','subagent','direct review','generic scattering']:
   self.assertIn(token,en);self.assertIn(token,it)
 def test_core_values_are_identical(self):
  en=FILES[1].read_text();it=FILES[2].read_text()
  for token in ['r=3M','E=1','alpha=pi','alpha=2*pi','rank_fixed_preparation=1','scale_null_direction=[0,1]']:
   self.assertIn(token,en);self.assertIn(token,it)
if __name__=='__main__':unittest.main()
