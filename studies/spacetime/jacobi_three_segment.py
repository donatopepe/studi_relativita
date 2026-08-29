#!/usr/bin/env python3
import argparse,itertools,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-three-segment-results.json')
def segment(lam,L):
 if lam<=0 or L<=0:raise ValueError('positive segment parameters required')
 w=math.sqrt(lam);c=math.cos(w*L);s=math.sin(w*L);return [[c,s/w],[-w*s,c]]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def total(segments,order):
 out=[[1.,0.],[0.,1.]]
 for i in order:out=mul(segment(*segments[i]),out)
 return out
def trace(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def key(x):
 if isinstance(x,list):return tuple(round(v,12) for row in x for v in row)
 return round(x,12) if isinstance(x,float) else x
def permutation_records(segments):
 out=[]
 for order in itertools.permutations(range(3)):
  a=total(segments,order);out.append({'order':order,'matrix':a,'trace':trace(a),'determinant':det(a),'characteristic':(trace(a),det(a)),'vertex_endpoint':a[0][1],'vertex_derivative':a[1][1]})
 return out
def groups(records,field):
 out={}
 for r in records:
  v=r[field];k=tuple(round(x,12) for x in v) if isinstance(v,tuple) else key(v);out.setdefault(k,[]).append(r['order'])
 return out
def ell0_gate(symbols):return 'THREE_SEGMENT_OPTICAL_ORDER_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_ORDERED_PROFILE_LAW'
def evaluate():
 seg=[(1,.3),(2,.5),(4,.7)];records=permutation_records(seg)
 return {'study_id':'jacobi-three-segment-v1','segments':seg,'records':records,'spectrum_classes':[v for v in groups(records,'characteristic').values()],'endpoint_classes':[v for v in groups(records,'vertex_endpoint').values()],'full_map_classes':[v for v in groups(records,'matrix').values()],'spectrum_gate':'TOTAL_SPECTRUM_BLIND_TO_ALL_THREE_SCALAR_SEGMENT_PERMUTATIONS','endpoint_gate':'VERTEX_ENDPOINT_IDENTIFIES_MIDDLE_SEGMENT_ONLY_FOR_GENERIC_TRIPLE','collision_gate':'EQUAL_OR_SPECIAL_SEGMENTS_COLLAPSE_PERMUTATIONS','ell0_gate':ell0_gate(['lambda','L','permutation']),'status':'JACOBI_THREE_SEGMENT_SPECTRUM_PERMUTATION_BLIND_VERTEX_ENDPOINT_MIDDLE_ONLY_NOT_ELL0','classification':'EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact scalar piecewise-constant Jacobi profile, not smooth matrix Sachs optics, covariant screen transport, exact spacetime, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi three-segment artifact differs',file=sys.stderr);return 1
  print('Jacobi three-segment artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
