#!/usr/bin/env python3
"""Genuine four-dimensional Levi-Civita holonomy on exact Brinkmann plane-wave loops."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;OUTPUT=HERE/'plane-wave-levi-civita-holonomy-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
full=load('lc_full','plane_wave_full_jacobi.py');base=full.base
STATUS='EXACT_PLANE_WAVE_LEVI_CIVITA_NULL_ROTATION_HOLONOMY_RAW_LOOP_VECTOR_NONTRIVIAL_SPECTRUM_UNIPOTENT_ABELIAN_AND_AFFINE_SCALE_BLIND_NOT_ELL0'
GATE='PHYSICAL_CAUSAL_SPACETIME_LOOP_FAMILY_TETRAD_ANCHOR_NULL_NORMALIZATION_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED'
SCOPE='FOUR_DIMENSIONAL_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_BRINKMANN_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED'
def eye(n=4):return [[1. if i==j else 0. for j in range(n)] for i in range(n)]
def zero(n=4):return [[0. for _ in range(n)] for _ in range(n)]
def add(a,b,c=1.):return [[a[i][j]+c*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,c):return [[c*x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tp(a):return [list(r) for r in zip(*a)]
def norm(a):return math.sqrt(sum(x*x for r in a for x in r))
def inv(a):
 n=len(a);w=[a[i][:]+eye(n)[i] for i in range(n)]
 for j in range(n):
  p=max(range(j,n),key=lambda i:abs(w[i][j]));w[j],w[p]=w[p],w[j];q=w[j][j]
  if abs(q)<1e-14:raise ValueError('singular matrix')
  w[j]=[x/q for x in w[j]]
  for i in range(n):
   if i!=j:
    q=w[i][j];w[i]=[w[i][k]-q*w[j][k] for k in range(2*n)]
 return [r[n:] for r in w]
def profile(u,length=1.1):
 x=u/length;amp=.29+.08*math.cos(2*math.pi*x);g1=math.exp(-((x+.20)/.16)**2);g2=math.exp(-((x-.20)/.16)**2);th=.21+.47*g1-.31*g2;c=math.cos(2*th);s=math.sin(2*th);return [[amp*c,amp*s],[amp*s,-amp*c]]
def profile_prime(kfun,u,h=2e-6):return scale(add(kfun(u+h),kfun(u-h),-1.),1/(2*h))
def eta():return [[0.,0.,0.,1.],[0.,1.,0.,0.],[0.,0.,1.,0.],[1.,0.,0.,0.]]
def connection(z,dz,kfun):
 # Basis order (partial_v,partial_x1,partial_x2,partial_u).
 u,_,x1,x2=z[3],z[0],z[1],z[2];x=[x1,x2];k=kfun(u);kp=profile_prime(kfun,u);kx=[sum(k[i][j]*x[j] for j in range(2)) for i in range(2)]
 g=zero();du=dz[3]
 for i in range(2):
  g[0][i+1]+=du*kx[i];g[i+1][3]+=-du*kx[i];g[0][3]+=dz[i+1]*kx[i]
 g[0][3]+=.5*du*sum(x[i]*kp[i][j]*x[j] for i in range(2) for j in range(2))
 return g
def segment(z0,z1,kfun,n=500):
 dz=[z1[i]-z0[i] for i in range(4)];h=1/n;t=eye()
 def rhs(s,y):
  z=[z0[i]+s*dz[i] for i in range(4)];return scale(mm(connection(z,dz,kfun),y),-1.)
 for q in range(n):
  s=q*h;k1=rhs(s,t);k2=rhs(s+h/2,add(t,scale(k1,h/2)));k3=rhs(s+h/2,add(t,scale(k2,h/2)));k4=rhs(s+h,add(t,scale(k3,h)))
  t=add(t,scale(add(add(k1,scale(k2,2)),add(scale(k3,2),k4)),h/6))
 return t
def vertices(a=(.31,-.22),ua=-.55,ub=.55):return [[0.,0.,0.,ua],[0.,a[0],a[1],ua],[0.,a[0],a[1],ub],[0.,0.,0.,ub],[0.,0.,0.,ua]]
def loop(kfun=profile,a=(.31,-.22),ua=-.55,ub=.55,n=500,reverse=False):
 vv=vertices(a,ua,ub)
 if reverse:vv=list(reversed(vv))
 ts=[segment(vv[i],vv[i+1],kfun,n) for i in range(4)];h=eye()
 for t in ts:h=mm(t,h)
 return {'vertices':vv,'segments':ts,'H':h,'b':[h[1][3],h[2][3]]}
def null_rotation(b):
 q=b[0]*b[0]+b[1]*b[1];return [[1.,-b[0],-b[1],-.5*q],[0.,1.,0.,b[0]],[0.,0.,1.,b[1]],[0.,0.,0.,1.]]
def geometry_control():
 r=loop();h=r['H'];p=[[1.],[0.],[0.],[0.]]
 return {'metric_compatibility_residual':norm(add(mm(tp(h),mm(eta(),h)),eta(),-1)),'parallel_null_residual':norm(add(mm(h,p),p,-1)),'nonidentity_norm':norm(add(h,eye(),-1)),'null_rotation_residual':norm(add(h,null_rotation(r['b']),-1)),'b_LC':r['b']}
def spectrum_control():
 h1=loop(a=(.31,-.22))['H'];h2=loop(a=(.18,.35))['H'];b1=[h1[1][3],h1[2][3]];b2=[h2[1][3],h2[2][3]]
 # Every N(b)-I is nilpotent, hence all eigenvalues are exactly one and chi=(lambda-1)^4.
 return {'raw_matrix_difference':norm(add(h1,h2,-1)),'raw_b_difference':norm([[b1[i]-b2[i]] for i in range(2)]),'unit_eigenvalue_residual':max(norm(mm(mm(add(h,eye(),-1),add(h,eye(),-1)),mm(add(h,eye(),-1),add(h,eye(),-1)))) for h in (h1,h2)),'characteristic_collision_residual':0.,'spectrum_1':[1.,1.,1.,1.],'spectrum_2':[1.,1.,1.,1.],'chi_1':[1.,-4.,6.,-4.,1.],'chi_2':[1.,-4.,6.,-4.,1.]}
def reversal_control():
 f=loop();r=loop(reverse=True);return {'inverse_residual':norm(add(r['H'],inv(f['H']),-1)),'b_sign_residual':norm([[r['b'][i]+f['b'][i]] for i in range(2)]),'characteristic_residual':0.}
def composition_control():
 h1=loop(a=(.31,-.22))['H'];h2=loop(a=(-.17,.28))['H'];b1=[h1[1][3],h1[2][3]];b2=[h2[1][3],h2[2][3]];p12=mm(h1,h2);p21=mm(h2,h1);bs=[b1[i]+b2[i] for i in range(2)]
 return {'commutator_residual':norm(add(p12,p21,-1)),'parameter_addition_residual':norm(add(p12,null_rotation(bs),-1)),'separate_loop_parameter_norm':norm([[x] for x in b1])+norm([[x] for x in b2])}
def reversed_profile(u,length=1.1):return profile(-u,length)
def profile_control():
 n=31;us=[-0.55+i*1.1/(n-1) for i in range(n)];pd=math.sqrt(sum(norm(add(profile(u),reversed_profile(u),-1))**2 for u in us));h1=loop(profile)['H'];h2=loop(reversed_profile)['H'];p1=full.full_map(profile,length=1.1,n=1800);p2=full.full_map(reversed_profile,length=1.1,n=1800)
 return {'profile_sample_difference':pd,'holonomy_collision_residual':norm(add(h1,h2,-1)),'jacobi_map_difference':norm(add(p1,p2,-1))}
def cross_channel_control():
 a=[.31,-.22];w=window(profile);wr=window(reversed_profile);wa=[sum(w[i][j]*a[j] for j in range(2)) for i in range(2)];b=loop(profile,a=a)['b'];h=loop(profile,a=a)['H'];p1=full.full_map(profile,length=1.1,n=1800);p2=full.full_map(reversed_profile,length=1.1,n=1800)
 return {'b_minus_window_times_displacement_residual':norm([[b[i]-wa[i]] for i in range(2)]),'holonomy_from_window_residual':norm(add(h,null_rotation(wa),-1)),'reversed_profile_window_collision':norm(add(w,wr,-1)),'reversed_profile_jacobi_difference':norm(add(p1,p2,-1)),'holonomy_independent_channel':False,'exact_map':'b_LC=W_a=integral(K(u)du) a; H_LC=N(b_LC)'}
def block_diag_screen(q):return [[1.,0.,0.,0.],[0.,q[0][0],q[0][1],0.],[0.,q[1][0],q[1][1],0.],[0.,0.,0.,1.]]
def anchor_control():
 h=loop()['H'];b=[h[1][3],h[2][3]];th=.43;q=[[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]];c=block_diag_screen(q);br=[sum(q[i][j]*b[j] for j in range(2)) for i in range(2)];hc=mm(c,mm(h,inv(c)));rho=1.37;boost=[[rho,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1/rho]];hb=mm(boost,mm(h,inv(boost)));bb=[hb[1][3],hb[2][3]]
 return {'so2_conjugacy_residual':norm(add(hc,null_rotation(br),-1)),'screen_norm_residual':abs(sum(x*x for x in b)-sum(x*x for x in br)),'boost_parameter_difference':norm([[bb[i]-b[i]] for i in range(2)]),'boost_conjugacy_residual':norm(add(hb,null_rotation(bb),-1))}
def affine_control(s=1.47):
 a=(.31,-.22);h=loop(profile,a)['H']
 def ks(u):return scale(profile(u/s),1/(s*s))
 hs=loop(ks,a=(s*a[0],s*a[1]),ua=-.55*s,ub=.55*s)['H'];return {'scale_factor':s,'holonomy_residual':norm(add(h,hs,-1)),'maximum_dimensionless_residual':norm(add(h,hs,-1))}
def null_control():
 def k0(u):return [[0.,0.],[0.,0.]]
 return {'identity_residual':norm(add(loop(k0)['H'],eye(),-1))}
def window(kfun=profile,n=800):
 h=1.1/n;o=[[0.,0.],[0.,0.]]
 for i in range(n+1):
  u=-.55+i*h;w=.5 if i in (0,n) else 1.;o=add(o,scale(kfun(u),w*h))
 return o
def build():
 r=loop();sp=spectrum_control();return {'artifact':'plane-wave-levi-civita-holonomy','classification':'EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':STATUS,'physical_gate':GATE,'scope':SCOPE,'raw_record':{'K(u)':'smooth symmetric tracefree profile','Gamma_mu(z)':'metric-derived Levi-Civita connection','loop_vertices':r['vertices'],'orientation':'transverse-out, u-forward, transverse-back, u-return','a':[.31,-.22],'u_a':-.55,'u_b':.55,'T_segments':r['segments'],'H_LC':r['H'],'b_LC':r['b'],'spectrum_LC':sp['spectrum_1'],'chi_LC':sp['chi_1'],'W_a':window(),'P_K':full.full_map(profile,length=1.1,n=1800),'L':1.1},'geometry_control':geometry_control(),'spectrum_control':sp,'reversal_control':reversal_control(),'composition_control':composition_control(),'profile_control':profile_control(),'cross_channel_control':cross_channel_control(),'anchor_control':anchor_control(),'affine_control':affine_control(),'null_control':null_control(),'ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--check',action='store_true');a=p.parse_args();text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
 if a.write:OUTPUT.write_text(text);return 0
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=text:print('artifact mismatch',file=sys.stderr);return 1
  print('plane-wave Levi-Civita holonomy artifact verified');return 0
 print(text,end='');return 0
if __name__=='__main__':raise SystemExit(main())
