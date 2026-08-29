#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-reciprocity-involution-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return [list(x) for x in zip(*a)]
def distance(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def rot(t):return [[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]]
def spectral(eigs,t,f):
 q=rot(t);return mm(mm(q,[[f(eigs[0]),0],[0,f(eigs[1])]]),transpose(q))
def segment(eigs,t,L):
 c=spectral(eigs,t,lambda x:math.cos(math.sqrt(x)*L));s=spectral(eigs,t,lambda x:math.sin(math.sqrt(x)*L)/math.sqrt(x));ks=mm(spectral(eigs,t,lambda x:x),s)
 return [[c[0][0],c[0][1],s[0][0],s[0][1]],[c[1][0],c[1][1],s[1][0],s[1][1]],[-ks[0][0],-ks[0][1],c[0][0],c[0][1]],[-ks[1][0],-ks[1][1],c[1][0],c[1][1]]]
def exchange():return [[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]
def reverse_map(a):
 e=exchange();return mm(mm(e,transpose(a)),e)
def propagate(profile):
 out=[[float(i==j) for j in range(4)] for i in range(4)]
 for x in profile:out=mm(segment(*x),out)
 return out
def vertex_block(a):return [a[0][2:4],a[1][2:4]]
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def singular_values(a):
 ata=mm(transpose(a),a);t=ata[0][0]+ata[1][1];d=det2(ata);q=math.sqrt(max(0,t*t-4*d));return tuple(sorted((math.sqrt(max(0,(t-q)/2)),math.sqrt(max(0,(t+q)/2)))))
def antisymmetric_scalar(a):return (a[0][1]-a[1][0])/2
def ell0_gate(symbols):return 'FINITE_PRODUCT_RECIPROCITY_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_RECIPROCITY_BREAKING_LAW'
def evaluate():
 p=[((1,4),0,.3),((2,5),.4,.4),((3,7),-.25,.2),((1.5,6),.7,.15)];f=propagate(p);r=propagate(list(reversed(p)));bf=vertex_block(f);br=vertex_block(r)
 return {'study_id':'jacobi-reciprocity-involution-v1','segments':p,'involution':'R(P)=E P^T E with E exchanging displacement and velocity blocks','segment_fixed_residuals':[distance(reverse_map(segment(*x)),segment(*x)) for x in p],'product_reversal_residual':distance(r,reverse_map(f)),'vertex_transpose_residual':distance(br,transpose(bf)),'vertex_forward':bf,'vertex_reverse':br,'singular_values_forward':singular_values(bf),'singular_values_reverse':singular_values(br),'antisymmetric_forward':antisymmetric_scalar(bf),'antisymmetric_reverse':antisymmetric_scalar(br),'algebra_gate':'R_XY_EQUALS_R_Y_R_X_AND_EACH_SYMMETRIC_SEGMENT_IS_R_FIXED','observable_gate':'VERTEX_SINGULAR_VALUES_DETERMINANT_AND_FROBENIUS_REVERSAL_BLIND','orientation_gate':'VERTEX_ANTISYMMETRIC_PART_REVERSES_SIGN_IN_FIXED_ENDPOINT_FRAMES','ell0_gate':ell0_gate(['K','L','screen','order']),'status':'JACOBI_FINITE_SYMMETRIC_PROFILE_REVERSAL_EXACT_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_EXACT_MATRIX_CONTROL','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact finite products of symmetric piecewise-constant optical segments; not a smooth covariant Sachs theorem, exact-spacetime derivation, data result, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi reciprocity-involution artifact differs',file=sys.stderr);return 1
  print('Jacobi reciprocity-involution artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
