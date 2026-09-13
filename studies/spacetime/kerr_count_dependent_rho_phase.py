#!/usr/bin/env python3
"""Finite-count movement of full-support latent-lag rho phase window."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('count_phase_base',HERE/'kerr_rho_critical_lag_law_phase.py');phasebase=importlib.util.module_from_spec(S);S.loader.exec_module(phasebase)
law=phasebase.law;latent=phasebase.latent;paired=phasebase.paired;ar1=phasebase.ar1;TARGET=phasebase.TARGET;FRACTION=phasebase.FRACTION;COUNTS=[53,54,64,87,128,256];FINITE_COUNTS=COUNTS[1:];EXPECTED_LOW=[.08426533356447777,.3098163393254819,.4992434389165544,.6499918971371095,.8146286754250995];EXPECTED_HIGH=[.09587387505842565,.31310163195008234,.501157235677365,.651271982688411,.8153222242345937];EXPECTED_WIDTH=[.011608541493947883,.003285292624600422,.0019137967608106043,.0012800855513015463,.0006935488094941267];EPS=1e-8
RESULT='KERR_LATENT_LAG_LAW_RHO_SENSITIVITY_WINDOW_MOVES_UPWARD_AND_NARROWS_WITH_TOY_SAMPLE_COUNT_WHILE_N53_IS_UNSAFE_ALREADY_AT_IID_NOT_ELL0'
GATE='PHYSICAL_KERR_SAMPLE_COUNT_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,rho,lo,hi):
 ar1.validate(N,rho)
 if not math.isfinite(lo)or not math.isfinite(hi)or not(0<=lo<hi<1):raise ValueError('integer N>=2, finite rho and bracket 0<=lo<hi<1 required')
def risk(N,rho,kind,scale_factor=1.):
 validate(N,rho,0.,.999)
 if kind not in ('unrestricted','uniform'):raise ValueError("kind must be 'unrestricted' or 'uniform'")
 marginal,cross=latent.channel_coefficients();a=ar1.alpha(N,rho);b=min(v for _,v in law.coefficients(N,rho,FRACTION))if kind=='unrestricted'else latent.latent_beta(N,rho,FRACTION);tau=ar1.mismatch.threshold_control()['tau'];return (scale_factor**4*marginal*a-scale_factor**4*cross*b)/(scale_factor**4*tau**2)
def rho_root(N,kind,steps=100,scale_factor=1.):
 validate(N,0.,0.,.999);lo,hi=0.,.999;flo=risk(N,lo,kind,scale_factor)-TARGET;fhi=risk(N,hi,kind,scale_factor)-TARGET
 if not(flo<0<fhi):raise ValueError('nonnegative rho root not bracketed')
 for _ in range(steps):
  mid=(lo+hi)/2
  if risk(N,mid,kind,scale_factor)<=TARGET:lo=mid
  else:hi=mid
 root=(lo+hi)/2;return {'N':N,'kind':kind,'rho':root,'lower':lo,'upper':hi,'width':hi-lo,'risk':risk(N,root,kind,scale_factor),'risk_residual':abs(risk(N,root,kind,scale_factor)-TARGET),'side_below':risk(N,root-EPS,kind,scale_factor),'side_above':risk(N,root+EPS,kind,scale_factor)}
def phase_row(N,scale_factor=1.):
 u0=risk(N,0.,'uniform',scale_factor);x0=risk(N,0.,'unrestricted',scale_factor)
 if u0>TARGET or x0>TARGET:return {'N':N,'classification':'ALWAYS_UNSAFE_FROM_RHO_ZERO','iid_uniform_risk':u0,'iid_unrestricted_risk':x0,'rho_low':None,'rho_high':None,'window_width':None}
 lo=rho_root(N,'unrestricted',scale_factor=scale_factor);hi=rho_root(N,'uniform',scale_factor=scale_factor);return {'N':N,'classification':'FINITE_NONNEGATIVE_RHO_PHASE','iid_uniform_risk':u0,'iid_unrestricted_risk':x0,'rho_low':lo['rho'],'rho_high':hi['rho'],'window_width':hi['rho']-lo['rho'],'lower_risk_residual':lo['risk_residual'],'upper_risk_residual':hi['risk_residual'],'sides_classify':lo['side_below']<TARGET<lo['side_above']and hi['side_below']<TARGET<hi['side_above']}
def domain_control():
 validate(54,.1,0.,.999);rejected=0;cases=((1,.1,0.,.9),(2.5,.1,0.,.9),(54,-.1,0.,.9),(54,1.,0.,.9),(54,float('nan'),0.,.9),(54,.1,-.1,.9),(54,.1,.9,.1),(54,.1,0.,1.))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 nonroot=False
 try:rho_root(53,'uniform')
 except ValueError:nonroot=True
 return {'accepted':True,'invalid_cases_rejected':rejected,'invalid_cases':len(cases),'N53_nonroot_rejected':nonroot}
def iid_threshold_control():
 rows=[{'N':N,'uniform_risk':risk(N,0.,'uniform'),'unrestricted_risk':risk(N,0.,'unrestricted')}for N in range(2,55)];first=next(x['N']for x in rows if x['uniform_risk']<=TARGET and x['unrestricted_risk']<=TARGET);return {'N53':rows[-2],'N54':rows[-1],'first_safe_count':first,'N53_unsafe':rows[-2]['uniform_risk']>TARGET and rows[-2]['unrestricted_risk']>TARGET,'N54_safe':rows[-1]['uniform_risk']<TARGET and rows[-1]['unrestricted_risk']<TARGET}
def root_identity_control():
 rows=[]
 for kind,prior in (('unrestricted',phasebase.lower_root_control()),('uniform',phasebase.upper_root_control())):
  x=rho_root(87,kind);rows.append({'kind':kind,'generic':x['rho'],'prior':prior['rho'],'root_residual':abs(x['rho']-prior['rho']),'risk_residual':x['risk_residual'],'sides_classify':x['side_below']<TARGET<x['side_above']})
 return {'rows':rows,'residual':max(max(x['root_residual'],x['risk_residual'])for x in rows),'all_sides_classify':all(x['sides_classify']for x in rows)}
def boundaries_control():
 rows=[phase_row(N)for N in COUNTS];finite=rows[1:];res=[]
 for x,lo,hi,w in zip(finite,EXPECTED_LOW,EXPECTED_HIGH,EXPECTED_WIDTH):res.extend((abs(x['rho_low']-lo),abs(x['rho_high']-hi),abs(x['window_width']-w)))
 return {'rows':rows,'expected_low':EXPECTED_LOW,'expected_high':EXPECTED_HIGH,'expected_width':EXPECTED_WIDTH,'residual':max(res),'N53_no_window':rows[0]['classification']=='ALWAYS_UNSAFE_FROM_RHO_ZERO','all_sides_classify':all(x['sides_classify']for x in finite)}
def ordering_control():
 x=boundaries_control()['rows'][1:];lo=[r['rho_low']for r in x];hi=[r['rho_high']for r in x];return {'lower':lo,'upper':hi,'all_strictly_ordered':all(lo[i]<lo[i+1]and hi[i]<hi[i+1]for i in range(len(lo)-1)),'within_case_order':all(a<b for a,b in zip(lo,hi))}
def width_control():
 widths=[phase_row(N)['window_width']for N in FINITE_COUNTS];return {'counts':FINITE_COUNTS,'widths':widths,'expected':EXPECTED_WIDTH,'residual':max(abs(a-b)for a,b in zip(widths,EXPECTED_WIDTH)),'strictly_decreasing':all(widths[i]>widths[i+1]for i in range(len(widths)-1)),'largest_count':54,'smallest_count':256}
def basis_scale_control(theta=.37,factor=2.5):
 base={N:phase_row(N)for N in (54,87,256)};scaled={N:phase_row(N,factor)for N in (54,87,256)};scale_residual=max(max(abs(base[N][k]-scaled[N][k])for k in ('rho_low','rho_high'))for N in base);c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 marginal,cross=latent.channel_coefficients();rotm=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotc=4*paired.q(rot(ar1.mismatch.NOISE));rho=base[87]['rho_low'];a=ar1.alpha(87,rho);b=min(v for _,v in law.coefficients(87,rho,FRACTION));tau=ar1.mismatch.threshold_control()['tau'];rot_risk=(rotm*a-rotc*b)/tau**2
 return {'scale_boundary_residual':scale_residual,'basis_risk_residual':abs(rot_risk-TARGET),'N87_prior_residual':max(abs(base[87]['rho_low']-phasebase.lower_root_control()['rho']),abs(base[87]['rho_high']-phasebase.upper_root_control()['rho']))}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_COUNT_DEPENDENT_RHO_PHASE_NOT_EVIDENCE','count_phase_interpretation':'TOY_MARKOV_GATE_NOT_SAMPLE_SIZE_PRESCRIPTION_OR_CONFIDENCE'}
def controls():
 d=domain_control();i=iid_threshold_control();r=root_identity_control();b=boundaries_control();o=ordering_control();w=width_control();bs=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['invalid_cases_rejected']==d['invalid_cases']and d['N53_nonroot_rejected'],0.,1.,'boolean'),('iid_threshold',i['N53_unsafe']and i['N54_safe']and i['first_safe_count']==54,i['N54']['unrestricted_risk'],TARGET,'maximum'),('root_identity',r['residual']<2e-10 and r['all_sides_classify'],r['residual'],2e-10,'maximum'),('boundaries',b['residual']<2e-10 and b['N53_no_window']and b['all_sides_classify'],b['residual'],2e-10,'maximum'),('ordering',o['all_strictly_ordered']and o['within_case_order'],0.,1.,'boolean'),('width',w['residual']<2e-10 and w['strictly_decreasing'],w['residual'],2e-10,'maximum'),('basis_scale',max(bs.values())<2e-10,max(bs.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['count_phase_interpretation'].startswith('TOY_'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':kind}for x,p,v,h,kind in rows]
def scenario_control(name):
 table={'countphase_domain':lambda:domain_control()['N53_nonroot_rejected'],'countphase_iid':lambda:iid_threshold_control()['first_safe_count']==54,'countphase_identity':lambda:root_identity_control()['residual']<2e-10,'countphase_boundaries':lambda:boundaries_control()['residual']<2e-10 and boundaries_control()['N53_no_window'],'countphase_ordering':lambda:ordering_control()['all_strictly_ordered']and ordering_control()['within_case_order'],'countphase_width':lambda:width_control()['strictly_decreasing']and width_control()['residual']<2e-10,'countphase_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'countphase_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['count_phase_interpretation'].startswith('TOY_')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'counts':COUNTS,'finite_window_counts':FINITE_COUNTS,'fraction':FRACTION,'risk_ceiling':TARGET},'domain':domain_control(),'iid_threshold':iid_threshold_control(),'N87_root_identity':root_identity_control(),'fixed_count_boundaries':boundaries_control(),'boundary_ordering':ordering_control(),'window_contraction':width_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
