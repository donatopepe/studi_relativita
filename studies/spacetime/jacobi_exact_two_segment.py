#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-exact-two-segment-results.json')
def segment(lam,length):
 if lam<=0 or length<=0:raise ValueError('positive optical eigenvalue and length required')
 w=math.sqrt(lam);c=math.cos(w*length);s=math.sin(w*length)
 return [[c,s/w],[-w*s,c]]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def order_maps(lam1,L1,lam2,L2):
 p1=segment(lam1,L1);p2=segment(lam2,L2)
 return mul(p2,p1),mul(p1,p2)
def trace(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def characteristic(a):return (round(trace(a),14),round(det(a),14))
def maxdiff(a,b):return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))
def endpoint(a,boundary):return a[0][0]*boundary[0]+a[0][1]*boundary[1]
def vertex_endpoint(a):return endpoint(a,(0,1))
def vertex_derivative(a):return a[1][1]
def ell0_gate(symbols):return 'EXACT_OPTICAL_PHASE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_OPTICAL_PROFILE_LAW'
def evaluate():
 cases=[]
 for values in [(1,.7,3,.4),(2,.3,2,.3),(1,.2,4,.8)]:
  a,b=order_maps(*values);cases.append({'parameters':values,'forward':a,'reverse':b,'map_max_difference':maxdiff(a,b),'forward_trace':trace(a),'reverse_trace':trace(b),'forward_determinant':det(a),'reverse_determinant':det(b),'forward_vertex_endpoint':vertex_endpoint(a),'reverse_vertex_endpoint':vertex_endpoint(b)})
 return {'study_id':'jacobi-exact-two-segment-v1','equation':'d_second+lambda d=0','segment_map':'[[cos(wL),sin(wL)/w],[-w sin(wL),cos(wL)]]','cases':cases,'similarity_gate':'CYCLIC_TWO_SEGMENT_PRODUCTS_HAVE_IDENTICAL_CHARACTERISTIC_POLYNOMIAL','endpoint_gate':'VERTEX_DISPLACEMENT_ORDER_BLIND_FOR_TWO_SCALAR_SEGMENTS','derivative_gate':'VERTEX_DERIVATIVE_AND_FULL_PHASE_SPACE_MAP_RETAIN_ORDER','boundary_gate':'GENERAL_DISPLACEMENT_DEPENDS_ON_SOURCE_PHASE_AND_AFFINE_NORMALIZATION','collision_gate':'IDENTICAL_SEGMENTS_AND_SPECIAL_PARAMETERS_CAN_ERASE_ORDER','ell0_gate':ell0_gate(['lambda1','lambda2','L1','L2']),'status':'JACOBI_EXACT_SPECTRUM_AND_VERTEX_DISPLACEMENT_ORDER_BLIND_FULL_MAP_ORDER_SENSITIVE_NOT_ELL0','classification':'EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact scalar piecewise-constant Jacobi equation, not smooth varying matrix Sachs optics, covariant screen transport, exact spacetime solution, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi exact two-segment artifact differs',file=sys.stderr);return 1
  print('Jacobi exact two-segment artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
