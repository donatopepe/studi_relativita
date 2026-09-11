#!/usr/bin/env python3
"""Auxiliary Gaussian calibration-channel identifiability for Kerr receiver toy."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('calibration_profile_base',HERE/'kerr_composite_calibration.py');profile=importlib.util.module_from_spec(S);S.loader.exec_module(profile)
common=profile.common;receiver=profile.receiver
RESULT='KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION_AT_MODEL_LEVEL_BUT_UNKNOWN_REFERENCE_RESTORES_EXACT_COLLISION_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0'
GATE='PHYSICAL_KERR_CALIBRATOR_REFERENCE_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
DESIGN={'gains':[.8,1.1],'noise':[.25,.35],'reference':[.02,.02],'sample_counts':[1.,10.,100.]}
def joint_covariance(o,g1,g2,n1,n2,r1,r2,N):
 xs=(g1,g2,n1,n2,r1,r2,N)
 if o not in (-1,1)or not all(math.isfinite(x)and x>0 for x in xs):raise ValueError('positive finite branch/gain/noise/reference/sample count required')
 G=common.gamma(o);g=(g1,g2);n=(n1,n2);r=(r1,r2)
 return {'signal':[[g[i]*g[i]*G[i][i]+n[i]*n[i] if i==j else 0. for j in range(2)]for i in range(2)],'calibration':[[g[i]*g[i]*r[i]+n[i]*n[i] if i==j else 0. for j in range(2)]for i in range(2)],'sample_count':N}
def joint_map_control():
 x=joint_covariance(1,.8,1.1,.25,.35,.02,.02,10.);G=common.gamma(1);expected={'signal':[[.8**2*G[0][0]+.25**2,0.],[0.,1.1**2*G[1][1]+.35**2]],'calibration':[[.8**2*.02+.25**2,0.],[0.,1.1**2*.02+.35**2]]}
 return {'joint':x,'formula_residual':max(receiver.res(x[k],expected[k])for k in ('signal','calibration'))}
def known_reference_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];r=DESIGN['reference'];obs=[(gp[i]-r[i])*(gm[i]-r[i]) for i in range(2)]
 # Equal joint outputs require positive squared gains with opposite signs when products are positive.
 return {'reference':r,'sign_obstruction':obs,'positive_collision_possible':any(x<=0. for x in obs)}
def rank2(rows,tol=1e-12):return 2 if abs(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])>tol else 1
def fisher_rank_control():
 G=[common.gamma(1)[i][i]for i in range(2)];r=DESIGN['reference'];g=DESIGN['gains'];n=DESIGN['noise'];cr=[];jr=[];det=[]
 for i in range(2):
  cal=[2*g[i]**2*r[i],2*n[i]**2];sig=[2*g[i]**2*G[i],2*n[i]**2];cr.append(rank2([cal,cal]));jr.append(rank2([sig,cal]));det.append(abs(sig[0]*cal[1]-sig[1]*cal[0]))
 return {'calibration_only_ranks':cr,'joint_ranks':jr,'joint_determinants':det}
def finite_precision_control():
 N=DESIGN['sample_counts'];x=[math.sqrt(2/z)for z in N]
 return {'sample_counts':N,'relative_std':x,'strictly_decreasing':all(x[i+1]<x[i]for i in range(2)),'formula_residual':max(abs(x[i]**2-2/N[i])for i in range(3))}
def weak_channel_control():
 N=[1.,.1,.01];info=[z/2 for z in N]
 return {'effective_sample_counts':N,'relative_information':info,'strictly_decreasing':all(info[i+1]<info[i]for i in range(2)),'last_information':info[-1]}
def unknown_reference_collision_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];plus=[1.,1.];minus=[math.sqrt(gp[i]/gm[i])for i in range(2)];rp=[.02,.02];rm=[rp[i]/(minus[i]**2)for i in range(2)];n=[.25,.35]
 p=joint_covariance(1,*plus,*n,*rp,10.);m=joint_covariance(-1,*minus,*n,*rm,10.)
 return {'plus_gains':plus,'minus_gains':minus,'plus_reference':rp,'minus_reference':rm,'signal_residual':receiver.res(p['signal'],m['signal']),'calibration_residual':receiver.res(p['calibration'],m['calibration']),'joint_residual':max(receiver.res(p['signal'],m['signal']),receiver.res(p['calibration'],m['calibration']))}
def scale_nonclaim_control(factor):
 x=joint_map_control()['joint'];scaled={k:[[factor*factor*z for z in row]for row in x[k]]for k in ('signal','calibration')};back={k:[[z/(factor*factor)for z in row]for row in scaled[k]]for k in scaled};res=max(receiver.res(x[k],back[k])for k in back)
 return {'dimensionless_joint_residual':res,'scale_null_direction':[1.,0.,0.,0.,0.],'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE'}
def _reject(x):
 try:joint_covariance(*x);return False
 except ValueError:return True
def scenario_control(name,case):
 funcs={'calibration_joint_map':lambda:(joint_map_control()['formula_residual']<2e-10,joint_map_control()['formula_residual'],2e-10),'calibration_domain':lambda:(all(_reject(x)for x in ((0,.8,1.1,.25,.35,.02,.02,10),(1,0,1.1,.25,.35,.02,.02,10),(1,.8,1.1,0,.35,.02,.02,10),(1,.8,1.1,.25,.35,0,.02,10),(1,.8,1.1,.25,.35,.02,.02,0))),0.,1.),'calibration_noncollision':lambda:(not known_reference_control()['positive_collision_possible'],min(known_reference_control()['sign_obstruction']),1e-3),'calibration_fisher':lambda:(fisher_rank_control()['joint_ranks']==[2,2],min(fisher_rank_control()['joint_determinants']),1e-8),'calibration_precision':lambda:(finite_precision_control()['strictly_decreasing'],finite_precision_control()['formula_residual'],2e-10),'calibration_weak_limit':lambda:(weak_channel_control()['strictly_decreasing']and weak_channel_control()['last_information']<.1,weak_channel_control()['last_information'],.1),'calibration_unknown_reference':lambda:(unknown_reference_collision_control()['joint_residual']<2e-10,unknown_reference_collision_control()['joint_residual'],2e-10),'calibration_scale':lambda:(scale_nonclaim_control(2.5)['dimensionless_joint_residual']<2e-10,scale_nonclaim_control(2.5)['dimensionless_joint_residual'],2e-10)}
 if name not in funcs:raise KeyError(name)
 return funcs[name]()
def build_artifact():
 controls=[('joint_map',joint_map_control()['formula_residual']<2e-10,joint_map_control()['formula_residual'],2e-10,'maximum'),('domain',all(_reject(x)for x in ((0,.8,1.1,.25,.35,.02,.02,10),(1,0,1.1,.25,.35,.02,.02,10),(1,.8,1.1,0,.35,.02,.02,10),(1,.8,1.1,.25,.35,0,.02,10),(1,.8,1.1,.25,.35,.02,.02,0))),0.,1.,'boolean'),('known_reference_noncollision',not known_reference_control()['positive_collision_possible'],min(known_reference_control()['sign_obstruction']),1e-3,'minimum'),('fisher_rank',fisher_rank_control()['joint_ranks']==[2,2],min(fisher_rank_control()['joint_determinants']),1e-8,'minimum'),('finite_precision',finite_precision_control()['strictly_decreasing'],finite_precision_control()['formula_residual'],2e-10,'maximum'),('weak_limit',weak_channel_control()['strictly_decreasing']and weak_channel_control()['last_information']<.1,weak_channel_control()['last_information'],.1,'maximum'),('unknown_reference_collision',unknown_reference_collision_control()['joint_residual']<2e-10,unknown_reference_collision_control()['joint_residual'],2e-10,'maximum'),('scale_nonclaims',scale_nonclaim_control(2.5)['dimensionless_joint_residual']<2e-10,scale_nonclaim_control(2.5)['dimensionless_joint_residual'],2e-10,'maximum')]
 summary=scale_nonclaim_control(2.5)|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-auxiliary-calibration-channel-v1','result':RESULT,'physical_gate':GATE,'design':DESIGN,'control_summary':summary,'raw_output':{'joint_map':joint_map_control(),'known_reference':known_reference_control(),'fisher':fisher_rank_control(),'finite_precision':finite_precision_control(),'weak_channel':weak_channel_control(),'unknown_reference_collision':unknown_reference_collision_control()}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
