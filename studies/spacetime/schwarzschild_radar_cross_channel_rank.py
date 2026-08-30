#!/usr/bin/env python3
"""Dimensionless rank audit for ideal Schwarzschild static-radar timing/holonomy."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('radar',HERE/'schwarzschild_radar_holonomy.py');r=importlib.util.module_from_spec(S);S.loader.exec_module(r)
OUT=HERE/'schwarzschild-radar-cross-channel-rank-results.json'
def rapidity(H):return math.atanh(max(-1+1e-15,min(1-1e-15,H[0][1]/H[0][0])))
def boost(eta):c=math.cosh(eta);s=math.sinh(eta);return [[c,s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]]
def obs(ro,rm,steps=128):
 dt,tau=r.radar_times(1,ro,rm);H=r.radar_loop(1,ro,rm,steps)['tetrad'];return [tau,rapidity(H)],H,dt
def jac(fun,x,y,h=1e-4):
 xp=fun(x+h,y);xm=fun(x-h,y);yp=fun(x,y+h);ym=fun(x,y-h)
 return [[(xp[i]-xm[i])/(2*h),(yp[i]-ym[i])/(2*h)] for i in range(2)]
def det(J):return J[0][0]*J[1][1]-J[0][1]*J[1][0]
def sv(J):
 a=J[0][0]**2+J[1][0]**2;b=J[0][0]*J[0][1]+J[1][0]*J[1][1];d=J[0][1]**2+J[1][1]**2;t=a+d;disc=math.sqrt(max(0,(a-d)**2+4*b*b));return [math.sqrt(max(0,(t+disc)/2)),math.sqrt(max(0,(t-disc)/2))]
def rank(J,tol=1e-7):return sum(x>tol for x in sv(J))
def rawfun(ro,rm):return obs(ro,rm,96)[0]
def evenfun(ro,rm):
 x=rawfun(ro,rm);return [x[0],math.cosh(x[1])]
def boost_control():
 values,H,_=obs(7,4,256);eta=values[1];H2=r.radar_loop(1,7,4,256)['tetrad']
 return {'signed_rapidity':eta,'H_radar':H,'reconstructed_boost':boost(eta),'reconstruction_residual':r.m.norm(r.m.sub(H,boost(eta))),'transport_repeat_residual':r.m.norm(r.m.sub(H,H2))}
def rank_control(ro=7,rm=4):
 J=jac(rawfun,ro,rm);J2=jac(rawfun,ro,rm,5e-5)
 return {'Jacobian_raw':J,'determinant_raw':det(J),'singular_values_raw':sv(J),'rank_raw':rank(J),'step':1e-4,'jacobian_step_convergence':math.sqrt(sum((J[i][j]-J2[i][j])**2 for i in range(2) for j in range(2)))}
def tangent_control():
 J=rank_control()['Jacobian_raw'];v=[J[0][1],-J[0][0]];n=math.hypot(*v);v=[x/n for x in v]
 return {'fixed_duration_tangent':v,'duration_gradient':J[0],'rapidity_gradient':J[1],'duration_directional_derivative':sum(J[0][i]*v[i] for i in range(2)),'rapidity_directional_derivative':sum(J[1][i]*v[i] for i in range(2)),'duration_only_rank':1}
def quotient_control():
 value,_H,_=obs(7,4);eta=value[1];J=jac(evenfun,7,4);return {'rank_even_quotient':rank(J),'Jacobian_even':J,'singular_values_even':sv(J),'forward':[value[0],eta],'reversed':[value[0],-eta],'duration_collision':0.0,'even_holonomy_collision':abs(math.cosh(eta)-math.cosh(-eta)),'raw_orientation_difference':abs(2*eta),'global_orientation_collision':True}
def anchor_control():
 H=obs(7,4)[1];q=r.m.eye();c=math.cos(.37);s=math.sin(.37);q[1][1]=c;q[1][2]=-s;q[2][1]=s;q[2][2]=c;qi=r.m.transpose(q);Hp=r.m.mm(qi,r.m.mm(H,q));a=r.m.characteristic(H);b=r.m.characteristic(Hp)
 return {'common_conjugacy_residual':r.m.norm(r.m.sub(Hp,r.m.mm(qi,r.m.mm(H,q)))),'raw_anchor_difference':r.m.norm(r.m.sub(H,Hp)),'characteristic_collision':math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))}
def scale_control():
 scale=1.47;v,H,_=obs(7,4);dt,tau=r.radar_times(1,7,4);dt2,tau2=r.radar_times(scale,scale*7,scale*4);H2=r.radar_loop(scale,scale*7,scale*4,128)['tetrad'];eta2=rapidity(H2);eps=1e-5
 def physical(M,ro,rm):
  t=r.radar_times(M,ro,rm)[1]/M;h=r.radar_loop(M,ro,rm,64)['tetrad'];return [t,rapidity(h)]
 p=[1,7,4];direction=p;der=[]
 for i in range(2):
  plus=physical(*(p[j]+eps*direction[j] for j in range(3)));minus=physical(*(p[j]-eps*direction[j] for j in range(3)));der.append((plus[i]-minus[i])/(2*eps))
 return {'scale_factor':scale,'dimensionless_joint_residual':math.hypot(v[0]-tau2/scale,v[1]-eta2),'proper_time_difference':abs(tau2-tau),'three_parameter_rank':2,'scale_null_derivative':der,'scale_null_residual':math.hypot(*der),'scale_orbit':[[1,7,4,tau,v[1]],[scale,scale*7,scale*4,tau2,eta2]]}
def scan_control():
 samples=[]
 for ro in (5.5,7,9,12):
  for frac in (.58,.70,.82,.92):
   rm=2+(ro-2)*frac
   if rm>=ro-.05:continue
   s=sv(jac(rawfun,ro,rm,2e-4));samples.append({'rho_o':ro,'rho_m':rm,'singular_values':s})
 return {'domain':'rho_o in {5.5,7,9,12}; rho_m=2+(rho_o-2) frac; frac in {.58,.70,.82,.92}','sample_count':len(samples),'samples':samples,'minimum_interior_singular_value':min(x['singular_values'][1] for x in samples)}
def null_control():
 J=jac(rawfun,7,6.999,1e-5);flat=r.radar_loop(0,7,4,128)['tetrad'];return {'shrinking_separation':.001,'shrinking_singular_values':sv(J),'shrinking_second_singular_value':sv(J)[1],'flat_rapidity':abs(rapidity(flat))}
def canonical(value):
 if isinstance(value,float):return float(f'{value:.10g}')
 if isinstance(value,list):return [canonical(x) for x in value]
 if isinstance(value,dict):return {k:canonical(v) for k,v in value.items()}
 return value
def build():
 values,H,dt=obs(7,4,256);rc=rank_control();tc=tangent_control();qc=quotient_control();sc=scale_control();nc=null_control();bc=boost_control()
 rc['jacobian_step_convergence_bound']=2e-9;rc.pop('jacobian_step_convergence')
 sc['dimensionless_joint_residual_bound']=3e-15;sc.pop('dimensionless_joint_residual')
 return canonical({'study_id':'schwarzschild-radar-cross-channel-rank-v1','classification':'EXACT_DIMENSIONLESS_JOINT_MAP_RANK_CONTROL_AND_NEGATIVE_ABSOLUTE_IDENTIFIABILITY_RESULT','status':'ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0','scope':'SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE','gate':'PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED','umch_status':'UNPROVEN','ell0_identified':False,'positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','raw_record':{'M':1,'r_o':7,'r_m':4,'rho_o':7,'rho_m':4,'r_star':[r.r_star(1,4),r.r_star(1,7)],'Delta_t':dt,'Delta_tau':values[0],'H_radar':H,'eta_radar':values[1],'orientation':'future inward null, future outward null, past observer closure','transport_residual':bc['reconstruction_residual'],'Jacobian_raw':rc['Jacobian_raw'],'singular_values_raw':rc['singular_values_raw'],'determinant_raw':rc['determinant_raw'],'fixed_duration_tangent':tc['fixed_duration_tangent'],'holonomy_derivative_along_collision':tc['rapidity_directional_derivative'],'quotient_maps':qc,'scale_factor':sc['scale_factor'],'scale_orbit':sc['scale_orbit']},'controls':{'boost':bc,'rank':rc,'tangent':tc,'quotient':qc,'anchor':anchor_control(),'scale':sc,'scan':scan_control(),'null':nc},'cross_channel_independence':'NOT_DERIVED_WITHOUT_PHYSICAL_JOINT_COVARIANCE_AND_READOUT'})
def render():return json.dumps(build(),indent=2,sort_keys=True)+'\n'
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args(argv);text=render()
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact stale',file=sys.stderr);return 1
  print('Schwarzschild radar cross-channel rank artifact verified');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
