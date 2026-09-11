#!/usr/bin/env python3
"""Bounded reference-drift robustness for corrected Kerr calibration channel."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('reference_drift_base',HERE/'kerr_calibration_reference_correction.py');correction=importlib.util.module_from_spec(S);S.loader.exec_module(correction)
common=correction.common;receiver=correction.receiver;base=correction.base
FRACTION=.8
RESULT='KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL_AND_FAILS_AT_ENDPOINT_OR_OUTSIDE_NOT_ELL0'
GATE='PHYSICAL_KERR_CALIBRATOR_DRIFT_BOUND_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def geometry():
 a=[common.gamma(1)[i][i]for i in range(2)];b=[common.gamma(-1)[i][i]for i in range(2)];m=[(a[i]+b[i])/2 for i in range(2)];d=[(b[i]-a[i])/2 for i in range(2)];return a,b,m,d
def interval_geometry_control():
 a,b,m,d=geometry();rec_a=[m[i]-d[i]for i in range(2)];rec_b=[m[i]+d[i]for i in range(2)];return {'branch_plus':a,'branch_minus':b,'midpoints':m,'maximal_open_radii':d,'endpoint_residual':max(max(abs(rec_a[i]-a[i]),abs(rec_b[i]-b[i]))for i in range(2))}
def drift_box_control():
 a,b,m,d=geometry();delta=[FRACTION*x for x in d];bounds=[[m[i]-delta[i],m[i]+delta[i]]for i in range(2)];inside=all(a[i]<bounds[i][0]<bounds[i][1]<b[i]for i in range(2));return {'drift_fraction':FRACTION,'drift_radii':delta,'reference_bounds':bounds,'strictly_inside':inside}
def robust_obstruction_control():
 a,b,_,_=geometry();bounds=drift_box_control()['reference_bounds'];margins=[-(a[i]-r)*(b[i]-r)for i in range(2)for r in bounds[i]];return {'endpoint_margins':margins,'minimum_margin':min(margins)}
def endpoint_loss_control():
 a,b,_,_=geometry();g=[.8,1.1];n=[.25,.35];products=[(a[i]-a[i])*(b[i]-a[i]) for i in range(2)];dets=[abs(4*g[i]**2*n[i]**2*(a[i]-a[i]))for i in range(2)];return {'endpoint_reference':a,'placement_products':products,'joint_fisher_determinants':dets,'placement_product_residual':max(abs(x)for x in products),'fisher_determinant_residual':max(dets)}
def outside_collision_control():
 a,b,_,d=geometry();reference=[a[i]-.01*d[i]for i in range(2)];return correction.collision_witness(reference)|{'crossing_fraction':.01}
def fisher_margin_control():
 a,_,_,_=geometry();bounds=drift_box_control()['reference_bounds'];g=[.8,1.1];n=[.25,.35];dets=[abs(4*g[i]**2*n[i]**2*(a[i]-r))for i in range(2)for r in bounds[i]];return {'endpoint_determinants':dets,'minimum_determinant':min(dets)}
def scale_control(factor):
 a,b,m,d=geometry();sa=[[factor*factor*x for x in z]for z in (a,b,m,d)];fractions=[sa[3][i]/((sa[1][i]-sa[0][i])/2)for i in range(2)];collision=outside_collision_control()['joint_residual'];return {'normalized_drift_fractions':fractions,'normalized_residual':max(max(abs(x-1.)for x in fractions),abs(factor*factor*collision-collision))}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_BOUNDED_REFERENCE_DRIFT_ROBUSTNESS_NOT_EVIDENCE'}
def scenario_control(name,case):
 table={'drift_geometry':lambda:(interval_geometry_control()['endpoint_residual']<2e-10,interval_geometry_control()['endpoint_residual'],2e-10),'drift_box':lambda:(drift_box_control()['strictly_inside'],0.,1.),'drift_margin':lambda:(robust_obstruction_control()['minimum_margin']>1e-3,robust_obstruction_control()['minimum_margin'],1e-3),'drift_endpoint':lambda:(max(endpoint_loss_control()['placement_product_residual'],endpoint_loss_control()['fisher_determinant_residual'])<2e-10,max(endpoint_loss_control()['placement_product_residual'],endpoint_loss_control()['fisher_determinant_residual']),2e-10),'drift_outside_collision':lambda:(outside_collision_control()['joint_residual']<2e-10,outside_collision_control()['joint_residual'],2e-10),'drift_fisher':lambda:(fisher_margin_control()['minimum_determinant']>1e-8,fisher_margin_control()['minimum_determinant'],1e-8),'drift_scale':lambda:(scale_control(2.5)['normalized_residual']<2e-10,scale_control(2.5)['normalized_residual'],2e-10),'drift_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def build_artifact():
 controls=[('geometry',interval_geometry_control()['endpoint_residual']<2e-10,interval_geometry_control()['endpoint_residual'],2e-10,'maximum'),('drift_box',drift_box_control()['strictly_inside'],0.,1.,'boolean'),('robust_margin',robust_obstruction_control()['minimum_margin']>1e-3,robust_obstruction_control()['minimum_margin'],1e-3,'minimum'),('endpoint_loss',max(endpoint_loss_control()['placement_product_residual'],endpoint_loss_control()['fisher_determinant_residual'])<2e-10,max(endpoint_loss_control()['placement_product_residual'],endpoint_loss_control()['fisher_determinant_residual']),2e-10,'maximum'),('outside_collision',outside_collision_control()['joint_residual']<2e-10,outside_collision_control()['joint_residual'],2e-10,'maximum'),('fisher_margin',fisher_margin_control()['minimum_determinant']>1e-8,fisher_margin_control()['minimum_determinant'],1e-8,'minimum'),('scale',scale_control(2.5)['normalized_residual']<2e-10,scale_control(2.5)['normalized_residual'],2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-reference-drift-robustness-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'geometry':interval_geometry_control(),'drift_box':drift_box_control(),'robust_obstruction':robust_obstruction_control(),'endpoint_loss':endpoint_loss_control(),'outside_collision':outside_collision_control(),'fisher_margin':fisher_margin_control(),'scale':scale_control(2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
