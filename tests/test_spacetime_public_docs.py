import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class PublicDocs(unittest.TestCase):
 def test_readmes_present_new_core_and_history(self):
  for p in (ROOT/'README.md',ROOT/'README.en.md'):
   t=p.read_text()
   for x in ['Multiscale','ℓ₀','FRAME_UNRESOLVED','R_tidal','F_0','UNPROVEN','SUPERSEDED_AS_CORE']:self.assertIn(x,t)
   self.assertIn('a^μ=0',t);self.assertIn('reaction force',t.lower())
 def test_roadmap_restarts_sequence(self):
  t=(ROOT/'docs'/'roadmap.md').read_text()
  for x in ['Spacetime Paper I','Exact cases','Observables and data','Minkowski','FLRW','Schwarzschild','VSI','ALD remains outside']:self.assertIn(x,t)
if __name__=='__main__':unittest.main()
