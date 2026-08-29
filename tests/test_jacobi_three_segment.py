import importlib.util,itertools,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_three_segment.py';O=R/'studies/spacetime/jacobi-three-segment-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class ThreeSegment(unittest.TestCase):
 def setUp(self):self.m=mod();self.segs=[(1,.3),(2,.5),(4,.7)]
 def test_all_permutations(self):self.assertEqual(6,len(self.m.permutation_records(self.segs)))
 def test_spectrum_all_permutations_blind(self):
  r=self.m.permutation_records(self.segs);groups=self.m.groups(r,'characteristic');self.assertEqual([6],list(map(len,groups.values())))
 def test_reversal_spectrum_same(self):
  m=self.m;a=m.total(self.segs,(0,1,2));b=m.total(self.segs,(2,1,0));self.assertAlmostEqual(m.trace(a),m.trace(b));self.assertAlmostEqual(m.det(a),m.det(b))
 def test_vertex_endpoint_classes(self):
  r=self.m.permutation_records(self.segs);groups=self.m.groups(r,'vertex_endpoint');self.assertEqual([2,2,2],sorted(map(len,groups.values())))
 def test_full_maps_distinct_generic(self):
  r=self.m.permutation_records(self.segs);self.assertEqual(6,len(self.m.groups(r,'matrix')))
 def test_equal_segments_collapse(self):
  r=self.m.permutation_records([(2,.4)]*3);self.assertEqual(1,len(self.m.groups(r,'matrix')))
 def test_ell0_absent(self):self.assertEqual('THREE_SEGMENT_OPTICAL_ORDER_GEOMETRIC_NOT_ELL0',self.m.ell0_gate(['lambda','L','permutation']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_THREE_SEGMENT_SPECTRUM_PERMUTATION_BLIND_VERTEX_ENDPOINT_MIDDLE_ONLY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
