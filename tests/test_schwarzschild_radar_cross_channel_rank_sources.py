import pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];B=(R/'references/library.bib').read_text();L=(R/'references/verification-log.md').read_text()
class RankSources(unittest.TestCase):
 def test_existing_canonical_geometry_and_radar_sources_remain_registered(self):
  for key in ('Schwarzschild2003Translation','AmbroseSinger1953','Lin2020RadarCoordinates'):self.assertIn('{'+key+',',B);self.assertIn('## '+key,L)
 def test_sources_do_not_support_project_rank_claims(self):
  for token in ('cross-channel independence','endpoint rank','detector covariance','global injectivity','absolute-scale recovery','ell0','UMCH','detection'):self.assertIn(token,L)
if __name__=='__main__':unittest.main()
