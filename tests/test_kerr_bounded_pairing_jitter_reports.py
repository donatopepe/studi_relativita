import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-bounded-pairing-jitter-report-en.md';IT=R/'audit/kerr-bounded-pairing-jitter-report-it.md';TH=R/'theory/spacetime/kerr-bounded-pairing-jitter.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-bounded-pairing-jitter-results.json'
RESULT='KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_RADIUS_16_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0';GATE='PHYSICAL_KERR_PAIRING_JITTER_DISTRIBUTION_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','118/118','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_BOUNDED_PAIRING_JITTER_EROSION_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('rho=0.5','jitter_radii=[0,1,2,4,8,16]','beta_over_alpha_N64=[1.0,0.789485810,0.623302468,0.404555012,0.204269692,0.073046173]','risk_N64=[0.067498804,0.067615986,0.067708492,0.067830258,0.067941746,0.068014792]','minimum_counts=[87,87,87,87,87,88]','radius_16_risk_88=0.049473762','radius_16_risk_87=0.050042318'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('mixture-kernel','not claim equivalence','118/118',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION','KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM','F_0'):self.assertIn(x,t)
  self.assertIn('Kerr bounded pairing-jitter erosion MVP: tasks 1–5 completed',TODO.read_text());self.assertIn('scientific `8/8`, scenarios `118/118`, suite `1280/1280`',TODO.read_text());self.assertIn('Full suite: `1280/1280`.',TODO.read_text())
if __name__=='__main__':unittest.main()
