import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];FILES=[ROOT/'audit/plane-wave-screen-connection-holonomy-report-en.md',ROOT/'audit/plane-wave-screen-connection-holonomy-report-it.md',ROOT/'theory/spacetime/plane-wave-screen-connection-holonomy.md']
TOKENS=['EXACT_SPACETIME_SCREEN_CONNECTION_HOLONOMY_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','EXACT_PLANE_WAVE_SO2_SCREEN_HOLONOMY_ENDPOINT_MATCHED_AND_TRACE_SIGN_WINDING_ALIASED_CANONICAL_LOOP_NOT_INDEPENDENT_NOT_ELL0','PHYSICAL_SPACETIME_CONNECTION_LOOP_FAMILY_ANCHOR_BRANCH_PARITY_READOUT_AND_ELL0_LAW_NOT_DERIVED','omega_i,A_i,U_i(u),theta_i(u),trace_i(u),spectrum_i(u),H_21,P_canonical_loop,L','PRESCRIBED_SO2_SCREEN_CONNECTION_NOT_FOUR_DIMENSIONAL_LEVI_CIVITA_LOOP','6.840271371877088e-15','0.04595991799966567','7.143920687011176e-15','2.593513125236196e-16','1.8861921643140505','2.220446049250313e-16','6.7023824694539325e-15','10.1088/0264-9381/29/23/235023','UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','NOT_DECLARED']
class ReportTests(unittest.TestCase):
 def test_semantic_authority_tokens_align(self):
  texts=[p.read_text() for p in FILES]
  for token in TOKENS:
   for text in texts:self.assertIn(token,text)
 def test_scope_rejects_detection(self):
  for p in FILES:self.assertNotIn('POSITIVE_DETECTION_CLAIM',p.read_text().replace('NO_POSITIVE_DETECTION_CLAIM',''))
if __name__=='__main__':unittest.main()
