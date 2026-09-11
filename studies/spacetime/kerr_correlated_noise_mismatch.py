#!/usr/bin/env python3
"""Correlated shared-noise cancellation and differential mismatch threshold."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('noise_mismatch_base',HERE/'kerr_reference_drift.py');drift=importlib.util.module_from_spec(S);S.loader.exec_module(drift)
common=drift.common;receiver=drift.receiver
R=[.1,10.];NOISE=[[.4,.12],[.12,.7]];GAIN_MIN=.5;SAFE=.8
RESULT='KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION_BUT_DIFFERENTIAL_MISMATCH_AT_THE_EXACT_CONE_MARGIN_RESTORES_COLLISION_NOT_ELL0'
GATE='PHYSICAL_KERR_SIGNAL_CALIBRATION_NOISE_MATCHING_DRIFT_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def eig2(A):
 t=A[0][0]+A[1][1];q=math.sqrt((A[0][0]-A[1][1])**2+4*A[0][1]**2);return [(t-q)/2,(t+q)/2]
def validate_spd(A):
 if len(A)!=2 or any(len(row)!=2 for row in A)or not all(math.isfinite(x)for row in A for x in row)or abs(A[0][1]-A[1][0])>2e-10 or min(eig2(A))<=0:raise ValueError('finite symmetric positive-definite 2x2 noise required')
 return A
def spd_control():
 vals=eig2(NOISE);bad=([[1.,2.],[0.,1.]],[[1.,2.],[2.,1.]],[[float('nan'),0.],[0.,1.]])
 def reject(x):
  try:validate_spd(x);return False
  except ValueError:return True
 return {'anchor_spd':min(vals)>0,'eigenvalues':vals,'minimum_eigenvalue':min(vals),'invalid_rejected':all(reject(x)for x in bad)}
def joint_difference(o,gains,noise,mismatch=None):
 validate_spd(noise);G=common.gamma(o);M=[[0.,0.],[0.,0.]]if mismatch is None else mismatch;return [[gains[i]*gains[j]*(G[i][j]-(R[i]if i==j else 0.))-M[i][j]for j in range(2)]for i in range(2)]
def shared_noise_cancellation_control():
 gains=[.8,1.1];G=common.gamma(1);S=[[gains[i]*gains[j]*G[i][j]+NOISE[i][j]for j in range(2)]for i in range(2)];B=[[gains[i]*gains[j]*(R[i]if i==j else 0.)+NOISE[i][j]for j in range(2)]for i in range(2)];actual=[[S[i][j]-B[i][j]for j in range(2)]for i in range(2)];return {'noise':NOISE,'actual_difference':actual,'residual':receiver.res(actual,joint_difference(1,gains,NOISE))}
def sign_cone_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];signs=[[gp[i]-R[i]for i in range(2)],[gm[i]-R[i]for i in range(2)]];return {'signed_diagonals':signs,'opposite_definite':max(signs[0])<0<min(signs[1]),'exact_collision_possible':False}
def threshold_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];components=[GAIN_MIN**2*(gm[i]-gp[i])for i in range(2)];full_difference=[[components[i] if i==j else 0. for j in range(2)]for i in range(2)];tau=max(abs(x)for x in eig2(full_difference));return {'components':components,'minimum_gain_full_difference':full_difference,'tau':tau,'boundary_component':components.index(tau),'operator_norm_residual':abs(tau-max(abs(x)for x in eig2(full_difference)))}
def safe_mismatch_control():
 tau=threshold_control()['tau'];bound=SAFE*tau;return {'safe_fraction':SAFE,'aggregate_mismatch_bound':bound,'remaining_separation':tau-bound}
def threshold_collision_control():
 gains=[GAIN_MIN,GAIN_MIN];plus=joint_difference(1,gains,NOISE);minus=joint_difference(-1,gains,NOISE);M=[[plus[i][j]-minus[i][j]for j in range(2)]for i in range(2)];plus_observed=plus;minus_observed=[[minus[i][j]+M[i][j]for j in range(2)]for i in range(2)];signal_plus=[[gains[i]*gains[j]*common.gamma(1)[i][j]+NOISE[i][j]for j in range(2)]for i in range(2)];calibration_plus=[[gains[i]*gains[j]*(R[i]if i==j else 0.)+NOISE[i][j]for j in range(2)]for i in range(2)];minimum_observed=min(eig2(signal_plus)+eig2(calibration_plus));return {'gain':gains,'differential_mismatch':M,'operator_norm':max(abs(x)for x in eig2(M)),'plus_observable':plus_observed,'minus_observable':minus_observed,'observable_collision_residual':receiver.res(plus_observed,minus_observed),'minimum_observed_eigenvalue':minimum_observed}
def basis_scale_control(theta,factor):
 x=threshold_collision_control();tau=threshold_control()['tau'];co=math.cos(theta);si=math.sin(theta);Q=[[co,-si],[si,co]];M=x['differential_mismatch'];rot=receiver.mm(Q,receiver.mm(M,receiver.tr(Q)));basis=abs(max(abs(x)for x in eig2(rot))-tau);scaled_tau=factor*factor*tau;scaled=[[factor*factor*x for x in row]for row in M];scale=abs(max(abs(x)for x in eig2(scaled))/scaled_tau-1.);return {'basis_residual':basis,'scale_residual':scale,'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_CORRELATED_NOISE_MISMATCH_THRESHOLD_NOT_EVIDENCE'}
def scenario_control(name,case):
 table={'mismatch_spd':lambda:(spd_control()['anchor_spd']and spd_control()['invalid_rejected'],spd_control()['minimum_eigenvalue'],0.),'mismatch_cancellation':lambda:(shared_noise_cancellation_control()['residual']<2e-10,shared_noise_cancellation_control()['residual'],2e-10),'mismatch_cones':lambda:(sign_cone_control()['opposite_definite'],0.,1.),'mismatch_threshold':lambda:(threshold_control()['tau']>1.,threshold_control()['tau'],1.),'mismatch_safe':lambda:(safe_mismatch_control()['remaining_separation']>1.,safe_mismatch_control()['remaining_separation'],1.),'mismatch_collision':lambda:(threshold_collision_control()['observable_collision_residual']<2e-10,threshold_collision_control()['observable_collision_residual'],2e-10),'mismatch_basis_scale':lambda:(max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10),'mismatch_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def build_artifact():
 controls=[('spd',spd_control()['anchor_spd']and spd_control()['invalid_rejected'],spd_control()['minimum_eigenvalue'],0.,'minimum'),('cancellation',shared_noise_cancellation_control()['residual']<2e-10,shared_noise_cancellation_control()['residual'],2e-10,'maximum'),('sign_cones',sign_cone_control()['opposite_definite'],0.,1.,'boolean'),('threshold',threshold_control()['tau']>1.,threshold_control()['tau'],1.,'minimum'),('safe_mismatch',safe_mismatch_control()['remaining_separation']>1.,safe_mismatch_control()['remaining_separation'],1.,'minimum'),('threshold_collision',threshold_collision_control()['observable_collision_residual']<2e-10,threshold_collision_control()['observable_collision_residual'],2e-10,'maximum'),('basis_scale',max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-correlated-noise-mismatch-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'spd':spd_control(),'cancellation':shared_noise_cancellation_control(),'sign_cones':sign_cone_control(),'threshold':threshold_control(),'safe_mismatch':safe_mismatch_control(),'threshold_collision':threshold_collision_control(),'basis_scale':basis_scale_control(.37,2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
