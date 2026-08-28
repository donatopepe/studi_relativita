#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-thin-lens-results.json')
def validate(k,a):
 if k<=0 or a<=0:raise ValueError('k and a must be positive')
def post_slope(k,a):validate(k,a);return 1-k*a
def solution(s,k,a):
 validate(k,a)
 if s<0:raise ValueError('s must be nonnegative')
 return s if s<=a else a+post_slope(k,a)*(s-a)
def endpoint(S,k,a):
 if S<=a:raise ValueError('observer must be after lens')
 return solution(S,k,a)
def caustic(k,a):
 validate(k,a)
 return a+a/(k*a-1) if k*a>1 else None
def ell0_gate(symbols):return 'ORDERED_OPTICAL_PROFILE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_OPTICAL_PROFILE_LAW'
def evaluate():
 k=2;S=5;locations=[.25,.75,1,2,4]
 return {'study_id':'jacobi-thin-lens-v1','equation':'d_second+k delta(s-a)d=0','boundary':'d(0)=0,d_prime(0)=1','integrated_strength':k,'observer':S,'cases':[{'a':a,'post_slope':post_slope(k,a),'endpoint':endpoint(S,k,a),'caustic':caustic(k,a)} for a in locations],'profile_gate':'SAME_INTEGRATED_STRENGTH_DIFFERENT_ENDPOINT_AND_CAUSTIC','ell0_gate':ell0_gate(['k','a','S']),'status':'JACOBI_INTEGRATED_FOCUSING_INSUFFICIENT_PROFILE_LOCATION_REQUIRED','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Idealized scalar distributional thin lens; no smooth exact spacetime, matrix screen transport, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi thin-lens artifact differs',file=sys.stderr);return 1
  print('Jacobi thin-lens artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
