import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class PhotonOrbitReports(unittest.TestCase):
 def test_bilingual_reports_match_scientific_contract(self):
  en=(R/'audit/schwarzschild-photon-orbit-holonomy-report-en.md').read_text();it=(R/'audit/schwarzschild-photon-orbit-holonomy-report-it.md').read_text()
  shared=('UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0','FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT','PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED','18.84955592','148.8621186','464.9166525','NOT_DECLARED','Darwin1959GravityField')
  for x in shared:self.assertIn(x,en);self.assertIn(x,it)
  for x in ('future null photon orbit','past-directed static closure','path ordering is not an independent channel','winding is a discrete protocol label','geometric scale blindness'):
   self.assertIn(x,en)
  for x in ('orbita fotonica nulla futura','chiusura statica orientata al passato','path ordering non è un canale indipendente','winding è una label discreta di protocollo','cecità alla scala geometrica'):
   self.assertIn(x,it)
 def test_theory_and_roadmap_preserve_scope(self):
  t=(R/'theory/spacetime/schwarzschild-photon-orbit-holonomy.md').read_text();road=(R/'docs/roadmap.md').read_text()
  for x in ('r_ph = 3M','Delta tau = 6 pi M','H_photon','batched winding','not detector-derived','ell0_identified = false'):self.assertIn(x,t)
  self.assertIn('photon-orbit holonomy',road)
if __name__=='__main__':unittest.main()
