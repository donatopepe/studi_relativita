import importlib.util,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
RULES=ROOT/'docs/STANDARD_RULES.md'
VALIDATOR=ROOT/'tools/validate_text_utf8.py'
SPEC=importlib.util.spec_from_file_location('utf8_validator',VALIDATOR);validator=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(validator)
class StandardProjectRulesTests(unittest.TestCase):
 def test_rules_copy_covers_global_contract(self):
  text=RULES.read_text(encoding='utf-8')
  for token in ('primary `main` checkout','CodeGraph','single `TODO.md`','dependencies, order, completion criteria and tests','reread global memory rules','smallest useful MVP','no subagents','root cause','commit immediately','scenario matrix','total, scenario, and category','UTF-8','Never store secrets','full tests','project memory'):
   self.assertIn(token,text)
 def test_changed_governance_files_are_clean_utf8(self):
  failures=validator.validate([RULES,ROOT/'TODO.md',VALIDATOR,ROOT/'doc/specs/2026-09-10-kerr-jacobi-tidal-gate.md',ROOT/'doc/plans/2026-09-10-kerr-jacobi-tidal-gate.md',ROOT/'studies/spacetime/kerr-jacobi-scenarios.json'])
  self.assertEqual(failures,[])
if __name__=='__main__':unittest.main()
