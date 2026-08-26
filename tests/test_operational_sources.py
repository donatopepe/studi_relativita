import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];B=ROOT/'references'/'library.bib';L=ROOT/'references'/'verification-log.md';D=ROOT/'theory'/'spacetime'/'operational-protocols.md'
REQ={'PetitWolf2005':'10.1088/0026-1394/42/3/S14','Raychaudhuri1955':'10.1103/PhysRev.98.1123','Sachs1961':'10.1098/rspa.1961.0202'}
class Sources(unittest.TestCase):
 def test_entries(self):
  b=B.read_text()
  for k,d in REQ.items():self.assertIn('@article{'+k+',',b);self.assertIn('doi = {'+d+'}',b)
 def test_verification_scope(self):
  t=L.read_text()
  for k,d in REQ.items():
   self.assertIn('## '+k,t);s=t.split('## '+k,1)[1].split('\n## ',1)[0]
   for x in ['VERIFIED_METADATA_AND_SCOPE','Canonical metadata:','Exact supported topic:','Limits:','does not establish']:self.assertIn(x,s)
 def test_theory_citations_and_limits(self):
  t=D.read_text()
  for k in REQ:self.assertIn(k,t)
  self.assertIn('do not establish UMCH',t)
if __name__=='__main__':unittest.main()
