#!/usr/bin/env python3
"""Composite common-calibration profile gate for Kerr covariance hypotheses."""
from __future__ import annotations
import importlib.util,itertools,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('common_profile_base',HERE/'kerr_common_calibration.py');common=importlib.util.module_from_spec(S);S.loader.exec_module(common)
receiver=common.receiver
RESULT='KERR_COMPOSITE_BRANCH_SETS_ARE_DISJOINT_UNDER_TOY_BOUNDED_PROFILED_COMMON_CALIBRATION_BUT_RELAXED_POSITIVE_GAINS_COLLIDE_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0'
GATE='PHYSICAL_KERR_SHARED_CALIBRATION_MODEL_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def bounded_profile_covariance(o,g1,g2,n):
 if o not in (-1,1)or not all(math.isfinite(x)for x in (g1,g2,n))or not(.5<=g1<=1.5 and .5<=g2<=1.5 and .1<=n<=1.):raise ValueError('outside bounded profiled-calibration domain')
 return common.raw_receiver(o,g1,g2,n)
def interval(signal,n):return [.25*signal+n*n,2.25*signal+n*n]
def bounded_overlap_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)]
 # Global output intervals include all bounded noise values. A gap in either channel proves set disjointness.
 plus=[[.25*x+.01,2.25*x+1.]for x in gp];minus=[[.25*x+.01,2.25*x+1.]for x in gm]
 gaps=[max(0.,max(plus[i][0],minus[i][0])-min(plus[i][1],minus[i][1]))for i in range(2)]
 return {'plus_output_intervals':plus,'minus_output_intervals':minus,'channel_gaps':gaps,'second_channel_gap':gaps[1],'sets_overlap':all(x==0. for x in gaps)}
def diagonal_symkl(p,q):return .5*sum(p[i][i]/q[i][i]+q[i][i]/p[i][i]-2. for i in range(2))
def profile_minimum(size):
 if size<2:raise ValueError('grid size >=2')
 gains=[.5+i/(size-1)for i in range(size)];noise=[.1+.9*i/(size-1)for i in range(size)]
 points=list(itertools.product(gains,gains,noise));best=(math.inf,None,None)
 plus=[(x,bounded_profile_covariance(1,*x))for x in points];minus=[(x,bounded_profile_covariance(-1,*x))for x in points]
 for xp,p in plus:
  for xm,m in minus:
   v=diagonal_symkl(p,m)
   if v<best[0]:best=(v,xp,xm)
 return {'grid_size':size,'minimum_symmetric_KL':best[0],'plus_anchor':list(best[1]),'minus_anchor':list(best[2])}
def refinement_control():
 xs=[profile_minimum(n)for n in (3,5,9)];v=[x['minimum_symmetric_KL']for x in xs]
 return {'grid_sizes':[3,5,9],'minimum_symmetric_KL':v,'nonincreasing':all(v[i+1]<=v[i]+2e-10 for i in range(2)),'finest':xs[-1]}
def boundary_control():
 x=profile_minimum(9);pa=x['plus_anchor'];ma=x['minus_anchor'];v=diagonal_symkl(bounded_profile_covariance(1,*pa),bounded_profile_covariance(-1,*ma))
 on=any(z in (.5,1.5)for z in pa[:2]+ma[:2])and any(z in (.1,1.)for z in (pa[2],ma[2]))
 return {'plus_anchor':pa,'minus_anchor':ma,'on_declared_boundary':on,'direct_residual':abs(v-x['minimum_symmetric_KL'])}
def relaxed_collision_control():
 gp=[common.gamma(1)[i][i]for i in range(2)];gm=[common.gamma(-1)[i][i]for i in range(2)];plus=[1.,1.];minus=[math.sqrt(gp[i]/gm[i])for i in range(2)];n=.25
 p=common.raw_receiver(1,*plus,n);m=common.raw_receiver(-1,*minus,n)
 return {'plus_gains':plus,'minus_gains':minus,'noise_sigma':n,'target_covariance':p,'covariance_residual':receiver.res(p,m)}
