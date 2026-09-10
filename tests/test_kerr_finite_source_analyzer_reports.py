import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];EN=ROOT/'audit/kerr-finite-source-analyzer-report-en.md';IT=ROOT/'audit/kerr-finite-source-analyzer-report-it.md';THEORY=ROOT/'theory/spacetime/kerr-finite-source-analyzer.md';ROADMAP=ROOT/'docs/roadmap.md';LEDGER=ROOT/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=ROOT/'TODO.md';ART=ROOT/'studies/spacetime/kerr-finite-source-analyzer-results.json'
RESULT='KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE_AND_ANALYZER_SCAN_BUT_SOURCE_WIDTH_HOMOGENEITY_AND_ANALYZER_COLLISIONS_PREVENT_INDEPENDENT_BRANCH_OR_ABSOLUTE_SCALE_IDENTIFICATION_NOT_ELL0';GATE='PHYSICAL_KERR_SOURCE_DYNAMICS_EMISSION_INTENSITY_POLARIZATION_ANALYZER_HARDWARE_RECEIVER_TRANSFER_CALIBRATED_NOISE_LIKELIHOOD_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_bilingual_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','14/14','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_KERR_SOURCE_ANALYZER_CONTROL_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('Gamma_plus_diag=[0.039071011,4.432721]','Gamma_minus_diag=[0.19373503,79.624068]','orientation_difference=75.191347','collision_target=2.313228','collision_angles=[0.16408671,0.80300266]','collision_residual=0.0','scale_residual=0.0'):self.assertIn(x,t)
 def test_theory_history_and_todo(self):
  for x in ('Sigma_observer=P_bar Sigma_source P_bar^T','analyzer variance','width homogeneity','scalar collision',RESULT,GATE):self.assertIn(x,THEORY.read_text())
  for t in (ROADMAP.read_text(),LEDGER.read_text()):
   for x in (RESULT,GATE,'KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION','KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT','F_0'):self.assertIn(x,t)
  self.assertIn('5. [x] Closure and publication.',TODO.read_text())
  self.assertIn('GitHub Actions run `34468583168` tests/LaTeX passed.',TODO.read_text())
if __name__=='__main__':unittest.main()
