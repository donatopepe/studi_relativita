import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];EN=ROOT/'audit/kerr-receiver-likelihood-report-en.md';IT=ROOT/'audit/kerr-receiver-likelihood-report-it.md';THEORY=ROOT/'theory/spacetime/kerr-receiver-likelihood.md';ROADMAP=ROOT/'docs/roadmap.md';LEDGER=ROOT/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=ROOT/'TODO.md';ART=ROOT/'studies/spacetime/kerr-receiver-likelihood-results.json'
RESULT='KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION_BUT_UNCONSTRAINED_GAIN_NOISE_NUISANCES_CAN_COLLIDE_EXACTLY_AND_GEOMETRIC_SCALE_REMAINS_BLIND_NOT_ELL0';GATE='PHYSICAL_KERR_EMISSION_RECEIVER_HARDWARE_CALIBRATION_PRIORS_NOISE_SPECTRUM_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_bilingual(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','22/22','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_KERR_RECEIVER_LIKELIHOOD_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('C_plus_diag=[0.087505447,2.8994414]','C_minus_diag=[0.18649042,51.021903]','KL_plus_minus=1.0752327','KL_minus_plus=7.0519599','symmetric_KL=8.1271925','expected_LLR_25=[26.880816,176.299]','calibration_target=[1.0,100.0]','collision_residual=0.0'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('D_KL','fixed calibration','nuisance collision',RESULT,GATE):self.assertIn(x,THEORY.read_text())
  for t in (ROADMAP.read_text(),LEDGER.read_text()):
   for x in (RESULT,GATE,'KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE','KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate artifacts and bilingual scientific record.',TODO.read_text())
  self.assertIn('5. [ ] Closure and publication. **ACTIVE — local closure green; push/CI pending**',TODO.read_text())
  self.assertIn('Full suite and closure gates rerun after fixes: `1124/1124`',TODO.read_text())
if __name__=='__main__':unittest.main()
