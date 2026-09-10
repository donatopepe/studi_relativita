import pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];SPEC=ROOT/'doc/specs/2026-09-10-kerr-receiver-noise-likelihood.md';BIB=ROOT/'references/library.bib';LOG=ROOT/'references/verification-log.md';TODO=ROOT/'TODO.md'
class ReceiverSpecSources(unittest.TestCase):
 def test_spec_and_todo(self):
  text=SPEC.read_text()
  for x in ('RATIFIED_FOR_IMPLEMENTATION_PLANNING','threshold:** exactly `8/8`','J15','J22','22/22','D_KL','Calibration nuisance collision','NO_POSITIVE_DETECTION_CLAIM'):self.assertIn(x,text)
  self.assertIn('Kerr calibrated receiver/noise likelihood MVP',TODO.read_text())
 def test_sources(self):
  bib=BIB.read_text();log=LOG.read_text()
  for x in ('@article{KullbackLeibler1951','10.1214/aoms/1177729694','@misc{NISTMultivariateNormal'):self.assertIn(x,bib)
  for heading in ('## KullbackLeibler1951','## NISTMultivariateNormal'):
   self.assertIn(heading,log)
  section=log.split('## KullbackLeibler1951',1)[1]
  for x in ('information divergence','does not establish the Kerr receiver','ell0','detection'):self.assertIn(x,section)
if __name__=='__main__':unittest.main()
