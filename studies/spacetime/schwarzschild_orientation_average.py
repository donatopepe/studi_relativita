#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('schwarzschild-orientation-average-results.json')
def average(theta):
 if theta<0 or theta>math.pi:raise ValueError('theta must lie in [0,pi]')
 c=math.cos(theta);a=(c+c*c)/2;z=-c-c*c
 if abs(a)<1e-12:a=0.0
 if abs(z)<1e-12:z=0.0
 return [[a,0,0],[0,a,0],[0,0,z]]
def trace(a):return sum(a[i][i] for i in range(3))
def projective(a):
 n=sum(abs(a[i][i]) for i in range(3))
 return None if n==0 else [round(a[i][i]/n,12) for i in range(3)]
def projective_spectrum(a):
 p=projective(a);return None if p is None else sorted(p)
def ell0_gate(symbols):return 'ORIENTATION_MEASURE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_COVARIANT_REGION_LAW'
def evaluate():
 cases=[]
 for theta in [0,.2,.7,1.2,math.pi/2,2,2.8,math.pi]:
  a=average(theta);cases.append({'theta':theta,'operator':a,'trace':trace(a),'projective_spectrum':projective_spectrum(a)})
 return {'study_id':'schwarzschild-orientation-average-v1','local_pattern':'E(n)=I-3nn^T','measure':'uniform solid angle on cap 0<=theta<=Theta','analytic_average':'diag((c+c^2)/2,(c+c^2)/2,-c-c^2), c=cos(Theta)','cases':cases,'shape_gate':'FIXED_AXIAL_PATTERN_WITH_SIGN_SECTORS','zero_gate':'HEMISPHERE_ZERO_AND_SIGN_REVERSAL_FROM_ORIENTATION_DOMAIN','ell0_gate':ell0_gate(['Theta','n']),'status':'SCHWARZSCHILD_CAP_AVERAGE_SIGN_REVERSAL_ORIENTATION_DOMAIN_NOT_ELL0','classification':'EXACT_PATTERN_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact angular average of Schwarzschild algebraic pattern after assumed common-space alignment; no Schwarzschild parallel transport, radial amplitude, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Schwarzschild orientation artifact differs',file=sys.stderr);return 1
  print('Schwarzschild orientation artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
