import json,pathlib,subprocess,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'studies'/'spacetime'/'q_mechanism_survey.py';O=R/'studies'/'spacetime'/'q-mechanism-results.json';B=R/'references'/'library.bib';L=R/'references'/'verification-log.md'
class Survey(unittest.TestCase):
 def test_sources(self):
  b=B.read_text();l=L.read_text()
  for k,d in [('Hinterbichler2012','10.1103/RevModPhys.84.671'),('BiswasEtAl2012','10.1103/PhysRevLett.108.031101'),('BarvinskyVilkovisky1990','10.1016/0550-3213(90)90047-H')]:self.assertIn('@article{'+k+',',b);self.assertIn('doi = {'+d+'}',b);self.assertIn('## '+k,l);self.assertIn('does not establish',l.split('## '+k,1)[1].split('\n## ',1)[0])
 def test_result(self):
  r=subprocess.run(['python3',str(P),'--check'],cwd=R,text=True,capture_output=True);self.assertEqual(0,r.returncode,r.stderr or r.stdout);d=json.loads(O.read_text());self.assertEqual('NO_MODEL_INDEPENDENT_Q_DERIVATION_FOUND',d['status']);self.assertEqual('EXTERNAL_EVIDENCE_REQUIRED',d['gate']);self.assertEqual('NO_POSITIVE_DETECTION_CLAIM',d['conclusion'])
if __name__=='__main__':unittest.main()
