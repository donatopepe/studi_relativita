#!/usr/bin/env python3
"""Fourth-moment correction for one latent pairing lag per covariance window."""
from __future__ import annotations
import functools,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('latent_jitter_base',HERE/'kerr_bounded_pairing_jitter.py');kernel=importlib.util.module_from_spec(S);S.loader.exec_module(kernel)
lagbase=kernel.lagbase;paired=kernel.paired;ar1=kernel.ar1;COUNTS=kernel.COUNTS;RHO=kernel.RHO;RISK=kernel.RISK;FRACTIONS=[0.,.25,.5,1.]
RESULT='KERR_LATENT_WINDOW_JITTER_HAS_A_POSITIVE_FOURTH_MOMENT_JENSEN_CORRECTION_RELATIVE_TO_THE_GAUSSIAN_AVERAGED_KERNEL_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0'
GATE='PHYSICAL_KERR_LATENT_JITTER_DISTRIBUTION_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def validate(N,rho,fraction):
 if not isinstance(N,int)or isinstance(N,bool)or N<2 or not math.isfinite(rho)or not(0<=rho<1)or not math.isfinite(fraction)or not(0<=fraction<=1):raise ValueError('integer N>=2, finite 0<=rho<1 and finite 0<=fraction<=1 required')
def radius(N,fraction):validate(N,0.,fraction);return math.floor(fraction*N+.5)
def weights(N,fraction):
 J=radius(N,fraction);return [(d,1/(2*J+1))for d in range(-J,J+1)]
def _geom(rho,count):return 0. if count<=0 else rho*(1-rho**count)/(1-rho)
def _line_sum(N,rho,a):
 if 0<=a<N:return 1+_geom(rho,a)+_geom(rho,N-1-a)
 base=(1-rho**N)/(1-rho)
 if a<0:return rho**(-a)*base
 return rho**(a-N+1)*base
def _marginal_denominator(N,rho):return N-(N+2*sum((N-k)*rho**k for k in range(1,N)))/N
@functools.lru_cache(maxsize=None)
def fixed_beta(N,rho,offset):
 if not isinstance(offset,int)or isinstance(offset,bool)or abs(offset)>N:raise ValueError('integer |offset|<=N required')
 ar1.validate(N,rho);L=abs(offset);d=_marginal_denominator(N,rho);frob=sum((N-abs(m))*rho**(2*abs(m-L))for m in range(-(N-1),N));rows=[_line_sum(N,rho,i-L)for i in range(N)];cols=[_line_sum(N,rho,j+L)for j in range(N)];u=sum(rows);q=frob-sum(x*x for x in rows)/N-sum(x*x for x in cols)/N+u*u/N**2;return q/d**2
def fixed_beta_explicit(N,rho,offset):
 if not isinstance(offset,int)or isinstance(offset,bool)or abs(offset)>N:raise ValueError('integer |offset|<=N required')
 ar1.validate(N,rho);K=[[rho**abs(i-j-offset)for j in range(N)]for i in range(N)];rows=[sum(row)for row in K];cols=[sum(K[i][j]for i in range(N))for j in range(N)];u=sum(rows);q=sum(x*x for row in K for x in row)-sum(x*x for x in rows)/N-sum(x*x for x in cols)/N+u*u/N**2;return q/_marginal_denominator(N,rho)**2
@functools.lru_cache(maxsize=None)
def latent_beta(N,rho,fraction):
 ws=weights(N,fraction);return sum(w*fixed_beta(N,rho,d)for d,w in ws)
def _kernel_value(rho,J,m):
 if -J<=m<=J:return (1+_geom(rho,m+J)+_geom(rho,J-m))/(2*J+1)
 base=(1-rho**(2*J+1))/(1-rho)/(2*J+1)
 return rho**((-J-m)if m<-J else(m-J))*base
@functools.lru_cache(maxsize=None)
def kernel_beta(N,rho,fraction):
 validate(N,rho,fraction);J=radius(N,fraction);vals=[_kernel_value(rho,J,m)for m in range(-(N-1),N)];K=[[vals[i-j+N-1]for j in range(N)]for i in range(N)];rows=[sum(row)for row in K];u=sum(rows);q=sum(x*x for row in K for x in row)-2*sum(x*x for x in rows)/N+u*u/N**2;return q/_marginal_denominator(N,rho)**2
def channel_coefficients():
 marginal=0.;cross=0.;N=ar1.mismatch.NOISE
 for A,B,_ in paired.branch_pairs():
  for i in range(2):
   for j in range(2):
    marginal+=A[i][i]*A[j][j]+A[i][j]*A[j][i]+B[i][i]*B[j][j]+B[i][j]*B[j][i];cross+=2*(N[i][i]*N[j][j]+N[i][j]*N[j][i])
 return marginal,cross
