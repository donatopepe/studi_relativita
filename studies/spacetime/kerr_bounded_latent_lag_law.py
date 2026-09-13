#!/usr/bin/env python3
"""Exact density-ratio-bounded profiling of latent lag probabilities."""
from __future__ import annotations
import importlib.util,itertools,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('laglaw_base',HERE/'kerr_latent_window_jitter.py');latent=importlib.util.module_from_spec(S);S.loader.exec_module(latent)
paired=latent.paired;ar1=latent.ar1;COUNTS=latent.COUNTS;RHO=latent.RHO;RISK=latent.RISK;FRACTIONS=latent.FRACTIONS;KAPPAS=[1.,2.,4.]
RESULT='KERR_LATENT_LAG_LAW_DENSITY_RATIO_BOUNDS_GIVE_EXACT_RISK_ENVELOPES_BUT_KAPPA_4_CAN_RESTORE_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_LATENT_LAG_LAW_BOUNDS_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,rho,fraction,kappa):
 latent.validate(N,rho,fraction)
 if not math.isfinite(kappa)or kappa<1:raise ValueError('finite kappa>=1 required')
def coefficients(N,rho,fraction):
 validate(N,rho,fraction,1.);J=latent.radius(N,fraction);return [(d,latent.fixed_beta(N,rho,d))for d in range(-J,J+1)]
def extremum(values,kappa,maximize):
 if not values or not math.isfinite(kappa)or kappa<1 or any(not math.isfinite(x)for x in values):raise ValueError('finite nonempty values and finite kappa>=1 required')
 n=len(values);lo=1/(kappa*n);hi=kappa/n;prob=[lo]*n;remaining=1-lo*n
 for i in sorted(range(n),key=lambda i:values[i],reverse=maximize):
  add=min(hi-lo,remaining);prob[i]+=add;remaining-=add
  if remaining<=1e-15:break
 if remaining>2e-12:raise ValueError('infeasible probability box')
 return {'value':sum(prob[i]*values[i]for i in range(n)),'probabilities':prob,'lower':lo,'upper':hi,'sum':sum(prob),'bound_residual':max(max(lo-p,0.,p-hi)for p in prob)}
def brute_extremum(values,kappa,maximize):
 n=len(values);lo=1/(kappa*n);hi=kappa/n;candidates=[]
 for free in range(n):
  for bounds in itertools.product((lo,hi),repeat=n-1):
   p=[];j=0
   for i in range(n):
    if i==free:p.append(None)
    else:p.append(bounds[j]);j+=1
   p[free]=1-sum(x for x in p if x is not None)
   if lo-2e-12<=p[free]<=hi+2e-12:candidates.append(sum(a*b for a,b in zip(p,values)))
 if not candidates:raise ValueError('no feasible vertices')
 return max(candidates)if maximize else min(candidates)
def profiled_beta(N,rho,fraction,kappa,maximize):
 validate(N,rho,fraction,kappa);vals=[v for _,v in coefficients(N,rho,fraction)];return extremum(vals,kappa,maximize)
def risk_from_beta(N,rho,beta):
 marginal,cross=latent.channel_coefficients();return (marginal*ar1.alpha(N,rho)-cross*beta)/ar1.mismatch.threshold_control()['tau']**2
def risk(N,rho=RHO,fraction=0.,kappa=1.,side='worst'):
 if side not in ('worst','best'):raise ValueError("side must be 'worst' or 'best'")
 # risk worst=min beta; risk best=max beta
 e=profiled_beta(N,rho,fraction,kappa,side=='best');return risk_from_beta(N,rho,e['value'])
def minimum_count(fraction,kappa,side,rho=RHO):
 validate(2,rho,fraction,kappa);N=2
 while risk(N,rho,fraction,kappa,side)>RISK:N+=1
 return N
def domain_control():
 e=profiled_beta(16,RHO,.25,2.,False);rejected=0;cases=((1,.5,.5,2.),(2.5,.5,.5,2.),(16,-.1,.5,2.),(16,1.,.5,2.),(16,.5,-.1,2.),(16,.5,1.1,2.),(16,.5,.5,.9),(16,.5,.5,float('nan')))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 return {'probability_sum_residual':abs(e['sum']-1.),'bound_residual':e['bound_residual'],'minimum_probability':min(e['probabilities']),'maximum_probability':max(e['probabilities']),'lower_bound':e['lower'],'upper_bound':e['upper'],'invalid_cases_rejected':rejected,'invalid_cases':len(cases)}
