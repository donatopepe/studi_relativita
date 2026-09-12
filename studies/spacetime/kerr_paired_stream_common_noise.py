#!/usr/bin/env python3
"""Exact paired-stream covariance penalty under shared Gaussian receiver noise."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('paired_base',HERE/'kerr_ar1_temporal_dependence.py');ar1=importlib.util.module_from_spec(S);S.loader.exec_module(ar1)
COUNTS=ar1.COUNTS;RHO=.5;RISK=ar1.RISK
RESULT='KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0'
GATE='PHYSICAL_KERR_CROSS_STREAM_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'

def t(A):return [[A[j][i]for j in range(len(A))]for i in range(len(A[0]))]
def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
def tr(A):return sum(A[i][i]for i in range(len(A)))
def add(A,B):return [[A[i][j]+B[i][j]for j in range(len(A[0]))]for i in range(len(A))]
def scale(A,x):return [[x*v for v in row]for row in A]
def q(A):return tr(A)**2+tr(mm(A,t(A)))
def det(A):
 if len(A)==1:return A[0][0]
 return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:]for row in A[1:]])for j in range(len(A)))
def is_spd(A,tol=1e-12):
 return bool(A)and all(len(row)==len(A)for row in A)and max(abs(A[i][j]-A[j][i])for i in range(len(A))for j in range(len(A)))<=tol and all(det([row[:k]for row in A[:k]])>tol for k in range(1,len(A)+1))
def block(A,K,B):return [A[i]+K[i]for i in range(len(A))]+[t(K)[i]+B[i]for i in range(len(B))]
def validate_joint(A,B,K):
 if not(len(A)==len(B)==len(K)==2 and all(len(row)==2 for M in (A,B,K)for row in M)and is_spd(A)and is_spd(B)and is_spd(block(A,K,B))):raise ValueError('SPD 2x2 marginals and SPD paired block required')

def branch_pairs():
 cov=ar1.known.covariances();noise=ar1.mismatch.NOISE
 return [(cov[0],cov[1],noise),(cov[2],cov[3],noise)]
def independent_coefficient():return ar1.known.total_coefficient()
def paired_coefficient(K_scale=1.):
 pairs=branch_pairs();out=0.
 for A,B,K in pairs:
  K=scale(K,K_scale);validate_joint(A,B,K);out+=q(A)+q(B)-2*q(K)
 return out

def domain_control():
 pairs=branch_pairs();valid=all(is_spd(block(A,K,B))for A,B,K in pairs);rejected=0
 for K in ([[100.,0.],[0.,100.]],[[float('nan'),0.],[0.,0.]]):
  try:validate_joint(pairs[0][0],pairs[0][1],K)
  except ValueError:rejected+=1
 return {'valid_joint_blocks':valid,'invalid_cases_rejected':rejected,'cases':2}
def cross_wick_component(A,B,K):
 p=len(A);total=0.
 for i in range(p):
  for j in range(p):total+=A[i][i]*A[j][j]+A[i][j]*A[j][i]+B[i][i]*B[j][j]+B[i][j]*B[j][i]-2*(K[i][i]*K[j][j]+K[i][j]*K[j][i])
 return total
def identity_control():
 cases=[(*branch_pairs()[0],),(*branch_pairs()[1],)];rows=[]
 for A,B,K in cases:rows.append([cross_wick_component(A,B,K),q(A)+q(B)-2*q(K)])
 return {'cases':rows,'residual':max(abs(a-b)for a,b in rows)}
def coefficient_control():
 paired=paired_coefficient();ind=independent_coefficient();ratio=math.sqrt(paired/ind)
 return {'paired_coefficient':paired,'independent_coefficient':ind,'rms_ratio':ratio,'strict_reduction':0<paired<ind,'small_gain':.99<=ratio<1.}
def rms(N,rho=RHO,K_scale=1.):return math.sqrt(paired_coefficient(K_scale)*ar1.alpha(N,rho))
def rms_control():
 values=[rms(N)for N in COUNTS]
 return {'rho':RHO,'counts':COUNTS,'rms':values,'strictly_decreasing':all(math.isfinite(x)and x>0 for x in values)and all(values[i]>values[i+1]for i in range(len(values)-1))}
def risk(N,rho=RHO,K_scale=1.):return paired_coefficient(K_scale)*ar1.alpha(N,rho)/ar1.mismatch.threshold_control()['tau']**2
def minimum_count(rho=RHO,K_scale=1.):
 N=2
 while risk(N,rho,K_scale)>RISK:N+=1
 return N
def safe_count_control():
 N=minimum_count();return {'minimum_count':N,'risk_at_count':risk(N),'risk_at_predecessor':risk(N-1),'N64_risk':risk(64),'N64_passes':risk(64)<=RISK}
def zero_shared_control():
 paired=paired_coefficient(0.);ind=independent_coefficient();N=minimum_count(K_scale=0.)
 return {'paired_zero_coefficient':paired,'independent_coefficient':ind,'coefficient_residual':abs(paired-ind),'minimum_count':N,'independent_minimum_count':ar1.safe_count_control(RHO)['minimum_count']}
def basis_scale_control(theta=.37,factor=2.5):
 c,s=math.cos(theta),math.sin(theta);O=[[c,-s],[s,c]]
 def rot(A):return mm(mm(O,A),t(O))
 base=paired_coefficient();rotated=sum(q(rot(A))+q(rot(B))-2*q(rot(K))for A,B,K in branch_pairs())
 scaled=sum(q(scale(A,factor**2))+q(scale(B,factor**2))-2*q(scale(K,factor**2))for A,B,K in branch_pairs())
 scale_risk=scaled*ar1.alpha(64,RHO)/(factor**4*ar1.mismatch.threshold_control()['tau']**2)
 return {'basis_residual':abs(rotated/base-1.),'scale_residual':abs(scale_risk-risk(64))}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_PAIRED_COMMON_NOISE_COVARIANCE_GAIN_NOT_EVIDENCE'}
def controls():
 d=domain_control();i=identity_control();c=coefficient_control();r=rms_control();safe=safe_count_control();z=zero_shared_control();b=basis_scale_control();n=no_ell0_gate()
 rows=[('domain',d['valid_joint_blocks']and d['invalid_cases_rejected']==d['cases'],0.,1.,'boolean'),('identity',i['residual']<2e-10,i['residual'],2e-10,'maximum'),('coefficient',c['strict_reduction']and c['small_gain'],1-c['rms_ratio'],.01,'maximum'),('rms',r['strictly_decreasing'],r['rms'][-1],r['rms'][0],'maximum'),('safe_count',safe['minimum_count']==87 and safe['risk_at_count']<=RISK<safe['risk_at_predecessor']and not safe['N64_passes'],safe['risk_at_count'],RISK,'maximum'),('zero_shared',z['coefficient_residual']<2e-10 and z['minimum_count']==z['independent_minimum_count']==88,z['coefficient_residual'],2e-10,'maximum'),('basis_scale',max(b.values())<2e-10,max(b.values()),2e-10,'maximum'),('nonclaims',not n['L_identified']and not n['ell0_identified']and n['Detection']=='NO_POSITIVE_DETECTION_CLAIM',0.,1.,'boolean')]
 return [{'name':x,'passed':bool(p),'residual':v,'threshold':h,'threshold_kind':k}for x,p,v,h,k in rows]
def scenario_control(name):
 table={'paired_domain':lambda:domain_control()['valid_joint_blocks']and domain_control()['invalid_cases_rejected']==2,'paired_identity':lambda:identity_control()['residual']<2e-10,'paired_coefficient':lambda:coefficient_control()['strict_reduction']and coefficient_control()['small_gain'],'paired_rms':lambda:rms_control()['strictly_decreasing'],'paired_safe_count':lambda:safe_count_control()['minimum_count']==87 and not safe_count_control()['N64_passes'],'paired_zero_shared':lambda:zero_shared_control()['coefficient_residual']<2e-10 and zero_shared_control()['minimum_count']==88,'paired_basis_scale':lambda:max(basis_scale_control().values())<2e-10,'paired_nonclaims':lambda:not no_ell0_gate()['ell0_identified']}
 return bool(table[name]())
def report():
 cs=controls();n=no_ell0_gate();return {'result':RESULT,'physical_gate':GATE,'parameters':{'rho':RHO,'counts':COUNTS,'risk_ceiling':RISK,'cross_stream_model':'PAIRED_SHARED_ADDITIVE_GAUSSIAN_NOISE','pair_independence':'BRANCH_PAIRS_INDEPENDENT'},'joint_domain':domain_control(),'cross_wick_identity':identity_control(),'coefficient':coefficient_control(),'rms':rms_control(),'safe_count':safe_count_control(),'zero_shared_limit':zero_shared_control(),'basis_scale':basis_scale_control(),'control_summary':{**n,'controls':cs,'controls_passed':sum(x['passed']for x in cs),'controls_total':len(cs)}}
if __name__=='__main__':json.dump(report(),sys.stdout,indent=2,sort_keys=True);print()
