import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/transport_average_order.py';O=R/'studies/spacetime/transport-average-order-results.json'
def mod():
 s=importlib.util.spec_from_file_location('t',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class TransportAverage(unittest.TestCase):
 def test_raw_average_isotropic(self):self.assertEqual([2,2],mod().eigenvalues(mod().raw_average()))
 def test_transport_then_average_recovers_anisotropy(self):self.assertEqual([1,3],mod().eigenvalues(mod().transport_then_average()))
 def test_orders_differ(self):self.assertNotEqual(mod().raw_average(),mod().transport_then_average())
 def test_local_spectra_same(self):
  m=mod();self.assertEqual(m.eigenvalues(m.A),m.eigenvalues(m.B))
 def test_ell0_absent(self):self.assertEqual('AVERAGING_ORDER_PROTOCOL_NOT_ELL0',mod().ell0_gate(['A','Q','weights']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('TRANSPORT_AND_WINDOW_AVERAGING_ORDER_NONCOMMUTATIVE',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
