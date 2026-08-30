#!/usr/bin/env python3
"""Bounded Schwarzschild photon-sphere transport control; no detector or UMCH claim."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('mixed',HERE/'schwarzschild_mixed_levi_civita_holonomy.py');m=importlib.util.module_from_spec(S);S.loader.exec_module(m)
OUT=HERE/'schwarzschild-photon-orbit-holonomy-results.json'
ETA=m.diag([-1,1,1,1])
def params(M=1.0,orientation=1,winding=1):
 r=3*M;dp=orientation*2*math.pi*winding;dt=abs(dp)*3*math.sqrt(3)*M
 return r,dp,dt,dt/math.sqrt(3)
def generators(M=1.0,orientation=1,winding=1):
 r,dp,dt,proper=params(M,orientation,winding);gt=m.gamma(M,r,0);gp=m.gamma(M,r,3)
 an=m.scale(m.add(m.scale(gt,dt),m.scale(gp,dp)),-1);ac=m.scale(gt,dt)
 return {'r':r,'dp':dp,'dt':dt,'proper':proper,'gt':gt,'gp':gp,'an':an,'ac':ac}
def orbit(M=1.0,orientation=1,winding=1):
 x=generators(M,orientation,winding);tn=m.expm(x['an']);tc=m.expm(x['ac']);hc=m.mm(tc,tn);E=m.tetrad(M,x['r']);H=m.mm(m.inverse_diag(E),m.mm(hc,E))
 return {**x,'tn':tn,'tc':tc,'coordinate':hc,'tetrad':H}
def numerical_segment(M,r,dt,dp,steps=1024):
 return m.segment_transport(M,m.point(0,r,0),m.point(dt,r,dp),steps)
def numerical_orbit(M=1.0,orientation=1,winding=1,steps=1024):
 r,dp,dt,_=params(M,orientation,winding);tn=numerical_segment(M,r,dt,dp,steps);tc=numerical_segment(M,r,-dt,0,steps);hc=m.mm(tc,tn);E=m.tetrad(M,r)
 return tn,tc,m.mm(m.inverse_diag(E),m.mm(hc,E))
def causal_control():
 M=1.;r,dp,dt,proper=params(M);v=[dt/dp,0,0,1];g=m.metric(M,r);null=sum(g[i][j]*v[i]*v[j] for i in range(4) for j in range(4));acc=[]
 for a in range(4):acc.append(sum(m.gamma(M,r,mu)[a][nu]*v[mu]*v[nu] for mu in range(4) for nu in range(4)))
 return {'photon_radius':r,'null_residual':abs(null),'geodesic_residual':acc,'maximum_geodesic_residual':max(abs(z) for z in acc),'coordinate_duration':dt,'proper_duration':proper}
def transport_control():
 a=orbit();tn,tc,H=numerical_orbit()
 return {'null_segment_transport_residual':m.norm(m.sub(a['tn'],tn)),'closure_segment_transport_residual':m.norm(m.sub(a['tc'],tc)),'maximum_segment_transport_residual':max(m.norm(m.sub(a['tn'],tn)),m.norm(m.sub(a['tc'],tc))),'loop_transport_residual':m.norm(m.sub(a['tetrad'],H))}
def geometry_control():
 H=orbit()['tetrad'];return {'lorentz_residual':m.norm(m.sub(m.mm(m.transpose(H),m.mm(ETA,H)),ETA)),'nonidentity_norm':m.norm(m.sub(H,m.eye()))}
def reversal_control():
 a=orbit();rev=m.mm(m.expm(m.scale(a['an'],-1)),m.expm(m.scale(a['ac'],-1)));E=m.tetrad(1,3);Hr=m.mm(m.inverse_diag(E),m.mm(rev,E))
 return {'H_reverse':Hr,'inverse_residual':m.norm(m.sub(m.mm(Hr,a['tetrad']),m.eye()))}
def ordering_control():
 a=orbit();x=m.mm(a['tn'],a['tc'])
 return {'ordered_reverse':x,'segment_commutator_norm':m.norm(m.sub(m.mm(a['tc'],a['tn']),m.mm(a['tn'],a['tc']))),'ordered_product_difference':m.norm(m.sub(a['coordinate'],x)),'ordering_independent_channel':False}
def winding_control():
 one=orbit();two=orbit(winding=2);rep=m.mm(one['tetrad'],one['tetrad'])
 return {'one_winding':one['tetrad'],'two_winding':two['tetrad'],'repeated_complete_loop':rep,'two_winding_nonidentity_norm':m.norm(m.sub(two['tetrad'],m.eye())),'batched_vs_repeated_loop_difference':m.norm(m.sub(two['tetrad'],rep)),'continuous_geometric_rank_from_winding':0,'winding_role':'DISCRETE_PROTOCOL_LABEL'}
def orientation_control():
 p=orbit(orientation=1)['tetrad'];q=orbit(orientation=-1)['tetrad'];cp=m.characteristic(p);cq=m.characteristic(q)
 return {'positive':p,'negative':q,'raw_orientation_difference':m.norm(m.sub(p,q)),'characteristic_collision':math.sqrt(sum((a-b)**2 for a,b in zip(cp,cq))),'orientation_survives_characteristic_quotient':False}
def anchor_control():
 H=orbit()['tetrad'];c=math.cos(.41);s=math.sin(.41);Q=[[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]];Hq=m.mm(m.transpose(Q),m.mm(H,Q));a=m.characteristic(H);b=m.characteristic(Hq)
 return {'conjugated':Hq,'raw_conjugacy_difference':m.norm(m.sub(H,Hq)),'characteristic_collision':math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))}
def scale_control(scale_factor=1.47):
 a=orbit(1);b=orbit(scale_factor);return {'scale_factor':scale_factor,'dimensionless_duration_residual':abs(a['proper']-b['proper']/scale_factor),'holonomy_residual':m.norm(m.sub(a['tetrad'],b['tetrad'])),'proper_duration_difference':abs(b['proper']-a['proper']),'ell0_identified':False,'scale_orbit':'(M,r,Delta_t,Delta_tau)->s(M,r,Delta_t,Delta_tau)'}
def partial_loop(eps):
 M=1.;r=3.;dp=eps;dt=abs(dp)*3*math.sqrt(3);gt=m.gamma(M,r,0);gp=m.gamma(M,r,3)
 tn=m.expm(m.scale(m.add(m.scale(gt,dt),m.scale(gp,dp)),-1));tc=m.expm(m.scale(gt,dt));ta=m.expm(m.scale(gp,dp));E=m.tetrad(M,r)
 return m.mm(m.inverse_diag(E),m.mm(m.mm(ta,m.mm(tc,tn)),E))
def null_control():
 f=partial_loop(.4);s=partial_loop(1e-4)
 return {'finite_arc_nonidentity_norm':m.norm(m.sub(f,m.eye())),'shrinking_arc_nonidentity_norm':m.norm(m.sub(s,m.eye())),'partial_arc_scope':'MATHEMATICAL_NULL_ARC_WITH_STATIC_CLOSURE_NOT_CLOSED_NULL_GEODESIC'}
def canonical(x):
 if isinstance(x,float):return float(f'{x:.10g}')
 if isinstance(x,list):return [canonical(y) for y in x]
 if isinstance(x,dict):return {k:canonical(v) for k,v in x.items()}
 return x
def build():
 a=orbit();r=reversal_control();o=ordering_control();w=winding_control();sc=scale_control()
 raw={'M':1.0,'r_ph':a['r'],'f_ph':1/3,'tetrad':m.tetrad(1,3),'orientation':1,'winding':1,'Delta_phi':a['dp'],'Delta_t':a['dt'],'Delta_tau':a['proper'],'null_tangent':[a['dt']/a['dp'],0,0,1],'null_residual':causal_control()['null_residual'],'geodesic_residual':causal_control()['geodesic_residual'],'Gamma_t':a['gt'],'Gamma_phi':a['gp'],'A_null':a['an'],'A_closure':a['ac'],'T_null':a['tn'],'T_closure':a['tc'],'H_photon':a['tetrad'],'ordered_reverse':o['ordered_reverse'],'H_reverse':r['H_reverse'],'characteristic_coefficients':m.characteristic(a['tetrad']),'winding_products':w,'scale_factor':sc['scale_factor'],'scale_orbit':sc['scale_orbit']}
 return canonical({'classification':'EXACT_NONRADIAL_NULL_ORBIT_LEVI_CIVITA_HOLONOMY_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL','status':'SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0','scope':'FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT','gate':'PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED','raw':raw,'controls':{'causal':causal_control(),'transport':transport_control(),'geometry':geometry_control(),'reversal':r,'ordering':o,'winding':w,'orientation':orientation_control(),'anchor':anchor_control(),'scale':sc,'null':null_control()},'umch_status':'UNPROVEN','ell0_identified':False,'positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED'})
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,default=OUT);a=p.parse_args();a.output.write_text(json.dumps(build(),indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