def basis_scale_control(theta,factor):
 x=profile_minimum(9);p=bounded_profile_covariance(1,*x['plus_anchor']);m=bounded_profile_covariance(-1,*x['minus_anchor']);base=receiver.KL(p,m)+receiver.KL(m,p);co=math.cos(theta);si=math.sin(theta);Q=[[co,-si],[si,co]]
 def cv(A):return receiver.mm(Q,receiver.mm(A,receiver.tr(Q)))
 basis=receiver.KL(cv(p),cv(m))+receiver.KL(cv(m),cv(p));scaled=[[factor*factor*z for z in row]for row in p],[[factor*factor*z for z in row]for row in m];scale=receiver.KL(*scaled)+receiver.KL(scaled[1],scaled[0])
 return {'basis_KL_residual':abs(base-basis),'scale_KL_residual':abs(base-scale),'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'UMCH':'UNPROVEN_SECONDARY_CANDIDATE','L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','Maximum_interpretation':'MODEL_LEVEL_BOUNDED_COMPOSITE_CALIBRATION_PROFILE_NOT_EVIDENCE'}
def scenario_control(name,case):
 table={'profile_overlap':lambda:(not bounded_overlap_control()['sets_overlap'],bounded_overlap_control()['second_channel_gap'],1.),'profile_domain':lambda:(all(_reject(x)for x in ((0,.8,.2),(.8,.8,0),(.4,.8,.2),(.8,1.6,.2),(.8,.8,1.1))),0.,1.),'profile_minimum':lambda:(profile_minimum(9)['minimum_symmetric_KL']>1e-3,profile_minimum(9)['minimum_symmetric_KL'],1e-3),'profile_refinement':lambda:(refinement_control()['nonincreasing'],0.,1.),'profile_boundary':lambda:(boundary_control()['on_declared_boundary']and boundary_control()['direct_residual']<2e-10,boundary_control()['direct_residual'],2e-10),'profile_collision':lambda:(relaxed_collision_control()['covariance_residual']<2e-10,relaxed_collision_control()['covariance_residual'],2e-10),'profile_basis_scale':lambda:(max(basis_scale_control(.37,2.5)['basis_KL_residual'],basis_scale_control(.37,2.5)['scale_KL_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_KL_residual'],basis_scale_control(.37,2.5)['scale_KL_residual']),2e-10),'profile_nonclaims':lambda:(not no_ell0_gate()['ell0_identified'],0.,1.)}
 if name not in table:raise KeyError(name)
 return table[name]()
def _reject(x):
 try:bounded_profile_covariance(1,*x);return False
 except ValueError:return True
def build_artifact():
 controls=[('analytic_overlap',not bounded_overlap_control()['sets_overlap'],bounded_overlap_control()['second_channel_gap'],1.,'minimum'),('bounded_domain',all(_reject(x)for x in ((0,.8,.2),(.8,.8,0),(.4,.8,.2),(.8,1.6,.2),(.8,.8,1.1))),0.,1.,'boolean'),('positive_profile_minimum',profile_minimum(9)['minimum_symmetric_KL']>1e-3,profile_minimum(9)['minimum_symmetric_KL'],1e-3,'minimum'),('refinement',refinement_control()['nonincreasing'],0.,1.,'boolean'),('boundary',boundary_control()['on_declared_boundary']and boundary_control()['direct_residual']<2e-10,boundary_control()['direct_residual'],2e-10,'maximum'),('relaxed_collision',relaxed_collision_control()['covariance_residual']<2e-10,relaxed_collision_control()['covariance_residual'],2e-10,'maximum'),('basis_scale',max(basis_scale_control(.37,2.5)['basis_KL_residual'],basis_scale_control(.37,2.5)['scale_KL_residual'])<2e-10,max(basis_scale_control(.37,2.5)['basis_KL_residual'],basis_scale_control(.37,2.5)['scale_KL_residual']),2e-10,'maximum'),('nonclaims',not no_ell0_gate()['ell0_identified'],0.,1.,'boolean')]
 summary=no_ell0_gate()|{'controls_total':8,'controls_passed':sum(x[1]for x in controls),'controls':[{'name':n,'passed':p,'residual':r,'threshold':t,'threshold_kind':k}for n,p,r,t,k in controls]}
 return {'schema':'kerr-composite-calibration-profile-v1','result':RESULT,'physical_gate':GATE,'control_summary':summary,'raw_output':{'overlap':bounded_overlap_control(),'profile_refinement':refinement_control(),'boundary':boundary_control(),'relaxed_collision':relaxed_collision_control(),'basis_scale':basis_scale_control(.37,2.5)}}
if __name__=='__main__':json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);print()
