import importlib.util,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1];SD=ROOT/'studies/spacetime';P=SD/'schwarzschild_null_scattering_jacobi.py'
S=importlib.util.spec_from_file_location('sj',P);s=importlib.util.module_from_spec(S);S.loader.exec_module(s)
class ScatteringJacobiReportTests(unittest.TestCase):
 def test_artifact_is_deterministic_and_authoritative(self):
  out=SD/'schwarzschild-null-scattering-jacobi-results.json';x=json.loads(out.read_text())
  self.assertEqual(out.read_text(),s.render(s.build_result()))
  self.assertEqual((x['status'],x['scope'],x['gate']),(s.STATUS,s.SCOPE,s.GATE))
 def test_bilingual_reports_have_exact_authority_and_values(self):
  en=(ROOT/'audit/schwarzschild-null-scattering-jacobi-report-en.md').read_text();it=(ROOT/'audit/schwarzschild-null-scattering-jacobi-report-it.md').read_text()
  for token in (s.STATUS,s.SCOPE,s.GATE,s.CLASSIFICATION,'rank_shape_boundary = 2','rank_with_log_M = 2','log_M_column_norm = 4.317417286094902e-09','scale_null_direction = [0, 0, 1]','UMCH = UNPROVEN','detection = NO_POSITIVE_DETECTION_CLAIM','structural_dead_end = NOT_DECLARED','DIRECT_REVIEW_NO_SUBAGENT'):
   self.assertIn(token,en);self.assertIn(token,it)
  for token in ('Schwarzschild2003Translation','Darwin1959GravityField','Sachs1961','NO_DETECTOR_READOUT','NO_COVARIANCE','NO_ELL0_LAW'):
   self.assertIn(token,en);self.assertIn(token,it)
 def test_theory_and_roadmap_preserve_primary_map_and_negative_result(self):
  theory=(ROOT/'theory/spacetime/schwarzschild-null-scattering-jacobi.md').read_text();road=(ROOT/'docs/roadmap.md').read_text()
  for token in (s.STATUS,s.GATE,'FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS','GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_PHASE_RATE_AND_ENDPOINT_CONVERSION','NOT_ESTABLISHED'):
   self.assertIn(token,theory);self.assertIn(token,road)
if __name__=='__main__':unittest.main()
