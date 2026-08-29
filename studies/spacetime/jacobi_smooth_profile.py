#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-smooth-profile-results.json')
def integrate(f,S,n=20000):
 if S<=0 or n<=0:raise ValueError('positive S and n required')
 h=S/n;return h*(.5*f(0)+sum(f(i*h) for i in range(1,n))+.5*f(S))
def uniform(t,S):return 1/S
def beta22(t,S):return 6*t*(S-t)/S**3
def weighted(f,S):return integrate(lambda t:(S-t)*t*f(t),S)
def first_endpoint(f,S,epsilon):return S-epsilon*weighted(f,S)
def ell0_gate(symbols):return 'SMOOTH_OPTICAL_PROFILE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_OPTICAL_PROFILE_LAW'
def evaluate():
 S=2;e=.1;wu=weighted(lambda t:uniform(t,S),S);wb=weighted(lambda t:beta22(t,S),S)
 return {'study_id':'jacobi-smooth-profile-v1','equation':'d_second+epsilon f(s)d=0','boundary':['d(0)=0','d_prime(0)=1'],'observer':S,'epsilon':e,'profiles':{'uniform':{'integral':integrate(lambda t:uniform(t,S),S),'weighted_moment':wu,'first_order_endpoint':first_endpoint(lambda t:uniform(t,S),S,e)},'beta22':{'integral':integrate(lambda t:beta22(t,S),S),'weighted_moment':wb,'first_order_endpoint':first_endpoint(lambda t:beta22(t,S),S,e)}},'analytic_weighted_moments':['S^2/6','S^2/5'],'analytic_endpoint_difference':'epsilon S^2/30','sufficiency_gate':'INTEGRATED_STRENGTH_INSUFFICIENT_WEIGHTED_PROFILE_MOMENT_REQUIRED_AT_FIRST_ORDER','reflection_gate':'VERTEX_OBSERVER_KERNEL_REFLECTION_DEGENERACY','ell0_gate':ell0_gate(['epsilon','f','S']),'status':'JACOBI_SMOOTH_EQUAL_INTEGRAL_DIFFERENT_WEIGHTED_ENDPOINT_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'First-order scalar perturbation with fixed affine interval and vertex data; no exact finite-epsilon matrix Sachs system, spacetime derivation, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi smooth-profile artifact differs',file=sys.stderr);return 1
  print('Jacobi smooth-profile artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
