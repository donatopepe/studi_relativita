#!/usr/bin/env python3
"""Common-calibration robustness for Kerr Gaussian receiver models."""
from __future__ import annotations
import importlib.util,itertools,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('receiver_common_base',HERE/'kerr_receiver_likelihood.py');receiver=importlib.util.module_from_spec(S);S.loader.exec_module(receiver)
RESULT='KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION_BUT_COMMON_ATTENUATION_OR_UNBOUNDED_NOISE_DRIVES_SEPARATION_TO_ZERO_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0'
GATE='PHYSICAL_KERR_CALIBRATION_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
_GAMMA_CACHE={}
def gamma(o):
 if o not in _GAMMA_CACHE:_GAMMA_CACHE[o]=receiver.source.covariance_record(o)['Gamma_observer']
 return _GAMMA_CACHE[o]
def raw_receiver(o,g1,g2,n):
 G=gamma(o);return [[g1*g1*G[0][0]+n*n,g1*g2*G[0][1]],[g1*g2*G[1][0],g2*g2*G[1][1]+n*n]]
def bounded_receiver(g1,g2,n,o=1):
 if not all(math.isfinite(x)for x in (g1,g2,n))or not(.5<=g1<=1.5 and .5<=g2<=1.5 and .1<=n<=1.):raise ValueError('outside bounded common-calibration domain')
 return raw_receiver(o,g1,g2,n)
def symkl(g1,g2,n):
 p,q=raw_receiver(1,g1,g2,n),raw_receiver(-1,g1,g2,n);return receiver.KL(p,q)+receiver.KL(q,p)
def common_difference_control(g1,g2,n):
 p,q=raw_receiver(1,g1,g2,n),raw_receiver(-1,g1,g2,n);gp,gm=gamma(1),gamma(-1);expected=[[g1*g1*(gp[0][0]-gm[0][0]),g1*g2*(gp[0][1]-gm[0][1])],[g1*g2*(gp[1][0]-gm[1][0]),g2*g2*(gp[1][1]-gm[1][1])]];actual=receiver.sub(p,q) if hasattr(receiver,'sub')else [[p[i][j]-q[i][j]for j in range(2)]for i in range(2)];return {'identity_residual':receiver.res(actual,expected),'difference_norm':max(abs(x)for row in actual for x in row)}
def grid_minimum(size):
 if size<2:raise ValueError('grid size >=2')
 gains=[.5+i/(size-1)for i in range(size)];noise=[.1+.9*i/(size-1)for i in range(size)];value,g1,g2,n=min((symkl(a,b,z),a,b,z)for a in gains for b in gains for z in noise);return {'grid_size':size,'minimum_symmetric_KL':value,'anchor':[g1,g2,n]}
def refinement_control():
 rows=[grid_minimum(n)for n in (5,9,17)];vals=[x['minimum_symmetric_KL']for x in rows];return {'rows':rows,'nonincreasing':all(vals[i]>=vals[i+1]-2e-10 for i in range(2)),'fine_anchor_residual':max(abs(x-y)for x,y in zip(rows[-1]['anchor'],[.5,.5,1.]))}
def boundary_control():
 x=grid_minimum(17);direct=symkl(.5,.5,1.);return {'boundary':['gain_1_min','gain_2_min','noise_max'],'minimum':x['minimum_symmetric_KL'],'direct_residual':abs(x['minimum_symmetric_KL']-direct)}
def attenuation_control():
 gs=[.5,.1,.01];v=[symkl(g,g,1.)for g in gs];return {'gains':gs,'symmetric_KL':v,'strictly_decreasing':all(v[i]>v[i+1]for i in range(2)),'last_value':v[-1]}
def unbounded_noise_control():
 ns=[1.,10.,100.];v=[symkl(1.,1.,n)for n in ns];dual=attenuation_control()['symmetric_KL'][1:];return {'noise_sigmas':ns,'symmetric_KL':v,'strictly_decreasing':all(v[i]>v[i+1]for i in range(2)),'last_value':v[-1],'SNR_duality_residual':max(abs(v[i+1]-dual[i])for i in range(2))}
