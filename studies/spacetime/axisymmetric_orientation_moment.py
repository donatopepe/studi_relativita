#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('axisymmetric-orientation-moment-results.json')
def average(mu2):
 if mu2<0 or mu2>1:raise ValueError('mu2 must lie in [0,1]')
 a=(3*mu2-1)/2;z=1-3*mu2
 if abs(a)<1e-12:a=0.0
 if abs(z)<1e-12:z=0.0
 return [[a,0,0],[0,a,0],[0,0,z]]
def moment_of_discrete(points):
 total=sum(w for _,w in points)
 if total<=0:raise ValueError('positive total weight required')
 if any(w<0 or u<0 or u>1 for u,w in points):raise ValueError('invalid discrete measure')
 return sum(u*w for u,w in points)/total
def average_from_measure(points):return average(moment_of_discrete(points))
def projective_spectrum(a):
 d=[a[i][i] for i in range(3)];n=sum(abs(x) for x in d)
 return None if n==0 else sorted(round(x/n,12) for x in d)
def ell0_gate(symbols):return 'ORIENTATION_SECOND_MOMENT_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_COVARIANT_MEASURE_LAW'
def evaluate():
 collision_a=[(1,.5),(0,.5)];collision_b=[(.5,1)]
 return {'study_id':'axisymmetric-orientation-moment-v1','pattern':'E(n)=I-3nn^T','average_formula':'diag((3mu2-1)/2,(3mu2-1)/2,1-3mu2)','cases':[{'mu2':m,'operator':average(m),'projective_spectrum':projective_spectrum(average(m))} for m in [0,.1,1/3,.5,.8,1]],'measure_collision':{'measure_a':collision_a,'measure_b':collision_b,'shared_mu2':moment_of_discrete(collision_a),'shared_operator':average_from_measure(collision_a),'gate':'DISTINCT_MEASURES_SAME_SECOND_MOMENT_IDENTICAL_AVERAGE'},'zero_gate':'MU2_ONE_THIRD_ZERO_SIGNED_RAY_REVERSAL','ell0_gate':ell0_gate(['mu2']),'status':'AXISYMMETRIC_ORIENTATION_AVERAGE_SECOND_MOMENT_ONLY_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Axisymmetric probability-measure theorem for algebraic pattern after common-space alignment; no Schwarzschild transport, radial amplitude, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Axisymmetric moment artifact differs',file=sys.stderr);return 1
  print('Axisymmetric moment artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
