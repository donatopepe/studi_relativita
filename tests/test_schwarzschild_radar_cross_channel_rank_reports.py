import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class Reports(unittest.TestCase):
 def test_bilingual_reports_match_contract(self):
  en=(R/'audit/schwarzschild-radar-cross-channel-rank-report-en.md').read_text();it=(R/'audit/schwarzschild-radar-cross-channel-rank-report-it.md').read_text()
  shared=('UNPROVEN','NO_POSITIVE_DETECTION_CLAIM','ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0','SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE','PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED','0.24720445606033067','0.05792048249378249','0.009280233527716465','0.00017366826156943785','NOT_DECLARED')
  for x in shared:self.assertIn(x,en);self.assertIn(x,it)
  for x in ('local rank is not channel independence','global collision','absolute scale','ideal mirror','Lin2020RadarCoordinates'):self.assertIn(x,en)
  for x in ('rango locale non è indipendenza dei canali','collisione globale','scala assoluta','specchio ideale','Lin2020RadarCoordinates'):self.assertIn(x,it)
 def test_theory_and_roadmap_are_bounded(self):
  t=(R/'theory/spacetime/schwarzschild-radar-cross-channel-rank.md').read_text();road=(R/'docs/roadmap.md').read_text();self.assertIn('rank_raw = 2',t);self.assertIn('orientation quotient',t);self.assertIn('not a detector-derived covariance model',t);self.assertIn('radar cross-channel rank',road)
if __name__=='__main__':unittest.main()
