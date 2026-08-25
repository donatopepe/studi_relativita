import importlib.util, json, pathlib, subprocess, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=ROOT/'studies'/'classical-dynamics'; TOOL=S/'hard_constraint_gate_check.py'; IN=S/'hard-constraint-gate-cases.json'; OUT=S/'hard-constraint-gate-results.json'; DOC=ROOT/'theory'/'classical-dynamics'/'pointwise-conditional-no-go.md'
def module():
 spec=importlib.util.spec_from_file_location('hardgate',TOOL); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
class HardConstraintGateTests(unittest.TestCase):
 def test_feasible_data_and_limit_paths(self):
  m=module()
  self.assertEqual('EMPTY_INTERSECTION',m.geodesic_intersection(1.0))
  self.assertEqual('GEODESICS_INCLUDED_AT_LIMIT_SET',m.geodesic_intersection(0.0))
  fixed=m.limit_path('fixed-positive-curvature',1e-6,1.0)
  geo=m.limit_path('geodesic',1e-6,1.0)
  active=m.limit_path('active-boundary',1e-6,1.0)
  self.assertEqual('EVENTUALLY_FEASIBLE',fixed['classification'])
  self.assertEqual('INFEASIBLE_FOR_EVERY_POSITIVE_KAPPA0',geo['classification'])
  self.assertEqual('MULTIPLIER_COEFFICIENT_SINGULAR_UNLESS_LAMBDA_SCALES',active['classification'])
 def test_gate_and_conditional_no_go(self):
  run=subprocess.run(['python3',str(TOOL),'--check'],cwd=ROOT,text=True,capture_output=True); self.assertEqual(0,run.returncode,run.stderr or run.stdout)
  data=json.loads(OUT.read_text())
  self.assertEqual('CONTRADICTED_UNDER_ASSUMPTIONS',data['candidate_a_state'])
  self.assertEqual('CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B',data['combined_result'])
  self.assertEqual('BLOCKED',data['paper_iii_gate'])
  for key in ['global_well_posedness','standard_solution_limit','equivalence_compatibility','observable_mapping']:
   self.assertIn(key,data['failed_required_checks'])
  self.assertFalse(data['all_umch_falsified'])
 def test_document_scope(self):
  text=DOC.read_text()
  for token in ['CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B','Candidate A','Candidate B','BLOCKED','UNPROVEN','does not exclude','ALTERNATIVE_HYPOTHESIS']:
   self.assertIn(token,text)
  self.assertNotIn('all UMCH is false',text)
if __name__=='__main__': unittest.main()
