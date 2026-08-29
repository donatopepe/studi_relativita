import importlib.util,json,math,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies/spacetime/sphere_harmonic_channels.py';O=R/'studies/spacetime/sphere-harmonic-channels-results.json'
def mod():
 s=importlib.util.spec_from_file_location('s',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class HarmonicChannels(unittest.TestCase):
 def test_chebyshev_dependence(self):
  m=mod()
  for a in [0,.3,1,2,math.pi]:
   y=m.channels(a);self.assertAlmostEqual(y[1],2*y[0]**2-1)
 def test_global_collisions(self):
  m=mod()
  for a in [.2,1,2.3]:
   for x,y in zip(m.channels(a),m.channels(-a)):self.assertAlmostEqual(x,y)
   for x,y in zip(m.channels(a),m.channels(a+2*math.pi)):self.assertAlmostEqual(x,y)
 def test_gap_pair_redundant(self):
  m=mod()
  for a in [.2,1,2.3]:
   g,y2=m.gap_pair(a);self.assertAlmostEqual(y2,2*g*g-1)
   for x,y in zip(m.gap_pair(a),m.gap_pair(math.pi-a)):self.assertAlmostEqual(x,y)
 def test_principal_branch(self):
  m=mod()
  for a in [0,.2,1,math.pi]:self.assertAlmostEqual(a,m.principal_phase(m.channels(a)[0]))
 def test_jacobian_rank(self):self.assertEqual(1,mod().phase_jacobian_rank(.7));self.assertEqual(0,mod().phase_jacobian_rank(0))
 def test_geometry_confounding(self):
  m=mod()
  for e in [.2,1,2]:self.assertEqual(m.scaled_channels(e,2,.5),m.scaled_channels(e,4,2))
 def test_ell0_absent(self):self.assertEqual('HARMONIC_PHASE_CHANNELS_GEOMETRIC_NOT_ELL0',mod().ell0_gate(['alpha','eta','r']))
 def test_artifact(self):
  p=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,p.returncode,p.stderr or p.stdout);d=json.loads(O.read_text());self.assertEqual('SPHERE_CROSS_CHANNEL_HARMONIC_ALGEBRAIC_DEPENDENCE_NOT_ELL0',d['status']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
