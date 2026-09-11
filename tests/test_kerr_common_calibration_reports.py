import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-common-calibration-report-en.md';IT=R/'audit/kerr-common-calibration-report-it.md';TH=R/'theory/spacetime/kerr-common-calibration.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-common-calibration-results.json'
RESULT='KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION_BUT_COMMON_ATTENUATION_OR_UNBOUNDED_NOISE_DRIVES_SEPARATION_TO_ZERO_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0';GATE='PHYSICAL_KERR_CALIBRATION_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','30/30','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_COMMON_CALIBRATION_ROBUSTNESS_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('bounded_min_KL=4.0094352','bounded_anchor=[0.5,0.5,1.0]','attenuation_KL=[4.0094352,0.15069819,2.8033078e-05]','noise_KL=[6.4635633,0.15069819,2.8033078e-05]','identity_residual=0.0','scale_residual=0.0'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('common calibration','bounded invertible','asymptotic',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION','KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE','F_0'):self.assertIn(x,t)
  todo=TODO.read_text();self.assertIn('Previous milestone closure evidence',todo)
  self.assertIn('Full suite: `1137/1137`.',todo)
  self.assertIn('GitHub Actions run `34537112452` tests/LaTeX passed.',todo)
if __name__=='__main__':unittest.main()
