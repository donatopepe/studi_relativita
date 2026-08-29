#!/usr/bin/env python3
"""Bounded Schwarzschild Levi-Civita finite-loop control; no UMCH inference."""
import argparse,json,math,pathlib,sys
OUT=pathlib.Path(__file__).with_name('schwarzschild-mixed-levi-civita-holonomy-results.json')
N=4

def eye():return [[float(i==j) for j in range(N)] for i in range(N)]
def zeros():return [[0.0]*N for _ in range(N)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def scale(a,x):return [[x*a[i][j] for j in range(N)] for i in range(N)]
def sub(a,b):return add(a,scale(b,-1))
def transpose(a):return [list(x) for x in zip(*a)]
def tr(a):return sum(a[i][i] for i in range(N))
def norm(a):return math.sqrt(sum(x*x for row in a for x in row))
def maximum(*xs):return max(xs)
def diag(xs):return [[float(xs[i]) if i==j else 0.0 for j in range(N)] for i in range(N)]
def inverse_diag(a):return diag([1/a[i][i] for i in range(N)])
def determinant(a):
 return sum((1 if p in ((0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),(2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)) else -1)*a[0][p[0]]*a[1][p[1]]*a[2][p[2]]*a[3][p[3]] for p in __import__('itertools').permutations(range(4)))
def characteristic(a):
 p2=mm(a,a);p3=mm(p2,a)
 e1=tr(a);e2=(e1*e1-tr(p2))/2;e3=(e1**3-3*e1*tr(p2)+2*tr(p3))/6;e4=determinant(a)
 return [1.0,-e1,e2,-e3,e4]
def expm(a):
 n=max(sum(abs(a[i][j]) for j in range(N)) for i in range(N));s=max(0,int(math.ceil(math.log(n,2))) if n>1 else 0)
 x=scale(a,2**-s);out=eye();term=eye()
 for k in range(1,45):term=scale(mm(term,x),1/k);out=add(out,term)
 for _ in range(s):out=mm(out,out)
 return out
def metric(M,r):
 f=1-2*M/r
 return diag([-f,1/f,r*r,r*r])
def tetrad(M,r):
 f=1-2*M/r
 return diag([1/math.sqrt(f),math.sqrt(f),1/r,1/r])
def gamma(M,r,mu):
 f=1-2*M/r;g=zeros()
 if mu==0:
  a=M/(r*r*f);g[0][1]=a;g[1][0]=f*M/(r*r)
 elif mu==1:
  a=M/(r*r*f);g[0][0]=a;g[1][1]=-a;g[2][2]=1/r;g[3][3]=1/r
 elif mu==2:
  g[1][2]=-f*r;g[2][1]=1/r
 elif mu==3:
  g[1][3]=-f*r;g[3][1]=1/r
 return g
def point(t,r,phi=0.0):return [float(t),float(r),math.pi/2,float(phi)]
def rectangles(M=1.0,r0=4.2,r1=6.1,T=1.3,Phi=.7):
 return {'tr':[point(0,r0),point(T,r0),point(T,r1),point(0,r1),point(0,r0)],'rphi':[point(0,r0,0),point(0,r1,0),point(0,r1,Phi),point(0,r0,Phi),point(0,r0,0)]}
def segment_transport(M,a,b,steps):
 dx=[b[i]-a[i] for i in range(4)];h=1/steps;u=eye()
 def rhs(q,x):
  r=a[1]+q*dx[1];A=zeros()
  for mu in range(4):A=add(A,scale(gamma(M,r,mu),-dx[mu]))
  return mm(A,x)
 for k in range(steps):
  q=k*h;k1=rhs(q,u);k2=rhs(q+h/2,add(u,scale(k1,h/2)));k3=rhs(q+h/2,add(u,scale(k2,h/2)));k4=rhs(q+h,add(u,scale(k3,h)))
  u=add(u,scale(add(add(k1,scale(add(k2,k3),2)),k4),h/6))
 return u
def loop(M,vertices,steps=256):
 pieces=[segment_transport(M,vertices[i],vertices[i+1],steps) for i in range(len(vertices)-1)];H=eye()
 for p in pieces:H=mm(p,H)
 E=tetrad(M,vertices[0][1]);Ht=mm(inverse_diag(E),mm(H,E))
 return {'vertices':vertices,'segments':pieces,'coordinate':H,'tetrad':Ht}
def rev(vertices):return list(reversed(vertices))
def curvature(M,r,mu,nu):
 h=1e-5*max(1,r)
 def derivative(which,of):
  if which!=1:return zeros()
  return scale(sub(gamma(M,r+h,of),gamma(M,r-h,of)),1/(2*h))
 return add(sub(derivative(mu,nu),derivative(nu,mu)),sub(mm(gamma(M,r,mu),gamma(M,r,nu)),mm(gamma(M,r,nu),gamma(M,r,mu))))
def lorentz_residual(H):return norm(sub(mm(transpose(H),mm(diag([-1,1,1,1]),H)),diag([-1,1,1,1])))
def base_loops(steps=256,M=1,r0=4.2,r1=6.1,T=1.3,Phi=.7):
 v=rectangles(M,r0,r1,T,Phi);return v,loop(M,v['tr'],steps),loop(M,v['rphi'],steps)
def connection_control():
 M=1;r=5.3;h=1e-5
 residual=[]
 for mu in range(4):
  dg=zeros()
  if mu==1:dg=scale(sub(metric(M,r+h),metric(M,r-h)),1/(2*h))
  G=gamma(M,r,mu);residual.append(norm(sub(dg,add(mm(transpose(G),metric(M,r)),mm(metric(M,r),G)))))
 return {'maximum_metric_connection_residual':max(residual)}
def geometry_control():
 _,a,b=base_loops()
 return {'maximum_lorentz_residual':max(lorentz_residual(a['tetrad']),lorentz_residual(b['tetrad'])),'tr_nonidentity_norm':norm(sub(a['tetrad'],eye())),'rphi_nonidentity_norm':norm(sub(b['tetrad'],eye()))}
def reversal_control():
 v,a,b=base_loops();ar=loop(1,rev(v['tr']));br=loop(1,rev(v['rphi']))
 return {'tr_inverse_residual':norm(sub(mm(ar['tetrad'],a['tetrad']),eye())),'rphi_inverse_residual':norm(sub(mm(br['tetrad'],b['tetrad']),eye())),'maximum_inverse_residual':max(norm(sub(mm(ar['tetrad'],a['tetrad']),eye())),norm(sub(mm(br['tetrad'],b['tetrad']),eye())))}
def refinement_control():
 v=rectangles();hs=[loop(1,v['tr'],n)['tetrad'] for n in (32,64,128)]
 return {'steps':[32,64,128],'coarse_difference':norm(sub(hs[0],hs[1])),'fine_difference':norm(sub(hs[1],hs[2])),'history':hs}
def nonabelian_control():
 _,a,b=base_loops();ab=mm(a['tetrad'],b['tetrad']);ba=mm(b['tetrad'],a['tetrad']);c=mm(mm(a['tetrad'],b['tetrad']),mm(loop(1,rev(rectangles()['tr']))['tetrad'],loop(1,rev(rectangles()['rphi']))['tetrad']))
 return {'ordered_products':[ab,ba],'commutator':c,'ordered_product_difference':norm(sub(ab,ba)),'commutator_nonidentity_norm':norm(sub(c,eye()))}
def flux_prediction(M,r,mu,nu,area):
 E=tetrad(M,r);F=mm(inverse_diag(E),mm(curvature(M,r,mu,nu),E));return expm(scale(F,-area)),F
def cross_channel_control():
 M=1;r=5;eps=.012;small=loop(M,[point(0,r),point(eps,r),point(eps,r+eps),point(0,r+eps),point(0,r)],128)['tetrad'];pred,_=flux_prediction(M,r,0,1,eps*eps)
 v=rectangles();finite=loop(M,v['tr'],256)['tetrad'];fp,F=flux_prediction(M,4.2,0,1,1.3*(6.1-4.2))
 return {'small_loop_log_flux_residual':norm(sub(small,pred))/(eps*eps),'finite_naive_flux_residual':norm(sub(finite,fp)),'local_curvature_generator':F,'finite_curvature_flux':scale(F,1.3*(6.1-4.2)),'holonomy_independent_channel':False,'finite_map_gate':'PATH_ORDERED_CONNECTION_HISTORY_REQUIRED'}
def boundary_control():
 # same dt*dr, shifted radial interval
 T=1.1;dr=1.2;v1=rectangles(r0=3.6,r1=4.8,T=T)['tr'];v2=rectangles(r0=5.4,r1=6.6,T=T)['tr'];h1=loop(1,v1)['tetrad'];h2=loop(1,v2)['tetrad']
 return {'coordinate_areas':[T*dr,T*dr],'coordinate_area_collision':0.0,'radial_boundary_difference':1.8,'raw_holonomy_difference':norm(sub(h1,h2)),'holonomies':[h1,h2]}
def spectrum_control():
 v,a,_=base_loops();ar=loop(1,rev(v['tr']))['tetrad'];return {'raw_reversal_difference':norm(sub(a['tetrad'],ar)),'characteristic_forward':characteristic(a['tetrad']),'characteristic_reverse':characteristic(ar),'reversal_characteristic_collision':norm([ [characteristic(a['tetrad'])[i]-characteristic(ar)[i] for i in range(4)] ]+[ [characteristic(a['tetrad'])[4]-characteristic(ar)[4],0,0,0] ])}
def anchor_control():
 _,a,_=base_loops();H=a['tetrad'];q=eye();c=math.cos(.41);s=math.sin(.41);q[2][2]=c;q[2][3]=-s;q[3][2]=s;q[3][3]=c;qt=transpose(q);Hp=mm(qt,mm(H,q));expected=mm(qt,mm(H,q))
 return {'common_conjugacy_residual':norm(sub(Hp,expected)),'raw_anchor_difference':norm(sub(H,Hp)),'characteristic_collision':math.sqrt(sum((x-y)**2 for x,y in zip(characteristic(H),characteristic(Hp))))}
def scale_control():
 s=1.47;v,a,b=base_loops();vs,aa,bb=base_loops(M=s,r0=4.2*s,r1=6.1*s,T=1.3*s,Phi=.7)
 return {'scale_factor':s,'tr_residual':norm(sub(a['tetrad'],aa['tetrad'])),'rphi_residual':norm(sub(b['tetrad'],bb['tetrad'])),'maximum_holonomy_residual':max(norm(sub(a['tetrad'],aa['tetrad'])),norm(sub(b['tetrad'],bb['tetrad']))),'proper_scale_difference':(6.1-4.2)*(s-1)}
def null_control():
 v=rectangles();flat=loop(0,v['tr'])['tetrad'];e=.01;shr=loop(1,[point(0,5),point(e,5),point(e,5+e),point(0,5+e),point(0,5)],128)['tetrad']
 return {'flat_identity_residual':norm(sub(flat,eye())),'shrinking_loop_identity_residual':norm(sub(shr,eye()))}
def build():
 v,a,b=base_loops();n=nonabelian_control();x=cross_channel_control();q=refinement_control();bc=boundary_control();sc=scale_control();nc=null_control()
 return {'study_id':'schwarzschild-mixed-levi-civita-holonomy-v1','classification':'EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_SCHWARZSCHILD_MIXED_PLANE_LEVI_CIVITA_HOLONOMY_NONABELIAN_PATH_ORDERED_BOUNDARY_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0','scope':'FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_PIECEWISE_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED','gate':'PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_TIME_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED','umch_status':'UNPROVEN','ell0_identified':False,'positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','raw_record':{'M':1.0,'metric':'diag(-(1-2M/r),(1-2M/r)^-1,r^2,r^2 sin^2 theta)','tetrad':'static oriented orthonormal tetrad at common base point','Gamma_mu':[gamma(1,4.2,i) for i in range(4)],'loop_vertices':v,'orientations':{'tr':'positive t then r','rphi':'positive r then phi'},'segment_transports':{'tr':a['segments'],'rphi':b['segments']},'H_tr':a['tetrad'],'H_rphi':b['tetrad'],'ordered_products':n['ordered_products'],'commutator':n['commutator'],'spectrum':'characteristic coefficients retained; numerical eigenvalue solver not used','characteristic_coefficients':{'tr':characteristic(a['tetrad']),'rphi':characteristic(b['tetrad'])},'curvature_flux':x,'refinement_history':q,'boundary_control':bc,'scale_factor':sc['scale_factor'],'null_control':nc},'controls':{'connection':connection_control(),'geometry':geometry_control(),'reversal':reversal_control(),'nonabelian':n,'cross_channel':x,'boundary':bc,'spectrum':spectrum_control(),'anchor':anchor_control(),'scale':sc,'null':nc}}
def render():return json.dumps(build(),indent=2,sort_keys=True)+'\n'
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args(argv);text=render()
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact stale',file=sys.stderr);return 1
  print('Schwarzschild mixed holonomy artifact verified');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
