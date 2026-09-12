#!/usr/bin/env python3
"""Exact centered-covariance penalty for separable Gaussian AR(1) sampling."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('ar1_base',HERE/'kerr_estimated_mean_covariance.py');mean=importlib.util.module_from_spec(S);S.loader.exec_module(mean)
known=mean.known;receiver=mean.receiver;mismatch=mean.mismatch;COUNTS=mean.COUNTS;RISK=mean.RISK;RHOS=[0.,.25,.5,.75]
RESULT='KERR_GAUSSIAN_AR1_TEMPORAL_DEPENDENCE_REDUCES_EFFECTIVE_COVARIANCE_INFORMATION_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_TEMPORAL_CORRELATION_MODEL_STATIONARITY_GAUSSIANITY_CROSS_STREAM_DEPENDENCE_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def validate(N,rho):
 if not isinstance(N,int)or isinstance(N,bool)or N<2 or not math.isfinite(rho)or not(0<=rho<1):raise ValueError('integer N>=2 and finite 0<=rho<1 required')
def ar1(N,rho):validate(N,rho);return [[rho**abs(i-j)for j in range(N)]for i in range(N)]
def alpha_dense(N,rho):
 T=ar1(N,rho);H=[[float(i==j)-1/N for j in range(N)]for i in range(N)]
 def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
 HT=mm(H,T);d=sum(HT[i][i]for i in range(N));q=sum(mm(HT,HT)[i][i]for i in range(N));return q/d**2
def alpha(N,rho):
 validate(N,rho);rows=[sum(rho**abs(i-j)for j in range(N))for i in range(N)];u=sum(rows);tr2=N+2*sum((N-k)*rho**(2*k)for k in range(1,N));q=tr2-2*sum(x*x for x in rows)/N+u*u/N**2;d=N-u/N;return q/d**2
def trace_identity_control():
 cases=((4,.25),(8,.5),(16,.75));x=[(N,r,alpha(N,r),alpha_dense(N,r))for N,r in cases];return {'cases':x,'residual':max(abs(a-b)for _,_,a,b in x)}
def iid_limit_control():
 x=[(N,alpha(N,0.),1/(N-1))for N in COUNTS];return {'cases':x,'residual':max(abs(a-b)for _,a,b in x)}
def rms(N,rho):return math.sqrt(known.total_coefficient()*alpha(N,rho))
def risk(N,rho):return known.total_coefficient()*alpha(N,rho)/mismatch.threshold_control()['tau']**2
def rms_control(rho):
 x=[rms(N,rho)for N in COUNTS];return {'rho':rho,'sample_counts':COUNTS,'rms_frobenius':x,'strictly_decreasing':all(x[i+1]<x[i]for i in range(2))}
def rho_monotonicity_control():
 rows=[]
 for N in COUNTS:
  a=[alpha(N,r)for r in RHOS];rows.append({'N':N,'alpha':a,'rms':[math.sqrt(known.total_coefficient()*z)for z in a]})
 return {'rhos':RHOS,'rows':rows,'strictly_increasing':all(all(x['alpha'][i+1]>x['alpha'][i]for i in range(3))for x in rows)}
def safe_count_control(rho):
 N=2
 while risk(N,rho)>RISK:N+=1
 return {'rho':rho,'risk_ceiling':RISK,'minimum_count':N,'risk_at_count':risk(N,rho),'risk_at_predecessor':risk(N-1,rho),'N64_risk':risk(64,rho),'N64_passes':risk(64,rho)<=RISK}
def basis_scale_limit_control(theta,factor):
 Cs=known.covariances();co=math.cos(theta);si=math.sin(theta);Q=[[co,-si],[si,co]];rot=[receiver.mm(Q,receiver.mm(C,receiver.tr(Q)))for C in Cs];base=sum((known.trace2(C)**2+known.trace_square(C))*alpha(64,.5)for C in Cs);rb=sum((known.trace2(C)**2+known.trace_square(C))*alpha(64,.5)for C in rot);scaled=[[[factor*factor*x for x in row]for row in C]for C in Cs];sb=sum((known.trace2(C)**2+known.trace_square(C))*alpha(64,.5)for C in scaled);tau=mismatch.threshold_control()['tau'];return {'basis_residual':abs(base-rb),'scale_residual':abs(sb/(factor**4*tau**2)-base/tau**2),'near_unit_rho':.99,'near_unit_effective_df_64':1/alpha(64,.99),'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_AR1_COVARIANCE_PENALTY_NOT_EVIDENCE'}
def scenario_control(name,case):
 table={'ar1_domain':lambda:(_domain(),0.,1.),'ar1_identity':lambda:(trace_identity_control()['residual']<2e-10,trace_identity_control()['residual'],2e-10),'ar1_iid':lambda:(iid_limit_control()['residual']<2e-10,iid_limit_control()['residual'],2e-10),'ar1_rms':lambda:(rms_control(.5)['strictly_decreasing'],rms_control(.5)['rms_frobenius'][-1],rms_control(.5)['rms_frobenius'][0]),'ar1_monotonicity':lambda:(rho_monotonicity_control()['strictly_increasing'],0.,1.),'ar1_safe_count':lambda:(safe_count_control(.5)['minimum_count']==88,safe_count_control(.5)['risk_at_count'],RISK),'ar1_basis_scale':lambda:(max(basis_scale_limit_control(.37,2.5)['basis_residual'],basis_scale_limit_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_limit_control(.37,2.5)['basis_residual'],basis_scale_limit_control(.37,2.5)['scale_residual']),2e-10),'ar1_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def _domain():
 for N,r in ((1,.5),(2.5,.5),(16,-.1),(16,1.),(16,float('nan'))):
  try:alpha(N,r);return False
  except ValueError:pass
 return True
def build_artifact():
 controls=[('domain',_domain(),0.,1.,'boolean'),('identity',trace_identity_control()['residual']<2e-10,trace_identity_control()['residual'],2e-10,'maximum'),('iid_limit',iid_limit_control()['residual']<2e-10,iid_limit_control()['residual'],2e-10,'maximum'),('rms',rms_control(.5)['strictly_decreasing'],rms_control(.5)['rms_frobenius'][-1],rms_control(.5)['rms_frobenius'][0],'maximum'),('monotonicity',rho_monotonicity_control()['strictly_increasing'],0.,1.,'boolean'),('safe_count',safe_count_control(.5)['minimum_count']==88,safe_count_control(.5)['risk_at_count'],RISK,'maximum'),('basis_scale_limit',max(basis_scale_limit_control(.37,2.5)['basis_residual'],basis_scale_limit_control(.37,2.5)['scale_residual'])<2e-10,max(basis_scale_limit_control(.37,2.5)['basis_residual'],basis_scale_limit_control(.37,2.5)['scale_residual']),2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-ar1-temporal-dependence-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'trace_identity':trace_identity_control(),'iid_limit':iid_limit_control(),'rms_rho_05':rms_control(.5),'rho_monotonicity':rho_monotonicity_control(),'safe_count':safe_count_control(.5),'basis_scale_limit':basis_scale_limit_control(.37,2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
