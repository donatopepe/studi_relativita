import cmath,importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/sphere_path_measure.py';O=R/'studies/spacetime/sphere-path-measure-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class PathMeasure(unittest.TestCase):
 def test_deterministic_preserves_spectrum(self):self.assertEqual((1,3),mod().eigenvalues(3,1,[(.7,1)]))
 def test_uniform_quarter_paths_isotropic(self):self.assertEqual((2,2),mod().eigenvalues(3,1,[(0,.5),(math.pi/2,.5)]))
 def test_distinct_measures_same_matrix(self):
  m=mod();a=[(0,.5),(math.pi/2,.5)];b=[(math.pi/4,.5),(-math.pi/4,.5)];self.assertAlmostEqual(0,abs(m.circular_moment(a)));self.assertAlmostEqual(0,abs(m.circular_moment(b)));A=m.average_matrix(3,1,a);B=m.average_matrix(3,1,b)
  for i in range(2):
   for j in range(2):self.assertAlmostEqual(A[i][j],B[i][j])
 def test_same_magnitude_isospectral(self):
  m=mod();a=[(0,.75),(math.pi/2,.25)];b=[(math.pi/4,.75),(3*math.pi/4,.25)];self.assertAlmostEqual(abs(m.circular_moment(a)),abs(m.circular_moment(b)));self.assertEqual(m.eigenvalues(3,1,a),m.eigenvalues(3,1,b));self.assertNotEqual(m.average_matrix(3,1,a),m.average_matrix(3,1,b))
 def test_invalid_weights(self):self.assertRaises(ValueError,mod().circular_moment,[(0,.4),(1,.4)])
 def test_ell0_absent(self):self.assertEqual('PATH_MEASURE_MOMENT_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['mu','K','area']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SPHERE_PATH_MEASURE_SECOND_CIRCULAR_MOMENT_ONLY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
