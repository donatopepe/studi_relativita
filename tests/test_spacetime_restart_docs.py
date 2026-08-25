import pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
HIST=ROOT/'archive'/'worldline-program'/'README.md'
THEORY=ROOT/'theory'/'spacetime'
FILES=['hypothesis.md','admissible-regions.md','physical-frame.md','response-vector.md','threshold-families.md','limiting-cases.md','open-problems.md']
class RestartDocs(unittest.TestCase):
 def test_history_is_preserved_and_superseded(self):
  t=HIST.read_text();self.assertIn('HISTORICAL_WORLDLINE_FORMULATION',t);self.assertIn('SUPERSEDED_AS_CORE',t);self.assertIn('CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B',t);self.assertIn('not deleted',t.lower())
 def test_core_documents_exist_and_no_force_is_explicit(self):
  for f in FILES:self.assertTrue((THEORY/f).is_file(),f)
  t=(THEORY/'hypothesis.md').read_text();self.assertIn('a^μ=0',t);self.assertIn('no reaction force',t.lower());self.assertIn('ℓ≥ℓ₀',t);self.assertIn('UNPROVEN',t)
 def test_frame_and_response_contracts(self):
  f=(THEORY/'physical-frame.md').read_text();self.assertIn('T^μ',f);self.assertIn('CMB',f);self.assertIn('FRAME_UNRESOLVED',f)
  r=(THEORY/'response-vector.md').read_text();
  for x in ['R_tidal','R_mag','R_hol','R_clock','R_null','R_cong','C_2','C_infinity']:self.assertIn(x,r)
  self.assertIn('raw vector',r.lower())
 def test_thresholds_include_null_and_preregistered_families(self):
  t=(THEORY/'threshold-families.md').read_text()
  for x in ['F_0','F_P','F_E','F_PE','no post-data']:self.assertIn(x,t)
if __name__=='__main__':unittest.main()
