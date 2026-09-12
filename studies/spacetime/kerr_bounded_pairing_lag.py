#!/usr/bin/env python3
"""Exact finite-N erosion of paired covariance cancellation under AR(1) timing lag."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('lag_base',HERE/'kerr_paired_stream_common_noise.py');paired=importlib.util.module_from_spec(S);S.loader.exec_module(paired)
ar1=paired.ar1;COUNTS=paired.COUNTS;RHO=paired.RHO;RISK=paired.RISK;FRACTIONS=[0.,.25,.5,1.]
RESULT='KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_A_ONE_WINDOW_LAG_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_PAIRING_LAG_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,rho,fraction):
 if not isinstance(N,int)or isinstance(N,bool)or N<2 or not math.isfinite(rho)or not(0<=rho<1)or not math.isfinite(fraction)or not(0<=fraction<=1):raise ValueError('integer N>=2, finite 0<=rho<1 and finite 0<=fraction<=1 required')
def lag(N,fraction):validate(N,0.,fraction);return math.floor(fraction*N+.5)
def cross_time(N,rho,L):
 if not isinstance(L,int)or isinstance(L,bool)or not(0<=L<=N):raise ValueError('integer 0<=L<=N required')
 ar1.validate(N,rho);return [[rho**abs(i-j-L)for j in range(N)]for i in range(N)]
def beta_dense(N,rho,fraction):
 validate(N,rho,fraction);K=cross_time(N,rho,lag(N,fraction));H=[[float(i==j)-1/N for j in range(N)]for i in range(N)];HK=paired.mm(H,K);q=paired.tr(paired.mm(paired.mm(HK,H),paired.t(K)));T=ar1.ar1(N,rho);d=paired.tr(paired.mm(H,T));return q/d**2
def beta(N,rho,fraction):
 validate(N,rho,fraction);K=cross_time(N,rho,lag(N,fraction));rows=[sum(row)for row in K];cols=[sum(K[i][j]for i in range(N))for j in range(N)];u=sum(rows);q=sum(x*x for row in K for x in row)-sum(x*x for x in rows)/N-sum(x*x for x in cols)/N+u*u/N**2;T=ar1.ar1(N,rho);d=N-sum(sum(row)for row in T)/N;return q/d**2
def noise_cross_coefficient():return 4*paired.q(ar1.mismatch.NOISE)
def total_mse(N,rho=RHO,fraction=0.):return ar1.known.total_coefficient()*ar1.alpha(N,rho)-noise_cross_coefficient()*beta(N,rho,fraction)
def risk(N,rho=RHO,fraction=0.):return total_mse(N,rho,fraction)/ar1.mismatch.threshold_control()['tau']**2
def minimum_count(fraction,rho=RHO):
 validate(2,rho,fraction);N=2
 while risk(N,rho,fraction)>RISK:N+=1
 return N
def domain_control():
 accepted=lag(16,.5)==8 and lag(3,.5)==2 and len(cross_time(8,.5,8))==8;rejected=0;cases=((1,.5,.5),(2.5,.5,.5),(16,-.1,.5),(16,1.,.5),(16,float('nan'),.5),(16,.5,-.1),(16,.5,1.1),(16,.5,float('nan')))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 try:cross_time(8,.5,9)
 except ValueError:rejected+=1
 return {'accepted':accepted,'invalid_cases_rejected':rejected,'invalid_cases':len(cases)+1,'round_half_up_example':lag(3,.5)}
def identity_control():
 cases=[(8,.25),(16,.5),(32,1.)];rows=[]
 for N,f in cases:rows.append({'N':N,'fraction':f,'lag':lag(N,f),'explicit':beta(N,RHO,f),'dense':beta_dense(N,RHO,f)})
 return {'cases':rows,'residual':max(abs(x['explicit']-x['dense'])for x in rows)}
def synchronous_control():
 rows=[]
 for N in COUNTS:rows.append({'N':N,'lag_mse':total_mse(N,RHO,0.),'paired_mse':paired.paired_coefficient()*ar1.alpha(N,RHO),'lag_risk':risk(N,RHO,0.),'paired_risk':paired.risk(N,RHO)})
 return {'cases':rows,'residual':max(max(abs(x['lag_mse']-x['paired_mse']),abs(x['lag_risk']-x['paired_risk']))for x in rows),'minimum_count':minimum_count(0.)}
def risk_control():
 rows=[]
 for f in FRACTIONS:
  values=[risk(N,RHO,f)for N in COUNTS];rows.append({'fraction':f,'lags':[lag(N,f)for N in COUNTS],'risks':values,'strictly_decreasing':all(math.isfinite(x)and x>0 for x in values)and all(values[i]>values[i+1]for i in range(2))})
 return {'rho':RHO,'counts':COUNTS,'rows':rows,'all_strictly_decreasing':all(x['strictly_decreasing']for x in rows)}
def monotonicity_control():
 rows=[]
 for N in COUNTS:
  ratios=[beta(N,RHO,f)/ar1.alpha(N,RHO)for f in FRACTIONS];risks=[risk(N,RHO,f)for f in FRACTIONS];rows.append({'N':N,'cancellation_ratios':ratios,'risks':risks,'cancellation_strictly_decreasing':all(ratios[i]>ratios[i+1]for i in range(3)),'risk_strictly_increasing':all(risks[i]<risks[i+1]for i in range(3))})
 return {'rows':rows,'all_monotonic':all(x['cancellation_strictly_decreasing']and x['risk_strictly_increasing']for x in rows)}
def count_transition_control():
 rows=[]
 for f in FRACTIONS:
  N=minimum_count(f);rows.append({'fraction':f,'minimum_count':N,'risk_at_count':risk(N,RHO,f),'risk_at_predecessor':risk(N-1,RHO,f),'N64_risk':risk(64,RHO,f),'N64_passes':risk(64,RHO,f)<=RISK})
 return {'rows':rows,'minimum_counts':[x['minimum_count']for x in rows],'expected':[87,87,87,88],'all_predecessors_fail':all(x['risk_at_count']<=RISK<x['risk_at_predecessor']for x in rows),'all_N64_unsafe':all(not x['N64_passes']for x in rows)}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 base=sum(paired.q(A)+paired.q(B)for A,B,_ in paired.branch_pairs());cross=noise_cross_coefficient();rotbase=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotcross=4*paired.q(rot(ar1.mismatch.NOISE));scaledbase=sum(paired.q(paired.scale(A,factor**2))+paired.q(paired.scale(B,factor**2))for A,B,_ in paired.branch_pairs());scaledcross=4*paired.q(paired.scale(ar1.mismatch.NOISE,factor**2));a=ar1.alpha(64,RHO);b=beta(64,RHO,.5);tau=ar1.mismatch.threshold_control()['tau'];base_risk=(base*a-cross*b)/tau**2;scale_risk=(scaledbase*a-scaledcross*b)/(factor**4*tau**2)
 return {'basis_residual':max(abs(rotbase/base-1.),abs(rotcross/cross-1.)),'scale_residual':abs(scale_risk-base_risk)}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_BOUNDED_PAIRING_LAG_EROSION_NOT_EVIDENCE'}
def controls():
 d=domain_control();i=identity_control();s=synchronous_control();r=risk_control();m=monotonicity_control();c=count_transition_control();b=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['invalid_cases_rejected']==d['invalid_cases'],0.,1.,'boolean'),('identity',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('synchronous',s['residual']<2e-10 and s['minimum_count']==87,s['residual'],2e-10,'maximum'),('risk',r['all_strictly_decreasing'],max(x['risks'][-1]for x in r['rows']),max(x['risks'][0]for x in r['rows']),'maximum'),('monotonicity',m['all_monotonic'],0.,1.,'boolean'),('count_transition',c['minimum_counts']==c['expected']and c['all_predecessors_fail']and c['all_N64_unsafe'],max(x['risk_at_count']for x in c['rows']),RISK,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM',0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':k}for x,p,v,h,k in rows]
def scenario_control(name):
 table={'lag_domain':lambda:domain_control()['invalid_cases_rejected']==domain_control()['invalid_cases'],'lag_identity':lambda:identity_control()['residual']<2e-10,'lag_synchronous':lambda:synchronous_control()['residual']<2e-10 and synchronous_control()['minimum_count']==87,'lag_risk':lambda:risk_control()['all_strictly_decreasing'],'lag_monotonicity':lambda:monotonicity_control()['all_monotonic'],'lag_count_transition':lambda:count_transition_control()['minimum_counts']==[87,87,87,88]and count_transition_control()['all_N64_unsafe'],'lag_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'lag_nonclaims':lambda:not no_ell0_gate()['ell0_identified']};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'counts':COUNTS,'lag_fractions':FRACTIONS,'rounding':'ROUND_HALF_UP_FLOOR_F_N_PLUS_HALF','risk_ceiling':RISK},'domain':domain_control(),'trace_identity':identity_control(),'synchronous_limit':synchronous_control(),'fixed_fraction_risk':risk_control(),'monotonicity':monotonicity_control(),'count_transition':count_transition_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