def extrema_identity_control():
 cases=[([.1,.4,.9],2.),([.2,.3,.7,1.1],1.5)];rows=[]
 for vals,k in cases:
  for maximize in (False,True):
   greedy=extremum(vals,k,maximize)['value'];brute=brute_extremum(vals,k,maximize);rows.append({'values':vals,'kappa':k,'maximize':maximize,'greedy':greedy,'brute':brute,'residual':abs(greedy-brute)})
 vals=[v for _,v in coefficients(8,RHO,.25)]
 for maximize in (False,True):
  greedy=extremum(vals,2.,maximize)['value'];brute=brute_extremum(vals,2.,maximize);rows.append({'case':'N8_f0.25_k2','maximize':maximize,'greedy':greedy,'brute':brute,'residual':abs(greedy-brute)})
 return {'cases':rows,'residual':max(x['residual']for x in rows)}
def uniform_control():
 rows=[]
 for N in COUNTS:
  for f in FRACTIONS:
   lo=profiled_beta(N,RHO,f,1.,False)['value'];hi=profiled_beta(N,RHO,f,1.,True)['value'];u=latent.latent_beta(N,RHO,f);rows.append({'N':N,'fraction':f,'minimum':lo,'maximum':hi,'uniform':u,'risk':risk(N,RHO,f,1.,'worst'),'uniform_risk':latent.risk(N,RHO,f,'latent')})
 return {'rows':rows,'residual':max(max(abs(x['minimum']-x['uniform']),abs(x['maximum']-x['uniform']),abs(x['risk']-x['uniform_risk']))for x in rows),'counts':[minimum_count(f,1.,'worst')for f in FRACTIONS]}
def envelope_control():
 rows=[]
 for k in KAPPAS:
  for N in COUNTS:
   for f in FRACTIONS:
    best=risk(N,RHO,f,k,'best');uniform=latent.risk(N,RHO,f,'latent');worst=risk(N,RHO,f,k,'worst');rows.append({'kappa':k,'N':N,'fraction':f,'best_risk':best,'uniform_risk':uniform,'worst_risk':worst,'ordered':best<=uniform+2e-10 and uniform<=worst+2e-10})
 return {'rows':rows,'all_ordered':all(x['ordered']for x in rows)}
def widening_control():
 rows=[]
 for N in COUNTS:
  for f in FRACTIONS:
   widths=[risk(N,RHO,f,k,'worst')-risk(N,RHO,f,k,'best')for k in KAPPAS];rows.append({'N':N,'fraction':f,'widths':widths,'nondecreasing':all(widths[i]<=widths[i+1]+2e-10 for i in range(2)),'zero_support_zero':f!=0. or max(abs(x)for x in widths)<2e-10})
 return {'rows':rows,'all_nondecreasing':all(x['nondecreasing']and x['zero_support_zero']for x in rows)}
