import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/nonabelian_commutator_holonomy.py';O=R/'studies/spacetime/nonabelian-commutator-holonomy-results.json'
def mod():
 s=importlib.util.spec_from_file_location('n',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
class NonAbelian(unittest.TestCase):
 def test_commutator_exact(self):
  m=mod()
  for a,b in [(.2,.3),(1,-2),(-.5,-.7)]:
   c=m.commutator(a,b);self.assertAlmostEqual(1,m.det(c));self.assertAlmostEqual(2+(a*b)**2,m.trace(c))
 def test_noncommuting(self):
  m=mod();self.assertNotEqual(mul(m.shear_a(1),m.shear_b(2)),mul(m.shear_b(2),m.shear_a(1)))
 def test_product_collision(self):
  m=mod();base=m.trace(m.commutator(.4,.7))
  for c in [.2,2,-3]:self.assertAlmostEqual(base,m.trace(m.commutator(.4*c,.7/c)))
 def test_sign_collision(self):
  m=mod();self.assertAlmostEqual(m.trace(m.commutator(.4,.7)),m.trace(m.commutator(-.4,.7)))
 def test_threshold_moves(self):
  m=mod();target=3;tau=3;p=q=1;prod=math.sqrt(tau-2)/target**(p+q);self.assertAlmostEqual(target,m.threshold(tau,prod,p,q))
 def test_exponent_sum_only(self):
  m=mod()
  for ell in [.2,1,3]:self.assertAlmostEqual(m.scaled_trace(ell,2,3,1,2),m.scaled_trace(ell,2,3,.5,2.5))
 def test_ell0_absent(self):self.assertEqual('NONABELIAN_PRODUCT_PHASE_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['a','b','ell']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('NONABELIAN_COMMUTATOR_TRACE_PRODUCT_DEGENERACY_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
