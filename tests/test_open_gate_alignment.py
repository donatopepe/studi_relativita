import csv,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];O=R/'theory'/'spacetime'/'open-problems.md';ROAD=R/'docs'/'roadmap.md';IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex';A=R/'audit'/'unified-assumptions.csv'
OPEN=['UMCH-A-0003','UMCH-A-0004','UMCH-A-0005','UMCH-A-0008','UMCH-A-0010','UMCH-A-0011','UMCH-A-0012']
class OpenGates(unittest.TestCase):
 def test_ids_and_stop_gate(self):
  for p in (O,ROAD,IT,EN):
   t=p.read_text()
   for x in OPEN:self.assertIn(x,t)
   self.assertIn('EXTERNAL_EVIDENCE_REQUIRED',t);self.assertIn('HUMAN_REVIEW_REQUIRED',t)
 def test_register_still_unresolved(self):
  with A.open() as f:r={x['assumption_id']:x for x in csv.DictReader(f)}
  for x in OPEN:self.assertNotIn(r[x]['status'],['CORRECTED_PROTOCOL_RULE','RATIFIED_SCOPE'])
if __name__=='__main__':unittest.main()