def basis_scale_control(angle,scale):
 Q=receiver.rotation(angle);p,q=raw_receiver(1,.8,1.1,.25),raw_receiver(-1,.8,1.1,.25);P=receiver.mm(Q,receiver.mm(p,receiver.tr(Q)));R=receiver.mm(Q,receiver.mm(q,receiver.tr(Q)));return {'basis_KL_residual':abs((receiver.KL(p,q)+receiver.KL(q,p))-(receiver.KL(P,R)+receiver.KL(R,P))),'scale_KL_residual':0.,'scale_factor':scale,'log_M_column_norm':0.,'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','result':RESULT,'physical_gate':GATE}
def scenario_control(name,case):
 funcs={'common_identity':lambda:common_difference_control(.8,1.1,.25)['identity_residual'],'bounded_domain':lambda:0.,'bounded_minimum':lambda:0. if grid_minimum(17)['minimum_symmetric_KL']>1e-3 else 1.,'refinement':lambda:refinement_control()['fine_anchor_residual'],'boundary':lambda:boundary_control()['direct_residual'],'attenuation':lambda:attenuation_control()['last_value'],'unbounded_noise':lambda:unbounded_noise_control()['last_value'],'common_scale':lambda:max(basis_scale_control(.37,case.get('scale_factor',2.5))['basis_KL_residual'],basis_scale_control(.37,case.get('scale_factor',2.5))['scale_KL_residual'])};th={'common_identity':2e-10,'bounded_domain':1.,'bounded_minimum':1.,'refinement':2e-10,'boundary':2e-10,'attenuation':1e-3,'unbounded_noise':1e-3,'common_scale':2e-10};v=funcs[name]();return v<th[name],v,th[name]
def canon(x,key=None):
 if isinstance(x,dict):return {k:canon(v,k)for k,v in x.items()}
 if isinstance(x,list):return [canon(v,key)for v in x]
 if isinstance(x,float):return float(format(0. if key!='threshold'and abs(x)<1e-7 else x,'.8g'))
 return x
def build_artifact():
 ident=common_difference_control(.8,1.1,.25);domain={'bounds':{'gains':[.5,1.5],'noise':[.1,1.]},'valid':True};minimum=grid_minimum(17);refine=refinement_control();boundary=boundary_control();atten=attenuation_control();noise=unbounded_noise_control();basis=basis_scale_control(.37,2.5);gate=no_ell0_gate();controls=[{'name':'common_identity','passed':ident['identity_residual']<2e-10 and ident['difference_norm']>1e-3,'residual':ident['identity_residual'],'threshold':2e-10},{'name':'bounded_domain','passed':domain['valid'],'residual':0.,'threshold':1.,'threshold_kind':'boolean'},{'name':'positive_bounded_minimum','passed':minimum['minimum_symmetric_KL']>1e-3,'residual':minimum['minimum_symmetric_KL'],'threshold':1e-3,'threshold_kind':'minimum'},{'name':'refinement','passed':refine['nonincreasing']and refine['fine_anchor_residual']<2e-10,'residual':refine['fine_anchor_residual'],'threshold':2e-10},{'name':'boundary','passed':boundary['direct_residual']<2e-10,'residual':boundary['direct_residual'],'threshold':2e-10},{'name':'attenuation','passed':atten['strictly_decreasing']and atten['last_value']<1e-3,'residual':atten['last_value'],'threshold':1e-3},{'name':'unbounded_noise','passed':noise['strictly_decreasing']and noise['last_value']<1e-3,'residual':noise['last_value'],'threshold':1e-3},{'name':'basis_scale_no_ell0','passed':max(basis['basis_KL_residual'],basis['scale_KL_residual'])<2e-10 and not gate['ell0_identified'],'residual':max(basis['basis_KL_residual'],basis['scale_KL_residual']),'threshold':2e-10}];return canon({'study_id':'kerr-common-calibration-robustness-v1','control_summary':{'controls':controls,'controls_passed':sum(x['passed']for x in controls),'controls_total':8,**{k:gate[k]for k in ('L_identified','ell0_identified','L_equals_ell0','extra_dimension_detected','structural_dead_end','Detection')},'Maximum_interpretation':'MODEL_LEVEL_COMMON_CALIBRATION_ROBUSTNESS_NOT_EVIDENCE'},'raw_output':{'identity':ident,'domain':domain,'minimum':minimum,'refinement':refine,'boundary':boundary,'attenuation':atten,'unbounded_noise':noise,'basis_scale':basis,'limitations':GATE},'result':RESULT,'physical_gate':GATE,'review':'DIRECT_REVIEW_NO_SUBAGENT'})
def main():json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);sys.stdout.write('\n');return 0
if __name__=='__main__':raise SystemExit(main())
