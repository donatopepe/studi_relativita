#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('transport-average-order-results.json');A=[[3,0],[0,1]];B=[[1,0],[0,3]];Q=[[0,-1],[1,0]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(a):return [[a[j][i] for j in range(2)] for i in range(2)]
def avg(a,b):return [[(a[i][j]+b[i][j])/2 for j in range(2)] for i in range(2)]
def raw_average():return avg(A,B)
def transport_then_average():return avg(A,mm(mm(tr(Q),B),Q))
def eigenvalues(a):
 t=a[0][0]+a[1][1];d=a[0][0]*a[1][1]-a[0][1]*a[1][0];q=math.sqrt(max(0,t*t-4*d));return [round((t-q)/2,12),round((t+q)/2,12)]
def ell0_gate(symbols):return 'AVERAGING_ORDER_PROTOCOL_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_COVARIANT_FIXED_ORDER_MAP'
def evaluate():
 return {'study_id':'transport-average-order-v1','local_A':A,'local_B':B,'local_spectra':[eigenvalues(A),eigenvalues(B)],'raw_coordinate_average':{'operator':raw_average(),'spectrum':eigenvalues(raw_average()),'gate':'APPARENT_ISOTROPIZATION_FROM_FRAME_MIXING'},'transport_then_average':{'operator':transport_then_average(),'spectrum':eigenvalues(transport_then_average()),'gate':'ANISOTROPY_RECOVERED_AFTER_ALIGNMENT'},'ell0_gate':ell0_gate(['A','Q','weights']),'status':'TRANSPORT_AND_WINDOW_AVERAGING_ORDER_NONCOMMUTATIVE','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'2x2 orthogonal-frame toy; no covariant spacetime bitensor transport, path family, region measure, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Transport-average artifact differs',file=sys.stderr);return 1
  print('Transport-average artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
