import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];BIB=(ROOT/'references/library.bib').read_text();LOG=(ROOT/'references/verification-log.md').read_text()
class RadarSources(unittest.TestCase):
 def test_radar_source_registered(self):
  self.assertRegex(BIB,r'@article\{Lin2020RadarCoordinates,');self.assertIn('## Lin2020RadarCoordinates',LOG)
  for token in ('10.1103/PhysRevD.101.124001','1911.03950'):self.assertIn(token,BIB);self.assertIn(token,LOG)
 def test_supported_scope_and_exclusions(self):
  for token in ('radar coordinates','localized observers','Schwarzschild-like','ideal static mirror','finite Levi-Civita loop','vector readout','ell0','UMCH','detection'):
   self.assertIn(token,LOG)
if __name__=='__main__':unittest.main()