def count_transition_control():
 out={}
 for k in (2.,4.):
  rows=[]
  for f in FRACTIONS:
   worst=minimum_count(f,k,'worst');best=minimum_count(f,k,'best');rows.append({'fraction':f,'worst_count':worst,'best_count':best,'worst_risk_at_count':risk(worst,RHO,f,k,'worst'),'worst_risk_at_predecessor':risk(worst-1,RHO,f,k,'worst'),'best_risk_at_count':risk(best,RHO,f,k,'best'),'best_risk_at_predecessor':risk(best-1,RHO,f,k,'best'),'worst_N64_risk':risk(64,RHO,f,k,'worst'),'best_N64_risk':risk(64,RHO,f,k,'best')})
  out[str(int(k))]={'rows':rows,'worst_counts':[x['worst_count']for x in rows],'best_counts':[x['best_count']for x in rows],'all_predecessors_fail':all(x['worst_risk_at_count']<=RISK<x['worst_risk_at_predecessor']and x['best_risk_at_count']<=RISK<x['best_risk_at_predecessor']for x in rows),'all_N64_unsafe':all(x['worst_N64_risk']>RISK and x['best_N64_risk']>RISK for x in rows)}
 return {'kappas':out,'expected_k2_worst':[87,87,87,87],'expected_k4_worst':[87,87,87,88],'expected_best':[87,87,87,87]}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 marginal,cross=latent.channel_coefficients();rotm=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotc=4*paired.q(rot(ar1.mismatch.NOISE));scaledm=sum(paired.q(paired.scale(A,factor**2))+paired.q(paired.scale(B,factor**2))for A,B,_ in paired.branch_pairs());scaledc=4*paired.q(paired.scale(ar1.mismatch.NOISE,factor**2));bmin=profiled_beta(64,RHO,.5,4.,False)['value'];bmax=profiled_beta(64,RHO,.5,4.,True)['value'];a=ar1.alpha(64,RHO);tau=ar1.mismatch.threshold_control()['tau'];res=[]
 for b in (bmin,bmax):
  base=(marginal*a-cross*b)/tau**2;rotated=(rotm*a-rotc*b)/tau**2;scaled=(scaledm*a-scaledc*b)/(factor**4*tau**2);res.extend((abs(rotated-base),abs(scaled-base)))
 return {'basis_residual':max(res[::2]),'scale_residual':max(res[1::2])}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_BOUNDED_LATENT_LAG_LAW_ROBUSTNESS_NOT_EVIDENCE','lag_law_bounds':'TOY_DENSITY_RATIO_BOX_NOT_MEASURED'}
def controls():
 d=domain_control();i=extrema_identity_control();u=uniform_control();e=envelope_control();w=widening_control();c=count_transition_control();b=basis_scale_control();n=no_ell0_gate();k2=c['kappas']['2'];k4=c['kappas']['4'];rows=[('domain',max(d['probability_sum_residual'],d['bound_residual'])<2e-10 and d['invalid_cases_rejected']==d['invalid_cases'],max(d['probability_sum_residual'],d['bound_residual']),2e-10,'maximum'),('extrema',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('uniform',u['residual']<2e-10 and u['counts']==[87,87,87,87],u['residual'],2e-10,'maximum'),('envelope',e['all_ordered'],0.,1.,'boolean'),('widening',w['all_nondecreasing'],0.,1.,'boolean'),('count_transition',k2['worst_counts']==c['expected_k2_worst']and k4['worst_counts']==c['expected_k4_worst']and k2['best_counts']==k4['best_counts']==c['expected_best']and k2['all_predecessors_fail']and k4['all_predecessors_fail']and k2['all_N64_unsafe']and k4['all_N64_unsafe'],max(max(x['worst_risk_at_count']for x in k2['rows']),max(x['worst_risk_at_count']for x in k4['rows'])),RISK,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['lag_law_bounds'].startswith('TOY_'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':k}for x,p,v,h,k in rows]
def scenario_control(name):
 table={'laglaw_domain':lambda:domain_control()['invalid_cases_rejected']==domain_control()['invalid_cases'],'laglaw_extrema':lambda:extrema_identity_control()['residual']<2e-10,'laglaw_uniform':lambda:uniform_control()['residual']<2e-10 and uniform_control()['counts']==[87,87,87,87],'laglaw_envelope':lambda:envelope_control()['all_ordered'],'laglaw_widening':lambda:widening_control()['all_nondecreasing'],'laglaw_count_transition':lambda:count_transition_control()['kappas']['4']['worst_counts']==[87,87,87,88]and count_transition_control()['kappas']['4']['all_N64_unsafe'],'laglaw_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'laglaw_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['lag_law_bounds'].startswith('TOY_')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'counts':COUNTS,'radius_fractions':FRACTIONS,'kappas':KAPPAS,'probability_box':'UNIFORM_DENSITY_RATIO_LOWER_1_OVER_KAPPA_UPPER_KAPPA','risk_ceiling':RISK},'domain':domain_control(),'linear_program_identity':extrema_identity_control(),'uniform_limit':uniform_control(),'risk_envelope':envelope_control(),'envelope_widening':widening_control(),'count_transition':count_transition_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
