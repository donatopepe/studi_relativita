#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-exact-matrix-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def transpose(a):return [list(x) for x in zip(*a)]
def distance(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def rot(t):return [[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]]
def spectral(eigs,t,f):
 q=rot(t);return mm(mm(q,[[f(eigs[0]),0],[0,f(eigs[1])]]),transpose(q))
def segment(eigs,t,L):
 c=spectral(eigs,t,lambda x:math.cos(math.sqrt(x)*L));s=spectral(eigs,t,lambda x:math.sin(math.sqrt(x)*L)/math.sqrt(x));k=spectral(eigs,t,lambda x:x);ks=mm(k,s)
 return [[c[0][0],c[0][1],s[0][0],s[0][1]],[c[1][0],c[1][1],s[1][0],s[1][1]],[-ks[0][0],-ks[0][1],c[0][0],c[0][1]],[-ks[1][0],-ks[1][1],c[1][0],c[1][1]]]
def order_maps(theta,eigs2=(2,5)):
 p1=segment((1,4),0,.3);p2=segment(eigs2,theta,.4);return mm(p2,p1),mm(p1,p2)
def vertex_block(a):return [a[0][2:4],a[1][2:4]]
def characteristic(a):
 a2=mm(a,a);a3=mm(a2,a);a4=mm(a3,a);p1=tr(a);p2=tr(a2);p3=tr(a3);p4=tr(a4);e2=(p1*p1-p2)/2;e3=(p1**3-3*p1*p2+2*p3)/6;e4=(p1**4-6*p1*p1*p2+3*p2*p2+8*p1*p3-6*p4)/24;return tuple(round(x,12) for x in (p1,e2,e3,e4))
def singular_values(a):
 ata=mm(transpose(a),a);t=tr(ata);d=det2(ata);disc=math.sqrt(max(0,t*t-4*d));return tuple(sorted((math.sqrt(max(0,(t-disc)/2)),math.sqrt(max(0,(t+disc)/2)))))
def symplectic_error(a):
 j=[[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]];return distance(mm(mm(transpose(a),j),a),j)
def ell0_gate(symbols):return 'MATRIX_OPTICAL_ORDER_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_MATRIX_PROFILE_LAW'
def evaluate():
 cases=[]
 for theta in [0,.2,.4,math.pi/4]:
  a,b=order_maps(theta);cases.append({'theta':theta,'characteristic_forward':characteristic(a),'characteristic_reverse':characteristic(b),'full_map_distance':distance(a,b),'vertex_block_forward':vertex_block(a),'vertex_block_reverse':vertex_block(b),'vertex_block_distance':distance(vertex_block(a),vertex_block(b)),'vertex_singular_values_forward':singular_values(vertex_block(a)),'vertex_singular_values_reverse':singular_values(vertex_block(b))})
 return {'study_id':'jacobi-exact-matrix-v1','profile':'two exact positive symmetric 2x2 optical segments with relative rotation','cases':cases,'spectrum_gate':'TOTAL_PHASE_SPACE_CHARACTERISTIC_POLYNOMIAL_ORDER_BLIND','vertex_gate':'REVERSED_VERTEX_BLOCK_IS_TRANSPOSE_FOR_TWO_SYMMETRIC_SEGMENTS','aligned_gate':'ALIGNED_OR_ISOTROPIC_PROFILES_MAKE_VERTEX_BLOCK_IDENTICAL','metric_gate':'VERTEX_SINGULAR_VALUES_ORDER_BLIND_EVEN_WITH_FIXED_SCREEN_METRIC','ell0_gate':ell0_gate(['K1','K2','theta','L']),'status':'JACOBI_EXACT_MATRIX_SPECTRUM_AND_VERTEX_SINGULAR_VALUES_ORDER_BLIND_BLOCK_TRANSPOSE_SENSITIVE_NOT_ELL0','classification':'EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact piecewise-constant matrix optical profile, not smooth Sachs integration in an exact spacetime, covariant screen transport, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi exact-matrix artifact differs',file=sys.stderr);return 1
  print('Jacobi exact-matrix artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
