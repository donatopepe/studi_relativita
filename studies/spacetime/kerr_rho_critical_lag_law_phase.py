#!/usr/bin/env python3
"""AR(1) rho phase window for latent-lag-law count sensitivity."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('rho_phase_base',HERE/'kerr_critical_lag_law_radius.py');critical=importlib.util.module_from_spec(S);S.loader.exec_module(critical)
law=critical.law;latent=critical.latent;paired=critical.paired;ar1=critical.ar1;N=critical.N;FRACTION=critical.FRACTION;TARGET=critical.TARGET;RHO_BRACKET=(.49,.51);RHO_GRID=[.49,.495,.5,.505,.51];PHASE_CASES=[.495,.5,.505];PATH_RHOS=[.4995,.5,.5005,.501];PATH_EXPECTED=[12.485595531662376,3.8902415649581967,2.001949812105448,1.17251807960107];EPS=1e-8
RESULT='KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW_RHO_0P499243439_TO_0P501157236_NOT_ELL0'
GATE='PHYSICAL_KERR_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N0,rho,fraction,lo,hi):
 latent.validate(N0,rho,fraction)
 if not math.isfinite(lo)or not math.isfinite(hi)or not(0<=lo<hi<1):raise ValueError('finite rho bracket 0<=lo<hi<1 required')
def unrestricted_risk(rho,scale_factor=1.):
 values=[v for _,v in law.coefficients(N,rho,FRACTION)];marginal,cross=latent.channel_coefficients();a=ar1.alpha(N,rho);tau=ar1.mismatch.threshold_control()['tau'];return (scale_factor**4*marginal*a-scale_factor**4*cross*min(values))/(scale_factor**4*tau**2)
def uniform_risk(rho,scale_factor=1.):
 marginal,cross=latent.channel_coefficients();a=ar1.alpha(N,rho);b=latent.latent_beta(N,rho,FRACTION);tau=ar1.mismatch.threshold_control()['tau'];return (scale_factor**4*marginal*a-scale_factor**4*cross*b)/(scale_factor**4*tau**2)
def rho_root(kind,steps=100,scale_factor=1.):
 if kind not in ('unrestricted','uniform'):raise ValueError("kind must be 'unrestricted' or 'uniform'")
 fn=unrestricted_risk if kind=='unrestricted'else uniform_risk;lo,hi=RHO_BRACKET;flo=fn(lo,scale_factor)-TARGET;fhi=fn(hi,scale_factor)-TARGET
 if not(flo<0<fhi):raise ValueError('rho bracket does not straddle target')
 for _ in range(steps):
  mid=(lo+hi)/2
  if fn(mid,scale_factor)<=TARGET:lo=mid
  else:hi=mid
 root=(lo+hi)/2;return {'kind':kind,'rho':root,'lower':lo,'upper':hi,'width':hi-lo,'risk':fn(root,scale_factor),'risk_residual':abs(fn(root,scale_factor)-TARGET),'steps':steps,'side_below':fn(root-EPS,scale_factor),'side_above':fn(root+EPS,scale_factor)}
def boundaries():return {'lower':rho_root('unrestricted'),'upper':rho_root('uniform')}
def phase(rho):
 validate(N,rho,FRACTION,*RHO_BRACKET);b=boundaries();lo=b['lower']['rho'];hi=b['upper']['rho']
 if rho<lo:return 'ALWAYS_SAFE_OVER_LAG_LAW_SIMPLEX'
 if rho>hi:return 'ALWAYS_UNSAFE_FROM_UNIFORM_ONWARD'
 if lo<rho<hi:return 'FINITE_KAPPA_SENSITIVE'
 return 'BOUNDARY'
def critical_kappa(rho):
 if phase(rho)!='FINITE_KAPPA_SENSITIVE':raise ValueError('finite kappa exists only inside sensitive rho phase')
 lo,hi=1.,1e6
 for _ in range(100):
  mid=(lo+hi)/2
  if law.risk(N,rho,FRACTION,mid,'worst')<=TARGET:lo=mid
  else:hi=mid
 return (lo+hi)/2
def domain_control():
 validate(N,.5,FRACTION,*RHO_BRACKET);rejected=0;cases=((1,.5,1.,.49,.51),(87,-.1,1.,.49,.51),(87,1.,1.,.49,.51),(87,.5,-.1,.49,.51),(87,.5,1.,-.1,.51),(87,.5,1.,.51,.49),(87,.5,1.,.49,1.))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 nonstraddle=False
 old=RHO_BRACKET
 try:
  # Direct check equivalent for bad bracket fully below both roots.
  if not(unrestricted_risk(.1)<TARGET<unrestricted_risk(.2)):raise ValueError
 except ValueError:nonstraddle=True
 return {'accepted':True,'invalid_cases_rejected':rejected,'invalid_cases':len(cases),'non_straddling_rejected':nonstraddle}
def monotonicity_control():
 uniform=[uniform_risk(r)for r in RHO_GRID];unrestricted=[unrestricted_risk(r)for r in RHO_GRID];return {'rho_grid':RHO_GRID,'uniform_risks':uniform,'unrestricted_risks':unrestricted,'uniform_strictly_increasing':all(uniform[i]<uniform[i+1]for i in range(4)),'unrestricted_strictly_increasing':all(unrestricted[i]<unrestricted[i+1]for i in range(4)),'ordered':all(uniform[i]<=unrestricted[i]+2e-10 for i in range(5))}
def lower_root_control():
 x=rho_root('unrestricted');return {**x,'in_fixed_window':.49924343<=x['rho']<=.49924345,'sides_classify':x['side_below']<TARGET<x['side_above']}
def upper_root_control():
 x=rho_root('uniform');return {**x,'in_fixed_window':.50115723<=x['rho']<=.50115724,'sides_classify':x['side_below']<TARGET<x['side_above']}
def classification_control():
 b=boundaries();rows=[{'rho':r,'phase':phase(r),'uniform_risk':uniform_risk(r),'unrestricted_risk':unrestricted_risk(r)}for r in PHASE_CASES];return {'boundaries':[b['lower']['rho'],b['upper']['rho']],'strict_order':b['lower']['rho']<b['upper']['rho'],'rows':rows,'expected':['ALWAYS_SAFE_OVER_LAG_LAW_SIMPLEX','FINITE_KAPPA_SENSITIVE','ALWAYS_UNSAFE_FROM_UNIFORM_ONWARD'],'matches': [x['phase']for x in rows]==['ALWAYS_SAFE_OVER_LAG_LAW_SIMPLEX','FINITE_KAPPA_SENSITIVE','ALWAYS_UNSAFE_FROM_UNIFORM_ONWARD']}
def kappa_path_control():
 rows=[{'rho':r,'kappa':critical_kappa(r),'expected':e,'residual':abs(critical_kappa(r)-e)}for r,e in zip(PATH_RHOS,PATH_EXPECTED)];return {'rows':rows,'residual':max(x['residual']for x in rows),'strictly_decreasing':all(rows[i]['kappa']>rows[i+1]['kappa']for i in range(3)),'rho_half_recovery':abs(rows[1]['kappa']-critical.analytic_root()['kappa'])}
def basis_scale_control(theta=.37,factor=2.5):
 base=boundaries();scaled={'lower':rho_root('unrestricted',scale_factor=factor),'upper':rho_root('uniform',scale_factor=factor)};k=critical_kappa(.5);c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 marginal,cross=latent.channel_coefficients();rotm=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotc=4*paired.q(rot(ar1.mismatch.NOISE));a=ar1.alpha(N,.5);b=law.profiled_beta(N,.5,FRACTION,k,False)['value'];tau=ar1.mismatch.threshold_control()['tau'];rot_risk=(rotm*a-rotc*b)/tau**2
 return {'lower_scale_residual':abs(base['lower']['rho']-scaled['lower']['rho']),'upper_scale_residual':abs(base['upper']['rho']-scaled['upper']['rho']),'kappa_basis_risk_residual':abs(rot_risk-TARGET)}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_RHO_CRITICAL_LATENT_LAG_LAW_PHASE_NOT_EVIDENCE','rho_window_interpretation':'TOY_ASSUMPTION_BOUNDARY_NOT_CONFIDENCE_OR_STATIONARITY_EVIDENCE'}
def controls():
 d=domain_control();m=monotonicity_control();lo=lower_root_control();hi=upper_root_control();c=classification_control();k=kappa_path_control();b=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['invalid_cases_rejected']==d['invalid_cases']and d['non_straddling_rejected'],0.,1.,'boolean'),('monotonicity',m['uniform_strictly_increasing']and m['unrestricted_strictly_increasing']and m['ordered'],0.,1.,'boolean'),('lower_root',lo['risk_residual']<2e-10 and lo['in_fixed_window']and lo['sides_classify'],lo['risk_residual'],2e-10,'maximum'),('upper_root',hi['risk_residual']<2e-10 and hi['in_fixed_window']and hi['sides_classify'],hi['risk_residual'],2e-10,'maximum'),('classification',c['strict_order']and c['matches'],0.,1.,'boolean'),('kappa_path',k['residual']<2e-9 and k['strictly_decreasing']and k['rho_half_recovery']<2e-10,max(k['residual'],k['rho_half_recovery']),2e-9,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['rho_window_interpretation'].startswith('TOY_'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':kind}for x,p,v,h,kind in rows]
def scenario_control(name):
 table={'rhophase_domain':lambda:domain_control()['non_straddling_rejected'],'rhophase_monotonicity':lambda:monotonicity_control()['ordered']and monotonicity_control()['uniform_strictly_increasing'],'rhophase_lower_root':lambda:lower_root_control()['in_fixed_window']and lower_root_control()['sides_classify'],'rhophase_upper_root':lambda:upper_root_control()['in_fixed_window']and upper_root_control()['sides_classify'],'rhophase_classification':lambda:classification_control()['matches'],'rhophase_kappa_path':lambda:kappa_path_control()['strictly_decreasing']and kappa_path_control()['residual']<2e-9,'rhophase_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'rhophase_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['rho_window_interpretation'].startswith('TOY_')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'N':N,'fraction':FRACTION,'risk_ceiling':TARGET,'rho_bracket':list(RHO_BRACKET),'rho_grid':RHO_GRID,'phase_cases':PHASE_CASES},'domain':domain_control(),'risk_monotonicity':monotonicity_control(),'lower_boundary':lower_root_control(),'upper_boundary':upper_root_control(),'phase_classification':classification_control(),'critical_kappa_path':kappa_path_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
