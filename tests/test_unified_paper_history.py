import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class History(unittest.TestCase):
 def test_markers(self):
  for d in ('foundation','classical-dynamics','spacetime-foundations'):
   t=(R/'papers'/d/'README.md').read_text();self.assertIn('HISTORICAL_TECHNICAL_RECORD',t);self.assertIn('SUPERSEDED_BY_UNIFIED_UMCH_PAPER',t);self.assertIn('papers/umch',t)
if __name__=='__main__':unittest.main()
