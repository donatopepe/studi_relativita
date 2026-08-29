#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-smooth-reciprocity-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def add(a,b,c=1.):return [[a[i][j]+c*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,c):return [[c*x for x in r] for r in a]
def norm(a):return math.sqrt(sum(x*x for r in a for x in r))
def sub(a,b):return add(a,b,-1.)
def rot(t):return [[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]]
def sym_k(s):
 q=rot(.7*s+.2*math.sin(2.3*s));d=[[.45+.08*math.sin(1.9*s),0],[0,.16+.05*math.cos(1.3*s)]];return mm(mm(q,d),tr(q))
def nonsym_k(s):
 k=sym_k(s);k[0][1]+=.17*(1+.2*math.sin(s));return k
def h(k):return [[0,0,1,0],[0,0,0,1],[-k[0][0],-k[0][1],0,0],[-k[1][0],-k[1][1],0,0]]
def rhs(s,y,kfun):return mm(h(kfun(s)),y)
def rk4_step(s,y,dt,kfun):
 a=rhs(s,y,kfun);b=rhs(s+dt/2,add(y,scale(a,dt/2)),kfun);c=rhs(s+dt/2,add(y,scale(b,dt/2)),kfun);d=rhs(s+dt,add(y,scale(c,dt)),kfun);return add(y,scale(add(add(a,scale(b,2)),add(scale(c,2),d)),dt/6))
def integrate(kfun,n,S=1.3):
 y=[[1 if i==j else 0 for j in range(4)] for i in range(4)];dt=S/n;s=0.
 for _ in range(n):y=rk4_step(s,y,dt,kfun);s+=dt
 return y
def anti(p):
 e=[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]];return mm(mm(e,tr(p)),e)
def block(p,r,c):return [[p[r+i][c+j] for j in range(2)] for i in range(2)]
def sv(a):
 z=mm(tr(a),a);t=z[0][0]+z[1][1];d=z[0][0]*z[1][1]-z[0][1]*z[1][0];q=math.sqrt(max(0,t*t-4*d));return sorted([math.sqrt(max(0,(t-q)/2)),math.sqrt(max(0,(t+q)/2))])
def control(kfun,n):
 S=1.3;f=integrate(kfun,n,S);r=integrate(lambda s:kfun(S-s),n,S);bf=block(f,0,2);br=block(r,0,2);return {'steps':n,'full_involution_residual':norm(sub(r,anti(f))),'block_transpose_residual':norm(sub(br,tr(bf))),'forward_singular_values':sv(bf),'reverse_singular_values':sv(br)}
def symmetric_control(n=4000):return control(sym_k,n)
def nonsymmetric_counterexample(n=4000):return control(nonsym_k,n)
def ell0_gate(symbols):return 'SMOOTH_RECIPROCITY_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_SCALE_MAP'
def evaluate():return {'study_id':'jacobi-smooth-reciprocity-v1','symmetric_control':symmetric_control(),'nonsymmetric_counterexample':nonsymmetric_counterexample(),'derivation_gate':'CONTINUOUS_SYMMETRIC_K_PRODUCT_LIMIT_EXTENDS_ANTI_INVOLUTION','boundary_gate':'SAME_AFFINE_INTERVAL_VERTEX_NORMALIZATION_AND_FULL_PROFILE_REVERSAL_REQUIRED','endpoint_gate':'INDEPENDENT_ENDPOINT_FRAME_QUOTIENT_STILL_IDENTIFIES_B_AND_TRANSPOSE','ell0_gate':ell0_gate(['K','S','affine','screen']),'status':'JACOBI_CONTINUOUS_SYMMETRIC_PROFILE_REVERSAL_BLOCK_TRANSPOSE_RECIPROCITY_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Continuous symmetric optical-profile theorem and RK4 control; not connection-derived 4D spacetime transport, detector observable, data result, or UMCH mechanism.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Smooth reciprocity artifact differs',file=sys.stderr);return 1
  print('Smooth reciprocity artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
