import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
IT=ROOT/'audit'/'paper-iia-report-it.md'; EN=ROOT/'audit'/'paper-iia-report-en.md'; PIT=ROOT/'papers'/'classical-dynamics'/'it'/'hard-constraint-appendix.tex'; PEN=ROOT/'papers'/'classical-dynamics'/'en'/'hard-constraint-appendix.tex'; CI=ROOT/'.github'/'workflows'/'verify.yml'
def heads(p): return re.findall(r'^## (UMCH-P2A-\d{4})',p.read_text(),re.M)
def labels(p): return set(re.findall(r'\\label\{([^}]+)\}',p.read_text()))
class Reports(unittest.TestCase):
 def test_audits_align(self):
  self.assertEqual(heads(IT),heads(EN));self.assertGreaterEqual(len(heads(IT)),8)
  for p in (IT,EN):
   t=p.read_text()
   for x in ['CONTRADICTED_UNDER_ASSUMPTIONS','CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B','BLOCKED','UNPROVEN','DISTRIBUTIONAL_MATCHING_REQUIRED'] : self.assertIn(x,t)
   self.assertIn('does not',t.lower())
 def test_appendices_align(self):
  self.assertEqual(labels(PIT),labels(PEN)); req={'sec:p2a-model','sec:p2a-branches','sec:p2a-transition','sec:p2a-limit','sec:p2a-nogo','sec:p2a-limits','sec:p2a-ai'};self.assertTrue(req<=labels(PIT))
  for p in (PIT,PEN):
   t=p.read_text();self.assertIn(r'\texttt{BLOCKED}',t);self.assertIn(r'\texttt{CONTRADICTED\_UNDER\_ASSUMPTIONS}',t);self.assertIn(r'\kappa_0',t)
 def test_ci(self):
  t=CI.read_text(); self.assertIn('hard-constraint-appendix.tex',t);self.assertIn('hard-constraint-appendix-it.pdf',t);self.assertIn('hard-constraint-appendix-en.pdf',t)
if __name__=='__main__':unittest.main()
