import pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1];IT=R/'papers'/'umch'/'it'/'main.tex';EN=R/'papers'/'umch'/'en'/'main.tex';PROMPT=R/'prompts'/'scientific-research-autoevolution.md';CI=R/'.github'/'workflows'/'verify.yml'
def labels(p):return set(re.findall(r'\\label\{([^}]+)\}',p.read_text()))
def claims(p):return set(re.findall(r'UMCH-U-\d{4}',p.read_text()))
def cites(p):return set(sum((x.split(',') for x in re.findall(r'\\cite\{([^}]+)\}',p.read_text())),[]))
class Unified(unittest.TestCase):
 def test_bilingual_alignment(self):
  self.assertEqual(labels(IT),labels(EN));self.assertGreaterEqual(len(labels(IT)),16);self.assertEqual(claims(IT),claims(EN));self.assertGreaterEqual(len(claims(IT)),12);self.assertEqual(cites(IT),cites(EN))
 def test_scientific_ledger(self):
  for p in (IT,EN):
   t=p.read_text()
   for x in ['UNPROVEN','SUPERSEDED_AS_CORE','CONTRADICTED_UNDER_ASSUMPTIONS','FRAME_UNRESOLVED','ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES','MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY','BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM','NO_POSITIVE_DETECTION_CLAIM',r'a^\mu=0',r'F_0',r'F_T']:self.assertIn(x,t)
 def test_prompt_safeguards(self):
  t=PROMPT.read_text()
  for x in ['UNPROVEN','canonical','counterexample','identifiability','bilingual','worktree','test-first','Hermes','Do not invent','Stop conditions','raw response vector','F_0'] :self.assertIn(x,t)
 def test_ci(self):
  t=CI.read_text();self.assertIn('papers/umch/it',t);self.assertIn('papers/umch/en',t);self.assertIn('umch-unified-it.pdf',t);self.assertIn('umch-unified-en.pdf',t)
if __name__=='__main__':unittest.main()
