import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-estimated-mean-covariance-report-en.md';IT=R/'audit/kerr-estimated-mean-covariance-report-it.md';TH=R/'theory/spacetime/kerr-estimated-mean-covariance.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-estimated-mean-covariance-results.json'
RESULT='KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0';GATE='PHYSICAL_KERR_UNKNOWN_MEAN_NON_GAUSSIANITY_SAMPLE_DEPENDENCE_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','86/86','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_ESTIMATED_MEAN_COVARIANCE_PENALTY_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('degrees_of_freedom=[15,63,255]','penalty=[1.0666667,1.015873,1.0039216]','rms=[7.8472642,3.8290729,1.9032411]','minimum_count=54','risk_54=0.049321491','risk_53=0.050269981','risk_16=0.17426927'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('estimated mean','degree of freedom','centered Wishart',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING','KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text());self.assertIn('5. [x] Closure and publication.',TODO.read_text());self.assertIn('Full suite: `1228/1228`.',TODO.read_text());self.assertIn('GitHub Actions run `34652593522` tests/LaTeX passed.',TODO.read_text())
if __name__=='__main__':unittest.main()
