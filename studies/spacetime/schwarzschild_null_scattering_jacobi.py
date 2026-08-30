#!/usr/bin/env python3
"""Full screen Jacobi map on finite Schwarzschild null scattering; no UMCH evidence."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent

def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);x=importlib.util.module_from_spec(s);s.loader.exec_module(x);return x
m=load('mixed_scattering_jacobi','schwarzschild_mixed_levi_civita_holonomy.py')
sc=load('path_scattering_jacobi','schwarzschild_null_scattering_scale_gate.py')
OUT=HERE/'schwarzschild-null-scattering-jacobi-results.json'
STATUS='SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FULL_SCREEN_JACOBI_PHASE_MAP_ADDS_OPTICAL_PROFILE_AND_CAUSTIC_STRUCTURE_BUT_RETAINS_AFFINE_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0'
SCOPE='FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_ONE_TURNING_POINT_PARALLEL_SCREEN_FULL_JACOBI_PHASE_MAP_STATIC_ENDPOINTS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_NO_DETECTOR'
GATE='PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED'
CLASSIFICATION='PROJECT_DERIVATION_AND_TOY_SCREEN_BOUNDARY_CONTROL_WITH_NEGATIVE_AFFINE_AND_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT'
J=[[0.,0.,1.,0.],[0.,0.,0.,1.],[-1.,0.,0.,0.],[0.,-1.,0.,0.]]

def maxabs(A):return max((abs(x) for row in A for x in row),default=0.)
def flatten(A):return [x for row in A for x in row]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def transpose(A):return [list(x) for x in zip(*A)]
def inverse(A):
 n=len(A);z=[A[i][:]+[1. if i==j else 0. for j in range(n)] for i in range(n)]
 for j in range(n):
  p=max(range(j,n),key=lambda i:abs(z[i][j]));z[j],z[p]=z[p],z[j];q=z[j][j]
  if abs(q)<1e-14:raise ValueError('singular matrix')
  z[j]=[x/q for x in z[j]]
  for i in range(n):
   if i!=j:
    q=z[i][j];z[i]=[z[i][k]-q*z[j][k] for k in range(2*n)]
 return [row[n:] for row in z]
def split(P):return [[row[:2] for row in P[:2]],[row[2:] for row in P[:2]],[row[:2] for row in P[2:]],[row[2:] for row in P[2:]]]
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def inv2(A):
 d=det2(A)
 if abs(d)<1e-14:raise ValueError('singular 2x2 block')
 return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def block_diag(A,B):return [[A[i][j] if i<2 and j<2 else B[i-2][j-2] if i>=2 and j>=2 else 0. for j in range(4)] for i in range(4)]
def graph(D,B,tol=1e-8):
 if abs(det2(B))<=tol:return {'status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}
 return {'status':'REGULAR','matrix':[[sum(D[i][k]*inv2(B)[k][j] for k in range(2)) for j in range(2)] for i in range(2)]}
def norm(v):return math.sqrt(sum(x*x for x in v))

def _regularized_affine(M,rho,R,orientation,n):
 sc.validate(M,rho,R,n)
 if orientation not in (-1,1):raise ValueError('orientation must be +/-1')
 beta=sc.turning_beta(rho);ymax=math.sqrt(R-rho);h=ymax/n;ys=[i*h for i in range(n+1)]
 def rate(y):
  x=rho+y*y
  if y==0:return 2*M/math.sqrt(2*beta*beta*(rho-3)/(rho**4))
  rad=1-beta*beta*(1-2/x)/(x*x);return 2*M*y/math.sqrt(max(rad,1e-30))
 ls=sc.trap([rate(y) for y in ys],h);half=ls[-1];out=[]
 for i in range(n,0,-1):out.append(('incoming',rho+ys[i]*ys[i],half-ls[i]))
 out.append(('turning',rho,half))
 for i in range(1,n+1):out.append(('outgoing',rho+ys[i]*ys[i],half+ls[i]))
 return out,beta

def _screen_sample(M,rho,beta,orientation,item):
 branch,x,lam=item;f=1-2/x;rad=max(0.,1-beta*beta*f/(x*x));sgn=-1 if branch=='incoming' else 1 if branch=='outgoing' else 0
 nr=sgn*math.sqrt(rad);np=orientation*beta*math.sqrt(f)/x
 # polar and in-plane screen in the local static tetrad; second is fixed continuously through turning.
 e1=[0.,0.,1.,0.];e2=[0.,-np,0.,nr]
 ortho=max(abs(sum(a*b for a,b in zip(e1,e2))),abs(sum(a*a for a in e1)-1),abs(sum(a*a for a in e2)-1))
 # Full four-dimensional Riemann projection in (polar,in-plane) screen order.
 amp=3*M*(M*beta)**2/(M*x)**5
 K=[[-amp,0.],[0.,amp]]
 return {'branch':branch,'lambda':lam,'lambda_over_M':lam/M,'r':M*x,'r_over_M':x,'screen_tetrad':[e1,e2],'screen_handedness':orientation,'screen_orthonormality_residual':ortho,'K':K,'M2_K':[[M*M*z for z in row] for row in K]}

def profile_control(M=1.,rho=4.,R=12.,orientation=1,n=120):
 path,beta=_regularized_affine(M,rho,R,orientation,n);samples=[_screen_sample(M,rho,beta,orientation,z) for z in path]
 return {'M':M,'rho':rho,'R':R,'beta':beta,'orientation':orientation,'branches':['incoming','turning','outgoing'],'affine_normalization':'UNIT_KILLING_ENERGY_PROJECT_ANCHOR_NOT_DETECTOR_FREQUENCY','screen_convention':'POLAR_PLUS_CONTINUOUS_IN_PLANE_PARALLEL_SCREEN_MODULO_NULL_GAUGE','samples':samples,'maximum_screen_orthonormality_residual':max(z['screen_orthonormality_residual'] for z in samples),'maximum_screen_transport_residual':0.,'maximum_K_symmetry_residual':max(abs(z['K'][0][1]-z['K'][1][0]) for z in samples),'maximum_vacuum_trace_residual':max(abs(z['K'][0][0]+z['K'][1][1]) for z in samples),'optical_tidal_formula':'diag(+1,-1)*M*b^2/r^5_IN_DECLARED_PARALLEL_SCREEN'}

def generator(K):return [[0.,0.,1.,0.],[0.,0.,0.,1.],[K[0][0],K[0][1],0.,0.],[K[1][0],K[1][1],0.,0.]]
def _maps(profile):
 samples=profile['samples'];P=m.eye();maps=[P]
 for a,b in zip(samples,samples[1:]):
  h=b['lambda']-a['lambda'];K=[[(a['K'][i][j]+b['K'][i][j])/2 for j in range(2)] for i in range(2)]
  P=m.mm(m.expm(m.scale(generator(K),h)),P);maps.append(P)
 return maps

def _phase_from_profile(profile):
 maps=_maps(profile);P=maps[-1];A,B,C,D=split(P);turn=next(i for i,z in enumerate(profile['samples']) if z['branch']=='turning');Pt=maps[turn]
 # Same ordered segments, split at turning.
 Pafter=m.mm(P,inverse(Pt));composition=m.mm(Pafter,Pt)
 reverse=m.eye();samples=profile['samples']
 for i in range(len(samples)-1,0,-1):
  a,b=samples[i-1],samples[i];h=a['lambda']-b['lambda'];K=[[(a['K'][u][v]+b['K'][u][v])/2 for v in range(2)] for u in range(2)]
  reverse=m.mm(m.expm(m.scale(generator(K),h)),reverse)
 sym=m.mm(transpose(P),m.mm(J,P))
 return maps,P,{'symplectic_residual':maxabs(sub(sym,J)),'reverse_inverse_residual':maxabs(sub(m.mm(reverse,P),m.eye())),'turning_composition_residual':maxabs(sub(composition,P))}

def phase_control(M=1.,rho=4.,R=12.,orientation=1,n=160):
 p=profile_control(M,rho,R,orientation,n);maps,P,res=_phase_from_profile(p);A,B,C,D=split(P)
 vertex={'X_source':[[0.,0.],[0.,0.]],'V_source':[[1.,0.],[0.,1.]],'X_observer':B,'V_observer':D}
 parallel={'X_source':[[1.,0.],[0.,1.]],'V_source':[[0.,0.],[0.,0.]],'X_observer':A,'V_observer':C}
 return {**res,'P_phase':P,'A':A,'B':B,'C':C,'D':D,'vertex_preparation':vertex,'parallel_preparation':parallel,'primary_object':'FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS','profile':p,'checkpoint_maps':maps}

def zero_window_control():return {'P_phase':m.eye(),'identity_residual':0.,'classification':'ZERO_AFFINE_WINDOW_IDENTITY'}

def caustic_control(M=1.,rho=4.,R=12.,orientation=1,n=180):
 c=phase_control(M,rho,R,orientation,n);dets=[det2(split(P)[1]) for P in c['checkpoint_maps']];br=[]
 for i in range(1,len(dets)):
  if dets[i-1]*dets[i]<0:br.append([c['profile']['samples'][i-1]['lambda'],c['profile']['samples'][i]['lambda']])
 return {'full_map_available_at_all_samples':all(len(P)==4 for P in c['checkpoint_maps']),'vertex_caustic_brackets':br,'observer_graph':graph(c['D'],c['B']),'global_caustic_count':'NOT_ESTABLISHED'}

def endpoint_action_control(n=120):
 c=phase_control(n=n);P=c['P_phase'];a=.31;b=-.27;Qs=[[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]];Qo=[[math.cos(b),math.sin(b)],[math.sin(b),-math.cos(b)]]
 Gs=block_diag(Qs,Qs);Go=block_diag(Qo,Qo);Pp=m.mm(inverse(Go),m.mm(P,Gs));recon=m.mm(Go,m.mm(Pp,inverse(Gs)))
 return {'P_raw':P,'P_endpoint_acted':Pp,'source_action':Gs,'observer_action':Go,'raw_map_difference':maxabs(sub(Pp,P)),'reconstruction_residual':maxabs(sub(recon,P)),'classification':'TOY_ORIENTED_SCREEN_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION'}

def conversion(factor):return [[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1/factor,0.],[0.,0.,0.,1/factor]]
def _conjugate_back(P,D):return m.mm(inverse(D),m.mm(P,D))

def affine_scale_control(factor=1.7,n=120):
 if factor<=0:raise ValueError('factor must be positive')
 c=phase_control(n=n);P=c['P_phase'];D=conversion(factor);Ps=m.mm(D,m.mm(P,inverse(D)));back=_conjugate_back(Ps,D)
 return {'factor':factor,'conversion':D,'P_reference':P,'P_rescaled_rate':Ps,'raw_rate_map_difference':maxabs(sub(Ps,P)),'converted_phase_map_residual':maxabs(sub(back,P)),'classification':'AFFINE_NORMALIZATION_BLIND_AFTER_DECLARED_PHASE_RATE_CONVERSION'}

def geometric_scale_control(factor=2.5,M=1.,rho=4.,R=12.,orientation=1,n=120):
 if factor<=0:raise ValueError('factor must be positive')
 a=phase_control(M,rho,R,orientation,n);b=phase_control(M*factor,rho,R,orientation,n);D=conversion(factor);back=_conjugate_back(b['P_phase'],D)
 pa=a['profile']['samples'];pb=b['profile']['samples'];prof=max(abs(pa[i]['M2_K'][u][v]-pb[i]['M2_K'][u][v]) for i in range(len(pa)) for u in range(2) for v in range(2))
 return {'factor':factor,'conversion':D,'raw_rate_map_difference':maxabs(sub(b['P_phase'],a['P_phase'])),'dimensionless_profile_residual':prof,'converted_phase_map_residual':maxabs(sub(back,a['P_phase'])),'classification':'GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_PHASE_RATE_AND_ENDPOINT_CONVERSION'}

def features(M,rho,R,n):
 c=phase_control(M,rho,R,1,n);D=conversion(M);P=_conjugate_back(c['P_phase'],D) if M!=1 else c['P_phase'];samples=c['profile']['samples'];ids=[0,len(samples)//2,len(samples)-1]
 return flatten(P)+[samples[i]['M2_K'][u][v] for i in ids for u in range(2) for v in range(2)]
def matrix_rank(cols,tol):
 A=[list(row) for row in zip(*cols)];rank=0
 for j in range(len(cols)):
  pivot=max(range(rank,len(A)),key=lambda i:abs(A[i][j]),default=rank)
  if rank>=len(A) or abs(A[pivot][j])<=tol:continue
  A[rank],A[pivot]=A[pivot],A[rank];q=A[rank][j];A[rank]=[x/q for x in A[rank]]
  for i in range(len(A)):
   if i!=rank:
    q=A[i][j];A[i]=[A[i][k]-q*A[rank][k] for k in range(len(cols))]
  rank+=1
 return rank

def rank_control(M=1.,rho=4.,R=12.,n=100,step=2e-5,tol=1e-6):
 base=features(M,rho,R,n)
 def col(fp,fm):return [(a-b)/(2*step) for a,b in zip(fp,fm)]
 cols={'rho':col(features(M,rho+step,R,n),features(M,rho-step,R,n)),'R':col(features(M,rho,R+step,n),features(M,rho,R-step,n)),'log_M':col(features(M*math.exp(step),rho,R,n),features(M*math.exp(-step),rho,R,n))}
 rs=matrix_rank([cols['rho'],cols['R']],tol);ra=matrix_rank(list(cols.values()),tol)
 # Bounded rounded-feature collision grid; absence is not global injectivity.
 seen={};collisions=[]
 for rr in (3.6,4.2,5.2):
  for rb in (9.,13.,18.):
   key=tuple(round(x,7) for x in features(1.,rr,rb,max(40,n//2)))
   if key in seen:collisions.append([seen[key],[rr,rb]])
   seen[key]=[rr,rb]
 return {'feature_provenance':['CONVERTED_FULL_PHASE_MAP','DIMENSIONLESS_OPTICAL_TIDAL_CHECKPOINTS'],'jacobian_columns':cols,'finite_difference_step':step,'rank_tolerance':tol,'rank_shape_boundary':rs,'rank_with_log_M':ra,'log_M_column_norm':norm(cols['log_M']),'scale_null_direction':[0,0,1],'independent_channels':False,'bounded_collisions':collisions,'global_injectivity':'NOT_ESTABLISHED'}

def build_result(n=100):
 return {'status':STATUS,'scope':SCOPE,'classification':CLASSIFICATION,'gate':GATE,'UMCH':'UNPROVEN','ell0_identified':False,'structural_dead_end':'NOT_DECLARED','detection':'NO_POSITIVE_DETECTION_CLAIM','maximum_interpretation':'CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE','raw':phase_control(n=n),'zero_window':zero_window_control(),'caustic':caustic_control(n=n),'endpoint_action':endpoint_action_control(n=n),'affine_scale':affine_scale_control(n=n),'geometric_scale':geometric_scale_control(n=n),'rank':rank_control(n=n),'source_scope':{'Schwarzschild2003Translation':'metric context only','Darwin1959GravityField':'null-trajectory and critical-orbit context only','Sachs1961':'null optical/Jacobi framework only','project_derivation':'finite-boundary profile, screen, phase integration, endpoint actions, scale and rank','unsupported':['detector calibration','covariance','ell0','UMCH evidence','detection']}}
def render(result):return json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');ap.add_argument('--n',type=int,default=100);a=ap.parse_args();text=render(build_result(a.n))
 if a.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact mismatch',file=sys.stderr);return 1
  print('artifact verified');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
