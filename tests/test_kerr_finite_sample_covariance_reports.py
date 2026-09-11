import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-finite-sample-covariance-report-en.md';IT=R/'audit/kerr-finite-sample-covariance-report-it.md';TH=R/'theory/spacetime/kerr-finite-sample-covariance.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-finite-sample-covariance-results.json'
RESULT='KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING_AND_ONLY_A_CONSERVATIVE_TOY_COUNT_GATE_BOUNDS_BRANCH_COLLISION_SCALE_NOT_ELL0';GATE='PHYSICAL_KERR_SAMPLE_INDEPENDENCE_GAUSSIANITY_MEAN_ESTIMATION_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','78/78','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_GAUSSIAN_COVARIANCE_UNCERTAINTY_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('total_coefficient=923.69333','counts=[16,64,256]','rms=[7.5980809,3.7990405,1.8995202]','minimum_count=53','risk_53=0.049321491','risk_52=0.050269981','risk_16=0.16337744','risk_64=0.04084436'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('finite-sample','Wishart','Markov',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION','KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL','F_0'):self.assertIn(x,t)
  todo=TODO.read_text();self.assertIn('Previous milestone closure evidence',todo);self.assertIn('Full suite: `1215/1215`.',todo);self.assertIn('GitHub Actions run `34631514528` tests/LaTeX passed.',todo)
if __name__=='__main__':unittest.main()
