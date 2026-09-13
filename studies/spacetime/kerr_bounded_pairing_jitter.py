#!/usr/bin/env python3
"""Exact Gaussian mixture-kernel penalty for bounded symmetric pairing jitter."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('jitter_base',HERE/'kerr_bounded_pairing_lag.py');lagbase=importlib.util.module_from_spec(S);S.loader.exec_module(lagbase)
paired=lagbase.paired;ar1=lagbase.ar1;COUNTS=lagbase.COUNTS;RHO=lagbase.RHO;RISK=lagbase.RISK;RADII=[0,1,2,4,8,16]
RESULT='KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_RADIUS_16_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_PAIRING_JITTER_DISTRIBUTION_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,rho,J):
 if not isinstance(N,int)or isinstance(N,bool)or N<2 or not math.isfinite(rho)or not(0<=rho<1)or not isinstance(J,int)or isinstance(J,bool)or not(0<=J<=N):raise ValueError('integer N>=2, finite 0<=rho<1 and integer 0<=J<=N required')
def mixture_cross_time(N,rho,J):
 validate(N,rho,J);w=1/(2*J+1);return [[w*sum(rho**abs(i-j-d)for d in range(-J,J+1))for j in range(N)]for i in range(N)]
def mixture_direct(N,rho,J):
 validate(N,rho,J);w=1/(2*J+1);mats=[[[rho**abs(i-j-d)for j in range(N)]for i in range(N)]for d in range(-J,J+1)];return [[w*sum(M[i][j]for M in mats)for j in range(N)]for i in range(N)]
def beta_dense(N,rho,J):
 K=mixture_cross_time(N,rho,J);H=[[float(i==j)-1/N for j in range(N)]for i in range(N)];HK=paired.mm(H,K);q=paired.tr(paired.mm(paired.mm(HK,H),paired.t(K)));T=ar1.ar1(N,rho);d=paired.tr(paired.mm(H,T));return q/d**2
def beta(N,rho,J):
 K=mixture_cross_time(N,rho,J);rows=[sum(row)for row in K];cols=[sum(K[i][j]for i in range(N))for j in range(N)];u=sum(rows);q=sum(x*x for row in K for x in row)-sum(x*x for x in rows)/N-sum(x*x for x in cols)/N+u*u/N**2;T=ar1.ar1(N,rho);d=N-sum(sum(row)for row in T)/N;return q/d**2
def total_mse(N,rho=RHO,J=0):return ar1.known.total_coefficient()*ar1.alpha(N,rho)-lagbase.noise_cross_coefficient()*beta(N,rho,J)
def risk(N,rho=RHO,J=0):return total_mse(N,rho,J)/ar1.mismatch.threshold_control()['tau']**2
def minimum_count(J,rho=RHO):
 if not isinstance(J,int)or isinstance(J,bool)or J<0:raise ValueError('nonnegative integer J required')
 N=max(2,J)
 while risk(N,rho,J)>RISK:N+=1
 return N
def domain_control():
 K=mixture_cross_time(8,RHO,2);symmetric=max(abs(K[i][j]-K[j][i])for i in range(8)for j in range(8));rejected=0;cases=((1,.5,0),(2.5,.5,0),(8,-.1,0),(8,1.,0),(8,float('nan'),0),(8,.5,-1),(8,.5,1.5),(8,.5,9))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 return {'accepted':len(K)==8,'symmetry_residual':symmetric,'invalid_cases_rejected':rejected,'invalid_cases':len(cases)}
def identity_control():
 rows=[]
 for N,J in ((8,1),(16,4),(32,16)):
  A=mixture_cross_time(N,RHO,J);B=mixture_direct(N,RHO,J);element=max(abs(A[i][j]-B[i][j])for i in range(N)for j in range(N));rows.append({'N':N,'J':J,'element_residual':element,'explicit':beta(N,RHO,J),'dense':beta_dense(N,RHO,J)})
 return {'cases':rows,'residual':max(max(x['element_residual'],abs(x['explicit']-x['dense']))for x in rows)}
def zero_jitter_control():
 rows=[]
 for N in COUNTS:rows.append({'N':N,'jitter_mse':total_mse(N,RHO,0),'paired_mse':paired.paired_coefficient()*ar1.alpha(N,RHO),'jitter_risk':risk(N,RHO,0),'paired_risk':paired.risk(N,RHO)})
 return {'cases':rows,'residual':max(max(abs(x['jitter_mse']-x['paired_mse']),abs(x['jitter_risk']-x['paired_risk']))for x in rows),'minimum_count':minimum_count(0)}
def risk_control():
 rows=[]
 for J in RADII:
  values=[risk(N,RHO,J)for N in COUNTS];rows.append({'J':J,'risks':values,'strictly_decreasing':all(math.isfinite(x)and x>0 for x in values)and all(values[i]>values[i+1]for i in range(2))})
 return {'rho':RHO,'counts':COUNTS,'rows':rows,'all_strictly_decreasing':all(x['strictly_decreasing']for x in rows)}
def monotonicity_control():
 rows=[]
 for N in COUNTS:
  ratios=[beta(N,RHO,J)/ar1.alpha(N,RHO)for J in RADII];risks=[risk(N,RHO,J)for J in RADII];rows.append({'N':N,'cancellation_ratios':ratios,'risks':risks,'cancellation_strictly_decreasing':all(ratios[i]>ratios[i+1]for i in range(len(RADII)-1)),'risk_strictly_increasing':all(risks[i]<risks[i+1]for i in range(len(RADII)-1))})
 return {'rows':rows,'all_monotonic':all(x['cancellation_strictly_decreasing']and x['risk_strictly_increasing']for x in rows)}
def count_transition_control():
 rows=[]
 for J in RADII:
  N=minimum_count(J);rows.append({'J':J,'minimum_count':N,'risk_at_count':risk(N,RHO,J),'risk_at_predecessor':risk(N-1,RHO,J),'N64_risk':risk(64,RHO,J),'N64_passes':risk(64,RHO,J)<=RISK})
 return {'rows':rows,'minimum_counts':[x['minimum_count']for x in rows],'expected':[87,87,87,87,87,88],'all_predecessors_fail':all(x['risk_at_count']<=RISK<x['risk_at_predecessor']for x in rows),'all_N64_unsafe':all(not x['N64_passes']for x in rows)}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 base=sum(paired.q(A)+paired.q(B)for A,B,_ in paired.branch_pairs());cross=lagbase.noise_cross_coefficient();rotbase=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotcross=4*paired.q(rot(ar1.mismatch.NOISE));scaledbase=sum(paired.q(paired.scale(A,factor**2))+paired.q(paired.scale(B,factor**2))for A,B,_ in paired.branch_pairs());scaledcross=4*paired.q(paired.scale(ar1.mismatch.NOISE,factor**2));a=ar1.alpha(64,RHO);b=beta(64,RHO,8);tau=ar1.mismatch.threshold_control()['tau'];base_risk=(base*a-cross*b)/tau**2;scale_risk=(scaledbase*a-scaledcross*b)/(factor**4*tau**2)
 return {'basis_residual':max(abs(rotbase/base-1.),abs(rotcross/cross-1.)),'scale_residual':abs(scale_risk-base_risk)}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_BOUNDED_PAIRING_JITTER_EROSION_NOT_EVIDENCE','latent_window_mixture':'NOT_CLAIMED_REQUIRES_NON_GAUSSIAN_FOURTH_MOMENTS'}
def controls():
 d=domain_control();i=identity_control();z=zero_jitter_control();r=risk_control();m=monotonicity_control();c=count_transition_control();b=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['symmetry_residual']<2e-10 and d['invalid_cases_rejected']==d['invalid_cases'],max(d['symmetry_residual'],0.),2e-10,'maximum'),('identity',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('zero_jitter',z['residual']<2e-10 and z['minimum_count']==87,z['residual'],2e-10,'maximum'),('risk',r['all_strictly_decreasing'],max(x['risks'][-1]for x in r['rows']),max(x['risks'][0]for x in r['rows']),'maximum'),('monotonicity',m['all_monotonic'],0.,1.,'boolean'),('count_transition',c['minimum_counts']==c['expected']and c['all_predecessors_fail']and c['all_N64_unsafe'],max(x['risk_at_count']for x in c['rows']),RISK,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['latent_window_mixture'].startswith('NOT_CLAIMED'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':k}for x,p,v,h,k in rows]
def scenario_control(name):
 table={'jitter_domain':lambda:domain_control()['invalid_cases_rejected']==domain_control()['invalid_cases'],'jitter_identity':lambda:identity_control()['residual']<2e-10,'jitter_zero':lambda:zero_jitter_control()['residual']<2e-10 and zero_jitter_control()['minimum_count']==87,'jitter_risk':lambda:risk_control()['all_strictly_decreasing'],'jitter_monotonicity':lambda:monotonicity_control()['all_monotonic'],'jitter_count_transition':lambda:count_transition_control()['minimum_counts']==[87,87,87,87,87,88]and count_transition_control()['all_N64_unsafe'],'jitter_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'jitter_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['latent_window_mixture'].startswith('NOT_CLAIMED')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'counts':COUNTS,'jitter_radii':RADII,'jitter_kernel':'UNIFORM_SYMMETRIC_GAUSSIAN_CROSS_COVARIANCE_MIXTURE','risk_ceiling':RISK},'domain':domain_control(),'mixture_identity':identity_control(),'zero_jitter_limit':zero_jitter_control(),'fixed_support_risk':risk_control(),'monotonicity':monotonicity_control(),'count_transition':count_transition_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
