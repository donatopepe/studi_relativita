import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_reciprocity_involution.py';O=R/'studies/spacetime/jacobi-reciprocity-involution-results.json'
def mod():
 s=importlib.util.spec_from_file_location('jri',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Involution(unittest.TestCase):
 def setUp(self):self.m=mod();self.p=[((1,4),0,.3),((2,5),.4,.4),((3,7),-.25,.2),((1.5,6),.7,.15)]
 def test_segment_fixed_by_reversal_map(self):
  m=self.m;s=m.segment(*self.p[1]);self.assertLess(m.distance(m.reverse_map(s),s),1e-12)
 def test_reverse_map_is_anti_automorphism(self):
  m=self.m;x=m.segment(*self.p[0]);y=m.segment(*self.p[1]);self.assertLess(m.distance(m.reverse_map(m.mm(x,y)),m.mm(m.reverse_map(y),m.reverse_map(x))),1e-12)
 def test_reversed_profile_equals_involution(self):
  m=self.m;f=m.propagate(self.p);r=m.propagate(list(reversed(self.p)));self.assertLess(m.distance(r,m.reverse_map(f)),1e-12)
 def test_vertex_block_transposes(self):
  m=self.m;f=m.vertex_block(m.propagate(self.p));r=m.vertex_block(m.propagate(list(reversed(self.p))));self.assertLess(m.distance(r,m.transpose(f)),1e-12)
 def test_vertex_singular_values_blind(self):
  m=self.m;f=m.vertex_block(m.propagate(self.p));r=m.vertex_block(m.propagate(list(reversed(self.p))));self.assertEqual(tuple(round(x,12) for x in m.singular_values(f)),tuple(round(x,12) for x in m.singular_values(r)))
 def test_oriented_antisymmetric_part_changes_sign(self):
  m=self.m;f=m.vertex_block(m.propagate(self.p));r=m.vertex_block(m.propagate(list(reversed(self.p))));self.assertGreater(m.distance(f,r),1e-6);self.assertAlmostEqual(m.antisymmetric_scalar(r),-m.antisymmetric_scalar(f))
 def test_ell0_absent(self):self.assertEqual('FINITE_PRODUCT_RECIPROCITY_NOT_ELL0',self.m.ell0_gate(['K','L','screen','order']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_FINITE_SYMMETRIC_PROFILE_REVERSAL_EXACT_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
