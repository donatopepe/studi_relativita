#!/usr/bin/env python3
"""Canonical and velocity Sachs graphs in a rotating exact-plane-wave screen."""
import argparse, importlib.util, json, math, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent
OUTPUT=HERE/'plane-wave-covariant-sachs-screen-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
can=load('canonical_for_sachs','plane_wave_canonical_screen_phase.py')
twistmod=load('twist_for_covariant','plane_wave_sachs_twist_boundary.py')
cov,screen,base,full,optics=can.cov,can.screen,can.base,can.full,twistmod.optics

def transpose(a): return cov.transpose(a)
def mm(a,b): return base.mm(a,b)
def residual(a,b): return cov.matrix_residual(a,b)
def inv(a): return cov.inverse2(a)
def safe_graph(x,p,tol=1e-12):
 if abs(optics.determinant(x))<=tol:return {'status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}
 return {'status':'REGULAR','matrix':mm(p,inv(x))}
def state_from_map(p,x0,p0):
 a,b,c,d=full.split(p); return base.add(mm(a,x0),mm(b,p0)),base.add(mm(c,x0),mm(d,p0))
def inertial_endpoint(length=.94,n=5000,kfun=base.base_k,s0=None):
 s0=twistmod.boundary_matrix() if s0 is None else s0
 p=full.full_map(kfun=kfun,length=length,n=n); return state_from_map(p,base.eye(),s0)
def rotating_boundary(length=.94,s0=None,qfun=screen.transport,afun=cov.connection_a):
 s0=twistmod.boundary_matrix() if s0 is None else s0; us=-length/2; q= qfun(us)
 x=transpose(q); p=mm(transpose(q),s0); v=base.add(p,base.scale(mm(afun(us),x),-1.0)); return x,p,v

def graphs(length=.94,n=5000,kfun=base.base_k,qfun=screen.transport,afun=cov.connection_a,s0=None):
 s0=twistmod.boundary_matrix() if s0 is None else s0; us,uo=-length/2,length/2
 y,u=inertial_endpoint(length,n,kfun,s0); qo=qfun(uo); a=afun(uo)
 x_graph=mm(transpose(qo),y); p_graph=mm(transpose(qo),u); v_graph=base.add(p_graph,base.scale(mm(a,x_graph),-1.0))
 x0,p0,v0=rotating_boundary(length,s0,qfun,afun)
 pc=can.canonical_map(length,n,kfun,qfun,afun); pv=cov.covariant_map(length,n,kfun,qfun,afun,lambda z: cov.connection_a_prime(z))
 xc,pp=state_from_map(pc,x0,p0); xv,vv=state_from_map(pv,x0,v0)
 rg=safe_graph(x_graph,p_graph)['matrix']; sg=safe_graph(x_graph,v_graph)['matrix']
 return {'Y':y,'U':u,'X_graph':x_graph,'P_graph':p_graph,'V_graph':v_graph,'X_direct':xc,'P_direct':pp,'X_velocity_direct':xv,'V_direct':vv,'R':rg,'S_rot':sg,'A_observer':a,'S_inertial':safe_graph(y,u)['matrix'],'S0':s0}

def zero_connection_control(length=.94,n=5000):
 q=lambda u:base.eye(); a=lambda u:base.zero(); ap=lambda u:base.zero(); s0=twistmod.boundary_matrix()
 y,u=inertial_endpoint(length,n,s0=s0); x0,p0,v0=rotating_boundary(length,s0,q,a)
 pc=can.canonical_map(length,n,qfun=q,afun=a); pv=cov.covariant_map(length,n,qfun=q,afun=a,aprimefun=ap)
 xc,p=state_from_map(pc,x0,p0); xv,v=state_from_map(pv,x0,v0)
 return {'canonical_x_residual':residual(xc,y),'canonical_p_residual':residual(p,u),'velocity_x_residual':residual(xv,y),'velocity_v_residual':residual(v,u)}
def graph_equivalence_control(length=.94,n=5000):
 g=graphs(length,n)
 rd=safe_graph(g['X_direct'],g['P_direct'])['matrix']; sd=safe_graph(g['X_velocity_direct'],g['V_direct'])['matrix']
 return {'canonical_graph_residual':residual(rd,g['R']),'velocity_graph_residual':residual(sd,g['S_rot']),'s_equals_r_minus_a_residual':residual(g['S_rot'],base.add(g['R'],g['A_observer'],-1.0))}
def fixed_source_graph(observer,source=-.47,n=5000,s0=None):
 s0=twistmod.boundary_matrix() if s0 is None else s0
 y,u=base.eye(),s0; step=(observer-source)/n; z=source
 for _ in range(n): y,u=base.rk4_pair(z,y,u,step,base.base_k); z+=step
 q=screen.transport(observer); a=cov.connection_a(observer); x=mm(transpose(q),y); p=mm(transpose(q),u)
 r=safe_graph(x,p)['matrix']; return r,base.add(r,a,-1)
def riccati_derivative(observer,n,kind):
 eps=1e-5
 def value(u):
  r,s=fixed_source_graph(u,n=n); return r if kind=='canonical' else s
 return base.scale(base.add(value(observer+eps),value(observer-eps),-1.0),1/(2*eps))
def twist_connection_control(length=.94,n=5000):
 observer=length/2; r,s=fixed_source_graph(observer,n=n); a=cov.connection_a(observer)
 kt=mm(mm(transpose(screen.transport(observer)),base.base_k(observer)),screen.transport(observer))
 rprime=riccati_derivative(observer,n,'canonical'); sprime=riccati_derivative(observer,n,'velocity')
 # Fixed-source Riccati equations: R'=-Kt-A R-R^2+R A and S'=-Kt-A'-A^2-2AS-S^2.
 rhsr=base.add(base.scale(kt,-1),base.add(base.scale(mm(a,r),-1),base.add(base.scale(mm(r,r),-1),mm(r,a))))
 ap=cov.connection_a_prime(observer); rhss=base.scale(base.add(base.add(base.add(kt,ap),mm(a,a)),base.add(base.scale(mm(a,s),2),mm(s,s))),-1)
 dr,ds,da=optics.decompose(r),optics.decompose(s),optics.decompose(a)
 return {'canonical_twist':dr['twist'],'velocity_twist':ds['twist'],'connection_twist':da['twist'],'twist_shift_residual':abs(ds['twist']-(dr['twist']-da['twist'])),'canonical_riccati_residual':residual(rprime,rhsr),'velocity_riccati_residual':residual(sprime,rhss)}
def endpoint_rate_mobility_control(length=.94,n=5000):
 g=graphs(length,n); alt=base.add(g['A_observer'],base.scale(cov.J,.29)); s_alt=base.add(g['R'],alt,-1)
 return {'canonical_graph_difference':residual(g['R'],g['R']),'velocity_graph_difference':residual(g['S_rot'],s_alt),'velocity_twist_difference':abs(optics.decompose(g['S_rot'])['twist']-optics.decompose(s_alt)['twist']),'scope':'ENDPOINT_RATE_CALIBRATION_COUNTEREXAMPLE_NOT_ALTERNATE_TRANSPORT'}
def orientation_control(length=.94,n=5000):
 g=graphs(length,n); rot=screen.rotation(.37); ref=[[1.,0.],[0.,-1.]]
 def conj(m,q):return mm(mm(transpose(q),m),q)
 rrot,srot=conj(g['R'],rot),conj(g['S_rot'],rot); rr,sr=conj(g['R'],ref),conj(g['S_rot'],ref)
 return {'so2_canonical_covariance_residual':abs(optics.decompose(rrot)['twist']-optics.decompose(g['R'])['twist']),'so2_velocity_covariance_residual':abs(optics.decompose(srot)['twist']-optics.decompose(g['S_rot'])['twist']),'reflection_twist_sign_residual':abs(optics.decompose(sr)['twist']+optics.decompose(g['S_rot'])['twist']),'reflection_canonical_twist_sign_residual':abs(optics.decompose(rr)['twist']+optics.decompose(g['R'])['twist'])}
def affine_orbit_control(length=.94,n=5000,factor=1.47):
 g=graphs(length,n); k,q,a,_=cov.scaled_functions(factor); s0s=base.scale(twistmod.boundary_matrix(),1/factor); gs=graphs(length*factor,n,k,q,a,s0s)
 vals=[residual(g['X_graph'],gs['X_graph']),residual(g['P_graph'],base.scale(gs['P_graph'],factor)),residual(g['R'],base.scale(gs['R'],factor)),residual(g['S_rot'],base.scale(gs['S_rot'],factor)),residual(g['A_observer'],base.scale(gs['A_observer'],factor))]
 return {'scale_factor':factor,'dimensionless_residuals':vals,'maximum_dimensionless_residual':max(vals)}
def ell0_gate(raw):return 'COVARIANT_SACHS_SCREEN_AFFINE_ORBIT_NOT_ELL0' if 'ell0' not in raw else 'REQUIRES_INJECTIVITY_TEST'
def build_artifact(n=5000):
 raw=['K','omega','Q','A','Y','U','X','P','V','R','S_rot','S_0','L']
 return {'classification':'EXACT_SPACETIME_COVARIANT_SACHS_SCREEN_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_PLANE_WAVE_ROTATING_SCREEN_SACHS_TWIST_CONNECTION_AND_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_GRAPH_AFFINE_SCALE_BLIND_NOT_ELL0','open_gate':'PHYSICAL_SACHS_SCREEN_TRANSPORT_CANONICAL_BOUNDARY_ENDPOINT_RATE_AND_PARITY_NOT_DERIVED','raw_fields':raw,'zero_connection':zero_connection_control(n=n),'graph_equivalence':graph_equivalence_control(n=n),'twist_connection':twist_connection_control(n=n),'endpoint_rate_mobility':endpoint_rate_mobility_control(n=n),'orientation':orientation_control(n=n),'affine_orbit':affine_orbit_control(n=n),'ell0_gate':ell0_gate(raw),'prior_result_disposition':'INERTIAL_NONVERTEX_TWIST_AREA_CONSERVATION_RETAINED_ROTATING_VELOCITY_TWIST_HAS_CONNECTION_TERM','source_scope':'COLEY_MCNUTT_MILSON_2012_SUPPORTS_EXACT_BRINKMANN_PLANE_WAVES_AND_GEODESIC_DEVIATION_NOT_ROTATING_SACHS_SCREEN_BOUNDARY_ENDPOINT_RATE_PARITY_WINDOW_AFFINE_NUISANCE_ELL0_UMCH_OR_DETECTION','structural_dead_end':False,'hypothesis_status':'UNPROVEN','conclusion':'NO_POSITIVE_DETECTION_CLAIM'}
def render(d):return json.dumps(d,indent=2,sort_keys=True)+'\n'
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args(argv);t=render(build_artifact())
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=t:print(f'stale artifact: {OUTPUT}',file=sys.stderr);return 1
  return 0
 OUTPUT.write_text(t);return 0
if __name__=='__main__':raise SystemExit(main())
