import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'turnover_shape_gate.py';O=R/'studies'/'spacetime'/'turnover-shape-results.json'
def m():
 s=importlib.util.spec_from_file_location('sg',P);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
class Shape(unittest.TestCase):
 def test_area_channels(self):
  x=m()
  for c in ('tidal','magnetic','holonomy'):self.assertEqual((2,'DERIVED_REGULAR_SMALL_REGION_ONLY'),x.exponent(c,True,True))
 def test_unfixed_protocol(self):self.assertEqual((None,'PROTOCOL_GEOMETRY_REQUIRED'),m().exponent('clock',False,True))
 def test_irregular(self):self.assertEqual((None,'REGULAR_EXPANSION_UNAVAILABLE'),m().exponent('holonomy',True,False))
 def test_q(self):
  x=m();self.assertEqual('NOT_DERIVED_FROM_CURRENT_GEOMETRIC_CORE',x.q_gate(None));self.assertEqual('INDEPENDENT_MECHANISM_REQUIRED_AND_UNVALIDATED',x.q_gate('kernel'))
 def test_output(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM',d['turnover_status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
