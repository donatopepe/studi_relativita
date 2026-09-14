#!/usr/bin/env python3
"""Window-level latent scale-mixture covariance risk floor."""
from __future__ import annotations
import functools,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('scale_mixture_base',HERE/'kerr_latent_window_jitter.py');latent=importlib.util.module_from_spec(S);S.loader.exec_module(latent)
paired=latent.paired;ar1=latent.ar1;RHO=.5;FRACTION=1.;RISK=latent.RISK;CVS=[0.,.1,.2,.25];COUNTS=[64,87,256]
RESULT='KERR_WINDOW_LEVEL_SCALE_MIXTURE_CREATES_NONDECAYING_COVARIANCE_RISK_FLOOR_AND_CV_0P240718193_PRECLUDES_ANY_FINITE_TOY_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_WINDOW_SCALE_DISTRIBUTION_NON_GAUSSIANITY_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,cv):
 if not isinstance(N,int)or isinstance(N,bool)or N<2 or not math.isfinite(cv)or cv<0:raise ValueError('integer N>=2 and finite cv>=0 required')
def moments(cv):
 validate(2,cv);return {'mean':1.,'variance':cv**2,'second_moment':1+cv**2}
def differences():
 out=[]
 for A,B,_ in paired.branch_pairs():out.append([[A[i][j]-B[i][j]for j in range(2)]for i in range(2)])
 return out
def frobenius2(A):return sum(x*x for row in A for x in row)
@functools.lru_cache(maxsize=None)
def delta_coefficient():return sum(frobenius2(D)for D in differences())
@functools.lru_cache(maxsize=None)
def base_mse(N):return latent.total_mse(N,RHO,FRACTION,'latent')
def total_mse(N,cv):
 validate(N,cv);return (1+cv**2)*base_mse(N)+cv**2*delta_coefficient()
def risk(N,cv):return total_mse(N,cv)/ar1.mismatch.threshold_control()['tau']**2
def floor_risk(cv):
 validate(2,cv);return cv**2*delta_coefficient()/ar1.mismatch.threshold_control()['tau']**2
def minimum_count(cv,max_count=100000):
 validate(2,cv)
 if floor_risk(cv)>=RISK:return None
 lo,hi=2,2
 while hi<=max_count and risk(hi,cv)>RISK:lo=hi+1;hi*=2
 if hi>max_count:hi=max_count
 if risk(hi,cv)>RISK:return None
 while lo<hi:
  mid=(lo+hi)//2
  if risk(mid,cv)<=RISK:hi=mid
  else:lo=mid+1
 return lo
def domain_control():
 m=moments(.2);rejected=0
 for args in ((1,.1),(1.5,.1),(16,-.1),(16,float('nan'))):
  try:validate(*args)
  except ValueError:rejected+=1
 return {'moments':m,'mean_residual':abs(m['mean']-1.),'second_moment_residual':abs(m['second_moment']-(1+m['variance'])),'invalid_cases_rejected':rejected,'invalid_cases':4}
def direct_branch_mse(N,cv):
 validate(N,cv);mu2=1+cv**2;alpha=ar1.alpha(N,RHO);beta=latent.latent_beta(N,RHO,FRACTION);out=0.
 for (A,B,K),D in zip(paired.branch_pairs(),differences()):out+=mu2*(alpha*(paired.q(A)+paired.q(B))-2*beta*paired.q(K))+cv**2*frobenius2(D)
 return out
def identity_control():
 rows=[]
 for N in (16,64):
  for cv in (.1,.2):
   direct=direct_branch_mse(N,cv);compact=total_mse(N,cv);rows.append({'N':N,'cv':cv,'direct':direct,'compact':compact,'residual':abs(direct-compact)})
 return {'cases':rows,'residual':max(x['residual']for x in rows)}
def zero_variance_control():
 rows=[{'N':N,'scale_risk':risk(N,0.),'latent_risk':latent.risk(N,RHO,FRACTION,'latent')}for N in COUNTS];return {'cases':rows,'residual':max(abs(x['scale_risk']-x['latent_risk'])for x in rows),'minimum_count':minimum_count(0.)}
def floor_control():
 rows=[]
 for cv in CVS:
  counts=(64,256,1024);f=floor_risk(cv);values=[risk(N,cv)for N in counts];expected=[f+(1+cv**2)*base_mse(N)/ar1.mismatch.threshold_control()['tau']**2 for N in counts];rows.append({'cv':cv,'floor':f,'counts':list(counts),'risks':values,'expected':expected,'residual':max(abs(a-b)for a,b in zip(values,expected)),'strictly_decreasing':all(values[i]>values[i+1]>f for i in range(len(values)-1))})
 return {'floor_coefficient':delta_coefficient()/ar1.mismatch.threshold_control()['tau']**2,'rows':rows,'residual':max(x['residual']for x in rows),'all_decrease_to_floor':all(x['strictly_decreasing']for x in rows)}
