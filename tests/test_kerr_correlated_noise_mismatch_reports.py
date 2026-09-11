import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-correlated-noise-mismatch-report-en.md';IT=R/'audit/kerr-correlated-noise-mismatch-report-it.md';TH=R/'theory/spacetime/kerr-correlated-noise-mismatch.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-correlated-noise-mismatch-results.json'
RESULT='KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION_BUT_DIFFERENTIAL_MISMATCH_AT_THE_EXACT_CONE_MARGIN_RESTORES_COLLISION_NOT_ELL0';GATE='PHYSICAL_KERR_SIGNAL_CALIBRATION_NOISE_MATCHING_DRIFT_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','70/70','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_CORRELATED_NOISE_MISMATCH_THRESHOLD_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('noise_eigenvalues=[0.35790627,0.74209373]','cancellation_residual=8.8817842e-16','tau=18.797837','safe_bound=15.038269','remaining_separation=3.7595673','threshold_collision=1.3322676e-15','minimum_observed_eigenvalue=0.39954509'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('correlated','shared noise','full branch',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL','SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**',TODO.read_text())
if __name__=='__main__':unittest.main()
