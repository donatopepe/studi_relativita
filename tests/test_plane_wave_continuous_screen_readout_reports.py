import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];EN=ROOT/'audit/plane-wave-continuous-screen-readout-report-en.md';IT=ROOT/'audit/plane-wave-continuous-screen-readout-report-it.md';THEORY=ROOT/'theory/spacetime/plane-wave-continuous-screen-readout.md'
TOKENS=['EXACT_SPACETIME_CONTINUOUS_SCREEN_READOUT_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','EXACT_PLANE_WAVE_CONTINUOUS_CANONICAL_SCREEN_HISTORY_LOCAL_GAUGE_EQUIVALENT_RAW_VELOCITY_HISTORY_CALIBRATION_DEPENDENT_NOT_ELL0','PHYSICAL_CONTINUOUS_TETRAD_READOUT_LOCAL_SCREEN_GAUGE_CAUSAL_SAMPLING_AND_ELL0_LAW_NOT_DERIVED','K,omega_i,Q_i,A_i,P_inertial(u),P_canonical_i(u),P_velocity_i(u),G_21(u),L','0.06888558039493263','0.18058782579069355','5.098567434843205e-16','6.397467560108161e-16','2.8053161131044195e-14','10.1088/0264-9381/29/23/235023','UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','NOT_DECLARED']
class ReportTests(unittest.TestCase):
 def test_authority_tokens_align(self):
  texts=[p.read_text() for p in (EN,IT,THEORY)]
  for token in TOKENS:
   for text in texts:self.assertIn(token,text)
 def test_no_positive_claim(self):
  for p in (EN,IT,THEORY):self.assertNotRegex(p.read_text().lower(),r'positive detection|rilevazione positiva')
if __name__=='__main__':unittest.main()
