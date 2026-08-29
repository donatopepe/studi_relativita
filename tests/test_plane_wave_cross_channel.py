import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/plane_wave_cross_channel.py';O=R/'studies/spacetime/plane-wave-cross-channel-results.json'
def mod():
 s=importlib.util.spec_from_file_location('pwc',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class CrossChannel(unittest.TestCase):
 def setUp(self):self.m=mod()
 def test_same_window_different_jacobi(self):
  d=self.m.equal_window_counterexample(5000);self.assertLess(d['window_residual'],1e-10);self.assertGreater(d['jacobi_residual'],1e-4)
 def test_boundary_changes_jacobi_not_window(self):
  d=self.m.boundary_counterexample(4000);self.assertLess(d['window_residual'],1e-12);self.assertGreater(d['jacobi_residual'],1e-3)
 def test_joint_curve_locally_noncollinear_when_calibrated(self):
  d=self.m.local_rank_control();self.assertGreater(d['joint_derivative_norm'],1e-3);self.assertGreater(d['joint_second_difference_noncollinearity'],1e-8)
 def test_free_gains_match_two_widths(self):
  d=self.m.free_gain_equivalence(.7,1.1);self.assertLess(d['quotient_residual'],1e-10)
 def test_affine_profile_rescaling_equivalence(self):
  d=self.m.affine_rescaling_equivalence(.8,1.3);self.assertLess(d['dimensionless_jacobi_residual'],2e-9);self.assertLess(d['dimensionless_window_residual'],2e-9)
 def test_ell0_absent(self):self.assertEqual('EXACT_CROSS_CHANNEL_SUPPORT_WIDTH_NOT_ELL0',self.m.ell0_gate(['L','K','W','B','gain','boundary']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('EXACT_PLANE_WAVE_WINDOW_JACOBI_MAP_CONDITIONAL_SUPPORT_IDENTIFIABILITY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
