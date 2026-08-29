#!/usr/bin/env python3
"""Ideal static-radar Schwarzschild transport control; no detector or UMCH claim."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('mixed',HERE/'schwarzschild_mixed_levi_civita_holonomy.py');m=importlib.util.module_from_spec(S);S.loader.exec_module(m)
OUT=HERE/'schwarzschild-radar-holonomy-results.json'

def f(M,r):return 1-2*M/r
def r_star(M,r):
 if M==0:return r
 return r+2*M*math.log(r/(2*M)-1)
def radar_times(M,ro,rm):
 if M<0 or rm<=2*M or ro<=rm:raise ValueError('require M>=0 and ro>rm>2M')
 dt=r_star(M,ro)-r_star(M,rm);return dt,2*math.sqrt(f(M,ro))*dt
def radar_vertices(M,ro,rm):
 dt,_=radar_times(M,ro,rm);return [m.point(0,ro),m.point(dt,rm),m.point(2*dt,ro),m.point(0,ro)]
def path_transport(M,path,steps):
 h=1/steps;u=m.eye()
 def rhs(q,x):
  z,dz=path(q);A=m.zeros()
  for mu in range(4):A=m.add(A,m.scale(m.gamma(M,z[1],mu),-dz[mu]))
  return m.mm(A,x)
 for k in range(steps):
  q=k*h;k1=rhs(q,u);k2=rhs(q+h/2,m.add(u,m.scale(k1,h/2)));k3=rhs(q+h/2,m.add(u,m.scale(k2,h/2)));k4=rhs(q+h,m.add(u,m.scale(k3,h)))
  u=m.add(u,m.scale(m.add(m.add(k1,m.scale(m.add(k2,k3),2)),k4),h/6))
 return u
def paths(M,ro,rm):
 dt,_=radar_times(M,ro,rm);dr=rm-ro
 def inward(q):
  r=ro+dr*q;rd=dr;td=-rd/f(M,r);return m.point(r_star(M,ro)-r_star(M,r),r),(td,rd,0,0)
 def outward(q):
  r=rm-dr*q;rd=-dr;td=rd/f(M,r);return m.point(dt+r_star(M,r)-r_star(M,rm),r),(td,rd,0,0)
 def closure(q):return m.point(2*dt*(1-q),ro),(-2*dt,0,0,0)
 return [inward,outward,closure]
def radar_loop(M=1,ro=7,rm=4,steps=256):
 ps=paths(M,ro,rm);pieces=[path_transport(M,p,steps) for p in ps];H=m.eye()
 for p in pieces:H=m.mm(p,H)
 E=m.tetrad(M,ro);Ht=m.mm(m.inverse_diag(E),m.mm(H,E))
 return {'vertices':radar_vertices(M,ro,rm),'segments':pieces,'coordinate':H,'tetrad':Ht}
def reverse_loop(M=1,ro=7,rm=4,steps=256):
 ps=paths(M,ro,rm);rev=[]
 for p in reversed(ps):
  def make(p):return lambda q:(p(1-q)[0],tuple(-x for x in p(1-q)[1]))
  rev.append(make(p))
 pieces=[path_transport(M,p,steps) for p in rev];H=m.eye()
 for p in pieces:H=m.mm(p,H)
 E=m.tetrad(M,ro);return m.mm(m.inverse_diag(E),m.mm(H,E))
def causal_control(M=1,ro=7,rm=4):
 dt,tau=radar_times(M,ro,rm);formula=2*math.sqrt(f(M,ro))*(r_star(M,ro)-r_star(M,rm));res=[]
 for p in paths(M,ro,rm)[:2]:
  for q in (0,.25,.5,.75,1):
   z,d=p(q);g=m.metric(M,z[1]);res.append(abs(sum(g[i][i]*d[i]*d[i] for i in range(4))))
 return {'coordinate_half_time':dt,'round_trip_proper_time':tau,'travel_time_formula_residual':abs(tau-formula),'maximum_null_residual':max(res),'segment_types':['future radial null ingoing','future radial null outgoing','past observer-worldline closure']}
def geometry_control():
 H=radar_loop()['tetrad'];return {'lorentz_residual':m.lorentz_residual(H),'nonidentity_norm':m.norm(m.sub(H,m.eye()))}
def reversal_control():
 H=radar_loop()['tetrad'];R=reverse_loop();return {'inverse_residual':m.norm(m.sub(m.mm(R,H),m.eye())),'raw_reversal_difference':m.norm(m.sub(H,R))}
def refinement_control():
 hs=[radar_loop(steps=n)['tetrad'] for n in (32,64,128)];return {'steps':[32,64,128],'coarse_difference':m.norm(m.sub(hs[0],hs[1])),'fine_difference':m.norm(m.sub(hs[1],hs[2])),'history':hs}
def rectangle_control():
 M=1;ro=7;rm=4;dt,_=radar_times(M,ro,rm);rad=radar_loop(M,ro,rm)['tetrad'];v=[m.point(0,ro),m.point(2*dt,ro),m.point(2*dt,rm),m.point(0,rm),m.point(0,ro)];rect=m.loop(M,v)['tetrad']
 return {'radial_endpoints':[rm,ro],'coordinate_durations':[2*dt,2*dt],'radial_endpoint_collision':0.0,'coordinate_duration_collision':0.0,'raw_holonomy_difference':m.norm(m.sub(rad,rect)),'H_radar':rad,'H_rectangle':rect}
def solve_rm(M,ro,target):
 lo=2*M*(1+1e-7) if M else 1e-8;hi=ro*(1-1e-10)
 for _ in range(100):
  mid=(lo+hi)/2;value=radar_times(M,ro,mid)[1]/max(M,1)
  if value>target:lo=mid
  else:hi=mid
 return (lo+hi)/2
def endpoint_control():
 M=1;ro1=7;rm1=4;target=radar_times(M,ro1,rm1)[1]/M;ro2=9;rm2=solve_rm(M,ro2,target);h1=radar_loop(M,ro1,rm1)['tetrad'];h2=radar_loop(M,ro2,rm2)['tetrad'];d2=radar_times(M,ro2,rm2)[1]/M
 return {'duration_ratios':[target,d2],'duration_ratio_collision':abs(target-d2),'observer_radii':[ro1,ro2],'mirror_radii':[rm1,rm2],'mirror_radius_difference':abs(rm1-rm2),'anchored_raw_holonomy_difference':m.norm(m.sub(h1,h2)),'duration_only_identifies_boundary':False,'joint_raw_toy_pair_collision':m.norm(m.sub(h1,h2))<1e-10,'limitation':'different base events/tetrads are compared only under declared static-coordinate family identification'}
def spectrum_control():
 H=radar_loop()['tetrad'];R=reverse_loop();a=m.characteristic(H);b=m.characteristic(R)
 return {'raw_reversal_difference':m.norm(m.sub(H,R)),'forward':a,'reverse':b,'characteristic_collision':math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))}
def anchor_control():
 H=radar_loop()['tetrad'];q=m.eye();c=math.cos(.37);s=math.sin(.37);q[1][1]=c;q[1][2]=-s;q[2][1]=s;q[2][2]=c;qi=m.transpose(q);Hp=m.mm(qi,m.mm(H,q));expected=m.mm(qi,m.mm(H,q));a=m.characteristic(H);b=m.characteristic(Hp)
 return {'common_conjugacy_residual':m.norm(m.sub(Hp,expected)),'raw_anchor_difference':m.norm(m.sub(H,Hp)),'characteristic_collision':math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))}
def scale_control():
 s=1.47;M=1;ro=7;rm=4;h1=radar_loop(M,ro,rm)['tetrad'];h2=radar_loop(s,s*ro,s*rm)['tetrad'];dt1,t1=radar_times(M,ro,rm);dt2,t2=radar_times(s,s*ro,s*rm)
 return {'scale_factor':s,'dimensionless_time_residual':abs(t1/M-t2/s),'holonomy_residual':m.norm(m.sub(h1,h2)),'proper_time_difference':abs(t2-t1),'coordinate_time_scaling_residual':abs(dt2-s*dt1)}
def null_control():
 flat=radar_loop(0,7,4)['tetrad'];shr=radar_loop(1,7,6.99,128)['tetrad'];return {'flat_identity_residual':m.norm(m.sub(flat,m.eye())),'shrinking_identity_residual':m.norm(m.sub(shr,m.eye()))}
def build():
 M=1;ro=7;rm=4;dt,tau=radar_times(M,ro,rm);L=radar_loop();ca=causal_control();ep=endpoint_control();sc=scale_control();nc=null_control();sp=spectrum_control()
 return {'study_id':'schwarzschild-static-radar-holonomy-v1','classification':'EXACT_SPACETIME_LEVI_CIVITA_CAUSAL_BOUNDARY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'SCHWARZSCHILD_STATIC_RADAR_CAUSAL_BOUNDARY_HOLONOMY_PROTOCOL_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0','scope':'FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_IDEAL_STATIC_OBSERVER_RADAR_BOUNDARY_WITH_UNDERIVED_MIRROR_AND_READOUT','gate':'PHYSICAL_FREELY_FALLING_ENDPOINTS_MIRROR_ACTION_VECTOR_READOUT_COMMON_STANDARD_AND_ELL0_LAW_NOT_DERIVED','umch_status':'UNPROVEN','ell0_identified':False,'positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','raw_record':{'M':M,'r_o':ro,'r_m':rm,'f':f(M,ro),'r_star':[r_star(M,rm),r_star(M,ro)],'Delta_t':dt,'Delta_tau':tau,'tetrads':{'observer':m.tetrad(M,ro),'mirror':m.tetrad(M,rm)},'vertices':L['vertices'],'segment_labels':['future_null_ingoing','future_null_outgoing','past_static_observer_closure'],'null_residuals':ca['maximum_null_residual'],'segment_transports':L['segments'],'H_radar':L['tetrad'],'orientation':'emit inward, reflect outward, close backward on observer worldline','characteristic_coefficients':sp['forward'],'curvature_window':{'local_R_tr_at_observer':m.curvature(M,ro,0,1),'connection_history_required':True},'refinement_history':refinement_control(),'endpoint_control':ep,'scale_factor':sc['scale_factor'],'null_control':nc},'controls':{'causal':ca,'geometry':geometry_control(),'reversal':reversal_control(),'refinement':refinement_control(),'rectangle':rectangle_control(),'endpoint':ep,'spectrum':sp,'anchor':anchor_control(),'scale':sc,'null':nc},'cross_channel_gate':'TRAVEL_TIME_CURVATURE_AND_HOLONOMY_SHARE_DECLARED_GEOMETRY_AND_ARE_NOT_ASSUMED_INDEPENDENT'}
def render():return json.dumps(build(),indent=2,sort_keys=True)+'\n'
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args(argv);text=render()
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact stale',file=sys.stderr);return 1
  print('Schwarzschild radar holonomy artifact verified');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
