import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=ROOT/'doc/specs/2026-09-10-kerr-finite-source-analyzer.md';PLAN=ROOT/'doc/plans/2026-09-10-kerr-finite-source-analyzer.md';TODO=ROOT/'TODO.md'
class KerrFiniteSourceAnalyzerSpecTests(unittest.TestCase):
 def test_gate_is_complete_and_preregistered(self):
  text=SPEC.read_text()
  for token in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','**Objective:**','**Metric and threshold:**','threshold `8/8`','Sigma_observer=P_bar*Sigma_source*P_bar^T','J07','J14','14/14','Analyzer collision','NO_POSITIVE_DETECTION_CLAIM'):
   self.assertIn(token,text)
 def test_plan_and_todo_define_dependencies_and_tests(self):
  for text in (PLAN.read_text(),TODO.read_text()):
   for token in ('Objective','Metric','Depends on' if text==TODO.read_text() else 'Task 1','Test' if text==TODO.read_text() else 'closure'):
    self.assertIn(token,text)
if __name__=='__main__':unittest.main()
