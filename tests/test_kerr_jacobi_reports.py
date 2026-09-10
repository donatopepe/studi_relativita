import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
EN=ROOT/'audit/kerr-jacobi-tidal-gate-report-en.md';IT=ROOT/'audit/kerr-jacobi-tidal-gate-report-it.md';THEORY=ROOT/'theory/spacetime/kerr-jacobi-tidal-gate.md';ROADMAP=ROOT/'docs/roadmap.md';LEDGER=ROOT/'audit/kaluza-klein-reformulation-change-ledger.md';ARTIFACT=ROOT/'studies/spacetime/kerr-jacobi-tidal-gate-results.json'
RESULT='KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION_SENSITIVE_FOCUSING_AND_SHEAR_BEYOND_IDENTITY_SCREEN_QUOTIENT_BUT_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0'
GATE='PHYSICAL_KERR_JACOBI_SOURCE_SIZE_PROFILE_SCREEN_PREPARATION_POLARIZATION_ANALYZER_CAUSTIC_CONTINUATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
class KerrJacobiReports(unittest.TestCase):
 def test_bilingual_status(self):
  for text in (EN.read_text(),IT.read_text()):
   for token in (RESULT,GATE,'8/8','DIRECT_REVIEW_NO_SUBAGENT','UMCH=UNPROVEN_SECONDARY_CANDIDATE','ell0_identified=false','NO_POSITIVE_DETECTION_CLAIM','MODEL_LEVEL_KERR_JACOBI_CONFORMANCE_NOT_EVIDENCE'):self.assertIn(token,text)
 def test_values_match_artifact(self):
  x=json.loads(ARTIFACT.read_text());self.assertEqual(x['control_summary']['controls_passed'],8)
  for text in (EN.read_text(),IT.read_text()):
   for token in ('P_00=-1.8555935','P_02=-8.7010491','P_11=7.4061706','P_13=95.431407','orientation_phase_difference=297.70811','Schwarzschild_phase_residual=2.6279542e-06','scale_residual=0.0','scenario_battery=6/6'):self.assertIn(token,text)
 def test_theory_and_history(self):
  for token in ('BoeroMoreschi2020KerrOpticalScalars','K_screen=diag(-A,+A)','A=3*M*(xi-a)^2/r^5','FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS','identity screen quotient',RESULT,GATE):self.assertIn(token,THEORY.read_text())
  for text in (ROADMAP.read_text(),LEDGER.read_text()):
   for token in (RESULT,GATE,'KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT','KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS','DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J','F_0'):self.assertIn(token,text)
if __name__=='__main__':unittest.main()
