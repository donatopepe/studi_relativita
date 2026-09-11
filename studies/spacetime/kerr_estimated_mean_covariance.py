#!/usr/bin/env python3
"""Estimated-mean covariance degree-of-freedom penalty for Kerr receiver toy."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('estimated_mean_base',HERE/'kerr_finite_sample_covariance.py');known=importlib.util.module_from_spec(S);S.loader.exec_module(known)
receiver=known.receiver;mismatch=known.mismatch;COUNTS=known.COUNTS;RISK=known.RISK
RESULT='KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_UNKNOWN_MEAN_NON_GAUSSIANITY_SAMPLE_DEPENDENCE_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def estimated_mse(C,N):
 mismatch.validate_spd(C)
 if not isinstance(N,int)or isinstance(N,bool)or N<2:raise ValueError('integer sample count >=2 required')
 return (known.trace2(C)**2+known.trace_square(C))/(N-1)
def centered_componentwise(C,N):
 mismatch.validate_spd(C)
 if not isinstance(N,int)or isinstance(N,bool)or N<2:raise ValueError('integer sample count >=2 required')
 return sum((C[i][i]*C[j][j]+C[i][j]*C[i][j])/(N-1)for i in range(2)for j in range(2))
def centered_wishart_control():
 x=[(estimated_mse(C,64),centered_componentwise(C,64))for C in known.covariances()];return {'degrees_of_freedom':63,'per_covariance':x,'residual':max(abs(a-b)for a,b in x)}
def penalty_control():
 rows=[]
 for N in COUNTS:
  actual=sum(estimated_mse(C,N)for C in known.covariances())/sum(known.covariance_mse(C,N)for C in known.covariances());rows.append({'N':N,'actual':actual,'expected':N/(N-1)})
 return {'ratios':rows,'residual':max(abs(x['actual']-x['expected'])for x in rows)}
def total_mse(N):return sum(estimated_mse(C,N)for C in known.covariances())
def rms_control():
 x=[math.sqrt(total_mse(N))for N in COUNTS];expected=[math.sqrt((COUNTS[i+1]-1)/(COUNTS[i]-1))for i in range(2)];actual=[x[i]/x[i+1]for i in range(2)];return {'sample_counts':COUNTS,'degrees_of_freedom':[N-1 for N in COUNTS],'rms_frobenius':x,'strictly_decreasing':all(x[i+1]<x[i]for i in range(2)),'ratio_residual':max(abs(actual[i]-expected[i])for i in range(2))}
def risk_bound(N):return total_mse(N)/mismatch.threshold_control()['tau']**2
def safe_count_control():
 n=math.ceil(1+known.total_coefficient()/(RISK*mismatch.threshold_control()['tau']**2));return {'risk_ceiling':RISK,'minimum_count':n,'risk_at_count':risk_bound(n),'risk_at_predecessor':risk_bound(n-1)}
def safe_unsafe_control():return {'N16_risk':risk_bound(16),'N16_passes':risk_bound(16)<=RISK,'N64_risk':risk_bound(64),'N64_passes':risk_bound(64)<=RISK}
def basis_scale_control(theta,factor):
 Cs=known.covariances();co=math.cos(theta);si=math.sin(theta);Q=[[co,-si],[si,co]];rot=[receiver.mm(Q,receiver.mm(C,receiver.tr(Q)))for C in Cs];base=sum(estimated_mse(C,64)for C in Cs);rb=sum(estimated_mse(C,64)for C in rot);scaled=[[[factor*factor*x for x in row]for row in C]for C in Cs];sb=sum(estimated_mse(C,64)for C in scaled);tau=mismatch.threshold_control()['tau'];return {'basis_residual':abs(base-rb),'scale_residual':abs(sb/(factor**4*tau**2)-base/tau**2),'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_ESTIMATED_MEAN_COVARIANCE_PENALTY_NOT_EVIDENCE'}
def _domain():
 for C,N in (([[1.,0.],[0.,1.]],1),([[1.,0.],[0.,1.]],1.5),([[1.,2.],[2.,1.]],16)):
  try:estimated_mse(C,N);return False
  except ValueError:pass
 return True
def scenario_control(name,case):
 table={'mean_identity':lambda:(centered_wishart_control()['residual']<2e-10,centered_wishart_control()['residual'],2e-10),'mean_domain':lambda:(_domain(),0.,1.),'mean_penalty':lambda:(penalty_control()['residual']<2e-10,penalty_control()['residual'],2e-10),'mean_rms':lambda:(rms_control()['strictly_decreasing']and rms_control()['ratio_residual']<2e-10,rms_control()['ratio_residual'],2e-10),'mean_safe_count':lambda:(safe_count_control()['minimum_count']==54,safe_count_control()['risk_at_count'],RISK),'mean_unsafe':lambda:(not safe_unsafe_control()['N16_passes']and safe_unsafe_control()['N64_passes'],safe_unsafe_control()['N16_risk'],RISK),'mean_basis_scale':lambda:(max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10),'mean_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def build_artifact():
 controls=[('identity',centered_wishart_control()['residual']<2e-10,centered_wishart_control()['residual'],2e-10,'maximum'),('domain',_domain(),0.,1.,'boolean'),('penalty',penalty_control()['residual']<2e-10,penalty_control()['residual'],2e-10,'maximum'),('rms',rms_control()['strictly_decreasing']and rms_control()['ratio_residual']<2e-10,rms_control()['ratio_residual'],2e-10,'maximum'),('safe_count',safe_count_control()['minimum_count']==54,safe_count_control()['risk_at_count'],RISK,'maximum'),('unsafe_count',not safe_unsafe_control()['N16_passes']and safe_unsafe_control()['N64_passes'],safe_unsafe_control()['N16_risk'],RISK,'negative_control'),('basis_scale',max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_residual'],basis_scale_control(.37,2.5)['scale_residual']),2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-estimated-mean-covariance-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'centered_wishart':centered_wishart_control(),'penalty':penalty_control(),'rms':rms_control(),'safe_count':safe_count_control(),'safe_unsafe':safe_unsafe_control(),'basis_scale':basis_scale_control(.37,2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
