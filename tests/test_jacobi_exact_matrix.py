import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_exact_matrix.py';O=R/'studies/spacetime/jacobi-exact-matrix-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class MatrixJacobi(unittest.TestCase):
 def test_segment_symplectic(self):
  m=mod();p=m.segment((1,4),.4,.3);self.assertLess(m.symplectic_error(p),1e-12)
 def test_total_characteristic_order_blind(self):
  m=mod();a,b=m.order_maps(.4);self.assertEqual(m.characteristic(a),m.characteristic(b))
 def test_rotated_vertex_block_order_sensitive(self):
  m=mod();a,b=m.order_maps(.4);self.assertGreater(m.distance(m.vertex_block(a),m.vertex_block(b)),1e-6)
 def test_aligned_vertex_block_order_blind(self):
  m=mod();a,b=m.order_maps(0);self.assertLess(m.distance(m.vertex_block(a),m.vertex_block(b)),1e-12)
 def test_isotropic_rotation_irrelevant(self):
  m=mod();a,b=m.order_maps(.7,eigs2=(2,2));self.assertLess(m.distance(m.vertex_block(a),m.vertex_block(b)),1e-12)
 def test_vertex_blocks_transpose_and_singular_values_blind(self):
  m=mod();a,b=m.order_maps(.4);ba=m.vertex_block(a);bb=m.vertex_block(b);self.assertLess(m.distance(bb,m.transpose(ba)),1e-12);sa=m.singular_values(ba);sb=m.singular_values(bb);self.assertLess(max(abs(x-y) for x,y in zip(sa,sb)),1e-12)
 def test_ell0_absent(self):self.assertEqual('MATRIX_OPTICAL_ORDER_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['K1','K2','theta','L']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_EXACT_MATRIX_SPECTRUM_AND_VERTEX_SINGULAR_VALUES_ORDER_BLIND_BLOCK_TRANSPOSE_SENSITIVE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