def count_control():
 rows=[]
 for cv in CVS:
  N=minimum_count(cv);rows.append({'cv':cv,'minimum_count':N,'floor':floor_risk(cv),'risk_at_count':None if N is None else risk(N,cv),'risk_at_predecessor':None if N is None else risk(N-1,cv),'N64_risk':risk(64,cv),'N64_passes':risk(64,cv)<=RISK})
 return {'rows':rows,'minimum_counts':[x['minimum_count']for x in rows],'expected':[87,106,292,None],'finite_predecessors_fail':all(x['risk_at_count']<=RISK<x['risk_at_predecessor']for x in rows if x['minimum_count']is not None),'all_N64_unsafe':all(not x['N64_passes']for x in rows)}
def critical_cv():return math.sqrt(RISK/(delta_coefficient()/ar1.mismatch.threshold_control()['tau']**2))
def critical_control():
 c=critical_cv();below=c-1e-6;above=c+1e-6;f=floor_risk(c);bf=floor_risk(below);af=floor_risk(above);return {'critical_cv':c,'in_fixed_window':.24071819<=c<=.24071820,'floor':f,'floor_residual':abs(f-RISK),'below':below,'above':above,'below_floor':bf,'above_floor':af,'below_has_finite_count':bf<RISK,'at_finite_count_passes':False,'above_finite_count_passes':False,'no_finite_count_reason':'POSITIVE_SAMPLING_TERM_ABOVE_FLOOR_WHEN_FLOOR_GTE_CEILING'}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 delta=delta_coefficient();rot_delta=sum(frobenius2(rot(D))for D in differences());scaled_delta=sum(frobenius2(paired.scale(D,factor**2))for D in differences());tau=ar1.mismatch.threshold_control()['tau'];cv=.2;base=risk(87,cv);scaled=((1+cv**2)*factor**4*base_mse(87)+cv**2*scaled_delta)/(factor**4*tau**2)
 return {'basis_delta_residual':abs(rot_delta/delta-1.),'scale_risk_residual':abs(scaled-base),'critical_cv_residual':abs(math.sqrt(RISK/(rot_delta/tau**2))-critical_cv())}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_WINDOW_SCALE_MIXTURE_FLOOR_NOT_EVIDENCE','scale_mixture_interpretation':'TOY_WINDOW_NUISANCE_NOT_MEASURED_VARIABILITY_OR_SAMPLE_PRESCRIPTION'}
def controls():
 d=domain_control();i=identity_control();z=zero_variance_control();f=floor_control();c=count_control();crit=critical_control();b=basis_scale_control();n=no_ell0_gate();rows=[('domain',max(d['mean_residual'],d['second_moment_residual'])<2e-10 and d['invalid_cases_rejected']==d['invalid_cases'],max(d['mean_residual'],d['second_moment_residual']),2e-10,'maximum'),('identity',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('zero_variance',z['residual']<2e-10 and z['minimum_count']==87,z['residual'],2e-10,'maximum'),('floor',f['residual']<2e-10 and f['all_decrease_to_floor'],f['residual'],2e-10,'maximum'),('counts',c['minimum_counts']==c['expected']and c['finite_predecessors_fail']and c['all_N64_unsafe'],max(x['risk_at_count']for x in c['rows']if x['risk_at_count']is not None),RISK,'maximum'),('critical_cv',crit['in_fixed_window']and crit['floor_residual']<2e-10 and crit['below_has_finite_count']and not crit['at_finite_count_passes']and not crit['above_finite_count_passes'],crit['floor_residual'],2e-10,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['scale_mixture_interpretation'].startswith('TOY_'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':kind}for x,p,v,h,kind in rows]
def scenario_control(name):
 table={'scalemixture_domain':lambda:domain_control()['invalid_cases_rejected']==domain_control()['invalid_cases'],'scalemixture_identity':lambda:identity_control()['residual']<2e-10,'scalemixture_zero':lambda:zero_variance_control()['residual']<2e-10 and zero_variance_control()['minimum_count']==87,'scalemixture_floor':lambda:floor_control()['all_decrease_to_floor'],'scalemixture_counts':lambda:count_control()['minimum_counts']==[87,106,292,None]and count_control()['all_N64_unsafe'],'scalemixture_critical':lambda:critical_control()['in_fixed_window']and not critical_control()['at_finite_count_passes'],'scalemixture_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'scalemixture_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['scale_mixture_interpretation'].startswith('TOY_')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'fraction':FRACTION,'risk_ceiling':RISK,'cv_cases':CVS,'counts':COUNTS,'scale_moments':'E_W_1_VAR_W_CV2_ONE_SCALE_PER_BRANCH_PAIR_WINDOW'},'domain':domain_control(),'total_mse_identity':identity_control(),'zero_variance_limit':zero_variance_control(),'asymptotic_floor':floor_control(),'count_transition':count_control(),'critical_cv':critical_control(),'differences':{'matrices':differences(),'delta_coefficient':delta_coefficient()},'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
