import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-calibration-reference-correction-report-en.md';IT=R/'audit/kerr-calibration-reference-correction-report-it.md';TH=R/'theory/spacetime/kerr-calibration-reference-correction.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-calibration-reference-correction-results.json'
RESULT='KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES_WHILE_OUTSIDE_OR_UNKNOWN_REFERENCE_COLLIDES_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0';GATE='PHYSICAL_KERR_CALIBRATOR_REFERENCE_PLACEMENT_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','54/54','DIRECT_REVIEW_NO_SUBAGENT','CORRECTION_OF_16c9718','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_REFERENCE_PLACEMENT_CORRECTION_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('inside_reference=[0.1,10.0]','inside_products=[-0.0057111803,-387.61661]','outside_reference=[0.02,0.02]','outside_collision=1.7763568e-15','outside_minus_gains=[0.26505327,0.25898719]','unknown_reference_collision=8.8817842e-16'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('polarity','inside','outside',RESULT,GATE,'16c9718'):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION','SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Correct bilingual scientific record and preserved history.',TODO.read_text());self.assertIn('5. [ ] Closure and publication. **ACTIVE**',TODO.read_text())
if __name__=='__main__':unittest.main()
