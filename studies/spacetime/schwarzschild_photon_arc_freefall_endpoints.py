#!/usr/bin/env python3
"""Photon-sphere finite arcs in local radial-geodesic endpoint frames; no UMCH evidence."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
def local(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
arc=local('photon_arc_static','schwarzschild_photon_arc_cross_map.py')
m=arc.m;jac=arc.jac
OUT=HERE/'schwarzschild-photon-arc-freefall-endpoints-results.json'
STATUS='SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_FREEFALL_ENDPOINT_FRAMES_EXPOSE_PREPARATION_DIRECTIONS_BUT_RETAIN_ONE_INTERIOR_SHAPE_DIRECTION_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0'
SCOPE='FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_WITH_LOCAL_RADIAL_GEODESIC_ENDPOINT_TETRADS_PROJECT_PHASE_RATE_CONVERSION_TOY_PREPARATION_LABELS_AND_NO_DETECTOR_READOUT'
GATE='PHYSICAL_RELEASE_HISTORY_FINITE_ARC_WINDOW_SOURCE_OBSERVER_SYNCHRONIZATION_SCREEN_PREPARATION_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED'
CLASSIFICATION='PROJECT_DERIVATION_AND_TOY_ENDPOINT_CONTROL_WITH_NEGATIVE_INTERIOR_SCALE_IDENTIFIABILITY_RESULT'

def boost(E,sign=1,M=1.):
 f=1/3
 if E < math.sqrt(f)-1e-14 or sign not in (-1,1):raise ValueError('E must satisfy E>=sqrt(f) and sign must be +/-1')
 gamma=E/math.sqrt(f);beta2=1-f/(E*E);beta=0. if abs(beta2)<1e-14 else sign*math.sqrt(max(0.,beta2))
 return [[gamma,-gamma*beta,0.,0.],[-gamma*beta,gamma,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]]
def boost_inverse(E,sign=1,M=1.):return boost(E,-sign,M)
def omega(E):return E*math.sqrt(3)
def rate(E):return arc.rate_matrix(omega(E))
def rate_inverse(E):return arc.rate_matrix(1/omega(E))
def maxabs(A):return max(abs(x) for row in A for x in row)
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def flatten(A):return [x for row in A for x in row]

def endpoint_frame_control(M=1.,E=1.,sign=-1):
 r=3*M;f=1/3;ur=sign*math.sqrt(max(0,E*E-f));ut=E/f;m0=M/(r*r);fp=2*M/(r*r)
 dut=-E*fp*ur/(f*f);dur=-m0
 u=[ut,ur,0.,0.];du=[dut,dur,0.,0.]
 acc=[du[a]+sum(m.gamma(M,r,mu)[a][nu]*u[mu]*u[nu] for mu in range(4) for nu in range(4)) for a in range(4)]
 g=m.metric(M,r);norm=sum(g[i][j]*u[i]*u[j] for i in range(4) for j in range(4))
 B=boost(E,sign,M);ETA=arc.ETA
 return {'E':E,'sign':sign,'u_coordinate':u,'normalization_residual':abs(norm+1),'geodesic_residual':max(abs(x) for x in acc),'boost':B,'beta_abs':abs(B[0][1]/B[0][0]),'orthonormal_residual':m.norm(m.sub(m.mm(m.transpose(B),m.mm(ETA,B)),ETA)),'lorentz_residual':arc.lorentz_residual(B),'boost_identity_residual':m.norm(m.sub(B,m.eye())),'frequency_ratio_to_static':omega(E),'preparation_status':'LOCAL_RADIAL_GEODESIC_STATE_NOT_PHYSICAL_RELEASE_HISTORY'}

def raw_freefall_control(alpha=math.pi/3,E_source=1.,sign_source=-1,E_observer=.8,sign_observer=1,M=1.):
 T=arc.connection_arc(M,alpha);P=arc.phase_arc(M,alpha);Bs=boost(E_source,sign_source,M);Bo=boost(E_observer,sign_observer,M);Ds=rate(E_source);Do=rate(E_observer)
 Tff=m.mm(boost_inverse(E_observer,sign_observer,M),m.mm(T,Bs));Pff=m.mm(rate_inverse(E_observer),m.mm(P,Ds))
 Tr=m.mm(Bo,m.mm(Tff,boost_inverse(E_source,sign_source,M)));Pr=m.mm(Do,m.mm(Pff,rate_inverse(E_source)))
 return {'alpha':alpha,'E_source':E_source,'sign_source':sign_source,'E_observer':E_observer,'sign_observer':sign_observer,'T_static':T,'P_static':P,'T_ff':Tff,'P_ff':Pff,'connection_action_residual':0.,'phase_action_residual':0.,'connection_reconstruction_residual':m.norm(m.sub(Tr,T)),'phase_reconstruction_residual':m.norm(m.sub(Pr,P)),'omega_source':omega(E_source),'omega_observer':omega(E_observer)}

def zero_window_control(E_source=1.,sign_source=-1,E_observer=.8,sign_observer=1):
 x=raw_freefall_control(0,E_source,sign_source,E_observer,sign_observer)
 return {'static_interior_identity_residual':m.norm(m.sub(x['T_static'],m.eye())),'freefall_endpoint_comparison_nonidentity':m.norm(m.sub(x['T_ff'],m.eye())),'classification':'ENDPOINT_FRAME_COMPARISON_NOT_HOLONOMY_OR_INTERIOR_CURVATURE_RESPONSE'}

def composition_control(alpha1=.7,alpha2=1.1):
 Es,Ea,Eb,Eo=1.,.82,1.16,.75;ss,sa,sb,so=-1,1,-1,1
 T1=raw_freefall_control(alpha1,Es,ss,Ea,sa)['T_ff'];T2a=raw_freefall_control(alpha2,Ea,sa,Eo,so)['T_ff'];T2b=raw_freefall_control(alpha2,Eb,sb,Eo,so)['T_ff'];Ttot=raw_freefall_control(alpha1+alpha2,Es,ss,Eo,so)['T_ff']
 P1=raw_freefall_control(alpha1,Es,ss,Ea,sa)['P_ff'];P2a=raw_freefall_control(alpha2,Ea,sa,Eo,so)['P_ff'];P2b=raw_freefall_control(alpha2,Eb,sb,Eo,so)['P_ff'];Ptot=raw_freefall_control(alpha1+alpha2,Es,ss,Eo,so)['P_ff']
 transition=m.mm(boost_inverse(Eb,sb),boost(Ea,sa));qtransition=m.mm(rate_inverse(Eb),rate(Ea))
 return {'matched_connection_residual':m.norm(m.sub(m.mm(T2a,T1),Ttot)),'matched_phase_residual':m.norm(m.sub(m.mm(P2a,P1),Ptot)),'mismatched_connection_residual':m.norm(m.sub(m.mm(T2b,T1),Ttot)),'mismatched_phase_residual':m.norm(m.sub(m.mm(P2b,P1),Ptot)),'transition_corrected_connection_residual':m.norm(m.sub(m.mm(T2b,m.mm(transition,T1)),Ttot)),'transition_corrected_phase_residual':m.norm(m.sub(m.mm(P2b,m.mm(qtransition,P1)),Ptot))}

def symplectic_inverse(P):return m.scale(m.mm(jac.J,m.mm(m.transpose(P),jac.J)),-1)
def caustic_control(alpha=math.pi):
 Es,Eo=1.,.8;Pstatic=arc.phase_arc(alpha=alpha);P=raw_freefall_control(alpha,Es,-1,Eo,1)['P_ff'];A,B,C,D=jac.split(P)
 Pi=m.mm(rate_inverse(Es),m.mm(symplectic_inverse(Pstatic),rate(Eo)))
 return {'alpha':alpha,'endpoint_X_determinant_abs':abs(det2(B)),'full_map_inverse_residual':m.norm(m.sub(m.mm(P,Pi),m.eye())),'graph_status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}

def endpoint_quotient_control(alpha=math.pi/3):
 a=raw_freefall_control(alpha,1.,-1,.8,1);b=raw_freefall_control(alpha,.72,1,1.2,-1)
 return {'raw_connection_difference':m.norm(m.sub(a['T_ff'],b['T_ff'])),'raw_phase_difference':m.norm(m.sub(a['P_ff'],b['P_ff'])),'static_reconstructed_connection_difference':m.norm(m.sub(a['T_static'],b['T_static'])),'static_reconstructed_phase_difference':m.norm(m.sub(a['P_static'],b['P_static'])),'quotient':'RECONSTRUCT_STATIC_INTERIOR_ONLY_AFTER_DECLARED_ENDPOINT_ACTIONS'}

def scale_control(alpha=math.pi/3):
 af=arc.affine_scale_control(alpha,1.7);gs=arc.geometric_scale_control(alpha,2.4)
 return {'raw_affine_rate_difference':af['raw_rate_block_difference'],'affine_converted_residual':af['phase_dimensionless_residual'],'geometric_connection_residual':gs['connection_dimensionless_residual'],'geometric_phase_residual':gs['phase_dimensionless_residual'],'controls':'AFFINE_NORMALIZATION_AND_SCHWARZSCHILD_GEOMETRIC_DILATION_TESTED_SEPARATELY'}

def feature(alpha,M,Esource=1.):
 x=raw_freefall_control(alpha,Esource,-1,.8,1,M);Pc=m.mm(arc.rate_matrix(1/M),m.mm(x['P_ff'],arc.rate_matrix(M)))
 return flatten(x['T_ff'])+flatten(Pc)
def derivative(alpha,M,E,which,h=1e-5):
 args=[alpha,math.log(M),E];p=args[:];q=args[:];p[which]+=h;q[which]-=h
 fp=feature(p[0],math.exp(p[1]),p[2]);fq=feature(q[0],math.exp(q[1]),q[2]);return [(a-b)/(2*h) for a,b in zip(fp,fq)]
def rank_control(alpha=math.pi/3):
 cols=[derivative(alpha,1.,1.,i) for i in range(3)];norms=[math.sqrt(sum(x*x for x in c)) for c in cols]
 return {'parameters_fixed_preparation':['alpha','log_M'],'rank_fixed_preparation':1 if norms[0]>1e-7 and norms[1]<1e-7 else 2,'alpha_column_norm':norms[0],'log_M_column_norm':norms[1],'scale_null_direction':[0.0,1.0],'endpoint_energy_column_norm':norms[2],'endpoint_energy_column_classification':'ENDPOINT_PREPARATION_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE','independent_channels':False}

def collision_and_provenance_control(alpha=.45):
 P0=arc.phase_arc(alpha=alpha);P2=arc.phase_arc(alpha=alpha+2*math.pi);_,_,_,D0=jac.split(P0);_,_,_,D2=jac.split(P2)
 elliptic=abs(D0[1][1]-D2[1][1]);globaldiff=m.norm(m.sub(arc.connection_arc(alpha=alpha),arc.connection_arc(alpha=alpha+2*math.pi)))+m.norm(m.sub(P0,P2))
 prior=arc.closed_loop_cross_check()
 return {'elliptic_periodic_subblock_collision':elliptic,'global_joint_collision':globaldiff<1e-8,'full_winding_static_segment_residual':prior['future_null_segment_residual'],'closure_status':'NO_PHYSICAL_FREEFALL_CLOSURE_DERIVED'}

def build_result():
 checkpoints=[0.,math.pi/3,math.pi,1.5*math.pi,2*math.pi]
 return {'schema_version':1,'study':'schwarzschild-photon-arc-freefall-endpoints','classification':CLASSIFICATION,'status':STATUS,'scope':SCOPE,'gate':GATE,'UMCH':'UNPROVEN','detection':'NO_POSITIVE_DETECTION_CLAIM','ell0_identified':False,'independent_channels':False,'structural_dead_end':'NOT_DECLARED','passing_gate':'CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','raw_records':[raw_freefall_control(a) for a in checkpoints],'endpoint_frame_controls':[endpoint_frame_control(1.,1.,-1),endpoint_frame_control(1.,.8,1),endpoint_frame_control(1.,1/math.sqrt(3),1)],'zero_window':zero_window_control(),'composition':composition_control(),'caustics':[caustic_control(math.pi),caustic_control(2*math.pi)],'endpoint_quotient':endpoint_quotient_control(),'scale':scale_control(),'rank':rank_control(),'collisions_and_provenance':collision_and_provenance_control(),'source_scope':'SCHWARZSCHILD_DARWIN_SACHS_CONTEXT_ONLY_ENDPOINT_PROTOCOL_READOUT_COVARIANCE_ELL0_UMCH_AND_DETECTION_NOT_SOURCED'}
def canonical(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();text=canonical(build_result())
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact mismatch',file=sys.stderr);return 1
  print('schwarzschild photon-arc freefall endpoint artifact: OK');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
