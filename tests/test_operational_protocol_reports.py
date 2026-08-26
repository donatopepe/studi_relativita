import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];IT=ROOT/'audit'/'operational-protocol-report-it.md';EN=ROOT/'audit'/'operational-protocol-report-en.md';PIT=ROOT/'papers'/'spacetime-foundations'/'it'/'protocol-appendix.tex';PEN=ROOT/'papers'/'spacetime-foundations'/'en'/'protocol-appendix.tex';CI=ROOT/'.github'/'workflows'/'verify.yml'
def h(p):return re.findall(r'^## (UMCH-OP-\d{4})',p.read_text(),re.M)
def l(p):return set(re.findall(r'\\label\{([^}]+)\}',p.read_text()))
class Reports(unittest.TestCase):
 def test_audit(self):
  self.assertEqual(h(IT),h(EN));self.assertGreaterEqual(len(h(IT)),7)
  for p in (IT,EN):
   t=p.read_text();
   for x in ['R_hol','R_clock','R_null','R_cong','FRAME_UNRESOLVED','NON_IDENTIFIABLE','NO_POSITIVE_DETECTION_CLAIM']:self.assertIn(x,t)
 def test_paper(self):
  self.assertEqual(l(PIT),l(PEN));self.assertGreaterEqual(len(l(PIT)),7)
  for p in (PIT,PEN):
   t=p.read_text();self.assertIn(r'\texttt{NON\_IDENTIFIABLE}',t);self.assertIn(r'a^\mu=0',t)
 def test_ci(self):
  t=CI.read_text();self.assertIn('protocol-appendix.tex',t);self.assertIn('operational-protocol-it.pdf',t);self.assertIn('operational-protocol-en.pdf',t)
if __name__=='__main__':unittest.main()
