import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];A=json.loads((R/'studies/spacetime/schwarzschild-radar-holonomy-results.json').read_text());EN=R/'audit/schwarzschild-radar-holonomy-report-en.md';IT=R/'audit/schwarzschild-radar-holonomy-report-it.md';TH=R/'theory/spacetime/schwarzschild-radar-holonomy.md'
class RadarReports(unittest.TestCase):
 def test_authority_files_exist(self):
  for p in (EN,IT,TH):self.assertTrue(p.exists(),p)
 def test_exact_state_scope_gate_and_values_align(self):
  for p in (EN,IT,TH):
   t=p.read_text()
   for token in (A['status'],A['scope'],A['gate'],'UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','NOT_DECLARED','10.1103/PhysRevD.101.124001','non-Abelianity does not imply independent rank'):
    self.assertIn(token,t)
   for value in ('8.168553570818094','0.22713493607514745','0.8239284342654838','1.798766884999431e-16'):self.assertIn(value,t)
 def test_bilingual_semantic_tokens(self):
  for p in (EN,IT):
   t=p.read_text()
   for token in ('Delta tau','r_*','duration_only_identifies_boundary=false','ell0_identified=false','positive_detection_claim=false','structural_dead_end=NOT_DECLARED','TRAVEL_TIME_CURVATURE_AND_HOLONOMY_SHARE_DECLARED_GEOMETRY_AND_ARE_NOT_ASSUMED_INDEPENDENT'):
    self.assertIn(token,t)
if __name__=='__main__':unittest.main()
