import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-composite-calibration-report-en.md';IT=R/'audit/kerr-composite-calibration-report-it.md';TH=R/'theory/spacetime/kerr-composite-calibration.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-composite-calibration-results.json'
RESULT='KERR_COMPOSITE_BRANCH_SETS_ARE_DISJOINT_UNDER_TOY_BOUNDED_PROFILED_COMMON_CALIBRATION_BUT_RELAXED_POSITIVE_GAINS_COLLIDE_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0';GATE='PHYSICAL_KERR_SHARED_CALIBRATION_MODEL_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','38/38','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('analytic_channel_gap=8.9423947','profile_min_KL=0.2019263','profile_grids=[3,5,9]','plus_anchor=[1.0,1.5,1.0]','minus_anchor=[1.5,0.5,0.775]','relaxed_minus_gains=[0.44907953,0.23594622]','collision_residual=8.8817842e-16'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('composite','separately profiled','relaxed',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION','KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**',TODO.read_text())
if __name__=='__main__':unittest.main()
