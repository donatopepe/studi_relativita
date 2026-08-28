import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/jacobi_boundary_phase.py';O=R/'studies/spacetime/jacobi-boundary-phase-results.json'
def mod():
 s=importlib.util.spec_from_file_location('j',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class BoundaryPhase(unittest.TestCase):
 def test_vertex_first_zero(self):self.assertAlmostEqual(math.pi/2,mod().first_positive_zero(4,0,1))
 def test_target_zero_constructed(self):
  m=mod()
  for target in [.2,.7,1.2]:
   v=m.velocity_for_zero(4,1,target);self.assertAlmostEqual(0,m.solution(4,1,v,target),places=12);self.assertAlmostEqual(target,m.first_positive_zero(4,1,v),places=12)
 def test_common_amplitude_scale_preserves_zero(self):
  m=mod();self.assertAlmostEqual(m.first_positive_zero(4,1,-3),m.first_positive_zero(4,5,-15))
 def test_trivial_rejected(self):
  with self.assertRaises(ValueError):mod().first_positive_zero(4,0,0)
 def test_ell0_absent(self):self.assertEqual('BOUNDARY_PHASE_GEOMETRIC_ZERO_NOT_ELL0',mod().ell0_gate(['lambda','d0','v0']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('JACOBI_CAUSTIC_BOUNDARY_PHASE_MOVABLE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
