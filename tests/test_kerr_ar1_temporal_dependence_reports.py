import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-ar1-temporal-dependence-report-en.md';IT=R/'audit/kerr-ar1-temporal-dependence-report-it.md';TH=R/'theory/spacetime/kerr-ar1-temporal-dependence.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-ar1-temporal-dependence-results.json'
RESULT='KERR_GAUSSIAN_AR1_TEMPORAL_DEPENDENCE_REDUCES_EFFECTIVE_COVARIANCE_INFORMATION_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0';GATE='PHYSICAL_KERR_TEMPORAL_CORRELATION_MODEL_STATIONARITY_GAUSSIANITY_CROSS_STREAM_DEPENDENCE_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','94/94','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_AR1_COVARIANCE_PENALTY_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('rho=0.5','rms=[9.7334408,4.9038744,2.4524884]','minimum_count=88','risk_88=0.049511371','risk_87=0.050080099','risk_64=0.068055453','rho_0.99_effective_df_64=2.9130205'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('AR(1)','temporal','centered quadratic',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM','KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING','F_0'):self.assertIn(x,t)
  self.assertIn('4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**',TODO.read_text())
if __name__=='__main__':unittest.main()