def total_mse(N,rho=RHO,fraction=0.,model='latent'):
 validate(N,rho,fraction);marginal,cross=channel_coefficients();b=latent_beta(N,rho,fraction)if model=='latent'else kernel_beta(N,rho,fraction)if model=='kernel'else None
 if b is None:raise ValueError("model must be 'latent' or 'kernel'")
 return marginal*ar1.alpha(N,rho)-cross*b
def risk(N,rho=RHO,fraction=0.,model='latent'):return total_mse(N,rho,fraction,model)/ar1.mismatch.threshold_control()['tau']**2
def minimum_count(fraction,model='latent',rho=RHO):
 validate(2,rho,fraction);N=2
 while risk(N,rho,fraction,model)>RISK:N+=1
 return N
def domain_control():
 accepted=radius(3,.5)==2;ws=weights(16,.25);rejected=0;cases=((1,.5,.5),(2.5,.5,.5),(16,-.1,.5),(16,1.,.5),(16,float('nan'),.5),(16,.5,-.1),(16,.5,1.1),(16,.5,float('nan')))
 for args in cases:
  try:validate(*args)
  except ValueError:rejected+=1
 return {'accepted':accepted,'weight_sum':sum(w for _,w in ws),'weight_residual':abs(sum(w for _,w in ws)-1.),'support':len(ws),'invalid_cases_rejected':rejected,'invalid_cases':len(cases)}
def conditional_identity_control():
 marginal,cross=channel_coefficients();rows=[]
 for N,f in ((8,.25),(16,.5),(32,1.)):
  explicit=sum(w*(marginal*ar1.alpha(N,RHO)-cross*fixed_beta_explicit(N,RHO,d))for d,w in weights(N,f));compact=total_mse(N,RHO,f,'latent');rows.append({'N':N,'fraction':f,'radius':radius(N,f),'explicit_conditional_average':explicit,'compact':compact,'residual':abs(explicit-compact)})
 return {'cases':rows,'residual':max(x['residual']for x in rows)}
def zero_support_control():
 rows=[]
 for N in COUNTS:rows.append({'N':N,'latent_mse':total_mse(N,RHO,0.),'paired_mse':paired.paired_coefficient()*ar1.alpha(N,RHO),'latent_risk':risk(N,RHO,0.),'paired_risk':paired.risk(N,RHO)})
 return {'cases':rows,'residual':max(max(abs(x['latent_mse']-x['paired_mse']),abs(x['latent_risk']-x['paired_risk']))for x in rows),'minimum_count':minimum_count(0.)}
def jensen_control():
 rows=[]
 for N in COUNTS:
  for f in FRACTIONS:
   latent=latent_beta(N,RHO,f);gaussian=kernel_beta(N,RHO,f);gap=latent-gaussian;rows.append({'N':N,'fraction':f,'radius':radius(N,f),'latent_beta':latent,'kernel_beta':gaussian,'gap':gap,'latent_risk':risk(N,RHO,f,'latent'),'kernel_risk':risk(N,RHO,f,'kernel')})
 zero=max(abs(x['gap'])for x in rows if x['fraction']==0.);positive=min(x['gap']for x in rows if x['fraction']>0.);risk_order=all(x['latent_risk']<=x['kernel_risk']+2e-10 for x in rows)
 return {'rows':rows,'zero_support_residual':zero,'minimum_positive_gap':positive,'latent_risk_not_greater':risk_order}
def risk_control():
 rows=[]
 for f in FRACTIONS:
  values=[risk(N,RHO,f,'latent')for N in COUNTS];rows.append({'fraction':f,'radii':[radius(N,f)for N in COUNTS],'risks':values,'strictly_decreasing':all(math.isfinite(x)and x>0 for x in values)and all(values[i]>values[i+1]for i in range(2))})
 by_count=[]
 for N in COUNTS:
  values=[risk(N,RHO,f,'latent')for f in FRACTIONS];by_count.append({'N':N,'risks':values,'strictly_increasing':all(values[i]<values[i+1]for i in range(3))})
 return {'rows':rows,'by_count':by_count,'all_count_decreasing':all(x['strictly_decreasing']for x in rows),'all_fraction_increasing':all(x['strictly_increasing']for x in by_count)}
