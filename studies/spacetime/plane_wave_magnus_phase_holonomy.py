#!/usr/bin/env python3
"""Magnus ordering for canonical Jacobi phase connection in an exact plane wave."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;OUTPUT=HERE/'plane-wave-magnus-phase-holonomy-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
full=load('magnus_full','plane_wave_full_jacobi.py');base=full.base;spectrum=load('magnus_spectrum','plane_wave_common_spectrum.py')
def z(n=4):return [[0. for _ in range(n)] for _ in range(n)]
def eye(n=4):return [[1. if i==j else 0. for j in range(n)] for i in range(n)]
def add(a,b,c=1.):return [[a[i][j]+c*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,c):return [[c*x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tp(a):return [list(r) for r in zip(*a)]
def norm(a):return math.sqrt(sum(x*x for r in a for x in r))
def generator(k):return [[0.,0.,1.,0.],[0.,0.,0.,1.],[-k[0][0],-k[0][1],0.,0.],[-k[1][0],-k[1][1],0.,0.]]
def comm(a,b):return add(mm(a,b),mm(b,a),-1)
def profile(u,length=1.1):
 x=u/length;a=.29+.08*math.cos(2*math.pi*x);g1=math.exp(-((x+.20)/.16)**2);g2=math.exp(-((x-.20)/.16)**2);th=.21+.47*g1-.31*g2;c=math.cos(2*th);s=math.sin(2*th);return [[a*c,a*s],[a*s,-a*c]]
def perturbed_profile(u,length=1.1):
 k=profile(u,length);x=u/length;f=.22*math.sin(2*math.pi*x);return [[k[0][0]+f,k[0][1]],[k[1][0],k[1][1]-f]]
def integrate_matrix(fun,length,n):
 h=length/n;o=z(len(fun(0.)))
 for i in range(n+1):
  u=-length/2+i*h;w=.5 if i in (0,n) else 1.;o=add(o,scale(fun(u),w*h))
 return o
def magnus(kfun,length=1.1,n=900):
 h=length/n;ms=[generator(kfun(-length/2+(i+.5)*h)) for i in range(n)];o1=z();o2=z();prefix=z()
 for m in ms:o1=add(o1,scale(m,h));o2=add(o2,scale(comm(m,prefix),.5*h*h));prefix=add(prefix,m)
 return o1,o2
def expm(a,terms=70):
 out=eye(len(a));term=eye(len(a))
 for k in range(1,terms+1):term=scale(mm(term,a),1./k);out=add(out,term)
 return out
def full_map(kfun,length=1.1,n=900):return full.full_map(kfun,length,n)
def char(p):return spectrum.characteristic_coefficients(p)
def vector(a,b):return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def sample_profile(kfun,length,samples):return [{'u_over_L':(-.5+i/(samples-1)),'K':kfun(length*(-.5+i/(samples-1))),'M':generator(kfun(length*(-.5+i/(samples-1))))} for i in range(samples)]
def commutator_control():
 k1=profile(-.22);k2=profile(.27);m1,m2=generator(k1),generator(k2);direct=comm(m1,m2);dk=add(k1,k2,-1);expected=[[dk[0][0],dk[0][1],0.,0.],[dk[1][0],dk[1][1],0.,0.],[0.,0.,-dk[0][0],-dk[0][1]],[0.,0.,-dk[1][0],-dk[1][1]]]
 return {'K_1':k1,'K_2':k2,'commutator':direct,'expected':expected,'identity_residual':norm(add(direct,expected,-1)),'noncommuting_norm':norm(direct)}
def reversal_control(length=1.1,n=900,samples=17):
 k=lambda u:profile(u,length);kr=lambda u:k(-u);w=base.integrate_window(k,length,n);wr=base.integrate_window(kr,length,n);o1,o2=magnus(k,length,n);r1,r2=magnus(kr,length,n);p=full_map(k,length,n);pr=full_map(kr,length,n);involution=full.endpoint_swap_involution(p)
 return {'profile_samples':sample_profile(k,length,samples),'reversed_profile_samples':sample_profile(kr,length,samples),'window':w,'reversed_window':wr,'window_difference':norm(add(w,wr,-1)),'Omega_1':o1,'Omega_1_reversed':r1,'omega1_difference':norm(add(o1,r1,-1)),'Omega_2':o2,'Omega_2_reversed':r2,'omega2_norm':norm(o2),'omega2_sign_reversal_residual':norm(add(o2,r2)),'P':p,'P_reversed':pr,'raw_full_map_difference':norm(add(p,pr,-1)),'reciprocity_residual':norm(add(pr,involution,-1)),'characteristic':char(p),'characteristic_reversed':char(pr),'characteristic_difference':vector(char(p),char(pr))}
def constant_control(length=1.1,n=900):
 q=[[.21,.08],[.08,-.21]];k=lambda u:q;o1,o2=magnus(k,length,n);p=full_map(k,length,n);return {'K':q,'Omega_1':o1,'omega2_norm':norm(o2),'ordered_exponential_residual':norm(add(p,expm(o1),-1))}
def blockdiag(q):return [[q[0][0],q[0][1],0.,0.],[q[1][0],q[1][1],0.,0.],[0.,0.,q[0][0],q[0][1]],[0.,0.,q[1][0],q[1][1]]]
def orientation_control(length=1.1,n=900):
 t=.37;q=[[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]];g=blockdiag(q);gt=tp(g);k=lambda u:profile(u,length);kt=lambda u:mm(mm(tp(q),k(u)),q);p=full_map(k,length,n);pt=full_map(kt,length,n);f=[[1.,0.],[0.,-1.]];gf=blockdiag(f);pf=mm(mm(gf,p),gf);return {'so2_covariance_residual':norm(add(pt,mm(mm(gt,p),g),-1)),'o2_characteristic_residual':vector(char(p),char(pf))}
def dinv(d):return [[1./d[i][i] if i==j else 0. for j in range(4)] for i in range(4)]
def affine_control(length=1.1,n=900,samples=17,factor=1.47):
 k=lambda u:profile(u,length);ks=lambda u:scale(k(u/factor),1/factor**2);o1,o2=magnus(k,length,n);s1,s2=magnus(ks,length*factor,n);p=full_map(k,length,n);ps=full_map(ks,length*factor,n);d=[[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1/factor,0.],[0.,0.,0.,1/factor]];mapped=mm(mm(d,p),dinv(d));to1=mm(mm(d,o1),dinv(d));to2=mm(mm(d,o2),dinv(d));return {'factor':factor,'map_similarity_residual':norm(add(ps,mapped,-1)),'omega1_similarity_residual':norm(add(s1,to1,-1)),'omega2_similarity_residual':norm(add(s2,to2,-1)),'maximum_dimensionless_residual':max(norm(add(ps,mapped,-1)),norm(add(s1,to1,-1)),norm(add(s2,to2,-1)))}
def profile_control(length=1.1,n=900,samples=17):
 k=lambda u:profile(u,length);kp=lambda u:perturbed_profile(u,length);w=base.integrate_window(k,length,n);wp=base.integrate_window(kp,length,n);_,o2=magnus(k,length,n);_,p2=magnus(kp,length,n);p=full_map(k,length,n);pp=full_map(kp,length,n);return {'window_difference':norm(add(w,wp,-1)),'omega2_difference':norm(add(o2,p2,-1)),'full_map_difference':norm(add(p,pp,-1)),'perturbed_profile_samples':sample_profile(kp,length,samples)}
def build(n=900,samples=17):return {'classification':'EXACT_SPACETIME_CANONICAL_PHASE_CONNECTION_MAGNUS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_PLANE_WAVE_CANONICAL_MAGNUS_ORDER_NONCOMMUTATIVE_RAW_REVERSAL_ODD_SPECTRAL_QUOTIENT_AND_AFFINE_SCALE_BLIND_NOT_ELL0','open_gate':'PHYSICAL_SPACETIME_LOOP_PHASE_READOUT_ENDPOINT_ORDER_BRANCH_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED','raw_objects':['K(u)','M_K(u)','Omega_1','Omega_2','P_K','A','B','C','D','chi_P','W(L)','L'],'commutator':commutator_control(),'reversal':reversal_control(n=n,samples=samples),'constant':constant_control(n=n),'orientation':orientation_control(n=n),'affine':affine_control(n=n,samples=samples),'profile':profile_control(n=n,samples=samples),'scope':'CANONICAL_JACOBI_PHASE_CONNECTION_NOT_FOUR_DIMENSIONAL_LEVI_CIVITA_LOOP_HOLONOMY','omega2_independent_channel':False,'ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','source_scope':'Coley-McNutt-Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; not Magnus detector output, loops, endpoint calibration, ell0, UMCH, or detection.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=text:print('Artifact differs.',file=sys.stderr);return 1
  print('Plane-wave Magnus phase-holonomy artifact is current.');return 0
 if a.write:OUTPUT.write_text(text);print(OUTPUT);return 0
 print(text,end='');return 0
if __name__=='__main__':raise SystemExit(main())
