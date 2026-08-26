import importlib.util,json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];S=ROOT/'studies'/'spacetime';TOOL=S/'exact_cases.py';IN=S/'exact-cases.json';OUT=S/'exact-case-results.json'
def mod():
 spec=importlib.util.spec_from_file_location('exact',TOOL);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class Exact(unittest.TestCase):
 def test_minkowski_zero(self):
  r=mod().minkowski(ell=2);self.assertEqual([0.0]*6,r['raw_vector']);self.assertEqual(0,r['C_2']);self.assertEqual(0,r['C_infinity']);self.assertEqual('NULL_CONTROL',r['status'])
 def test_flrw_tidal_normalization(self):
  r=mod().flrw(ell=2,addot_over_a=-0.25,frame='COSMOLOGICAL_FLUID');self.assertAlmostEqual((3*(4*.25)**2)**.5,r['R_tidal']);self.assertEqual(0,r['R_mag']);self.assertEqual('FRAME_RESOLVED',r['frame_status'])
 def test_schwarzschild_tidal_eigenvalues(self):
  r=mod().schwarzschild(ell=2,mu_over_r3=.125,frame='STATIC_ORTHONORMAL');self.assertEqual([-0.25,0.125,0.125],r['tidal_eigenvalues']);self.assertAlmostEqual((.25**2+.125**2+.125**2)**.5*4,r['R_tidal']);self.assertEqual(0,r['R_mag'])
 def test_vsi_nonzero_operational_despite_zero_scalars(self):
  r=mod().vsi_wave(ell=2,wave_amplitude_per_l2=.1,frame='PREREGISTERED_TIMELIKE_OBSERVER');self.assertTrue(r['polynomial_scalar_invariants_zero']);self.assertGreater(r['R_tidal'],0);self.assertGreater(r['R_mag'],0);self.assertGreater(r['C_infinity'],0)
 def test_frame_unresolved_cannot_confirm(self):
  r=mod().schwarzschild(ell=1,mu_over_r3=1,frame=None);self.assertEqual('FRAME_UNRESOLVED',r['frame_status']);self.assertEqual('NOT_CONFIRMATORY',r['status'])
 def test_deterministic(self):
  x=subprocess.run(['python3',str(TOOL),'--check'],cwd=ROOT,text=True,capture_output=True);self.assertEqual(0,x.returncode,x.stderr or x.stdout);d=json.loads(OUT.read_text());self.assertEqual(['MINKOWSKI','FLRW','SCHWARZSCHILD','VSI_WAVE'],[x['case'] for x in d['cases']])
if __name__=='__main__':unittest.main()
