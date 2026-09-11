import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];EN=R/'audit/kerr-calibration-channel-report-en.md';IT=R/'audit/kerr-calibration-channel-report-it.md';TH=R/'theory/spacetime/kerr-calibration-channel.md';ROAD=R/'docs/roadmap.md';LED=R/'audit/kaluza-klein-reformulation-change-ledger.md';TODO=R/'TODO.md';ART=R/'studies/spacetime/kerr-calibration-channel-results.json'
RESULT='KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION_AT_MODEL_LEVEL_BUT_UNKNOWN_REFERENCE_RESTORES_EXACT_COLLISION_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0';GATE='PHYSICAL_KERR_CALIBRATOR_REFERENCE_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class Reports(unittest.TestCase):
 def test_contract(self):
  for t in (EN.read_text(),IT.read_text()):
   for x in (RESULT,GATE,'8/8','54/54','DIRECT_REVIEW_NO_SUBAGENT','CORRECTED_SCOPE=REFERENCE_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE'):self.assertIn(x,t)
 def test_values(self):
  self.assertEqual(json.loads(ART.read_text())['control_summary']['controls_passed'],8)
  for t in (EN.read_text(),IT.read_text()):
   for x in ('known_reference=[0.1,10.0]','placement_products=[-0.0057111803,-387.61661]','calibration_only_rank=[1,1]','joint_rank=[2,2]','relative_std=[1.4142136,0.4472136,0.14142136]','weak_information=[0.5,0.05,0.005]','unknown_reference_collision=8.8817842e-16'):self.assertIn(x,t)
 def test_history_todo(self):
  for x in ('auxiliary','known reference','unknown reference',RESULT,GATE):self.assertIn(x,TH.read_text())
  for t in (ROAD.read_text(),LED.read_text()):
   for x in (RESULT,GATE,'KERR_COMPOSITE_BRANCH_SETS_ARE_DISJOINT_UNDER_TOY_BOUNDED_PROFILED_COMMON_CALIBRATION','KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION','F_0'):self.assertIn(x,t)
  todo=TODO.read_text();self.assertIn('Superseded milestone evidence requiring correction',todo);self.assertIn('Full suite: `1163/1163`.',todo);self.assertIn('GitHub Actions run `34568400157` tests/LaTeX passed.',todo)
if __name__=='__main__':unittest.main()
