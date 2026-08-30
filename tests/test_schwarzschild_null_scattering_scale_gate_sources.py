import pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class NullScatteringSourceTests(unittest.TestCase):
 def test_existing_canonical_keys_and_scope_are_bounded(self):
  bib=(ROOT/'references/library.bib').read_text();log=(ROOT/'references/verification-log.md').read_text()
  for key in ('Schwarzschild2003Translation','Darwin1959GravityField'):
   self.assertIn('@article{'+key,bib);self.assertIn('## '+key,log)
  section=log.split('## Schwarzschild null-scattering finite-window reuse',1)[1]
  for token in ('metric context only','null-trajectory and critical-orbit context only','does not establish','detector','covariance','`ell0`','UMCH','detection'):
   self.assertIn(token,section)
if __name__=='__main__':unittest.main()
