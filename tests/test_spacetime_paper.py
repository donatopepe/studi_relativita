import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];IT=ROOT/'papers'/'spacetime-foundations'/'it'/'main.tex';EN=ROOT/'papers'/'spacetime-foundations'/'en'/'main.tex';CI=ROOT/'.github'/'workflows'/'verify.yml'
def labels(p):return set(re.findall(r'\\label\{([^}]+)\}',p.read_text()))
def cites(p):return set(sum((x.split(',') for x in re.findall(r'\\cite\{([^}]+)\}',p.read_text())),[]))
class Paper(unittest.TestCase):
 def test_alignment(self):
  self.assertEqual(labels(IT),labels(EN));self.assertGreaterEqual(len(labels(IT)),12);self.assertEqual(cites(IT),cites(EN));self.assertTrue({'Bonnor1995','MaartensBassett1998','PelavasEtAl2005'}<=cites(IT))
 def test_status(self):
  for p in (IT,EN):
   t=p.read_text()
   for x in ['UNPROVEN','NON\\_IDENTIFIABLE','FRAME\\_UNRESOLVED','NO\\_POSITIVE\\_DETECTION\\_CLAIM','SUPERSEDED\\_AS\\_CORE']:self.assertIn(x,t)
   self.assertIn(r'a^\mu=0',t);self.assertIn(r'F_0',t)
 def test_ci(self):
  t=CI.read_text();self.assertIn('papers/spacetime-foundations/it',t);self.assertIn('papers/spacetime-foundations/en',t);self.assertIn('spacetime-foundations-it.pdf',t);self.assertIn('spacetime-foundations-en.pdf',t)
if __name__=='__main__':unittest.main()
