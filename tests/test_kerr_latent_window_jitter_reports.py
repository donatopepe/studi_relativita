import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-latent-window-jitter-report-en.md';IT=R/'audit/kerr-latent-window-jitter-report-it.md';TH=R/'theory/spacetime/kerr-latent-window-jitter.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-latent-window-jitter-results.json'
RESULT='KERR_LATENT_WINDOW_JITTER_HAS_A_POSITIVE_FOURTH_MOMENT_JENSEN_CORRECTION_RELATIVE_TO_THE_GAUSSIAN_AVERAGED_KERNEL_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0';GATE='PHYSICAL_KERR_LATENT_JITTER_DISTRIBUTION_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','126/126','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_LATENT_WINDOW_JITTER_FOURTH_MOMENT_CORRECTION_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('rho=0.5','radius_fractions=[0,0.25,0.5,1.0]','latent_beta_N64=[0.026034597,0.022629281,0.019211490,0.012671070]','kernel_beta_N64=[0.026034597,0.001901728,0.000297949,0.000000013]','latent_risk_N64=[0.067498804,0.067571613,0.067644690,0.067784531]','kernel_risk_N64=[0.067498804,0.068014792,0.068049082,0.068055452]','latent_counts=[87,87,87,87]','kernel_counts=[87,88,88,88]'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('law of total covariance','Jensen','126/126',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION','KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text());self.assertIn('5. [x] Closure and publication.',TODO.read_text());self.assertIn('Full suite: `1293/1293`.',TODO.read_text())
if __name__=='__main__':unittest.main()
