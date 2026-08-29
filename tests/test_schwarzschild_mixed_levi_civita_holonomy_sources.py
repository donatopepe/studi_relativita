import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
BIB=(ROOT/'references/library.bib').read_text();LOG=(ROOT/'references/verification-log.md').read_text()
class SchwarzschildMixedHolonomySourceTests(unittest.TestCase):
 def test_canonical_sources_are_registered(self):
  for key in ('Schwarzschild2003Translation','AmbroseSinger1953'):
   self.assertRegex(BIB,rf'@article\{{{key},')
   self.assertIn(f'## {key}',LOG)
 def test_identifiers_supported_topics_and_limits_are_explicit(self):
  for doi in ('10.1023/A:1022971926521','10.1090/S0002-9947-1953-0063739-1'):
   self.assertIn(doi,BIB);self.assertIn(doi,LOG)
  for token in ('Schwarzschild exterior solution','holonomy Lie algebra','finite coordinate rectangles','numerical transport','causal loop family','detector','ell0','UMCH','detection'):
   self.assertIn(token,LOG)
if __name__=='__main__':unittest.main()
