import importlib.util,json,math,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];PATH=ROOT/'studies/spacetime/kerr_finite_source_analyzer.py';ARTIFACT=ROOT/'studies/spacetime/kerr-finite-source-analyzer-results.json'
SPEC=importlib.util.spec_from_file_location('kerr_source_analyzer',PATH);source=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(source)
WIDTHS=(0.08,0.12,0.015,0.02)
class KerrFiniteSourceAnalyzerTests(unittest.TestCase):
 def test_01_source_covariance_domain(self):
  c=source.source_covariance(WIDTHS);self.assertTrue(c['positive_definite']);self.assertEqual(c['normalization'],'ZERO_MEAN_NORMALIZED_GAUSSIAN_PHASE_SPACE_TOY')
  for bad in ((0,.12,.015,.02),(-.1,.12,.015,.02),(math.inf,.12,.015,.02)):
   with self.assertRaises(ValueError):source.source_covariance(bad)
 def test_02_covariance_propagation(self):
  for o in (-1,1):
   c=source.covariance_control(o,WIDTHS);self.assertLess(c['block_formula_residual'],2e-10);self.assertLess(c['symmetry_residual'],2e-10);self.assertTrue(c['positive_definite'])
 def test_03_width_homogeneity(self):
  c=source.width_homogeneity_control(WIDTHS,2.5);self.assertLess(c['covariance_residual'],2e-10);self.assertLess(c['normalized_shape_residual'],2e-10)
 def test_04_orientation_survives_finite_source(self):
  c=source.orientation_control(WIDTHS);self.assertGreater(c['covariance_difference'],1e-3);self.assertGreater(c['scan_difference'],1e-3)
 def test_05_analyzer_extrema(self):
  c=source.analyzer_extrema_control(1,WIDTHS);self.assertLess(c['analytic_eigenvalue_residual'],2e-10);self.assertLess(c['dense_scan_bracket_residual'],2e-5)
 def test_06_common_basis_covariance(self):
  c=source.basis_covariance_control(1,WIDTHS,0.37,0.61);self.assertLess(c['variance_residual'],2e-10);self.assertLess(c['eigenvalue_residual'],2e-10)
 def test_07_analyzer_scalar_collision(self):
  c=source.analyzer_collision_control(WIDTHS);self.assertGreater(c['full_covariance_difference'],1e-3);self.assertLess(c['scalar_collision_residual'],2e-10);self.assertTrue(c['intervals_overlap'])
 def test_08_scale_rank_and_nonclaims(self):
  c=source.scale_rank_control(WIDTHS,2.5);self.assertLess(c['dimensionless_covariance_residual'],2e-10);self.assertLess(c['log_M_column_norm'],2e-10);self.assertEqual(c['scale_null_direction'],[1.,0.,0.,0.,0.,0.]);g=source.no_ell0_gate();self.assertFalse(g['ell0_identified']);self.assertEqual(g['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_stable_artifact(self):
  expected=json.loads(ARTIFACT.read_text());generated=json.loads(subprocess.check_output(['python',str(PATH)],text=True));self.assertEqual(generated,expected);s=expected['control_summary'];self.assertEqual((s['controls_passed'],s['controls_total']),(8,8));self.assertTrue(all(x['passed']for x in s['controls']));self.assertEqual([x['threshold']for x in s['controls']],[1.,2e-10,2e-10,1e-3,2e-5,2e-10,2e-10,2e-10])
if __name__=='__main__':unittest.main()
