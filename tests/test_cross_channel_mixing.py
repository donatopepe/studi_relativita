import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/cross_channel_mixing.py';O=R/'studies/spacetime/cross-channel-mixing-results.json'
def mod():
 s=importlib.util.spec_from_file_location('c',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Mixing(unittest.TestCase):
 def test_latent_ratio_recovers_x(self):
  m=mod()
  for x in [.5,2,5]:self.assertAlmostEqual(x,m.projective_recover(m.response(x)))
 def test_mixing_collision(self):
  m=mod()
  for x,z in [(1,2),(2,5),(.5,3)]:self.assertEqual(m.response(z),m.mv(m.collision_matrix(x,z),m.response(x)))
 def test_collision_matrix_invertible(self):
  m=mod();self.assertGreater(m.det(m.collision_matrix(2,5)),0)
 def test_known_mixing_reversible(self):
  m=mod();x=3;M=[[2,1],[1,1]];self.assertEqual(m.response(x),m.mv(m.inv(M),m.mv(M,m.response(x))))
 def test_ell0_gate(self):self.assertEqual('MIXING_QUOTIENT_NOT_ELL0',mod().ell0_gate(['x','M']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('CROSS_CHANNEL_INJECTIVITY_DESTROYED_BY_FREE_MIXING_GROUP',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
