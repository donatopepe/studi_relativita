#!/usr/bin/env python3
"""Finite-sample Gaussian covariance uncertainty for Kerr calibrated receiver toy."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('finite_sample_base',HERE/'kerr_correlated_noise_mismatch.py');mismatch=importlib.util.module_from_spec(S);S.loader.exec_module(mismatch)
receiver=mismatch.receiver;common=mismatch.common
COUNTS=[16,64,256];RISK=.05
RESULT='KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING_AND_ONLY_A_CONSERVATIVE_TOY_COUNT_GATE_BOUNDS_BRANCH_COLLISION_SCALE_NOT_ELL0'
GATE='PHYSICAL_KERR_SAMPLE_INDEPENDENCE_GAUSSIANITY_MEAN_ESTIMATION_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def validate(C,N):
 mismatch.validate_spd(C)
 if not isinstance(N,int)or isinstance(N,bool)or N<=0:raise ValueError('positive integer sample count required')
def trace2(C):return C[0][0]+C[1][1]
def trace_square(C):return C[0][0]**2+C[1][1]**2+2*C[0][1]**2
def covariance_mse(C,N):validate(C,N);return (trace2(C)**2+trace_square(C))/N
def fourth_moment_mse(C,N):
 validate(C,N);s=0.
 for i in range(2):
  for j in range(2):s+=(C[i][i]*C[j][j]+C[i][j]*C[i][j])/N
 return s
def covariances():
 g=[.5,.5];N=mismatch.NOISE;R=mismatch.R;out=[]
 for o in (1,-1):
  G=common.gamma(o);out.append([[g[i]*g[j]*G[i][j]+N[i][j]for j in range(2)]for i in range(2)]);out.append([[g[i]*g[j]*(R[i]if i==j else 0.)+N[i][j]for j in range(2)]for i in range(2)])
 return out
def wishart_identity_control():
 values=[(covariance_mse(C,64),fourth_moment_mse(C,64))for C in covariances()];return {'per_covariance':values,'residual':max(abs(a-b)for a,b in values)}
def total_coefficient():return sum(covariance_mse(C,1)for C in covariances())
def combined_rms(N):return math.sqrt(total_coefficient()/N)
def rms_control():
 x=[combined_rms(N)for N in COUNTS];return {'sample_counts':COUNTS,'rms_frobenius':x,'strictly_decreasing':all(x[i+1]<x[i]for i in range(2)),'tau':mismatch.threshold_control()['tau']}
def scaling_control():
 x=rms_control()['rms_frobenius'];rat=[x[0]/x[1],x[1]/x[2]];return {'ratios':rat,'expected':[2.,2.],'ratio_residual':max(abs(z-2.)for z in rat)}
def risk_bound(N):return total_coefficient()/(N*mismatch.threshold_control()['tau']**2)
def safe_count_control():
 n=math.ceil(total_coefficient()/(RISK*mismatch.threshold_control()['tau']**2));return {'risk_ceiling':RISK,'minimum_count':n,'risk_at_count':risk_bound(n),'risk_at_predecessor':risk_bound(n-1)}
def safe_unsafe_control():return {'N16_risk':risk_bound(16),'N16_passes':risk_bound(16)<=RISK,'N64_risk':risk_bound(64),'N64_passes':risk_bound(64)<=RISK}
def basis_scale_control(theta,factor):
 Cs=covariances();co=math.cos(theta);si=math.sin(theta);Q=[[co,-si],[si,co]];rot=[receiver.mm(Q,receiver.mm(C,receiver.tr(Q)))for C in Cs];base=sum(covariance_mse(C,64)for C in Cs);rb=sum(covariance_mse(C,64)for C in rot);scaled=[[[factor*factor*x for x in row]for row in C]for C in Cs];sb=sum(covariance_mse(C,64)for C in scaled);tau=mismatch.threshold_control()['tau'];return {'basis_residual':abs(base-rb),'scale_residual':abs(sb/(factor**4*tau**2)-base/tau**2),'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_GAUSSIAN_COVARIANCE_UNCERTAINTY_NOT_EVIDENCE'}
def _domain():
 bad=(([[1.,2.],[0.,1.]],16),([[1.,2.],[2.,1.]],16),([[1.,0.],[0.,1.]],0),([[1.,0.],[0.,1.]],1.5))
 for C,N in bad:
  try:covariance_mse(C,N);return False
  except ValueError:pass
 return True
def scenario_control(name,case):
 table={'sample_identity':lambda:(wishart_identity_control()['residual']<2e-10,wishart_identity_control()['residual'],2e-10),'sample_domain':lambda:(_domain(),0.,1.),'sample_rms':lambda:(rms_control()['strictly_decreasing'],rms_control()['rms_frobenius'][-1],rms_control()['rms_frobenius'][0]),'sample_scaling':lambda:(scaling_control()['ratio_residual']<2e-10,scaling_control()['ratio_residual'],2e-10),'sample_safe_count':lambda:(safe_count_control()['risk_at_count']<=RISK<safe_count_control()['risk_at_predecessor'],safe_count_control()['risk_at_count'],RISK),'sample_unsafe':lambda:(not safe_unsafe_control()['N16_passes']and safe_unsafe_control()['N64_passes'],safe_unsafe_control()['N16_risk'],RISK),'sample_basis_scale':lambda:(max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10),'sample_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def build_artifact():
 controls=[('identity',wishart_identity_control()['residual']<2e-10,wishart_identity_control()['residual'],2e-10,'maximum'),('domain',_domain(),0.,1.,'boolean'),('rms',rms_control()['strictly_decreasing'],rms_control()['rms_frobenius'][-1],rms_control()['rms_frobenius'][0],'maximum'),('scaling',scaling_control()['ratio_residual']<2e-10,scaling_control()['ratio_residual'],2e-10,'maximum'),('safe_count',safe_count_control()['risk_at_count']<=RISK<safe_count_control()['risk_at_predecessor'],safe_count_control()['risk_at_count'],RISK,'maximum'),('unsafe_count',not safe_unsafe_control()['N16_passes']and safe_unsafe_control()['N64_passes'],safe_unsafe_control()['N16_risk'],RISK,'negative_control'),('basis_scale',max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-finite-sample-covariance-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'covariances':covariances(),'wishart_identity':wishart_identity_control(),'total_coefficient':total_coefficient(),'rms':rms_control(),'scaling':scaling_control(),'safe_count':safe_count_control(),'safe_unsafe':safe_unsafe_control(),'basis_scale':basis_scale_control(.37,2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
