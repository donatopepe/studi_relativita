#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('finite-holonomy-ordering-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def distance(a,b):return math.sqrt(sum(x*x for row in sub(a,b) for x in row))
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0];return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def segments(t):return [[1,t],[0,1]],[[1,0],[t,1]]
def invariants(a):
 tr=a[0][0]+a[1][1];det=a[0][0]*a[1][1]-a[0][1]*a[1][0];disc=max(0,tr*tr-4*det);d=math.sqrt(disc);return {'trace':round(tr,12),'determinant':round(det,12),'eigenvalues':[round((tr-d)/2,12),round((tr+d)/2,12)]}
def ell0_gate(symbols):return 'FINITE_LOOP_GEOMETRY_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_LOOP_MAP'
def evaluate():
 a,b=segments(.2);ab=mm(a,b);ba=mm(b,a)
 return {'study_id':'finite-holonomy-ordering-v1','parameter':.2,'AB':ab,'BA':ba,'raw_order_distance':distance(ab,ba),'AB_invariants':invariants(ab),'BA_invariants':invariants(ba),'similarity_residual':distance(mm(mm(inv(a),ab),a),ba),'ell0_gate':ell0_gate(['t','X','Y','path']),'status':'FINITE_HOLONOMY_RAW_ORDER_DIFF_CONJUGACY_AMBIGUOUS','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Invertible 2x2 segment-map toy; not connection-derived holonomy, exact geometry, observation, or UMCH mechanism.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Finite holonomy artifact differs',file=sys.stderr);return 1
  print('Finite holonomy artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
