import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/transport_gauge.py';O=R/'studies/spacetime/transport-gauge-results.json'
def mod():
 s=importlib.util.spec_from_file_location('t',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Transport(unittest.TestCase):
 def test_rotation_changes_coordinates_not_spectrum(self):
  m=mod();a=m.rotate_diag(3,1,0);b=m.rotate_diag(3,1,.7);self.assertNotEqual(m.project(a),m.project(b));self.assertEqual(m.invariants(a),m.invariants(b));self.assertEqual('APPARENT_NONRADIALITY_PURE_CONJUGATION',m.compare(a,b))
 def test_spectral_change_is_not_pure_rotation(self):
  m=mod();a=m.rotate_diag(3,1,.2);b=m.rotate_diag(4,1,.8);self.assertEqual('SPECTRAL_SHAPE_EVOLUTION_GEOMETRIC_ONLY',m.compare(a,b))
 def test_degenerate_rotation_blind(self):
  m=mod();self.assertEqual(m.rotate_diag(2,2,0),m.rotate_diag(2,2,1.1))
 def test_ell0_absent(self):self.assertEqual('ELL0_ABSENT_AFTER_TRANSPORT_QUOTIENT',mod().ell0_gate(['operator','transport','scale']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('TRANSPORT_GAUGE_QUOTIENT_REQUIRED_FOR_NONRADIALITY',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
