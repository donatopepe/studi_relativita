#!/usr/bin/env python3
import argparse,cmath,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('sphere-path-measure-results.json')
def validate(mu):
 if not mu or any(w<0 for _,w in mu) or abs(sum(w for _,w in mu)-1)>1e-12:raise ValueError('nonnegative normalized path measure required')
def circular_moment(mu):
 validate(mu);return sum(w*cmath.exp(2j*a) for a,w in mu)
def average_matrix(l1,l2,mu):
 m=circular_moment(mu);c=.5*(l1+l2);d=.5*(l1-l2);return ((c+d*m.real,d*m.imag),(d*m.imag,c-d*m.real))
def eigenvalues(l1,l2,mu):
 c=.5*(l1+l2);d=.5*abs(l1-l2)*abs(circular_moment(mu));return (c-d,c+d)
def ell0_gate(symbols):return 'PATH_MEASURE_MOMENT_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_PATH_MEASURE_SCALE_LAW'
def encode(z):return {'real':z.real,'imag':z.imag,'magnitude':abs(z)}
def evaluate():
 measures={'single':[(.7,1)],'opposite_quarter':[(0,.5),(math.pi/2,.5)],'symmetric_quarter':[(math.pi/4,.5),(-math.pi/4,.5)],'real_half':[(0,.75),(math.pi/2,.25)],'imag_half':[(math.pi/4,.75),(3*math.pi/4,.25)]}
 cases={}
 for name,mu in measures.items():cases[name]={'measure':mu,'m2':encode(circular_moment(mu)),'average_matrix':average_matrix(3,1,mu),'eigenvalues':eigenvalues(3,1,mu)}
 return {'study_id':'sphere-path-measure-v1','geometry':'constant-curvature two-sphere','average':'integral Q(alpha) D Q(alpha)^T dmu(alpha)','moment':'m2=integral exp(i2alpha)dmu(alpha)','eigenvalue_formula':'mean +- half-gap |m2|','cases':cases,'matrix_gate':'FULL_MATRIX_DEPENDS_ONLY_ON_COMPLEX_SECOND_CIRCULAR_MOMENT','spectrum_gate':'SPECTRUM_DEPENDS_ONLY_ON_SECOND_CIRCULAR_MOMENT_MAGNITUDE','null_space_gate':'HIGHER_PATH_DISTRIBUTION_DETAIL_UNIDENTIFIABLE','isotropy_gate':'M2_ZERO_MANY_PATH_MEASURES','ell0_gate':ell0_gate(['mu','K','area']),'status':'SPHERE_PATH_MEASURE_SECOND_CIRCULAR_MOMENT_ONLY_NOT_ELL0','classification':'KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact two-sphere path-angle measure algebra; no four-dimensional spacetime bitensor, physical path measure, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Sphere path-measure artifact differs',file=sys.stderr);return 1
  print('Sphere path-measure artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