def count_contrast_control():
 rows=[]
 for f in FRACTIONS:
  latent=minimum_count(f,'latent');gaussian=minimum_count(f,'kernel');rows.append({'fraction':f,'latent_count':latent,'kernel_count':gaussian,'latent_risk_at_count':risk(latent,RHO,f,'latent'),'latent_risk_at_predecessor':risk(latent-1,RHO,f,'latent'),'kernel_risk_at_count':risk(gaussian,RHO,f,'kernel'),'kernel_risk_at_predecessor':risk(gaussian-1,RHO,f,'kernel'),'latent_N64_risk':risk(64,RHO,f,'latent'),'kernel_N64_risk':risk(64,RHO,f,'kernel')})
 return {'rows':rows,'latent_counts':[x['latent_count']for x in rows],'kernel_counts':[x['kernel_count']for x in rows],'expected_latent':[87,87,87,87],'expected_kernel':[87,88,88,88],'all_predecessors_fail':all(x['latent_risk_at_count']<=RISK<x['latent_risk_at_predecessor']and x['kernel_risk_at_count']<=RISK<x['kernel_risk_at_predecessor']for x in rows),'all_N64_unsafe':all(x['latent_N64_risk']>RISK and x['kernel_N64_risk']>RISK for x in rows)}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return paired.mm(paired.mm(O,A),paired.t(O))
 base,cross=channel_coefficients();rotbase=sum(paired.q(rot(A))+paired.q(rot(B))for A,B,_ in paired.branch_pairs());rotcross=4*paired.q(rot(ar1.mismatch.NOISE));scaledbase=sum(paired.q(paired.scale(A,factor**2))+paired.q(paired.scale(B,factor**2))for A,B,_ in paired.branch_pairs());scaledcross=4*paired.q(paired.scale(ar1.mismatch.NOISE,factor**2));a=ar1.alpha(64,RHO);b=latent_beta(64,RHO,.5);tau=ar1.mismatch.threshold_control()['tau'];base_risk=(base*a-cross*b)/tau**2;scale_risk=(scaledbase*a-scaledcross*b)/(factor**4*tau**2)
 return {'basis_residual':max(abs(rotbase/base-1.),abs(rotcross/cross-1.)),'scale_residual':abs(scale_risk-base_risk)}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_LATENT_WINDOW_JITTER_FOURTH_MOMENT_CORRECTION_NOT_EVIDENCE','unconditional_sample_law':'NON_GAUSSIAN_MIXTURE_NOT_EMPIRICALLY_VALIDATED'}
def controls():
 d=domain_control();i=conditional_identity_control();z=zero_support_control();j=jensen_control();r=risk_control();c=count_contrast_control();b=basis_scale_control();n=no_ell0_gate();rows=[('domain',d['accepted']and d['weight_residual']<2e-10 and d['invalid_cases_rejected']==d['invalid_cases'],d['weight_residual'],2e-10,'maximum'),('conditional_identity',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('zero_support',z['residual']<2e-10 and z['minimum_count']==87,z['residual'],2e-10,'maximum'),('jensen',j['zero_support_residual']<2e-10 and j['minimum_positive_gap']>0 and j['latent_risk_not_greater'],j['zero_support_residual'],2e-10,'maximum'),('risk',r['all_count_decreasing']and r['all_fraction_increasing'],max(x['risks'][-1]for x in r['rows']),max(x['risks'][0]for x in r['rows']),'maximum'),('count_contrast',c['latent_counts']==c['expected_latent']and c['kernel_counts']==c['expected_kernel']and c['all_predecessors_fail']and c['all_N64_unsafe'],max(x['latent_risk_at_count']for x in c['rows']),RISK,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM'and n['unconditional_sample_law'].startswith('NON_GAUSSIAN'),0.,1.,'boolean')];return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':k}for x,p,v,h,k in rows]
def scenario_control(name):
 table={'latent_domain':lambda:domain_control()['invalid_cases_rejected']==domain_control()['invalid_cases'],'latent_identity':lambda:conditional_identity_control()['residual']<2e-10,'latent_zero':lambda:zero_support_control()['residual']<2e-10 and zero_support_control()['minimum_count']==87,'latent_jensen':lambda:jensen_control()['minimum_positive_gap']>0 and jensen_control()['latent_risk_not_greater'],'latent_risk':lambda:risk_control()['all_count_decreasing']and risk_control()['all_fraction_increasing'],'latent_count_contrast':lambda:count_contrast_control()['latent_counts']==[87,87,87,87]and count_contrast_control()['kernel_counts']==[87,88,88,88],'latent_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'latent_nonclaims':lambda:not no_ell0_gate()['ell0_identified']and no_ell0_gate()['unconditional_sample_law'].startswith('NON_GAUSSIAN')};return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'counts':COUNTS,'radius_fractions':FRACTIONS,'latent_law':'ONE_UNIFORM_INTEGER_LAG_PER_CENTERED_WINDOW','risk_ceiling':RISK},'domain':domain_control(),'conditional_fourth_moment_identity':conditional_identity_control(),'zero_support_limit':zero_support_control(),'jensen_gap':jensen_control(),'latent_risk':risk_control(),'count_contrast':count_contrast_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
