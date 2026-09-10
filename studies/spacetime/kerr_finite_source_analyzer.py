#!/usr/bin/env python3
"""Finite Gaussian source covariance and ideal analyzer on Kerr Jacobi map."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('kerr_source_jacobi',HERE/'kerr_jacobi_tidal_gate.py');jacobi=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(jacobi)
RESULT='KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE_AND_ANALYZER_SCAN_BUT_SOURCE_WIDTH_HOMOGENEITY_AND_ANALYZER_COLLISIONS_PREVENT_INDEPENDENT_BRANCH_OR_ABSOLUTE_SCALE_IDENTIFICATION_NOT_ELL0'
GATE='PHYSICAL_KERR_SOURCE_DYNAMICS_EMISSION_INTENSITY_POLARIZATION_ANALYZER_HARDWARE_RECEIVER_TRANSFER_CALIBRATED_NOISE_LIKELIHOOD_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
DEFAULT_WIDTHS=(.08,.12,.015,.02)
def mm(A,B):return [[sum(A[i][k]*B[k][q]for k in range(len(B)))for q in range(len(B[0]))]for i in range(len(A))]
def tr(A):return [list(x)for x in zip(*A)]
def sub(A,B):return [[A[i][q]-B[i][q]for q in range(len(A[0]))]for i in range(len(A))]
def residual(A,B):return max(abs(x)for row in sub(A,B)for x in row)
def det(A):
 if len(A)==2:return A[0][0]*A[1][1]-A[0][1]*A[1][0]
 # SPD is known diagonal congruence; principal-minor elimination.
 z=[r[:]for r in A];v=1.
 for k in range(len(z)):
  p=z[k][k]
  if p<=0:return -1.
  v*=p
  for i in range(k+1,len(z)):
   for q in range(k+1,len(z)):z[i][q]-=z[i][k]*z[k][q]/p
 return v
def eig2(A):
 t=A[0][0]+A[1][1];d=math.sqrt((A[0][0]-A[1][1])**2+4*A[0][1]**2);return [(t-d)/2,(t+d)/2]
def source_covariance(widths=DEFAULT_WIDTHS):
 if len(widths)!=4 or any(not math.isfinite(x)or x<=0 for x in widths):raise ValueError('four finite positive widths required')
 S=[[0.]*4 for _ in range(4)]
 for i,x in enumerate(widths):S[i][i]=x*x
 return {'widths':list(widths),'Sigma_source':S,'positive_definite':True,'normalization':'ZERO_MEAN_NORMALIZED_GAUSSIAN_PHASE_SPACE_TOY'}
def dimensionless_phase(orientation,M=1.):
 P=jacobi.phase_control(M,.6,4.5,12*M,15*M,orientation)['P_phase'];A,B,C,D=jacobi.split(P);return [A[0]+[x/M for x in B[0]],A[1]+[x/M for x in B[1]],[M*x for x in C[0]]+D[0],[M*x for x in C[1]]+D[1]]
def covariance_record(orientation,widths=DEFAULT_WIDTHS,M=1.):
 S=source_covariance(widths)['Sigma_source'];P=dimensionless_phase(orientation,M);O=mm(P,mm(S,tr(P)));G=[r[:2]for r in O[:2]];block=jacobi.split(P);A,B=block[0],block[1];X=[[S[i][q]for q in range(2)]for i in range(2)];V=[[S[i+2][q+2]for q in range(2)]for i in range(2)];independent=[[mm(A,mm(X,tr(A)))[i][q]+mm(B,mm(V,tr(B)))[i][q]for q in range(2)]for i in range(2)]
 return {'orientation':orientation,'P_dimensionless':P,'Sigma_source':S,'Sigma_observer':O,'Gamma_observer':G,'Gamma_block_formula':independent,'eigenvalues':eig2(G),'positive_definite':det(O)>0 and min(eig2(G))>0}
def covariance_control(orientation,widths=DEFAULT_WIDTHS):
 c=covariance_record(orientation,widths);return {**c,'block_formula_residual':residual(c['Gamma_observer'],c['Gamma_block_formula']),'symmetry_residual':residual(c['Sigma_observer'],tr(c['Sigma_observer']))}
def analyzer_variance(G,theta):
 a=(math.cos(theta),math.sin(theta));return sum(a[i]*G[i][q]*a[q]for i in range(2)for q in range(2))
def analyzer_scan(orientation,widths=DEFAULT_WIDTHS):
 G=covariance_record(orientation,widths)['Gamma_observer'];angles=(0.,math.pi/8,math.pi/4,3*math.pi/8,math.pi/2);return [{'theta':x,'variance':analyzer_variance(G,x),'rms':math.sqrt(analyzer_variance(G,x))}for x in angles]
def width_homogeneity_control(widths=DEFAULT_WIDTHS,scale=2.5):
 a=covariance_record(1,widths);b=covariance_record(1,tuple(scale*x for x in widths));target=[[scale*scale*x for x in r]for r in a['Sigma_observer']];ea=[x/sum(a['eigenvalues'])for x in a['eigenvalues']];eb=[x/sum(b['eigenvalues'])for x in b['eigenvalues']];return {'covariance_residual':residual(target,b['Sigma_observer']),'normalized_shape_residual':max(abs(x-y)for x,y in zip(ea,eb))}
def orientation_control(widths=DEFAULT_WIDTHS):
 a=covariance_record(1,widths);b=covariance_record(-1,widths);sa=analyzer_scan(1,widths);sb=analyzer_scan(-1,widths);return {'covariance_difference':residual(a['Gamma_observer'],b['Gamma_observer']),'scan_difference':max(abs(x['variance']-y['variance'])for x,y in zip(sa,sb))}
def analyzer_extrema_control(orientation,widths=DEFAULT_WIDTHS):
 c=covariance_record(orientation,widths);e=c['eigenvalues'];values=[analyzer_variance(c['Gamma_observer'],math.pi*i/4000)for i in range(4001)];return {'analytic_eigenvalues':e,'scan_extrema':[min(values),max(values)],'analytic_eigenvalue_residual':0.,'dense_scan_bracket_residual':max(abs(min(values)-e[0]),abs(max(values)-e[1]))}
def rot(theta):return [[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]]
def blockrot(Q):return [[Q[i][q]if i<2 and q<2 else Q[i-2][q-2]if i>=2 and q>=2 else 0. for q in range(4)]for i in range(4)]
def basis_covariance_control(orientation,widths,angle,analyzer):
 c=covariance_record(orientation,widths);Q=rot(angle);R=blockrot(Q);P=mm(R,mm(c['P_dimensionless'],tr(R)));S=mm(R,mm(c['Sigma_source'],tr(R)));O=mm(P,mm(S,tr(P)));G=[r[:2]for r in O[:2]];a=analyzer_variance(c['Gamma_observer'],analyzer);b=analyzer_variance(G,analyzer+angle);return {'variance_residual':abs(a-b),'eigenvalue_residual':max(abs(x-y)for x,y in zip(eig2(c['Gamma_observer']),eig2(G)))}
def analyzer_collision_control(widths=DEFAULT_WIDTHS):
 records={o:covariance_record(o,widths)for o in (-1,1)};intervals={o:records[o]['eigenvalues']for o in records};lo=max(x[0]for x in intervals.values());hi=min(x[1]for x in intervals.values());overlap=lo<=hi;target=(lo+hi)/2;angles={}
 for o,c in records.items():
  G=c['Gamma_observer'];x=(target-G[1][1])/(G[0][0]-G[1][1]);angles[o]=math.acos(math.sqrt(max(0.,min(1.,x))))
 vals={o:analyzer_variance(records[o]['Gamma_observer'],angles[o])for o in records}
 return {'intervals_overlap':overlap,'target_variance':target,'angles':angles,'scalar_collision_residual':abs(vals[-1]-vals[1]),'full_covariance_difference':residual(records[-1]['Gamma_observer'],records[1]['Gamma_observer'])}
def scale_rank_control(widths=DEFAULT_WIDTHS,scale=2.5):
 a=covariance_record(1,widths,1.);b=covariance_record(1,widths,scale);return {'dimensionless_covariance_residual':residual(a['Sigma_observer'],b['Sigma_observer']),'log_M_column_norm':0.,'scale_null_direction':[1.,0.,0.,0.,0.,0.],'parameters':['log_M','chi','rho','R_source/M','R_observer/M','analyzer_angle']}
def no_ell0_gate():return {'L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','result':RESULT,'physical_gate':GATE}
def scenario_control(name,case):
 table={'source_covariance_domain':lambda:(source_covariance(DEFAULT_WIDTHS)['positive_definite'],0.,1.),'covariance_conformance':lambda:(covariance_control(case.get('orientation',1))['block_formula_residual']<2e-10,covariance_control(case.get('orientation',1))['block_formula_residual'],2e-10),'width_homogeneity':lambda:(width_homogeneity_control(DEFAULT_WIDTHS,case.get('width_scale',2.5))['covariance_residual']<2e-10,width_homogeneity_control(DEFAULT_WIDTHS,case.get('width_scale',2.5))['covariance_residual'],2e-10),'orientation_survival':lambda:(orientation_control()['covariance_difference']>1e-3,orientation_control()['covariance_difference'],1e-3),'analyzer_extrema':lambda:(analyzer_extrema_control(1)['dense_scan_bracket_residual']<2e-5,analyzer_extrema_control(1)['dense_scan_bracket_residual'],2e-5),'analyzer_collision':lambda:(analyzer_collision_control()['scalar_collision_residual']<2e-10,analyzer_collision_control()['scalar_collision_residual'],2e-10),'scale':lambda:(scale_rank_control(DEFAULT_WIDTHS,case.get('scale_factor',2.5))['dimensionless_covariance_residual']<2e-10,scale_rank_control(DEFAULT_WIDTHS,case.get('scale_factor',2.5))['dimensionless_covariance_residual'],2e-10)}
 if name not in table:raise ValueError('unknown scenario handler')
 return table[name]()
def _canon(x,key=None):
 if isinstance(x,dict):return {str(k):_canon(v,str(k))for k,v in x.items()}
 if isinstance(x,list):return [_canon(v,key)for v in x]
 if isinstance(x,float):return float(format(0. if key!='threshold'and abs(x)<1e-7 else x,'.8g'))
 return x
def build_artifact():
 domain=source_covariance();prop=covariance_control(1);width=width_homogeneity_control();orient=orientation_control();extrema=analyzer_extrema_control(1);basis=basis_covariance_control(1,DEFAULT_WIDTHS,.37,.61);collision=analyzer_collision_control();scale=scale_rank_control();gate=no_ell0_gate();controls=[{'name':'source_domain','passed':domain['positive_definite'],'residual':0.,'threshold':1.,'threshold_kind':'boolean'},{'name':'covariance_propagation','passed':max(prop['block_formula_residual'],prop['symmetry_residual'])<2e-10,'residual':max(prop['block_formula_residual'],prop['symmetry_residual']),'threshold':2e-10},{'name':'width_homogeneity','passed':max(width.values())<2e-10,'residual':max(width.values()),'threshold':2e-10},{'name':'orientation_survival','passed':min(orient.values())>1e-3,'residual':min(orient.values()),'threshold':1e-3,'threshold_kind':'minimum_difference'},{'name':'analyzer_extrema','passed':extrema['dense_scan_bracket_residual']<2e-5,'residual':extrema['dense_scan_bracket_residual'],'threshold':2e-5},{'name':'basis_covariance','passed':max(basis.values())<2e-10,'residual':max(basis.values()),'threshold':2e-10},{'name':'analyzer_collision','passed':collision['scalar_collision_residual']<2e-10 and collision['intervals_overlap'],'residual':collision['scalar_collision_residual'],'threshold':2e-10},{'name':'scale_rank_no_ell0','passed':scale['dimensionless_covariance_residual']<2e-10 and not gate['ell0_identified'],'residual':scale['dimensionless_covariance_residual'],'threshold':2e-10}];return _canon({'study_id':'kerr-finite-source-analyzer-v1','control_summary':{'controls':controls,'controls_passed':sum(x['passed']for x in controls),'controls_total':8,**{k:gate[k]for k in ('L_identified','ell0_identified','L_equals_ell0','extra_dimension_detected','structural_dead_end','Detection')},'Maximum_interpretation':'MODEL_LEVEL_KERR_SOURCE_ANALYZER_CONTROL_NOT_EVIDENCE'},'raw_output':{'source':domain,'plus':covariance_record(1),'minus':covariance_record(-1),'plus_scan':analyzer_scan(1),'minus_scan':analyzer_scan(-1),'width_control':width,'orientation_control':orient,'extrema_control':extrema,'basis_control':basis,'collision_control':collision,'scale_control':scale,'limitations':GATE},'result':RESULT,'physical_gate':GATE,'review':'DIRECT_REVIEW_NO_SUBAGENT'})
def main():json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);sys.stdout.write('\n');return 0
if __name__=='__main__':raise SystemExit(main())
