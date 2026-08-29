import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
BIB=(ROOT/'references/library.bib').read_text()
LOG=(ROOT/'references/verification-log.md').read_text()
class EinsteinStaticSpatialHolonomySourceTests(unittest.TestCase):
 def test_canonical_geometry_sources_are_registered(self):
  for key in ('ORaifeartaighEtAl2017','DoCarmo2016'):
   self.assertRegex(BIB,rf'@(?:article|book)\{{{key},')
   self.assertIn(f'## {key}',LOG)
 def test_identifiers_and_scope_limits_are_explicit(self):
  self.assertIn('10.1140/epjh/e2017-80002-5',BIB)
  self.assertIn('9780486806990',BIB.replace('-',''))
  for token in ('Einstein static','spherical triangle','Gauss--Bonnet','finite loop family','detector','ell0','UMCH','detection'):
   self.assertIn(token,LOG)
if __name__=='__main__':unittest.main()
