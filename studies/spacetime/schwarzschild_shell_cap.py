#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('schwarzschild-shell-cap-results.json')
def uniform_radial_moment(r1,r2,mass=1):
 if mass<=0 or r1<=0 or r2<=r1:raise ValueError('positive mass and ordered positive shell required')
 return mass*(1/(2*r1*r1)-1/(2*r2*r2))/(r2-r1)
def cap_pattern(c):
 if c < -1 or c > 1:raise ValueError('cosine boundary must lie in [-1,1]')
 a=(c+c*c)/2
 return (a,a,-2*a)
def shell_cap(radial_moment,c):
 if radial_moment<=0:raise ValueError('positive radial moment required')
 return tuple(radial_moment*x for x in cap_pattern(c))
def hemisphere_crossing(rate):
 if rate<=0:raise ValueError('positive cap expansion rate required')
 return math.pi/(2*rate)
def ell0_gate(symbols):return 'SCHWARZSCHILD_SHELL_CAP_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_COVARIANT_WINDOW_LAW'
def evaluate():
 shells=[]
 for r1,r2 in [(2,3),(2,4),(4,8)]:
  u=uniform_radial_moment(r1,r2);shells.append({'r1':r1,'r2':r2,'radial_moment':u,'cap_c_0_5':shell_cap(u,.5),'hemisphere':shell_cap(u,0),'cap_c_minus_0_5':shell_cap(u,-.5)})
 return {'study_id':'schwarzschild-shell-cap-v1','field':'E(r,n)=m r^-3 (I-3nn^T)','measure':'product radial shell density times uniform angular cap','factorization':'Ebar=<m/r^3> diag((c+c^2)/2,(c+c^2)/2,-c-c^2)','shells':shells,'radial_gate':'POSITIVE_RADIAL_SHELL_CHANGES_AMPLITUDE_ONLY','boundary_gate':'HEMISPHERE_ZERO_AND_SIGN_REVERSAL_CAP_CONTROLLED','scale_gate':'FREE_CAP_EXPANSION_RATE_MOVES_HEMISPHERE_CROSSING','transport_gate':'COMMON_SPACE_ALIGNMENT_ASSUMED_NOT_SCHWARZSCHILD_PARALLEL_TRANSPORT','ell0_gate':ell0_gate(['r','theta','m']),'status':'SCHWARZSCHILD_PRODUCT_SHELL_CAP_REMAINS_FACTORABLE_NOT_ELL0','classification':'EXACT_PATTERN_WINDOW_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact algebraic Schwarzschild tidal field under product measure and assumed Euclidean tangent-space alignment; not covariant bitensor transport, causal spacetime window, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Schwarzschild shell-cap artifact differs',file=sys.stderr);return 1
  print('Schwarzschild shell-cap artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
