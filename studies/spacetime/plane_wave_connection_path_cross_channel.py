#!/usr/bin/env python3
"""Endpoint-matched screen-path counterexample across exact plane-wave channels."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
OUTPUT=HERE/'plane-wave-connection-path-cross-channel-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
screen=load('screen_path_base','plane_wave_screen_transport.py');cov=load('screen_path_cov','plane_wave_covariant_screen_phase.py');can=load('screen_path_can','plane_wave_canonical_screen_phase.py');sachs=load('screen_path_sachs','plane_wave_covariant_sachs_screen.py')
base,full,optics=screen.base,screen.full,sachs.optics
J=[[0.,-1.],[1.,0.]]
def mm(a,b):return base.mm(a,b)
def tr(a):return screen.transpose(a)
def diff(a,b):return screen.matrix_residual(a,b)
def scale(a,x):return base.scale(a,x)
def rotation(x):return screen.rotation(x)
def inverse4(a):return cov.inverse4(a)
def safe_graph(x,p,tol=1e-12):
 if abs(optics.determinant(x))<=tol:return {'status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}
 return {'status':'REGULAR','matrix':mm(p,full.inverse2(x))}
def omega1(u,length=.94):
 t=u/length;return (.37+.11*t+.08*t*t)/length
def bump(u,length=.94):
 t=u/length;return .52*t*(1-4*t*t)/length
def omega2(u,length=.94):return omega1(u,length)+bump(u,length)
def primitive(which,u,length):
 t=u/length;lo=-.5
 base_int=.37*(t-lo)+.055*(t*t-lo*lo)+(.08/3)*(t**3-lo**3)
 bump_int=.52*(.5*(t*t-lo*lo)-(t**4-lo**4))
 return base_int+(bump_int if which==2 else 0.)
def qfun(which,length=.94):return lambda u:rotation(-primitive(which,u,length))
def afun(which,length=.94):
 fun=omega1 if which==1 else omega2
 return lambda u:scale(J,-fun(u,length))
def transported_window(q,kfun=base.base_k,length=.94,n=5000):
 return scale(screen.window(lambda u:mm(mm(tr(q(u)),kfun(u)),q(u)),length,n=n),1/length)
def phase_diag(q):return full.assemble(q,base.zero(),base.zero(),q)
def canonical_endpoint_map(q,length=.94,n=5000,kfun=base.base_k):
 us,uo=-length/2,length/2;p=full.full_map(kfun,length,n)
 return mm(mm(inverse4(phase_diag(q(uo))),p),phase_diag(q(us)))
def velocity_map(pc,a,length=.94):
 us,uo=-length/2,length/2
 return mm(mm(inverse4(can.h_velocity_to_canonical(a(uo))),pc),can.h_velocity_to_canonical(a(us)))
def state(p,x0,v0):
 a,b,c,d=full.split(p);return base.add(mm(a,x0),mm(b,v0)),base.add(mm(c,x0),mm(d,v0))
def endpoint_graphs(q,a,length=.94,n=5000,kfun=base.base_k,s0=None):
 s0=sachs.twistmod.boundary_matrix() if s0 is None else s0;us,uo=-length/2,length/2
 pin=full.full_map(kfun,length,n);y,u=state(pin,base.eye(),s0);qo=q(uo);x=mm(tr(qo),y);p=mm(tr(qo),u);v=base.add(p,scale(mm(a(uo),x),-1))
 return safe_graph(x,p)['matrix'],safe_graph(x,v)['matrix']
def naive_map(q,length=.94,n=5000,kfun=base.base_k):return full.full_map(lambda u:mm(mm(tr(q(u)),kfun(u)),q(u)),length,n)
def path_counterexample(length=.94,n=5000,kfun=base.base_k,s0=None):
 q1,q2=qfun(1,length),qfun(2,length);a1,a2=afun(1,length),afun(2,length);us,uo=-length/2,length/2
 w1,w2=transported_window(q1,kfun,length,n),transported_window(q2,kfun,length,n)
 pc1,pc2=canonical_endpoint_map(q1,length,n,kfun),canonical_endpoint_map(q2,length,n,kfun)
 pv1,pv2=velocity_map(pc1,a1,length),velocity_map(pc2,a2,length)
 r1,s1=endpoint_graphs(q1,a1,length,n,kfun,s0);r2,s2=endpoint_graphs(q2,a2,length,n,kfun,s0)
 samples=[diff(q1(us+i*length/40),q2(us+i*length/40)) for i in range(41)]
 return {'source_q_difference':diff(q1(us),q2(us)),'observer_q_difference':diff(q1(uo),q2(uo)),'source_a_difference':diff(a1(us),a2(us)),'observer_a_difference':diff(a1(uo),a2(uo)),'internal_q_difference':max(samples),'transported_window_1':w1,'transported_window_2':w2,'transported_window_difference':diff(w1,w2),'canonical_map_difference':diff(pc1,pc2),'velocity_map_difference':diff(pv1,pv2),'canonical_sachs_difference':diff(r1,r2),'velocity_sachs_difference':diff(s1,s2),'naive_map_difference':diff(naive_map(q1,length,n,kfun),naive_map(q2,length,n,kfun)),'canonical_map_1':pc1,'velocity_map_1':pv1,'canonical_sachs_1':r1,'velocity_sachs_1':s1}
def orientation_control(length=.94,n=5000):
 r=rotation(.31);rt=tr(r);q=qfun(1,length);w=transported_window(q,length=length,n=n);p=canonical_endpoint_map(q,length,n);lift=phase_diag(r)
 kr=lambda u:mm(mm(rt,base.base_k(u)),r);qr=lambda u:mm(mm(rt,q(u)),r)
 wr=transported_window(qr,kr,length,n);pr=canonical_endpoint_map(qr,length,n,kr)
 ref=[[1.,0.],[0.,-1.]];wref=mm(mm(ref,w),ref)
 return {'so2_window_covariance_residual':diff(wr,mm(mm(rt,w),r)),'so2_map_covariance_residual':diff(pr,mm(mm(inverse4(lift),p),lift)),'reflection_oriented_component_sign_residual':abs(wref[0][1]+w[0][1])}
def affine_control(length=.94,n=5000,factor=1.47):
 raw=path_counterexample(length,n);sf=lambda u:scale(base.base_k(u/factor),1/factor**2);s0=scale(sachs.twistmod.boundary_matrix(),1/factor);scaled=path_counterexample(length*factor,n,sf,s0)
 vals=[abs(raw['transported_window_difference']*length**2-scaled['transported_window_difference']*(length*factor)**2),abs(raw['internal_q_difference']-scaled['internal_q_difference']),raw['canonical_map_difference'],scaled['canonical_map_difference'],raw['velocity_map_difference'],scaled['velocity_map_difference'],abs(raw['canonical_sachs_difference']*length-scaled['canonical_sachs_difference']*length*factor),abs(raw['velocity_sachs_difference']*length-scaled['velocity_sachs_difference']*length*factor)]
 return {'factor':factor,'maximum_dimensionless_residual':max(vals)}
def build(n=5000):
 return {'classification':'EXACT_SPACETIME_CONNECTION_PATH_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_PLANE_WAVE_INTERNAL_SCREEN_CONNECTION_PATH_MOVES_TRANSPORTED_WINDOW_NOT_COVARIANT_ENDPOINT_MAPS_CROSS_CHANNEL_RANK_NOT_AUTOMATIC_NOT_ELL0','open_gate':'PHYSICAL_CONTINUOUS_SCREEN_READOUT_PATH_KERNEL_ENDPOINT_TETRADS_AND_ELL0_LAW_NOT_DERIVED','raw_objects':['K','omega_1','omega_2','Q_1','Q_2','A_1','A_2','W_1','W_2','P_inertial','P_canonical','P_velocity','R','S_rot','S_0','L'],'path_counterexample':path_counterexample(n=n),'orientation':orientation_control(n=n),'affine':affine_control(n=n),'caustic_gate':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR','ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','source_scope':'Coley-McNutt-Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; not prescribed screen paths, finite windows, detector calibration, ell0, UMCH, or detection.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();data=build()
 text=json.dumps(data,indent=2,sort_keys=True)+'\n'
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=text:print('Artifact differs.',file=sys.stderr);return 1
  print('Plane-wave connection-path cross-channel artifact is current.');return 0
 if a.write:OUTPUT.write_text(text);print(OUTPUT);return 0
 print(text,end='');return 0
if __name__=='__main__':raise SystemExit(main())
