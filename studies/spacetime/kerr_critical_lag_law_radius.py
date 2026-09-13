#!/usr/bin/env python3
"""Exact active-set critical density-ratio radius for latent lag law."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('critical_base',HERE/'kerr_bounded_latent_lag_law.py');law=importlib.util.module_from_spec(S);S.loader.exec_module(law)
latent=law.latent;paired=law.paired;ar1=law.ar1;N=87;RHO=law.RHO;FRACTION=1.;TARGET=law.RISK;BRACKET=(2.,4.);GRID=[2.,2.5,3.,3.5,4.];EPS=1e-6
RESULT='KERR_FULL_SUPPORT_LATENT_LAG_LAW_HAS_TOY_CRITICAL_DENSITY_RATIO_KAPPA_3P890241565_FOR_THE_COUNT_87_GATE_NOT_ELL0'
GATE='PHYSICAL_KERR_LATENT_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N0,rho,fraction,lo,hi):
 latent.validate(N0,rho,fraction)
 if not math.isfinite(lo)or not math.isfinite(hi)or not(1<=lo<hi):raise ValueError('finite bracket 1<=lo<hi required')
def sorted_coefficients(N0=N,rho=RHO,fraction=FRACTION):return sorted(v for _,v in law.coefficients(N0,rho,fraction))
def active_count(n,kappa):
 if not isinstance(n,int)or isinstance(n,bool)or n<1 or not math.isfinite(kappa)or kappa<1:raise ValueError('integer n>=1 and finite kappa>=1 required')
 return math.floor(n/(kappa+1))
def piece(N0,rho,fraction,kappa):
 values=sorted_coefficients(N0,rho,fraction);n=len(values);m=active_count(n,kappa)
 if m>=n:raise ValueError('invalid active count')
 Sm=sum(values[:m]);pivot=values[m];A=(Sm-m*pivot)/n;B=sum(values)/n-Sm/n-pivot+m*pivot/n;C=pivot;lo=n/(m+1)-1 if m+1>0 else float('inf');hi=n/m-1 if m>0 else float('inf')
 return {'A':A,'B':B,'C':C,'active_count':m,'active_interval':[max(1.,lo),hi],'coefficient_count':n,'pivot':pivot}
def beta_piece(N0,rho,fraction,kappa):
 p=piece(N0,rho,fraction,kappa);return p['A']*kappa+p['B']/kappa+p['C']
def target_beta(N0=N,rho=RHO,target=TARGET,scale_factor=1.):
 marginal,cross=latent.channel_coefficients();a=ar1.alpha(N0,rho);tau=ar1.mismatch.threshold_control()['tau'];return (scale_factor**4*marginal*a-(scale_factor**2*tau)**2*target)/(scale_factor**4*cross)
def analytic_root(N0=N,rho=RHO,fraction=FRACTION,target=TARGET,lo=BRACKET[0],hi=BRACKET[1],scale_factor=1.):
 validate(N0,rho,fraction,lo,hi);probe=hi;p=piece(N0,rho,fraction,probe);bt=target_beta(N0,rho,target,scale_factor);disc=(p['C']-bt)**2-4*p['A']*p['B']
 if disc<0 or abs(p['A'])<1e-18:raise ValueError('no quadratic root in active piece')
 roots=[(-(p['C']-bt)+sign*math.sqrt(disc))/(2*p['A'])for sign in (1.,-1.)];valid=[x for x in roots if lo<=x<=hi and p['active_interval'][0]-2e-12<=x<=p['active_interval'][1]+2e-12 and active_count(p['coefficient_count'],x)==p['active_count']]
 if len(valid)!=1:raise ValueError('unique root not contained in bracket and active interval')
 return {'kappa':valid[0],'roots':roots,'discriminant':disc,'target_beta':bt,**p}
def bisection_root(steps=100):
 lo,hi=BRACKET
 if not law.risk(N,RHO,FRACTION,lo,'worst')<TARGET<law.risk(N,RHO,FRACTION,hi,'worst'):raise ValueError('bracket does not straddle target')
 for _ in range(steps):
  mid=(lo+hi)/2
  if law.risk(N,RHO,FRACTION,mid,'worst')<=TARGET:lo=mid
  else:hi=mid
 return {'steps':steps,'lower':lo,'upper':hi,'midpoint':(lo+hi)/2,'width':hi-lo}
def domain_control():
 validate(N,RHO,FRACTION,*BRACKET);rejected=0;cases=((1,.5,1.,2.,4.),(87,1.,1.,2.,4.),(87,.5,-.1,2.,4.),(87,.5,1.,.9,4.),(87,.5,1.,4.,2.),(87,.5,1.,2.,float('nan')))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 outside=False
 try:analytic_root(lo=2.,hi=3.)
 except ValueError:outside=True
 return {'accepted':True,'invalid_cases_rejected':rejected,'invalid_cases':len(cases),'outside_active_root_rejected':outside}
def active_set_control():
 rows=[]
 for k in GRID:
  p=piece(N,RHO,FRACTION,k);exact=law.profiled_beta(N,RHO,FRACTION,k,False);probs=exact['probabilities'];upper=sum(abs(x-exact['upper'])<2e-12 for x in probs);interior=sum(exact['lower']+2e-12<x<exact['upper']-2e-12 for x in probs);rows.append({'kappa':k,'piece_beta':beta_piece(N,RHO,FRACTION,k),'lp_beta':exact['value'],'residual':abs(beta_piece(N,RHO,FRACTION,k)-exact['value']),'active_count':p['active_count'],'upper_count':upper,'interior_count':interior})
 return {'rows':rows,'residual':max(x['residual']for x in rows),'counts_match':all(x['active_count']==x['upper_count']and x['interior_count']<=1 for x in rows)}
def bracket_control():
 risks=[law.risk(N,RHO,FRACTION,k,'worst')for k in GRID];return {'grid':GRID,'risks':risks,'lower_passes':risks[0]<TARGET,'upper_fails':risks[-1]>TARGET,'strictly_increasing':all(risks[i]<risks[i+1]for i in range(len(risks)-1))}
def root_control():
 a=analytic_root();b=bisection_root();k=a['kappa'];risk=law.risk(N,RHO,FRACTION,k,'worst');return {'analytic':k,'bisection':b,'residual':abs(k-b['midpoint']),'risk':risk,'risk_residual':abs(risk-TARGET),'in_fixed_window':3.89024156<=k<=3.89024157,'active_count':a['active_count'],'active_interval':a['active_interval'],'target_beta':a['target_beta'],'coefficients':{'A':a['A'],'B':a['B'],'C':a['C']}}
def side_control():
 k=analytic_root()['kappa'];below=k-EPS;above=k+EPS;return {'epsilon':EPS,'below':below,'above':above,'risk_87_below':law.risk(87,RHO,FRACTION,below,'worst'),'risk_87_above':law.risk(87,RHO,FRACTION,above,'worst'),'risk_88_below':law.risk(88,RHO,FRACTION,below,'worst'),'risk_88_above':law.risk(88,RHO,FRACTION,above,'worst'),'below_count':law.minimum_count(FRACTION,below,'worst'),'above_count':law.minimum_count(FRACTION,above,'worst')}
def support_control():
 rows=[]
 for f in (0.,.25,.5,1.):
  vals=[v for _,v in law.coefficients(N,RHO,f)];unrestricted=law.risk_from_beta(N,RHO,min(vals));rows.append({'fraction':f,'radius':latent.radius(N,f),'unrestricted_worst_risk_87':unrestricted,'count_87_passes':unrestricted<=TARGET})
 return {'rows':rows,'subfull_all_pass':all(x['count_87_passes']for x in rows[:-1]),'full_fails':not rows[-1]['count_87_passes']}
def basis_scale_control(theta=.37,factor=2.5):
 base=analytic_root();scaled=analytic_root(scale_factor=factor);c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 marginal,cross=latent.channel_coefficients();rotm=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotc=4*paired.q(rot(ar1.mismatch.NOISE));a=ar1.alpha(N,RHO);tau=ar1.mismatch.threshold_control()['tau'];rot_target=(rotm*a-tau**2*TARGET)/rotc;target_residual=abs(rot_target-base['target_beta']);k=base['kappa'];rot_risk=(rotm*a-rotc*beta_piece(N,RHO,FRACTION,k))/tau**2
 return {'scale_root_residual':abs(base['kappa']-scaled['kappa']),'basis_target_residual':target_residual,'basis_risk_residual':abs(rot_risk-TARGET)}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_CRITICAL_LATENT_LAG_LAW_RADIUS_NOT_EVIDENCE','critical_kappa_interpretation':'TOY_NUISANCE_SET_THRESHOLD_NOT_CONFIDENCE_OR_SIGNIFICANCE'}
def controls():
 d=domain_control();a=active_set_control();b=bracket_control();r=root_control();s=side_control();u=support_control();bs=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['invalid_cases_rejected']==d['invalid_cases']and d['outside_active_root_rejected'],0.,1.,'boolean'),('active_set',a['residual']<2e-10 and a['counts_match'],a['residual'],2e-10,'maximum'),('bracket',b['lower_passes']and b['upper_fails']and b['strictly_increasing'],0.,1.,'boolean'),('root',r['residual']<2e-10 and r['risk_residual']<2e-10 and r['in_fixed_window']and r['active_count']==35,max(r['residual'],r['risk_residual']),2e-10,'maximum'),('sides',s['risk_87_below']<TARGET<s['risk_87_above']and s['risk_88_below']<TARGET and s['risk_88_above']<TARGET and s['below_count']==87 and s['above_count']==88,s['risk_87_below'],TARGET,'maximum'),('support',u['subfull_all_pass']and u['full_fails'],max(x['unrestricted_worst_risk_87']for x in u['rows'][:-1]),TARGET,'maximum'),('basis_scale',max(bs.values())<2e-10,max(bs.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['critical_kappa_interpretation'].startswith('TOY_'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':kind}for x,p,v,h,kind in rows]
def scenario_control(name):
 table={'critical_domain':lambda:domain_control()['outside_active_root_rejected'],'critical_active_set':lambda:active_set_control()['residual']<2e-10 and active_set_control()['counts_match'],'critical_bracket':lambda:bracket_control()['lower_passes']and bracket_control()['upper_fails'],'critical_root':lambda:root_control()['in_fixed_window']and root_control()['active_count']==35,'critical_sides':lambda:side_control()['below_count']==87 and side_control()['above_count']==88,'critical_support':lambda:support_control()['subfull_all_pass']and support_control()['full_fails'],'critical_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'critical_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['critical_kappa_interpretation'].startswith('TOY_')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'N':N,'rho':RHO,'fraction':FRACTION,'risk_ceiling':TARGET,'bracket':list(BRACKET),'side_epsilon':EPS},'domain':domain_control(),'active_set_identity':active_set_control(),'bracket':bracket_control(),'critical_root':root_control(),'side_classification':side_control(),'support_contrast':support_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
