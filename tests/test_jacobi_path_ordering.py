import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_path_ordering.py';O=R/'studies/spacetime/jacobi-path-ordering-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class JacobiOrder(unittest.TestCase):
 def test_commuting_generators_order_independent(self):
  m=mod();a=[[1,0],[0,2]];self.assertAlmostEqual(0,m.distance(m.path(a,a,.1),m.path(a,a,.1)),places=12)
 def test_noncommuting_order_matters(self):
  m=mod();a=[[1,0],[0,3]];b=[[2,1],[1,2]];self.assertGreater(m.commutator_norm(a,b),0);self.assertGreater(m.distance(m.path(a,b,.1),m.path(b,a,.1)),0)
 def test_same_local_spectra_both_orders(self):
  m=mod();a=[[1,0],[0,3]];b=[[2,1],[1,2]];self.assertEqual(m.spectrum(a),m.spectrum(a));self.assertEqual(m.spectrum(b),m.spectrum(b))
 def test_ell0_absent(self):self.assertEqual('ORDERED_GEOMETRIC_MAP_NOT_ELL0',mod().ell0_gate(['K','h','screen']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_PATH_ORDER_REQUIRED_LOCAL_SPECTRA_INSUFFICIENT',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
