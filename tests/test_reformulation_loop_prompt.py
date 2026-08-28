import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];P=R/'prompts'/'scientific-research-reformulation-loop.md';S=R/'doc'/'specs'/'2026-08-28-reformulation-engineering-loop.md'
class Prompt(unittest.TestCase):
 def test_safeguards(self):
  for p in (P,S):
   t=p.read_text()
   for x in ['UNPROVEN','counterexample','worktree','bilingual','history','dead-end','reformulation','human ratification','Do not auto-merge' if p==S else 'DO NOT auto-merge']:self.assertIn(x.lower(),t.lower())
 def test_statuses(self):
  t=P.read_text();self.assertIn('STRUCTURAL_DEAD_END_CANDIDATE',t);self.assertIn('REFORMULATION_CANDIDATE_UNRATIFIED',t);self.assertIn('F_0',t);self.assertIn('operator-valued',t);self.assertIn('cancel loop',t)
if __name__=='__main__':unittest.main()
