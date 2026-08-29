import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_matrix_reciprocity.py';O=R/'studies/spacetime/jacobi-matrix-reciprocity-results.json'
def mod():
 s=importlib.util.spec_from_file_location('jmr',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Reciprocity(unittest.TestCase):
 def setUp(self):
  self.m=mod();self.profile=[((1,4),0,.3),((2,5),.4,.4),((3,7),-.25,.2)]
 def test_two_segment_transpose_control(self):
  p=self.profile[:2];a=self.m.vertex_block(self.m.propagate(p));b=self.m.vertex_block(self.m.propagate(list(reversed(p))));self.assertLess(self.m.distance(b,self.m.transpose(a)),1e-12)
 def test_three_segment_transpose_reciprocity_survives(self):
  a=self.m.vertex_block(self.m.propagate(self.profile));b=self.m.vertex_block(self.m.propagate(list(reversed(self.profile))));self.assertLess(self.m.distance(b,self.m.transpose(a)),1e-12)
 def test_three_segment_singular_values_reversal_blind(self):
  a=self.m.vertex_block(self.m.propagate(self.profile));b=self.m.vertex_block(self.m.propagate(list(reversed(self.profile))));sa=self.m.singular_values(a);sb=self.m.singular_values(b);self.assertLess(max(abs(x-y) for x,y in zip(sa,sb)),1e-12)
 def test_four_segment_transpose_reciprocity_survives(self):
  p=self.profile+[((1.5,6),.7,.15)];a=self.m.vertex_block(self.m.propagate(p));b=self.m.vertex_block(self.m.propagate(list(reversed(p))));self.assertLess(self.m.distance(b,self.m.transpose(a)),1e-12)
 def test_full_spectrum_reversal_blind(self):
  a=self.m.propagate(self.profile);b=self.m.propagate(list(reversed(self.profile)));self.assertEqual(self.m.characteristic(a),self.m.characteristic(b))
 def test_aligned_profile_vertex_reversal_blind(self):
  p=[((1,4),0,.3),((2,5),0,.4),((3,7),0,.2)];a=self.m.vertex_block(self.m.propagate(p));b=self.m.vertex_block(self.m.propagate(list(reversed(p))));self.assertLess(self.m.distance(a,b),1e-12)
 def test_ell0_absent(self):self.assertEqual('PROFILE_REVERSAL_GEOMETRIC_NOT_ELL0',self.m.ell0_gate(['K','L','order','screen']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_MATRIX_PROFILE_REVERSAL_TRANSPOSE_RECIPROCITY_SINGULAR_VALUES_BLIND_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
