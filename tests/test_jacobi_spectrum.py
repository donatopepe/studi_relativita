import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_spectrum.py';O=R/'studies/spacetime/jacobi-spectrum-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Jacobi(unittest.TestCase):
 def test_flat(self):self.assertAlmostEqual(2,mod().eigenvalue(0,2))
 def test_focusing_caustic(self):
  m=mod();self.assertAlmostEqual(math.pi/2,m.first_caustic(4));self.assertAlmostEqual(0,m.eigenvalue(4,math.pi/2),places=12)
 def test_defocusing_no_caustic(self):self.assertIsNone(mod().first_caustic(-1))
 def test_affine_curvature_phase_degeneracy(self):
  m=mod();self.assertAlmostEqual(m.phase(4,3),m.phase(1,6));self.assertEqual('AFFINE_OPTICAL_SCALE_DEGENERACY',m.affine_gate(False))
 def test_ell0_absent(self):self.assertEqual('GEOMETRIC_FOCUSING_SCALE_NOT_ELL0',mod().ell0_gate(['affine','optical_eigenvalue']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_CAUSTIC_GEOMETRIC_LANDMARK_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
