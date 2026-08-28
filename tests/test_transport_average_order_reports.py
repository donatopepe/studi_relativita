import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual(self):
  e=(R/'audit/transport-average-order-report-en.md').read_text();i=(R/'audit/transport-average-order-report-it.md').read_text()
  for x in ['TOY_CONTROL_AND_NEGATIVE_RESULT','TRANSPORT_AND_WINDOW_AVERAGING_ORDER_NONCOMMUTATIVE','NO_POSITIVE_DETECTION_CLAIM','ell0']:self.assertIn(x,e);self.assertIn(x,i)
 def test_scope(self):
  t=(R/'theory/spacetime/transport-average-order.md').read_text();self.assertIn('do not commute',t);self.assertIn('no core reformulation',t)
if __name__=='__main__':unittest.main()
