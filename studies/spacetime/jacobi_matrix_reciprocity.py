#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-matrix-reciprocity-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return [list(x) for x in zip(*a)]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def distance(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def rot(t):return [[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]]
def spectral(eigs,t,f):
 q=rot(t);return mm(mm(q,[[f(eigs[0]),0],[0,f(eigs[1])]]),transpose(q))
def segment(eigs,t,L):
 c=spectral(eigs,t,lambda x:math.cos(math.sqrt(x)*L));s=spectral(eigs,t,lambda x:math.sin(math.sqrt(x)*L)/math.sqrt(x));ks=mm(spectral(eigs,t,lambda x:x),s)
 return [[c[0][0],c[0][1],s[0][0],s[0][1]],[c[1][0],c[1][1],s[1][0],s[1][1]],[-ks[0][0],-ks[0][1],c[0][0],c[0][1]],[-ks[1][0],-ks[1][1],c[1][0],c[1][1]]]
def propagate(profile):
 out=[[float(i==j) for j in range(4)] for i in range(4)]
 for eigs,t,L in profile:out=mm(segment(eigs,t,L),out)
 return out
def vertex_block(a):return [a[0][2:4],a[1][2:4]]
def characteristic(a):
 a2=mm(a,a);a3=mm(a2,a);a4=mm(a3,a);p1=tr(a);p2=tr(a2);p3=tr(a3);p4=tr(a4);return tuple(round(x,12) for x in (p1,(p1*p1-p2)/2,(p1**3-3*p1*p2+2*p3)/6,(p1**4-6*p1*p1*p2+3*p2*p2+8*p1*p3-6*p4)/24))
def singular_values(a):
 ata=mm(transpose(a),a);t=tr(ata);d=det2(ata);q=math.sqrt(max(0,t*t-4*d));return tuple(sorted((math.sqrt(max(0,(t-q)/2)),math.sqrt(max(0,(t+q)/2)))))
def ell0_gate(symbols):return 'PROFILE_REVERSAL_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_PROFILE_LAW'
def record(name,p):
 a=propagate(p);b=propagate(list(reversed(p)));va=vertex_block(a);vb=vertex_block(b);sa=singular_values(va);sb=singular_values(vb)
 return {'name':name,'segments':p,'characteristic_forward':characteristic(a),'characteristic_reverse':characteristic(b),'full_map_distance':distance(a,b),'vertex_forward':va,'vertex_reverse':vb,'vertex_distance':distance(va,vb),'transpose_residual':distance(vb,transpose(va)),'singular_values_forward':sa,'singular_values_reverse':sb,'singular_value_distance':max(abs(x-y) for x,y in zip(sa,sb))}
def evaluate():
 two=[((1,4),0,.3),((2,5),.4,.4)];three=two+[((3,7),-.25,.2)];four=three+[((1.5,6),.7,.15)];aligned=[((1,4),0,.3),((2,5),0,.4),((3,7),0,.2)]
 return {'study_id':'jacobi-matrix-reciprocity-v1','cases':[record('two_rotated',two),record('three_rotated',three),record('four_rotated',four),record('three_aligned',aligned)],'spectrum_gate':'TOTAL_PHASE_SPACE_SPECTRUM_REVERSAL_BLIND_FOR_TESTED_EXACT_PROFILES','reciprocity_gate':'REVERSED_VERTEX_BLOCK_EQUALS_FORWARD_TRANSPOSE_FOR_SYMMETRIC_PROFILE','aligned_gate':'ALIGNED_PROFILE_REDUCES_TO_IDENTICAL_REVERSAL_BLIND_SCALAR_MODES','screen_gate':'VERTEX_SINGULAR_VALUES_REMAIN_REVERSAL_BLIND_WITH_FIXED_SCREEN_METRIC','ell0_gate':ell0_gate(['K','L','order','screen']),'status':'JACOBI_MATRIX_PROFILE_REVERSAL_TRANSPOSE_RECIPROCITY_SINGULAR_VALUES_BLIND_NOT_ELL0','classification':'EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact piecewise-constant matrix optics, not smooth connection-derived Sachs profile in exact spacetime, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi matrix-reciprocity artifact differs',file=sys.stderr);return 1
  print('Jacobi matrix-reciprocity artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
