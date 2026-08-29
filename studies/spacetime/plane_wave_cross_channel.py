#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('plane-wave-cross-channel-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b,c=1):return [[a[i][j]+c*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,c):return [[c*x for x in r] for r in a]
def norm(a):return math.sqrt(sum(x*x for r in a for x in r))
def eye():return [[1.,0.],[0.,1.]]
def zero():return [[0.,0.],[0.,0.]]
def base_k(u):
 a=0.34+0.07*u;th=.29+.82*u+.17*u*u;c=math.cos(2*th);s=math.sin(2*th);return [[a*c,a*s],[a*s,-a*c]]
def integrate_window(kfun,L,n=4000):
 h=L/n;o=zero()
 for i in range(n+1):
  u=-L/2+i*h;w=.5 if i in (0,n) else 1;o=add(o,kfun(u),w*h)
 return o
def rhs(u,d,v,kfun):return v,scale(mm(kfun(u),d),-1)
def rk4_pair(u,d,v,h,kfun):
 d1,v1=rhs(u,d,v,kfun);d2,v2=rhs(u+h/2,add(d,scale(d1,h/2)),add(v,scale(v1,h/2)),kfun);d3,v3=rhs(u+h/2,add(d,scale(d2,h/2)),add(v,scale(v2,h/2)),kfun);d4,v4=rhs(u+h,add(d,scale(d3,h)),add(v,scale(v3,h)),kfun)
 return add(d,scale(add(add(d1,scale(d2,2)),add(scale(d3,2),d4)),h/6)),add(v,scale(add(add(v1,scale(v2,2)),add(scale(v3,2),v4)),h/6))
def jacobi(kfun,L,n=4000,d0=None,v0=None):
 d=zero() if d0 is None else d0;v=eye() if v0 is None else v0;h=L/n;u=-L/2
 for _ in range(n):d,v=rk4_pair(u,d,v,h,kfun);u+=h
 return d
def channels(L,kfun=base_k,n=4000):return integrate_window(kfun,L,n),jacobi(kfun,L,n)
def equal_window_counterexample(n=5000):
 L=1.;q=[[.18,.09],[.09,-.18]]
 k1=lambda u:q;k2=lambda u:add(q,scale([[0.,1.],[1.,0.]],.7*u))
 w1,b1=channels(L,k1,n);w2,b2=channels(L,k2,n);return {'window_residual':norm(add(w1,w2,-1)),'jacobi_residual':norm(add(b1,b2,-1))}
def boundary_counterexample(n=4000):
 L=.9;w=integrate_window(base_k,L,n);b1=jacobi(base_k,L,n);b2=jacobi(base_k,L,n,d0=scale(eye(),.12),v0=eye());return {'window_residual':norm(add(w,w,-1)),'jacobi_residual':norm(add(b1,b2,-1))}
def flatten_pair(L):
 w,b=channels(L,n=2500);return [x for z in (w,b) for r in z for x in r]
def local_rank_control():
 h=1e-3;a=flatten_pair(.899);b=flatten_pair(.9);c=flatten_pair(.901);d=[(c[i]-a[i])/(2*h) for i in range(len(a))];dd=[c[i]-2*b[i]+a[i] for i in range(len(a))];dot=sum(x*y for x,y in zip(d,dd));dn=math.sqrt(sum(x*x for x in d));orth=math.sqrt(max(0,sum(x*x for x in dd)-(dot/dn)**2)) if dn else 0
 return {'joint_derivative_norm':dn,'joint_second_difference_noncollinearity':orth}
def free_gain_equivalence(L1,L2):
 w1,b1=channels(L1,n=2500);w2,b2=channels(L2,n=2500);s1=[norm(w1),norm(add(b1,scale(eye(),L1),-1))];s2=[norm(w2),norm(add(b2,scale(eye(),L2),-1))];g=[s1[i]/s2[i] for i in range(2)];return {'fitted_independent_gains':g,'quotient_residual':math.sqrt(sum((s1[i]-g[i]*s2[i])**2 for i in range(2))),'warning':'Scalar norm projections with independent gains, not raw-matrix equivalence.'}
def affine_rescaling_equivalence(L1,L2):
 s=L2/L1;k2=lambda u:scale(base_k(u/s),1/(s*s));w1,b1=channels(L1,n=4000);w2,b2=channels(L2,k2,4000);return {'dimensionless_window_residual':norm(add(scale(w1,L1),scale(w2,L2),-1)),'dimensionless_jacobi_residual':norm(add(scale(b1,1/L1),scale(b2,1/L2),-1))}
def ell0_gate(symbols):return 'EXACT_CROSS_CHANNEL_SUPPORT_WIDTH_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_INDEPENDENT_PROFILE_AND_CALIBRATION_LAW'
def evaluate():return {'study_id':'exact-plane-wave-window-jacobi-cross-channel-v1','geometry':'SAME_EXACT_VACUUM_PLANE_WAVE_PROFILE_AND_PARALLEL_SCREEN','equal_window_counterexample':equal_window_counterexample(),'boundary_counterexample':boundary_counterexample(),'local_calibrated_control':local_rank_control(),'free_gain_projection':free_gain_equivalence(.7,1.1),'affine_rescaling':affine_rescaling_equivalence(.8,1.3),'cross_channel_gate':'W_AND_B_SHARE_K_BUT_B_DEPENDS_ON_WEIGHTED_ORDERED_HISTORY_AND_BOUNDARY','identifiability_gate':'SUPPORT_WIDTH_CONDITIONAL_ON_PROFILE_AFFINE_NORMALIZATION_BOUNDARY_AND_GAINS','ell0_gate':ell0_gate(['L','K','W','B','gain','boundary']),'status':'EXACT_PLANE_WAVE_WINDOW_JACOBI_MAP_CONDITIONAL_SUPPORT_IDENTIFIABILITY_NOT_ELL0','classification':'EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact-profile channel map and deterministic integration; no physical detector calibration, universal-scale law, data result, or UMCH mechanism.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Plane-wave cross-channel artifact differs',file=sys.stderr);return 1
  print('Plane-wave cross-channel artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
