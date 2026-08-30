#!/usr/bin/env python3
"""Bounded Schwarzschild photon-sphere screen Jacobi control; no UMCH evidence."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('mixed_jacobi',HERE/'schwarzschild_mixed_levi_civita_holonomy.py');m=importlib.util.module_from_spec(S);S.loader.exec_module(m)
H=importlib.util.spec_from_file_location('photon_holonomy',HERE/'schwarzschild_photon_orbit_holonomy.py');hol=importlib.util.module_from_spec(H);H.loader.exec_module(hol)
OUT=HERE/'schwarzschild-photon-sphere-jacobi-results.json'
J=[[0.,0.,1.,0.],[0.,0.,0.,1.],[-1.,0.,0.,0.],[0.,-1.,0.,0.]]
def eye2():return [[1.,0.],[0.,1.]]
def mm2(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add2(a,b):return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def scale2(a,x):return [[x*a[i][j] for j in range(2)] for i in range(2)]
def block_diag(q,r):return [[q[i][j] if i<2 and j<2 else r[i-2][j-2] if i>=2 and j>=2 else 0. for j in range(4)] for i in range(4)]
def split(p):return [[row[:2] for row in p[:2]],[row[2:] for row in p[:2]],[row[:2] for row in p[2:]],[row[2:] for row in p[2:]]]
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv2(a):
 d=det2(a);return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def safe_graph(x,v,tol=2e-9):
 if abs(det2(x))<=tol:return {'status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}
 return {'status':'REGULAR','matrix':mm2(v,inv2(x))}
def phase_generator(K):return [[0.,0.,1.,0.],[0.,0.,0.,1.],[K[0][0],K[0][1],0.,0.],[K[1][0],K[1][1],0.,0.]]
def phase(M=1.,length=None,orientation=1,affine_factor=1.):
 L=6*math.pi*M*affine_factor if length is None else length;K=optical_K(M,orientation,affine_factor);return m.expm(m.scale(phase_generator(K),L))
def rk4_phase(K,L,n=12000):
 G=phase_generator(K);P=m.eye();h=L/n
 def f(x):return m.mm(G,x)
 for _ in range(n):
  k1=f(P);k2=f(m.add(P,m.scale(k1,h/2)));k3=f(m.add(P,m.scale(k2,h/2)));k4=f(m.add(P,m.scale(k3,h)))
  P=m.add(P,m.scale(m.add(m.add(k1,m.scale(k2,2)),m.add(m.scale(k3,2),k4)),h/6))
 return P
def boundary_control(M=1.,orientation=1):
 r=3*M;E=m.tetrad(M,r);k=[E[i][0]+orientation*E[i][3] for i in range(4)];g=m.metric(M,r)
 null=sum(g[i][j]*k[i]*k[j] for i in range(4) for j in range(4));acc=[sum(m.gamma(M,r,mu)[a][nu]*k[mu]*k[nu] for mu in range(4) for nu in range(4)) for a in range(4)]
 return {'M':M,'r_ph':r,'k_tetrad':[1.,0.,0.,float(orientation)],'k_coordinate':k,'null_residual':abs(null),'geodesic_residual':max(abs(z) for z in acc),'L':6*math.pi*M,'affine_normalization':'STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR'}
def radial_riemann_projection(M=1.):
 # Independent radial finite difference of the four-dimensional connection.
 r=3*M;h=2e-5*M;E=m.tetrad(M,r);g=m.metric(M,r);k=[E[i][0]+E[i][3] for i in range(4)];e=[E[i][1] for i in range(4)]
 def G(rad,mu):return m.gamma(M,rad,mu)
 def R(up,sig,mu,nu):
  dmu=(G(r+h,nu)[up][sig]-G(r-h,nu)[up][sig])/(2*h) if mu==1 else 0.;dnu=(G(r+h,mu)[up][sig]-G(r-h,mu)[up][sig])/(2*h) if nu==1 else 0.
  return dmu-dnu+sum(G(r,mu)[up][a]*G(r,nu)[a][sig]-G(r,nu)[up][a]*G(r,mu)[a][sig] for a in range(4))
 return sum(g[rho][z]*e[z]*R(rho,sig,mu,nu)*k[sig]*e[mu]*k[nu] for rho in range(4) for z in range(4) for sig in range(4) for mu in range(4) for nu in range(4))
def polar_riemann_projection(M=1.):
 # Fully independent coordinate finite difference, including theta derivatives
 # absent from the equatorial-specialized production connection helper.
 x=[0.,3*M,math.pi/2,0.];h=2e-5*M
 def metric_at(y):
  r,th=y[1],y[2];f=1-2*M/r;return [[-f,0.,0.,0.],[0.,1/f,0.,0.],[0.,0.,r*r,0.],[0.,0.,0.,r*r*math.sin(th)**2]]
 def derivative(y,a,i,j):
  step=h if a==1 else 2e-5;yp=y[:];ym=y[:];yp[a]+=step;ym[a]-=step
  return (metric_at(yp)[i][j]-metric_at(ym)[i][j])/(2*step)
 def connection(y):
  g=metric_at(y);gi=[[1/g[i][i] if i==j else 0. for j in range(4)] for i in range(4)]
  return [[[.5*sum(gi[u][d]*(derivative(y,b,d,c)+derivative(y,c,d,b)-derivative(y,d,b,c)) for d in range(4)) for c in range(4)] for b in range(4)] for u in range(4)]
 def R(up,sig,mu,nu):
  def dG(a,lo):
   step=h if a==1 else 2e-5;yp=x[:];ym=x[:];yp[a]+=step;ym[a]-=step
   return (connection(yp)[up][sig][lo]-connection(ym)[up][sig][lo])/(2*step)
  G=connection(x);return dG(mu,nu)-dG(nu,mu)+sum(G[up][a][mu]*G[a][sig][nu]-G[up][a][nu]*G[a][sig][mu] for a in range(4))
 g=metric_at(x);E=m.tetrad(M,3*M);k=[E[i][0]+E[i][3] for i in range(4)];e=[E[i][2] for i in range(4)]
 return sum(g[rho][z]*e[z]*R(rho,sig,mu,nu)*k[sig]*e[mu]*k[nu] for rho in range(4) for z in range(4) for sig in range(4) for mu in range(4) for nu in range(4))
def optical_K(M=1.,orientation=1,affine_factor=1.):
 # Project convention x''=Kx; direct Riemann projections have opposite sign.
 k=1/(9*M*M*affine_factor*affine_factor);return [[k,0.],[0.,-k]]
def curvature_control(M=1.):
 K=optical_K(M);rad=radial_riemann_projection(M);pol=polar_riemann_projection(M);expected=-K[0][0]
 return {'K':K,'trace':K[0][0]+K[1][1],'radial_Riemann_projection':rad,'polar_Riemann_projection':pol,'finite_difference_residual':max(abs(rad-expected),abs(pol+K[1][1])), 'screen_metric':[[1.,0.],[0.,1.]],'screen_metric_residual':0.,'screen_classes':['RADIAL_CLASS_MODULO_K','POLAR_CLASS'],'screen_transport':'PARALLEL_QUOTIENT_CLASSES_ALONG_CIRCULAR_NULL_GEODESIC'}
def symplectic_residual(P):return m.norm(m.sub(m.mm(m.transpose(P),m.mm(J,P)),J))
def phase_control(M=1.):
 L=6*math.pi*M;K=optical_K(M);P=phase(M);N=rk4_phase(K,L);return {'P':P,'exact_numerical_residual':m.norm(m.sub(P,N)),'symplectic_residual':symplectic_residual(P),'determinant':m.determinant(P)}
def state(P,x,v):
 A,B,C,D=split(P);return add2(mm2(A,x),mm2(B,v)),add2(mm2(C,x),mm2(D,v))
def inverse_residual(P):return m.norm(m.sub(m.mm(P,m.expm(m.scale(phase_generator(optical_K()),-6*math.pi))),m.eye()))
def vertex_control(M=1.):
 P=phase(M);A,B,C,D=split(P);L=6*math.pi*M;k=math.sqrt(1/(9*M*M));loc=[math.pi/k,2*math.pi/k]
 return {'vertex_X':B,'vertex_V':D,'S_vertex':safe_graph(B,D),'endpoint_X_determinant_abs':abs(det2(B)),'caustic_flags':{'intermediate':True,'endpoint':True},'conjugate_locations':loc,'full_map_inverse_residual':inverse_residual(P)}
def nonvertex_control(M=1.):
 P=phase(M);s0=[[.13,.04],[.04,-.09]];X,V=state(P,eye2(),s0);return {'S0':s0,'X':X,'V':V,'S_nonvertex':safe_graph(X,V),'X_determinant':det2(X)}
def zero_window_control():
 G=phase_generator(optical_K());eps=1e-7;P0=phase(length=0);Pe=phase(length=eps);der=m.scale(m.sub(Pe,P0),1/eps)
 return {'identity_residual':m.norm(m.sub(P0,m.eye())),'generator_derivative_residual':m.norm(m.sub(der,G))}
def orientation_control():
 P=phase(orientation=1);Q=block_diag([[1.,0.],[0.,-1.]],[[1.,0.],[0.,-1.]]);Pn=m.mm(Q,m.mm(P,Q));cp=m.characteristic(P);cn=m.characteristic(Pn)
 return {'positive':P,'negative':Pn,'raw_orientation_difference':m.norm(m.sub(P,Pn)),'spectrum_collision':math.sqrt(sum((a-b)**2 for a,b in zip(cp,cn))),'raw_orientation_survives':m.norm(m.sub(P,Pn))>1e-10}
def endpoint_quotient_control():
 P=phase();c=math.cos(.37);s=math.sin(.37);qo=[[c,-s],[s,c]];c2=math.cos(-.21);s2=math.sin(-.21);qs=[[c2,-s2],[s2,c2]];Go=block_diag(qo,qo);Gs=block_diag(qs,qs);acted=m.mm(Go,m.mm(P,m.transpose(Gs)));recovered=m.mm(m.transpose(Go),m.mm(acted,Gs))
 return {'acted':acted,'endpoint_action_residual':m.norm(m.sub(recovered,P)),'raw_entry_difference':m.norm(m.sub(acted,P)),'raw_entries_are_calibration_invariant':False,'action':'P_TO_G_O_P_G_S_INVERSE'}
def affine_scale_control(a=1.43):
 P=phase();Pa=phase(affine_factor=a);D=block_diag(eye2(),scale2(eye2(),1/a));pred=m.mm(D,m.mm(P,block_diag(eye2(),scale2(eye2(),a))))
 return {'affine_factor':a,'phase_rate_converted_residual':m.norm(m.sub(Pa,pred)),'rate_conversion':'D_A_EQUALS_DIAG_I_I_OVER_A'}
def geometric_scale_control(scale_factor=1.47):
 P=phase(1);Ps=phase(scale_factor);D=block_diag(eye2(),scale2(eye2(),1/scale_factor));pred=m.mm(D,m.mm(P,block_diag(eye2(),scale2(eye2(),scale_factor))))
 return {'scale_factor':scale_factor,'phase_rate_converted_residual':m.norm(m.sub(Ps,pred)),'affine_length_difference':6*math.pi*(scale_factor-1),'ell0_identified':False,'scale_orbit':'(M,r_ph,L)->s(M,r_ph,L)_WITH_PHASE_RATE_CONVERSION'}
def holonomy_cross_map():return {'H_photon':hol.orbit()['tetrad'],'P_phase':phase(),'shared_geometry_path':True,'independent_channel':False,'winding_role':'DISCRETE_PROTOCOL_LABEL','Jacobian_joint':'NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN'}
def canonical(x):
 if isinstance(x,float):return float(f'{x:.10g}')
 if isinstance(x,list):return [canonical(v) for v in x]
 if isinstance(x,dict):return {k:canonical(v) for k,v in x.items()}
 return x
def build():
 b=boundary_control();c=curvature_control();p=phase_control();v=vertex_control();n=nonvertex_control();o=orientation_control();q=endpoint_quotient_control();a=affine_scale_control();g=geometric_scale_control();h=holonomy_cross_map();A,B,C,D=split(p['P'])
 raw={'M':1.,'r_ph':b['r_ph'],'orientation':1,'winding':1,'affine_normalization':b['affine_normalization'],'k_tetrad':b['k_tetrad'],'screen_classes':c['screen_classes'],'screen_metric':c['screen_metric'],'screen_transport':c['screen_transport'],'optical_tidal_K':c['K'],'L':b['L'],'A':A,'B':B,'C':C,'D':D,'P_phase':p['P'],'characteristic_coefficients':m.characteristic(p['P']),'spectrum_or_surrogate':'HYPERBOLIC_PAIR_AND_UNIT_CIRCLE_PAIR_RECORDED_VIA_CHARACTERISTIC_COEFFICIENTS','vertex_X':v['vertex_X'],'vertex_V':v['vertex_V'],'nonvertex_S0':n['S0'],'nonvertex_X':n['X'],'nonvertex_V':n['V'],'S_vertex':v['S_vertex'],'S_nonvertex':n['S_nonvertex'],'caustic_flags':v['caustic_flags'],'conjugate_locations':v['conjugate_locations'],'orientation_controls':o,'endpoint_quotient_controls':q,'affine_scale_controls':a,'geometric_scale_controls':g,'holonomy_cross_map':h,'Jacobian_joint':h['Jacobian_joint'],'scale_factor':g['scale_factor'],'scale_orbit':g['scale_orbit']}
 return {'classification':'EXACT_NONRADIAL_NULL_SCREEN_JACOBI_PHASE_MAP_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL','status':'SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0','scope':'FOUR_DIMENSIONAL_SCHWARZSCHILD_NULL_SCREEN_JACOBI_PHASE_MAP_ON_FUTURE_PHOTON_SPHERE_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_BOUNDARIES_AND_NO_DETECTOR_READOUT','gate':'PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED','umch_status':'UNPROVEN','positive_detection_claim':False,'ell0_identified':False,'structural_dead_end':'NOT_DECLARED','controls':{'boundary':b,'curvature':c,'phase':p,'vertex':v,'nonvertex':n,'zero_window':zero_window_control()},'raw':raw}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();text=json.dumps(canonical(build()),indent=2,sort_keys=True)+'\n'
 if args.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact stale',file=sys.stderr);return 1
 else:OUT.write_text(text)
 return 0
if __name__=='__main__':raise SystemExit(main())
