import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-reference-drift-report-en.md';IT=R/'audit/kerr-reference-drift-report-it.md';TH=R/'theory/spacetime/kerr-reference-drift.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-reference-drift-results.json'
RESULT='KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL_AND_FAILS_AT_ENDPOINT_OR_OUTSIDE_NOT_ELL0';GATE='PHYSICAL_KERR_CALIBRATOR_DRIFT_BOUND_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','62/62','DIRECT_REVIEW_NO_SUBAGENT','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_BOUNDED_REFERENCE_DRIFT_ROBUSTNESS_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('midpoints=[0.11640302,42.028394]','max_radii=[0.077332007,37.595673]','drift_fraction=0.8','safe_radii=[0.061865606,30.076539]','minimum_margin=0.0021528862','endpoint_loss=0.0','outside_collision=8.8817842e-16','minimum_fisher_determinant=0.0024746242'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('drift','endpoint','outside',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES','SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION','F_0'):self.assertIn(x,t)
  self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',TODO.read_text());self.assertIn('5. [ ] Closure and publication. **ACTIVE**',TODO.read_text())
if __name__=='__main__':unittest.main()
