import importlib.util, json, pathlib, subprocess, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PROGRAM=ROOT/'studies/spacetime/plane_wave_covariant_sachs_screen.py'
ARTIFACT=ROOT/'studies/spacetime/plane-wave-covariant-sachs-screen-results.json'
def load():
 spec=importlib.util.spec_from_file_location('cov_sachs',PROGRAM); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
class CovariantSachsTests(unittest.TestCase):
 def setUp(self): self.m=load()
 def test_zero_connection_collapse(self):
  r=self.m.zero_connection_control(n=5000)
  self.assertLess(max(r.values()),3e-10)
 def test_graph_and_direct_boundary_equivalence(self):
  r=self.m.graph_equivalence_control(n=5000)
  self.assertLess(r['canonical_graph_residual'],3e-10)
  self.assertLess(r['velocity_graph_residual'],3e-10)
  self.assertLess(r['s_equals_r_minus_a_residual'],3e-10)
 def test_connection_twist_shift_and_riccati(self):
  r=self.m.twist_connection_control(n=5000)
  self.assertLess(r['twist_shift_residual'],3e-10)
  self.assertGreater(abs(r['velocity_twist']-r['canonical_twist']),1e-2)
  self.assertLess(r['canonical_riccati_residual'],2e-6)
  self.assertLess(r['velocity_riccati_residual'],2e-6)
 def test_endpoint_rate_calibration_moves_velocity_only(self):
  r=self.m.endpoint_rate_mobility_control(n=5000)
  self.assertEqual(r['canonical_graph_difference'],0.0)
  self.assertGreater(r['velocity_graph_difference'],1e-2)
  self.assertGreater(r['velocity_twist_difference'],1e-2)
 def test_orientation_and_affine_controls(self):
  c=self.m.orientation_control(n=5000); a=self.m.affine_orbit_control(n=5000)
  self.assertLess(c['so2_canonical_covariance_residual'],3e-10)
  self.assertLess(c['so2_velocity_covariance_residual'],3e-10)
  self.assertLess(c['reflection_twist_sign_residual'],3e-10)
  self.assertLess(a['maximum_dimensionless_residual'],5e-10)
 def test_caustic_and_artifact(self):
  self.assertEqual(self.m.safe_graph([[1,0],[0,0]],[[0,0],[0,0]])['status'],'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR')
  subprocess.run(['python3',str(PROGRAM),'--check'],check=True)
  d=json.loads(ARTIFACT.read_text())
  self.assertEqual(d['status'],'EXACT_PLANE_WAVE_ROTATING_SCREEN_SACHS_TWIST_CONNECTION_AND_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_GRAPH_AFFINE_SCALE_BLIND_NOT_ELL0')
  self.assertEqual(d['open_gate'],'PHYSICAL_SACHS_SCREEN_TRANSPORT_CANONICAL_BOUNDARY_ENDPOINT_RATE_AND_PARITY_NOT_DERIVED')
  self.assertFalse(d['structural_dead_end']); self.assertEqual(d['conclusion'],'NO_POSITIVE_DETECTION_CLAIM')
if __name__=='__main__': unittest.main()
