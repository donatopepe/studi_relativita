import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex';ROAD=R/'docs'/'roadmap.md';A=R/'audit'/'unified-assumptions.csv'
REQ=['RATIFIED_PRIMARY_RESEARCH_OBJECT','OPERATOR_IDENTIFIABILITY_NOT_YET_PHYSICALLY_DERIVED','SECONDARY_PROJECTION_SPECIFIC','PROJECTIVE_NON_IDENTIFIABLE_COLLINEAR','spectral flow','holonomy']
class Align(unittest.TestCase):
 def test_papers(self):
  for p in (IT,EN):
   t=p.read_text()
   for x in REQ:self.assertIn(x,t)
 def test_roadmap(self):
  t=ROAD.read_text();self.assertIn('Operator-valued primary response',t);self.assertIn('q',t);self.assertIn('secondary',t)
 def test_assumption(self):
  t=A.read_text();self.assertIn('UMCH-A-0013',t);self.assertIn('operator/projective invariant is physically derived and injective',t);self.assertIn('NOT_YET_DERIVED',t)
if __name__=='__main__':unittest.main()
