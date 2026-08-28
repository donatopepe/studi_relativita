import importlib.util,json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/holonomy_orientation.py';O=R/'studies/spacetime/holonomy-orientation-results.json'
def mod():
 s=importlib.util.spec_from_file_location('h',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Holonomy(unittest.TestCase):
 def test_rank_deficient_has_collision(self):
  m=mod();M=[[1,0,0],[0,1,0]];self.assertEqual(m.observe(M,[2,3,4],1),m.observe(M,[2,3,9],1));self.assertEqual('OPERATOR_TOMOGRAPHY_NON_IDENTIFIABLE_RANK_DEFICIENT',m.rank_gate(M,3))
 def test_full_rank_recovers_scaled_operator(self):
  m=mod();M=[[1,0,0],[0,1,0],[0,0,1]];self.assertEqual([8,12,16],m.observe(M,[2,3,4],2));self.assertEqual('SCALED_OPERATOR_TOMOGRAPHY_IDENTIFIABLE',m.rank_gate(M,3))
 def test_scale_curvature_reparameterization(self):
  m=mod();M=[[1,0],[0,1]];self.assertEqual(m.observe(M,[8,12],1),m.observe(M,[2,3],2));self.assertEqual('ELL_CURVATURE_AMPLITUDE_DEGENERACY',m.scale_gate(False))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('HOLONOMY_TOMOGRAPHY_RANK_CONDITIONAL_ELL0_ABSENT',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
