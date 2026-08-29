import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_exact_two_segment.py';O=R/'studies/spacetime/jacobi-exact-two-segment-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ExactTwoSegment(unittest.TestCase):
 def test_segment_symplectic(self):
  m=mod()
  for lam,L in [(1,.2),(2,.5),(4,1)]:self.assertAlmostEqual(1,m.det(m.segment(lam,L)))
 def test_orders_differ(self):
  m=mod();a,b=m.order_maps(1,.7,3,.4);self.assertGreater(m.maxdiff(a,b),1e-6)
 def test_total_spectrum_same(self):
  m=mod();a,b=m.order_maps(1,.7,3,.4);self.assertAlmostEqual(m.trace(a),m.trace(b));self.assertAlmostEqual(m.det(a),m.det(b));self.assertEqual(m.characteristic(a),m.characteristic(b))
 def test_vertex_displacement_order_blind_but_derivative_sensitive(self):
  m=mod();a,b=m.order_maps(1,.7,3,.4);self.assertAlmostEqual(m.vertex_endpoint(a),m.vertex_endpoint(b));self.assertGreater(abs(m.vertex_derivative(a)-m.vertex_derivative(b)),1e-6)
 def test_identical_segments_order_blind(self):
  m=mod();a,b=m.order_maps(2,.3,2,.3);self.assertLess(m.maxdiff(a,b),1e-12);self.assertAlmostEqual(m.vertex_endpoint(a),m.vertex_endpoint(b))
 def test_boundary_basis_matters(self):
  m=mod();a,b=m.order_maps(1,.7,3,.4);self.assertAlmostEqual(m.endpoint(a,(0,1)),m.endpoint(b,(0,1)));self.assertNotAlmostEqual(m.endpoint(a,(1,0)),m.endpoint(b,(1,0)))
 def test_ell0_absent(self):self.assertEqual('EXACT_OPTICAL_PHASE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['lambda1','lambda2','L1','L2']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_EXACT_SPECTRUM_AND_VERTEX_DISPLACEMENT_ORDER_BLIND_FULL_MAP_ORDER_SENSITIVE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
