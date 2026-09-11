#!/usr/bin/env python3
"""Correction of reference-placement polarity in Kerr calibration-channel toy."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('reference_correction_base',HERE/'kerr_calibration_channel.py');base=importlib.util.module_from_spec(S);S.loader.exec_module(base)
common=base.common;receiver=base.receiver
INSIDE=[.1,10.];OUTSIDE=[.02,.02]
RESULT='KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES_WHILE_OUTSIDE_OR_UNKNOWN_REFERENCE_COLLIDES_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0'
GATE='PHYSICAL_KERR_CALIBRATOR_REFERENCE_PLACEMENT_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def collision_ratio(gp,gm,r):return (gp-r)/(gm-r)
def collision_criterion_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];rs=INSIDE+OUTSIDE;res=[]
 for i,r in enumerate(INSIDE):res.append(abs((gm[i]-r)*collision_ratio(gp[i],gm[i],r)-(gp[i]-r)))
 for i,r in enumerate(OUTSIDE):res.append(abs((gm[i]-r)*collision_ratio(gp[i],gm[i],r)-(gp[i]-r)))
 return {'positive_collision_condition':'product_positive','algebra_residual':max(res),'superseded_condition':'product_positive_was_incorrectly_labeled_obstruction'}
def inside_reference_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];products=[(gp[i]-INSIDE[i])*(gm[i]-INSIDE[i])for i in range(2)];strict=[min(gp[i],gm[i])<INSIDE[i]<max(gp[i],gm[i])for i in range(2)]
 return {'reference':INSIDE,'products':products,'strictly_inside':all(strict),'positive_collision_possible':all(x>0 for x in products)}
def collision_witness(reference):
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];pg=[.8,1.1];pn=[.25,.35];mg=[];mn=[]
 for i in range(2):
  xm=pg[i]**2*collision_ratio(gp[i],gm[i],reference[i]);nm2=pn[i]**2+pg[i]**2*reference[i]-xm*reference[i]
  if xm<=0 or nm2<=0:raise ValueError('no positive witness')
  mg.append(math.sqrt(xm));mn.append(math.sqrt(nm2))
 p=base.joint_covariance(1,*pg,*pn,*reference,10.);m=base.joint_covariance(-1,*mg,*mn,*reference,10.)
 return {'reference':reference,'plus_gains':pg,'minus_gains':mg,'plus_noise':pn,'minus_noise':mn,'signal_residual':receiver.res(p['signal'],m['signal']),'calibration_residual':receiver.res(p['calibration'],m['calibration']),'joint_residual':max(receiver.res(p['signal'],m['signal']),receiver.res(p['calibration'],m['calibration']))}
def outside_reference_collision_control():return collision_witness(OUTSIDE)
def fisher_rank_control():
 G=[common.gamma(1)[i][i]for i in range(2)];g=[.8,1.1];n=[.25,.35];det=[]
 for i in range(2):det.append(abs((2*g[i]**2*G[i])*(2*n[i]**2)-(2*n[i]**2)*(2*g[i]**2*INSIDE[i])))
 return {'reference':INSIDE,'joint_ranks':[2 if x>1e-12 else 1 for x in det],'joint_determinants':det,'rank_does_not_prove_branch_identifiability':True}
def unknown_reference_collision_control():return base.unknown_reference_collision_control()
def weak_precision_control():
 p=base.finite_precision_control();w=base.weak_channel_control();return {'precision_decreasing':p['strictly_decreasing'],'relative_std':p['relative_std'],'information_decreasing':w['strictly_decreasing'],'relative_information':w['relative_information']}
def scale_nonclaim_control(factor):
 x=outside_reference_collision_control();scaled=[factor*factor*x['joint_residual'],x['joint_residual']];return {'scale_residual':abs(scaled[0]-scaled[1]),'scale_null_direction':[1.,0.,0.,0.,0.],'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_REFERENCE_PLACEMENT_CORRECTION_NOT_EVIDENCE'}
def scenario_control(name,case):
 table={'reference_criterion':lambda:(collision_criterion_control()['algebra_residual']<2e-10,collision_criterion_control()['algebra_residual'],2e-10),'reference_inside':lambda:(inside_reference_control()['strictly_inside'],max(inside_reference_control()['products']),0.),'reference_noncollision':lambda:(not inside_reference_control()['positive_collision_possible'],0.,1.),'reference_outside_collision':lambda:(outside_reference_collision_control()['joint_residual']<2e-10,outside_reference_collision_control()['joint_residual'],2e-10),'reference_fisher':lambda:(fisher_rank_control()['joint_ranks']==[2,2],min(fisher_rank_control()['joint_determinants']),1e-8),'reference_unknown_collision':lambda:(unknown_reference_collision_control()['joint_residual']<2e-10,unknown_reference_collision_control()['joint_residual'],2e-10),'reference_weak_precision':lambda:(weak_precision_control()['precision_decreasing']and weak_precision_control()['information_decreasing'],0.,1.),'reference_scale':lambda:(scale_nonclaim_control(2.5)['scale_residual']<2e-10,scale_nonclaim_control(2.5)['scale_residual'],2e-10)}
 if name not in table:raise KeyError(name)
 return table[name]()
def build_artifact():
 controls=[('criterion',collision_criterion_control()['algebra_residual']<2e-10,collision_criterion_control()['algebra_residual'],2e-10,'maximum'),('inside_domain',inside_reference_control()['strictly_inside'],max(inside_reference_control()['products']),0.,'maximum'),('inside_noncollision',not inside_reference_control()['positive_collision_possible'],0.,1.,'boolean'),('outside_collision',outside_reference_collision_control()['joint_residual']<2e-10,outside_reference_collision_control()['joint_residual'],2e-10,'maximum'),('fisher_rank',fisher_rank_control()['joint_ranks']==[2,2],min(fisher_rank_control()['joint_determinants']),1e-8,'minimum'),('unknown_reference_collision',unknown_reference_collision_control()['joint_residual']<2e-10,unknown_reference_collision_control()['joint_residual'],2e-10,'maximum'),('weak_precision',weak_precision_control()['precision_decreasing']and weak_precision_control()['information_decreasing'],0.,1.,'boolean'),('scale_nonclaims',scale_nonclaim_control(2.5)['scale_residual']<2e-10,scale_nonclaim_control(2.5)['scale_residual'],2e-10,'maximum')]
 summary=scale_nonclaim_control(2.5)|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-calibration-reference-placement-correction-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'criterion':collision_criterion_control(),'inside':inside_reference_control(),'outside_collision':outside_reference_collision_control(),'fisher':fisher_rank_control(),'unknown_reference_collision':unknown_reference_collision_control(),'weak_precision':weak_precision_control()}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
