import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/finite_holonomy_ordering.py';O=R/'studies/spacetime/finite-holonomy-ordering-results.json'
def mod():
 s=importlib.util.spec_from_file_location('h',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class HolonomyOrder(unittest.TestCase):
 def test_noncommuting_raw_order_differs(self):
  m=mod();a,b=m.segments(.2);self.assertGreater(m.distance(m.mm(a,b),m.mm(b,a)),0)
 def test_cyclic_products_same_conjugacy_invariants(self):
  m=mod();a,b=m.segments(.2);self.assertEqual(m.invariants(m.mm(a,b)),m.invariants(m.mm(b,a)))
 def test_similarity_identity(self):
  m=mod();a,b=m.segments(.2);self.assertLess(m.distance(m.mm(m.mm(m.inv(a),m.mm(a,b)),a),m.mm(b,a)),1e-12)
 def test_ell0_absent(self):self.assertEqual('FINITE_LOOP_GEOMETRY_NOT_ELL0',mod().ell0_gate(['t','X','Y','path']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('FINITE_HOLONOMY_RAW_ORDER_DIFF_CONJUGACY_AMBIGUOUS',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
