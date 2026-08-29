import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
FILES=[ROOT/'theory/spacetime/einstein-static-spatial-holonomy.md',ROOT/'audit/einstein-static-spatial-holonomy-report-en.md',ROOT/'audit/einstein-static-spatial-holonomy-report-it.md']
SHARED=['EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','EXACT_EINSTEIN_STATIC_SPATIAL_LEVI_CIVITA_HOLONOMY_NONABELIAN_RAW_ORDER_DEPENDENT_WINDOW_EXPONENTIAL_AND_CURVATURE_RADIUS_SCALE_BLIND_NOT_ELL0','FOUR_DIMENSIONAL_PRODUCT_SPACETIME_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_SPACELIKE_GEODESIC_TRIANGLES_NOT_DETECTOR_DERIVED','PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED','W_T=E J_ij','H_ij=exp(W_T)','UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ell0_identified=false','structural_dead_end=NOT_DECLARED','0.04264790744435022','0.2119332164995163']
class ReportTests(unittest.TestCase):
 def test_files_exist_and_share_authoritative_labels(self):
  for p in FILES:
   self.assertTrue(p.exists(),p)
   text=p.read_text()
   for token in SHARED:self.assertIn(token,text,(p,token))
 def test_audits_state_nonclaims_and_source_limits(self):
  for p in FILES[1:]:
   t=p.read_text()
   for token in ('non-Abelian','dependent channel','scale orbit','causal','detector','Gauss--Bonnet','do not establish'):
    self.assertIn(token,t,(p,token))
 def test_language_specific_authority(self):
  en=FILES[1].read_text();it=FILES[2].read_text()
  self.assertIn('Equal-excess shapes',en);self.assertIn('Forme a eccesso uguale',it)
  self.assertIn('No structural dead end',en);self.assertIn('Nessun vicolo cieco strutturale',it)
if __name__=='__main__':unittest.main()
