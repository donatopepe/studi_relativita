#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-path-ordering-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def eye(n):return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def add(*xs):return [[sum(x[i][j] for x in xs) for j in range(len(xs[0][0]))] for i in range(len(xs[0]))]
def scale(c,a):return [[c*x for x in row] for row in a]
def norm(a):return math.sqrt(sum(x*x for row in a for x in row))
def generator(k):return [[0,0,1,0],[0,0,0,1],[-k[0][0],-k[0][1],0,0],[-k[1][0],-k[1][1],0,0]]
def segment(k,h):
 g=generator(k);return add(eye(4),scale(h,g),scale(h*h/2,mm(g,g)))
def path(first,second,h):return mm(segment(second,h),segment(first,h))
def distance(a,b):return norm(sub(a,b))
def commutator_norm(a,b):return norm(sub(mm(a,b),mm(b,a)))
def spectrum(a):
 tr=a[0][0]+a[1][1];det=a[0][0]*a[1][1]-a[0][1]*a[1][0];d=math.sqrt(max(0,tr*tr-4*det));return [round((tr-d)/2,12),round((tr+d)/2,12)]
def ell0_gate(symbols):return 'ORDERED_GEOMETRIC_MAP_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_ORDERED_MAP'
def evaluate():
 ac=[[1,0],[0,2]];bc=ac;a=[[1,0],[0,3]];b=[[2,1],[1,2]];h=.1
 return {'study_id':'jacobi-path-ordering-v1','commuting':{'commutator_norm':commutator_norm(ac,bc),'order_distance':distance(path(ac,bc,h),path(bc,ac,h))},'noncommuting':{'spectra':[spectrum(a),spectrum(b)],'integrated_trace':sum(sum(x[i][i] for i in range(2)) for x in [a,b])*h,'commutator_norm':commutator_norm(a,b),'order_distance':distance(path(a,b,h),path(b,a,h))},'ell0_gate':ell0_gate(['K','h','screen']),'status':'JACOBI_PATH_ORDER_REQUIRED_LOCAL_SPECTRA_INSUFFICIENT','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Second-order segment propagator toy; not exact Sachs integration, covariant screen transport, data, or UMCH dynamics.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi path-order artifact differs',file=sys.stderr);return 1
  print('Jacobi path-order artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
