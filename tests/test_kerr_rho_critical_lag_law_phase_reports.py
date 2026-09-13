import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-rho-critical-lag-law-phase-report-en.md';IT=R/'audit/kerr-rho-critical-lag-law-phase-report-it.md';TH=R/'theory/spacetime/kerr-rho-critical-lag-law-phase.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-rho-critical-lag-law-phase-results.json'
RESULT='KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW_RHO_0P499243439_TO_0P501157236_NOT_ELL0';GATE='PHYSICAL_KERR_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','150/150','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_RHO_CRITICAL_LATENT_LAG_LAW_PHASE_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('N=87','fraction=1.0','risk_ceiling=0.05','rho_low=0.499243438917','rho_high=0.501157235677','rho_window_width=0.001913796761','path_rho=[0.4995,0.5,0.5005,0.501]','path_kappa=[12.485595532,3.890241565,2.001949812,1.172518080]'):self.assertIn(x,t)
 def test_history_and_todo(self):
  for x in ('Three regimes','150/150',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_FULL_SUPPORT_LATENT_LAG_LAW_HAS_TOY_CRITICAL_DENSITY_RATIO','KERR_LATENT_LAG_LAW_DENSITY_RATIO_BOUNDS_GIVE_EXACT_RISK_ENVELOPES','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text())
if __name__=='__main__':unittest.main()
