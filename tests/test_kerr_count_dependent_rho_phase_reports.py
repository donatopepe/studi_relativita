import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-count-dependent-rho-phase-report-en.md';IT=R/'audit/kerr-count-dependent-rho-phase-report-it.md';TH=R/'theory/spacetime/kerr-count-dependent-rho-phase.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-count-dependent-rho-phase-results.json'
RESULT='KERR_LATENT_LAG_LAW_RHO_SENSITIVITY_WINDOW_MOVES_UPWARD_AND_NARROWS_WITH_TOY_SAMPLE_COUNT_WHILE_N53_IS_UNSAFE_ALREADY_AT_IID_NOT_ELL0';GATE='PHYSICAL_KERR_SAMPLE_COUNT_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','158/158','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_COUNT_DEPENDENT_RHO_PHASE_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('counts=[53,54,64,87,128,256]','first_iid_safe_count=54','finite_counts=[54,64,87,128,256]','rho_low=[0.084265333564,0.309816339325,0.499243438917,0.649991897137,0.814628675425]','rho_high=[0.095873875058,0.313101631950,0.501157235677,0.651271982688,0.815322224235]','width=[0.011608541494,0.003285292625,0.001913796761,0.001280085551,0.000693548809]','N53_iid_uniform_risk=0.0500676203','N54_iid_uniform_risk=0.0491228897'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('rho_low(N)','158/158',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW','KERR_FULL_SUPPORT_LATENT_LAG_LAW_HAS_TOY_CRITICAL_DENSITY_RATIO','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text());self.assertIn('5. [x] Closure and publication.',TODO.read_text());self.assertIn('Full suite: `1345/1345`.',TODO.read_text())
if __name__=='__main__':unittest.main()
