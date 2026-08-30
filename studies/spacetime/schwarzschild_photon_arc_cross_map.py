#!/usr/bin/env python3
"""Finite photon-sphere open-arc connection/Jacobi cross-map; no UMCH evidence."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
def local(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
m=local('mixed_arc','schwarzschild_mixed_levi_civita_holonomy.py')
hol=local('photon_orbit_arc','schwarzschild_photon_orbit_holonomy.py')
jac=local('photon_jacobi_arc','schwarzschild_photon_sphere_jacobi.py')
OUT=HERE/'schwarzschild-photon-arc-cross-map-results.json'
ETA=m.diag([-1,1,1,1])
STATUS='SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_CONNECTION_JACOBI_CROSS_MAP_CAUSTIC_LANDMARKED_LOCALLY_ONE_SHAPE_DIRECTION_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0'
SCOPE='FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_CONNECTION_AND_SCREEN_PHASE_MAP_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_ENDPOINT_BASES_AND_NO_DETECTOR_READOUT'
GATE='PHYSICAL_FINITE_ARC_WINDOW_SELECTION_SOURCE_OBSERVER_TETRADS_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED'
def arc_params(M=1.,alpha=math.pi/3,orientation=1,affine_factor=1.):
 return {'M':M,'r_ph':3*M,'alpha':alpha,'orientation':orientation,'L':3*M*alpha*affine_factor,'delta_phi':orientation*alpha,'delta_t':3*math.sqrt(3)*M*alpha}
def geometry_control(alpha=math.pi/3,M=1.,orientation=1):
 x=arc_params(M,alpha,orientation);E=m.tetrad(M,x['r_ph']);k=[E[i][0]+orientation*E[i][3] for i in range(4)];g=m.metric(M,x['r_ph'])
 null=sum(g[i][j]*k[i]*k[j] for i in range(4) for j in range(4));acc=[sum(m.gamma(M,x['r_ph'],mu)[a][nu]*k[mu]*k[nu] for mu in range(4) for nu in range(4)) for a in range(4)]
 return {**x,'k_tetrad':[1.,0.,0.,float(orientation)],'k_coordinate':k,'null_residual':abs(null),'geodesic_residual':max(abs(z) for z in acc),'closed_arc':alpha>0 and abs(alpha/(2*math.pi)-round(alpha/(2*math.pi)))<1e-12,'affine_normalization':'STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR'}
def connection_generator(M=1.,orientation=1):
 r=3*M;return m.scale(m.add(m.scale(m.gamma(M,r,0),3*math.sqrt(3)*M),m.scale(m.gamma(M,r,3),orientation)),-1)
def connection_tetrad_generator(M=1.,orientation=1):
 E=m.tetrad(M,3*M);return m.mm(m.inverse_diag(E),m.mm(connection_generator(M,orientation),E))
def connection_arc(M=1.,alpha=math.pi/3,orientation=1):
 E=m.tetrad(M,3*M);T=m.expm(m.scale(connection_generator(M,orientation),alpha));return m.mm(m.inverse_diag(E),m.mm(T,E))
def phase_arc(M=1.,alpha=math.pi/3,orientation=1,affine_factor=1.):
 K=jac.optical_K(M,orientation,affine_factor);return m.expm(m.scale(jac.phase_generator(K),3*M*alpha*affine_factor))
def numerical_connection(M,alpha,orientation,steps=1600):
 T=hol.numerical_segment(M,3*M,3*math.sqrt(3)*M*alpha,orientation*alpha,steps);E=m.tetrad(M,3*M);return m.mm(m.inverse_diag(E),m.mm(T,E))
def lorentz_residual(T):return m.norm(m.sub(m.mm(m.transpose(T),m.mm(ETA,T)),ETA))
def symplectic_residual(P):return m.norm(m.sub(m.mm(m.transpose(P),m.mm(jac.J,P)),jac.J))
def raw_map_control(alpha=math.pi/3,M=1.,orientation=1):
 T=connection_arc(M,alpha,orientation);P=phase_arc(M,alpha,orientation);K=jac.optical_K(M,orientation);Pn=jac.rk4_phase(K,3*M*alpha,3000 if alpha else 1);Tn=numerical_connection(M,alpha,orientation,1200 if alpha else 1)
 A,B,C,D=jac.split(P)
 return {'alpha':alpha,'T_arc':T,'P_arc':P,'A':A,'B':B,'C':C,'D':D,'connection_generator':connection_tetrad_generator(M,orientation),'phase_generator':jac.phase_generator(K),'connection_characteristic_coefficients':m.characteristic(T),'phase_characteristic_coefficients':m.characteristic(P),'connection_exact_numerical_residual':m.norm(m.sub(T,Tn)),'phase_exact_numerical_residual':m.norm(m.sub(P,Pn)),'lorentz_residual':lorentz_residual(T),'symplectic_residual':symplectic_residual(P),'phase_determinant':m.determinant(P)}
def zero_window_control():
 T=connection_arc(alpha=0);P=phase_arc(alpha=0);h=1e-7;Td=m.scale(m.sub(connection_arc(alpha=h),T),1/h);Pd=m.scale(m.sub(phase_arc(alpha=h),P),1/h)
 return {'connection_identity_residual':m.norm(m.sub(T,m.eye())),'phase_identity_residual':m.norm(m.sub(P,m.eye())),'connection_generator_residual':m.norm(m.sub(Td,connection_tetrad_generator())),'phase_generator_residual':m.norm(m.sub(Pd,m.scale(jac.phase_generator(jac.optical_K()),3.)))}
def composition_control(alpha=.7,beta=1.1):
 Ta=connection_arc(alpha=alpha);Tb=connection_arc(alpha=beta);Tab=connection_arc(alpha=alpha+beta);Pa=phase_arc(alpha=alpha);Pb=phase_arc(alpha=beta);Pab=phase_arc(alpha=alpha+beta)
 return {'alpha':alpha,'beta':beta,'connection_composition_residual':m.norm(m.sub(Tab,m.mm(Tb,Ta))),'phase_composition_residual':m.norm(m.sub(Pab,m.mm(Pb,Pa)))}
def caustic_control():
 controls=[]
 for alpha in [math.pi,2*math.pi]:
  P=phase_arc(alpha=alpha);A,B,C,D=jac.split(P);controls.append({'alpha':alpha,'endpoint_X_determinant_abs':abs(jac.det2(B)),'S_vertex':jac.safe_graph(B,D),'full_map_inverse_residual':m.norm(m.sub(m.mm(P,phase_arc(alpha=-alpha)),m.eye()))})
 P=phase_arc(alpha=math.pi/3);A,B,C,D=jac.split(P);S0=[[.2,0.],[0.,-.1]];X=jac.add2(A,jac.mm2(B,S0));V=jac.add2(C,jac.mm2(D,S0))
 return {'conjugate_angles':[math.pi,2*math.pi],'controls':controls,'nonvertex':{'alpha':math.pi/3,'S0':S0,'S_nonvertex':jac.safe_graph(X,V)}}
def rotation4(angle):
 c=math.cos(angle);s=math.sin(angle);return [[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,c,-s],[0.,0.,s,c]]
def orientation_endpoint_control(alpha=math.pi/3):
 Tp=connection_arc(alpha=alpha,orientation=1);Tn=connection_arc(alpha=alpha,orientation=-1);Pp=phase_arc(alpha=alpha,orientation=1);Pn=phase_arc(alpha=alpha,orientation=-1)
 G=rotation4(.37);acted=m.mm(G,m.mm(Tp,m.transpose(G)));q=[[math.cos(.31),-math.sin(.31)],[math.sin(.31),math.cos(.31)]];Q=jac.block_diag(q,q);pacted=m.mm(Q,m.mm(Pp,m.transpose(Q)))
 return {'connection_raw_orientation_difference':m.norm(m.sub(Tp,Tn)),'connection_characteristic_orientation_collision':math.sqrt(sum((a-b)**2 for a,b in zip(m.characteristic(Tp),m.characteristic(Tn)))),'phase_orientation_collision':m.norm(m.sub(Pp,Pn)),'connection_endpoint_raw_difference':m.norm(m.sub(acted,Tp)),'connection_endpoint_characteristic_collision':math.sqrt(sum((a-b)**2 for a,b in zip(m.characteristic(acted),m.characteristic(Tp)))),'phase_endpoint_raw_difference':m.norm(m.sub(pacted,Pp)),'phase_endpoint_symplectic_residual':symplectic_residual(pacted),'connection_endpoint_action':'T_TO_G_T_G_INVERSE_COMMON_CONJUGACY_CONTROL','phase_endpoint_action':'P_TO_Q_P_Q_INVERSE_COMMON_SCREEN_CONTROL'}
def rate_matrix(scale):return jac.block_diag(jac.eye2(),jac.scale2(jac.eye2(),1/scale))
def converted_phase(P,scale):return m.mm(rate_matrix(1/scale),m.mm(P,rate_matrix(scale)))
def affine_scale_control(alpha=math.pi/3,factor=1.7):
 P=phase_arc(alpha=alpha);Pa=phase_arc(alpha=alpha,affine_factor=factor);pred=m.mm(rate_matrix(factor),m.mm(P,rate_matrix(1/factor)))
 return {'affine_factor':factor,'phase_dimensionless_residual':m.norm(m.sub(Pa,pred)),'raw_rate_block_difference':m.norm(m.sub(Pa,P)),'rate_conversion':'D_A_EQUALS_DIAG_I_I_OVER_A'}
def geometric_scale_control(alpha=math.pi/3,scale_factor=2.4):
 T=connection_arc(1,alpha);Ts=connection_arc(scale_factor,alpha);P=phase_arc(1,alpha);Ps=phase_arc(scale_factor,alpha);pred=m.mm(rate_matrix(scale_factor),m.mm(P,rate_matrix(1/scale_factor)));x=arc_params(1,alpha);y=arc_params(scale_factor,alpha)
 return {'scale_factor':scale_factor,'connection_dimensionless_residual':m.norm(m.sub(Ts,T)),'phase_dimensionless_residual':m.norm(m.sub(Ps,pred)),'affine_length_difference':y['L']-x['L'],'coordinate_duration_difference':y['delta_t']-x['delta_t'],'scale_orbit':'(M,r_ph,L,Delta_t)->s(M,r_ph,L,Delta_t)_WITH_PHASE_RATE_CONVERSION','ell0_identified':False}
def feature(alpha,M):
 T=connection_arc(M,alpha);P=phase_arc(M,alpha);Pc=m.mm(rate_matrix(1/M),m.mm(P,rate_matrix(M)))
 return m.characteristic(T)[1:]+m.characteristic(Pc)[1:]
def jacobian(alpha,M=1.,h=1e-5):
 def f(a,lm):return feature(a,math.exp(lm))
 ap=f(alpha+h,math.log(M));am=f(alpha-h,math.log(M));mp=f(alpha,math.log(M)+h);mmn=f(alpha,math.log(M)-h)
 return [[(ap[i]-am[i])/(2*h),(mp[i]-mmn[i])/(2*h)] for i in range(len(ap))]
def singular_values(J):
 a=sum(r[0]*r[0] for r in J);b=sum(r[0]*r[1] for r in J);d=sum(r[1]*r[1] for r in J);disc=math.sqrt(max(0,(a-d)**2+4*b*b));return [math.sqrt(max(0,(a+d+disc)/2)),math.sqrt(max(0,(a+d-disc)/2))]
def joint_rank_control(alpha=math.pi/3):
 J=jacobian(alpha,h=1e-5);J2=jacobian(alpha,h=5e-6);sv=singular_values(J)
 return {'parameters':['alpha','log_M'],'joint_feature_map':feature(alpha,1.),'Jacobian_joint':J,'singular_values_joint':sv,'rank_joint':sum(x>1e-7 for x in sv),'scale_column_norm':math.sqrt(sum(r[1]**2 for r in J)),'jacobian_step_convergence':math.sqrt(sum((J[i][j]-J2[i][j])**2 for i in range(len(J)) for j in range(2))),'scale_null_direction':[0.,1.],'independent_channels':False}
def collision_control(alpha=.45):
 P=phase_arc(alpha=alpha);Q=phase_arc(alpha=alpha+2*math.pi);_,_,_,D=jac.split(P);_,_,_,E=jac.split(Q);ell=lambda X:[[X[1][1],X[1][3]],[X[3][1],X[3][3]]]
 return {'alpha_pair':[alpha,alpha+2*math.pi],'phase_elliptic_periodic_collision':m.norm([[ell(P)[i][j]-ell(Q)[i][j] for j in range(2)] for i in range(2)]),'phase_full_map_difference':m.norm(m.sub(P,Q)),'joint_feature_difference':math.sqrt(sum((a-b)**2 for a,b in zip(feature(alpha,1),feature(alpha+2*math.pi,1)))),'global_joint_collision':False}
def closed_loop_cross_check():
 alpha=2*math.pi;T=connection_arc(alpha=alpha);old=hol.orbit();E=m.tetrad(1,3);oldnull=m.mm(m.inverse_diag(E),m.mm(old['tn'],E));closed=m.mm(m.inverse_diag(E),m.mm(old['tc'],m.mm(m.tetrad(1,3),T)))
 return {'future_null_segment_residual':m.norm(m.sub(T,oldnull)),'closed_loop_residual':m.norm(m.sub(closed,old['tetrad'])),'primary_object':'OPEN_ARC_ENDPOINT_TRANSPORT_NOT_HOLONOMY','closure_role':'DERIVED_PAST_DIRECTED_STATIC_CLOSURE_CROSS_CHECK_ONLY'}
def build():
 alpha=math.pi/3;raw=raw_map_control(alpha);return {'classification':'EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':STATUS,'scope':SCOPE,'gate':GATE,'hypothesis':'UNPROVEN','detection':'NO_POSITIVE_DETECTION_CLAIM','ell0_identified':False,'structural_dead_end':'NOT_DECLARED','confirmatory_state':'CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','primary_objects':['T_arc','P_arc'],'geometry':geometry_control(alpha),'raw_maps':raw,'zero_window_controls':zero_window_control(),'composition_controls':composition_control(),'caustic_controls':caustic_control(),'orientation_endpoint_controls':orientation_endpoint_control(alpha),'affine_scale_controls':affine_scale_control(alpha),'geometric_scale_controls':geometric_scale_control(alpha),'joint_rank':joint_rank_control(alpha),'collision_controls':collision_control(),'closed_loop_cross_check':closed_loop_cross_check(),'source_scope':{'Darwin1959GravityField':'Schwarzschild trajectory and critical circular-orbit context only','Sachs1961':'null optical framework only','not_supported':['finite-arc protocol','endpoint tetrads','detector','covariance','ell0','UMCH','detection']},'open_routes':['GENERIC_NONRADIAL_SCHWARZSCHILD_SCATTERING','FREELY_FALLING_ENDPOINTS','PHYSICAL_DETECTOR_READOUT_AND_COVARIANCE']}
def render():return json.dumps(build(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();text=render()
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact mismatch',file=sys.stderr);return 1
 else:OUT.write_text(text)
 return 0
if __name__=='__main__':raise SystemExit(main())
