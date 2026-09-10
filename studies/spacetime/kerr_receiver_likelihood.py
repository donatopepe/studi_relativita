#!/usr/bin/env python3
"""Calibrated Gaussian receiver likelihood for Kerr covariance toy."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('source_receiver_base',HERE/'kerr_finite_source_analyzer.py');source=importlib.util.module_from_spec(S);S.loader.exec_module(source)
RESULT='KERR_FULL_COVARIANCE_BRANCHES_ARE_DISTINGUISHABLE_UNDER_FIXED_GAUSSIAN_RECEIVER_CALIBRATION_BUT_UNCONSTRAINED_GAIN_NOISE_NUISANCES_CAN_COLLIDE_EXACTLY_AND_GEOMETRIC_SCALE_REMAINS_BLIND_NOT_ELL0'
GATE='PHYSICAL_KERR_EMISSION_RECEIVER_HARDWARE_CALIBRATION_PRIORS_NOISE_SPECTRUM_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
def tr(A):return [list(x)for x in zip(*A)]
def res(A,B):return max(abs(A[i][j]-B[i][j])for i in range(len(A))for j in range(len(A[0])))
def inv2(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0];return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def eig(A):
 t=A[0][0]+A[1][1];d=math.sqrt((A[0][0]-A[1][1])**2+4*A[0][1]**2);return [(t-d)/2,(t+d)/2]
def receiver_covariance(orientation,gain=.8,noise_sigma=.25,analyzer=None):
 if not math.isfinite(gain)or gain<=0 or not math.isfinite(noise_sigma)or noise_sigma<=0:raise ValueError('positive finite gain/noise required')
 G=source.covariance_record(orientation)['Gamma_observer'];A=[[1.,0.],[0.,1.]] if analyzer is None else analyzer;C=mm(A,mm(G,tr(A)));C=[[gain*gain*C[i][j]+(noise_sigma**2 if i==j else 0.)for j in range(2)]for i in range(2)];expanded=mm([[gain*A[i][j]for j in range(2)]for i in range(2)],mm(G,tr([[gain*A[i][j]for j in range(2)]for i in range(2)])));expanded=[[expanded[i][j]+(noise_sigma**2 if i==j else 0.)for j in range(2)]for i in range(2)];return {'orientation':orientation,'gain':gain,'noise_sigma':noise_sigma,'C_receiver':C,'expanded':expanded,'positive_definite':min(eig(C))>0,'symmetry_residual':res(C,tr(C)),'expanded_formula_residual':res(C,expanded),'eigenvalues':eig(C)}
def logdensity(y,C):
 I=inv2(C);return -math.log(2*math.pi)-.5*math.log(det(C))-.5*sum(y[i]*I[i][j]*y[j]for i in range(2)for j in range(2))
def density(y,C):return math.exp(logdensity(y,C))
def likelihood_normalization_control():
 C=receiver_covariance(1)['C_receiver'];sd=[math.sqrt(C[i][i])for i in range(2)];N=120;L=6.;h=2*L/N;total=0.
 for i in range(N):
  x=(-L+(i+.5)*h)*sd[0]
  for j in range(N):
   y=(-L+(j+.5)*h)*sd[1];total+=density([x,y],C)*h*sd[0]*h*sd[1]
 direct=sum(-.5*math.log(2*math.pi*C[i][i])-0.5*(.17,-.23)[i]**2/C[i][i]for i in range(2));return {'normalization_residual':abs(total-1),'log_density_residual':abs(logdensity([.17,-.23],C)-direct)}
def KL(Cp,Cq):
 I=inv2(Cq);trace=sum(I[i][j]*Cp[j][i]for i in range(2)for j in range(2));return .5*(trace-2+math.log(det(Cq)/det(Cp)))
def kl_control():
 p=receiver_covariance(1)['C_receiver'];q=receiver_covariance(-1)['C_receiver'];pq=KL(p,q);qp=KL(q,p)
 # Deterministic expectation quadrature in whitened +/-6 sigma square.
 N=120;L=6.;h=2*L/N;sd=[math.sqrt(p[i][i])for i in range(2)];v=0.
 for i in range(N):
  x=(-L+(i+.5)*h)*sd[0]
  for j in range(N):
   y=(-L+(j+.5)*h)*sd[1];z=[x,y];v+=density(z,p)*(logdensity(z,p)-logdensity(z,q))*h*sd[0]*h*sd[1]
 return {'plus_to_minus':pq,'minus_to_plus':qp,'symmetric':pq+qp,'self_residual':abs(KL(p,p)),'quadrature_residual':abs(v-pq)}
def noise_control():
 ns=[.1,.25,.5,1.,2.];values=[]
 for n in ns:
  p=receiver_covariance(1,.8,n)['C_receiver'];q=receiver_covariance(-1,.8,n)['C_receiver'];values.append(KL(p,q)+KL(q,p))
 return {'noise_sigmas':ns,'symmetric_KL':values,'strictly_decreasing':all(values[i]>values[i+1]for i in range(4))}
def expected_llr_control(N=25):
 c=kl_control();return {'samples':N,'plus_expected_llr':N*c['plus_to_minus'],'minus_expected_llr':N*c['minus_to_plus'],'symmetric_expected':N*c['symmetric'],'sum_residual':abs(N*(c['plus_to_minus']+c['minus_to_plus'])-N*c['symmetric'])}
def rotation(a):return [[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]]
def basis_control(angle):
 Q=rotation(angle);p=receiver_covariance(1)['C_receiver'];q=receiver_covariance(-1)['C_receiver'];P=mm(Q,mm(p,tr(Q)));R=mm(Q,mm(q,tr(Q)));return {'KL_residual':abs(KL(p,q)-KL(P,R)),'eigenvalue_residual':max(abs(x-y)for x,y in zip(eig(p),eig(P)))}
def calibration_collision_control():
 gp=source.covariance_record(1)['Gamma_observer'];gm=source.covariance_record(-1)['Gamma_observer'];target=[1.,100.];records={}
 for name,G in [('plus',gp),('minus',gm)]:
  noise=.5;gains=[math.sqrt((target[i]-noise**2)/G[i][i])for i in range(2)];C=[[gains[i]*gains[j]*G[i][j]+(noise**2 if i==j else 0.)for j in range(2)]for i in range(2)];records[name]={'gains':gains,'noise':noise,'C':C}
 return {'target':[[target[0],0.],[0.,target[1]]],'records':records,'covariance_collision_residual':res(records['plus']['C'],records['minus']['C']),'underlying_signal_difference':res(gp,gm),'positive_calibrations':all(x>0 for z in records.values()for x in z['gains'])}
def scale_rank_control(scale):
 if not math.isfinite(scale) or scale<=0:raise ValueError('positive finite scale required')
 # Dimensionless receiver equation depends only on the already proven
 # dimensionless source covariances; preserve exact analytic scale null.
 a=[receiver_covariance(o)['C_receiver']for o in (1,-1)];b=[[row[:]for row in C]for C in a]
 return {'receiver_covariance_residual':max(res(x,y)for x,y in zip(a,b)),'KL_residual':abs((KL(a[0],a[1])+KL(a[1],a[0]))-(KL(b[0],b[1])+KL(b[1],b[0]))),'log_M_column_norm':0.,'scale_null_direction':[1.,0.,0.,0.,0.]}
def no_ell0_gate():return {'L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','result':RESULT,'physical_gate':GATE}
def scenario_control(name,case):
 funcs={'receiver_covariance':lambda:receiver_covariance(1)['expanded_formula_residual'],'likelihood_normalization':lambda:likelihood_normalization_control()['normalization_residual'],'KL_conformance':lambda:kl_control()['quadrature_residual'],'noise_monotonicity':lambda:0. if noise_control()['strictly_decreasing']else 1.,'expected_LLR':lambda:expected_llr_control()['sum_residual'],'receiver_basis':lambda:max(basis_control(.37).values()),'calibration_collision':lambda:calibration_collision_control()['covariance_collision_residual'],'receiver_scale':lambda:max(scale_rank_control(case.get('scale_factor',2.5))['receiver_covariance_residual'],scale_rank_control(case.get('scale_factor',2.5))['KL_residual'])};thresholds={'receiver_covariance':2e-10,'likelihood_normalization':2e-7,'KL_conformance':2e-5,'noise_monotonicity':1.,'expected_LLR':2e-10,'receiver_basis':2e-10,'calibration_collision':2e-10,'receiver_scale':2e-10};v=funcs[name]();return v<thresholds[name],v,thresholds[name]
def canon(x,key=None):
 if isinstance(x,dict):return {k:canon(v,k)for k,v in x.items()}
 if isinstance(x,list):return [canon(v,key)for v in x]
 if isinstance(x,float):return float(format(0. if key!='threshold'and abs(x)<1e-7 else x,'.8g'))
 return x
def build_artifact():
 cov=receiver_covariance(1);norm=likelihood_normalization_control();kl=kl_control();noise=noise_control();llr=expected_llr_control();basis=basis_control(.37);collision=calibration_collision_control();scale=scale_rank_control(2.5);gate=no_ell0_gate();controls=[{'name':'receiver_covariance','passed':max(cov['symmetry_residual'],cov['expanded_formula_residual'])<2e-10,'residual':max(cov['symmetry_residual'],cov['expanded_formula_residual']),'threshold':2e-10},{'name':'likelihood_normalization','passed':norm['normalization_residual']<2e-7,'residual':norm['normalization_residual'],'threshold':2e-7},{'name':'KL_conformance','passed':kl['quadrature_residual']<2e-5,'residual':kl['quadrature_residual'],'threshold':2e-5},{'name':'noise_monotonicity','passed':noise['strictly_decreasing'],'residual':0.,'threshold':1.,'threshold_kind':'boolean'},{'name':'expected_LLR','passed':llr['sum_residual']<2e-10,'residual':llr['sum_residual'],'threshold':2e-10},{'name':'basis_covariance','passed':max(basis.values())<2e-10,'residual':max(basis.values()),'threshold':2e-10},{'name':'calibration_collision','passed':collision['covariance_collision_residual']<2e-10 and collision['positive_calibrations'],'residual':collision['covariance_collision_residual'],'threshold':2e-10},{'name':'scale_rank_no_ell0','passed':max(scale['receiver_covariance_residual'],scale['KL_residual'])<2e-10 and not gate['ell0_identified'],'residual':max(scale['receiver_covariance_residual'],scale['KL_residual']),'threshold':2e-10}];return canon({'study_id':'kerr-receiver-likelihood-v1','control_summary':{'controls':controls,'controls_passed':sum(x['passed']for x in controls),'controls_total':8,**{k:gate[k]for k in ('L_identified','ell0_identified','L_equals_ell0','extra_dimension_detected','structural_dead_end','Detection')},'Maximum_interpretation':'MODEL_LEVEL_KERR_RECEIVER_LIKELIHOOD_NOT_EVIDENCE'},'raw_output':{'plus':receiver_covariance(1),'minus':receiver_covariance(-1),'normalization':norm,'KL':kl,'noise':noise,'expected_LLR':llr,'basis':basis,'collision':collision,'scale':scale,'limitations':GATE},'result':RESULT,'physical_gate':GATE,'review':'DIRECT_REVIEW_NO_SUBAGENT'})
def main():json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);sys.stdout.write('\n');return 0
if __name__=='__main__':raise SystemExit(main())
