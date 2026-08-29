import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_endpoint_gauge.py';O=R/'studies/spacetime/jacobi-endpoint-gauge-results.json'
def mod():
 s=importlib.util.spec_from_file_location('jeg',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class EndpointGauge(unittest.TestCase):
 def setUp(self):self.m=mod();self.b=[[.62,.11],[-.04,.39]]
 def test_raw_antisymmetric_signal_reverses(self):self.assertAlmostEqual(self.m.antisymmetric_scalar(self.m.transpose(self.b)),-self.m.antisymmetric_scalar(self.b))
 def test_raw_signal_changes_under_endpoint_rotation(self):
  m=self.m;c=m.endpoint_action(self.b,.3,-.2);self.assertGreater(abs(m.antisymmetric_scalar(c)-m.antisymmetric_scalar(self.b)),1e-6)
 def test_singular_values_and_determinant_invariant(self):
  m=self.m;c=m.endpoint_action(self.b,.3,-.2);self.assertEqual(tuple(round(x,12) for x in m.singular_values(c)),tuple(round(x,12) for x in m.singular_values(self.b)));self.assertAlmostEqual(m.det2(c),m.det2(self.b))
 def test_transpose_same_so2_endpoint_orbit(self):
  m=self.m;fit=m.fit_endpoint_rotations(self.b,m.transpose(self.b));self.assertLess(fit['residual'],1e-10);self.assertAlmostEqual(m.det2(self.b),m.det2(m.transpose(self.b)))
 def test_common_conjugation_cannot_flip_generic_antisymmetric_part(self):
  m=self.m;fit=m.fit_common_rotation(self.b,m.transpose(self.b));self.assertGreater(fit['residual'],1e-4)
 def test_rank_deficient_transpose_still_o2_orbit(self):
  m=self.m;b=[[1,2],[0,0]];self.assertLess(m.fit_endpoint_orthogonal(b,m.transpose(b))['residual'],1e-10)
 def test_ell0_absent(self):self.assertEqual('ENDPOINT_FRAME_QUOTIENT_NOT_ELL0',self.m.ell0_gate(['B','Qo','Qs','screen']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_TRANSPOSE_REVERSAL_NONIDENTIFIABLE_UNDER_INDEPENDENT_ENDPOINT_FRAME_QUOTIENT',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
