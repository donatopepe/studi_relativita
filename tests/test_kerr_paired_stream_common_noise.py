import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/kerr_paired_stream_common_noise.py';A=R/'studies/spacetime/kerr-paired-stream-common-noise-results.json';S=importlib.util.spec_from_file_location('paired',P);c=importlib.util.module_from_spec(S);S.loader.exec_module(c)
class Controls(unittest.TestCase):
 def test_01_domain(self):
  x=c.domain_control();self.assertTrue(x['valid_joint_blocks']);self.assertEqual(x['invalid_cases_rejected'],x['cases'])
 def test_02_identity(self):self.assertLess(c.identity_control()['residual'],2e-10)
 def test_03_coefficient(self):
  x=c.coefficient_control();self.assertTrue(x['strict_reduction']);self.assertTrue(x['small_gain']);self.assertGreaterEqual(x['rms_ratio'],.99)
 def test_04_rms(self):self.assertTrue(c.rms_control()['strictly_decreasing'])
 def test_05_safe_count(self):
  x=c.safe_count_control();self.assertEqual(x['minimum_count'],87);self.assertLessEqual(x['risk_at_count'],.05);self.assertGreater(x['risk_at_predecessor'],.05);self.assertFalse(x['N64_passes'])
 def test_06_zero_shared(self):
  x=c.zero_shared_control();self.assertLess(x['coefficient_residual'],2e-10);self.assertEqual(x['minimum_count'],x['independent_minimum_count']);self.assertEqual(x['minimum_count'],88)
 def test_07_basis_scale(self):
  x=c.basis_scale_control();self.assertLess(x['basis_residual'],2e-10);self.assertLess(x['scale_residual'],2e-10)
 def test_08_nonclaims(self):
  x=c.no_ell0_gate();self.assertFalse(x['L_identified']);self.assertFalse(x['ell0_identified']);self.assertEqual(x['Detection'],'NO_POSITIVE_DETECTION_CLAIM')
 def test_artifact(self):self.assertEqual(json.loads(A.read_text()),json.loads(subprocess.check_output(['python',str(P)],text=True)))
if __name__=='__main__':unittest.main()
