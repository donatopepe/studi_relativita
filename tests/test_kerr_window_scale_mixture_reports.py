import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-window-scale-mixture-report-en.md';IT=R/'audit/kerr-window-scale-mixture-report-it.md';TH=R/'theory/spacetime/kerr-window-scale-mixture.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-window-scale-mixture-results.json'
RESULT='KERR_WINDOW_LEVEL_SCALE_MIXTURE_CREATES_NONDECAYING_COVARIANCE_RISK_FLOOR_AND_CV_0P240718193_PRECLUDES_ANY_FINITE_TOY_COUNT_GATE_NOT_ELL0';GATE='PHYSICAL_KERR_WINDOW_SCALE_DISTRIBUTION_NON_GAUSSIANITY_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','166/166','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_WINDOW_SCALE_MIXTURE_FLOOR_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('rho=0.5','fraction=1.0','Delta_coefficient=304.907367059628','floor_coefficient=0.862883522363','cv=[0,0.1,0.2,0.25]','minimum_counts=[87,106,292,None]','floor_risk=[0,0.008628835224,0.034515340895,0.053930220148]','critical_cv=0.240718192810'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('nondecaying','166/166',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_LATENT_LAG_LAW_RHO_SENSITIVITY_WINDOW_MOVES_UPWARD','KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text())
if __name__=='__main__':unittest.main()
