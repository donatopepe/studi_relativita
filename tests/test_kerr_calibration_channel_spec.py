import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];S=R/'doc/specs/2026-09-11-kerr-auxiliary-calibration-channel.md';P=R/'doc/plans/2026-09-11-kerr-auxiliary-calibration-channel.md';T=R/'TODO.md'
class Spec(unittest.TestCase):
 def test_contract(self):
  s=S.read_text();p=P.read_text();t=T.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','exactly `8/8`','J39-J46','calibration_channel','R=(0.02,0.02)','N_cal=(1,10,100)','Fisher','unknown and branch-profiled','MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,s)
  self.assertIn('Metric:** `8/8`',p);self.assertIn('Kerr auxiliary calibration-channel identifiability MVP',t);self.assertIn('1. [x] Ratify auxiliary calibration-channel specification.',t);self.assertIn('2. [x] Extend authoritative Kerr scenario matrix and runner.',t);self.assertIn('3. [x] Implement auxiliary-channel identifiability engine.',t);self.assertIn('4. [x] Generate stable artifacts and bilingual scientific record.',t);self.assertIn('5. [x] Closure and publication.',t)
if __name__=='__main__':unittest.main()
