import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];B=ROOT/'references'/'library.bib';L=ROOT/'references'/'verification-log.md'
REQ={'Bonnor1995':'10.1088/0264-9381/12/2/018','MaartensBassett1998':'10.1088/0264-9381/15/3/018','PelavasEtAl2005':'10.1063/1.1904707'}
class Biblio(unittest.TestCase):
 def test_entries(self):
  b=B.read_text()
  for k,d in REQ.items():self.assertIn('@article{'+k+',',b);self.assertIn('doi = {'+d+'}',b)
 def test_scope(self):
  t=L.read_text()
  for k,d in REQ.items():
   self.assertIn('## '+k,t);s=t.split('## '+k,1)[1].split('\n## ',1)[0];self.assertIn('Canonical metadata:',s);self.assertIn('Exact supported topic:',s);self.assertIn('Limits:',s);self.assertIn('does not establish',s)
if __name__=='__main__':unittest.main()
