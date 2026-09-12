import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-paired-stream-common-noise-report-en.md';IT=R/'audit/kerr-paired-stream-common-noise-report-it.md';TH=R/'theory/spacetime/kerr-paired-stream-common-noise.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-paired-stream-common-noise-results.json'
RESULT='KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0';GATE='PHYSICAL_KERR_CROSS_STREAM_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','102/102','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_PAIRED_COMMON_NOISE_COVARIANCE_GAIN_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('rho=0.5','independent_coefficient=923.6933349','paired_coefficient=916.1381349','rms_ratio=0.995901934','rms=[9.6935525,4.8837780,2.4424379]','minimum_count=87','risk_87=0.049670477','risk_86=0.050247654','risk_64=0.067498804','zero_shared_minimum_count=88'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('cross-Wishart','0.4098%','102/102',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_GAUSSIAN_AR1_TEMPORAL_DEPENDENCE_REDUCES_EFFECTIVE_COVARIANCE_INFORMATION','KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text());self.assertIn('5. [x] Closure and publication.',TODO.read_text());self.assertIn('Full suite: `1254/1254`.',TODO.read_text())
if __name__=='__main__':unittest.main()
