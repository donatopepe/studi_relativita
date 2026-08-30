import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];BIB=(ROOT/'references/library.bib').read_text();LOG=(ROOT/'references/verification-log.md').read_text()
class PhotonOrbitSources(unittest.TestCase):
 def test_canonical_photon_orbit_source_registered(self):
  self.assertIn('@article{Darwin1959GravityField',BIB);self.assertIn('## Darwin1959GravityField',LOG)
  for token in ('The gravity field of a particle','10.1098/rspa.1959.0015','249','180--194'):
   self.assertIn(token,BIB);self.assertIn(token,LOG)
 def test_source_scope_is_bounded(self):
  for token in ('Schwarzschild null trajectories','critical circular orbit','finite Levi-Civita loop','static worldline closure','emitter','absorber','vector readout','detector covariance','ell0','UMCH','detection'):
   self.assertIn(token,LOG)
if __name__=='__main__':unittest.main()
