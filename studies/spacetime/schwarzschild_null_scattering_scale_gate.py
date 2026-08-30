#!/usr/bin/env python3
"""Finite-boundary Schwarzschild null scattering/open transport; no UMCH evidence."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
S=importlib.util.spec_from_file_location('mixed_scattering',HERE/'schwarzschild_mixed_levi_civita_holonomy.py');m=importlib.util.module_from_spec(S);S.loader.exec_module(m)
OUT=HERE/'schwarzschild-null-scattering-scale-gate-results.json'
STATUS='SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FINITE_WINDOW_OPEN_TRANSPORT_HAS_TURNING_AND_BOUNDARY_SHAPE_DIRECTIONS_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0'
SCOPE='FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_SCATTERING_WITH_ONE_TURNING_POINT_STATIC_ENDPOINT_TETRADS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_AND_NO_DETECTOR_READOUT'
GATE='PHYSICAL_SCATTERING_WINDOW_EMITTER_ABSORBER_TETRADS_AFFINE_FREQUENCY_STANDARD_SCREEN_JACOBI_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED'
CLASSIFICATION='PROJECT_DERIVATION_AND_TOY_FINITE_BOUNDARY_CONTROL_WITH_NEGATIVE_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT'

def turning_beta(rho):
 if rho<=3:raise ValueError('rho must exceed 3 on scattering branch')
 return rho/math.sqrt(1-2/rho)
def maxabs(A):return max(abs(x) for row in A for x in row)
def flatten(A):return [x for row in A for x in row]
def validate(M,rho,R,n):
 if M<=0 or rho<=3 or R<=rho or n<20:raise ValueError('require M>0, R>rho>3 and n>=20')
def trap(values,h):return [0.]+[sum((values[k]+values[k+1])*h/2 for k in range(i)) for i in range(1,len(values))]
def _regularized_half(M,rho,R,orientation,n):
 validate(M,rho,R,n);beta=turning_beta(rho);ymax=math.sqrt(R-rho);h=ymax/n
 ys=[i*h for i in range(n+1)]
 def rates(y):
  x=rho+y*y;f=1-2/x
  if y==0:mfac=2/math.sqrt(2*beta*beta*(rho-3)/(rho**4))
  else:
   rad=1-beta*beta*f/(x*x)
   mfac=2*y/math.sqrt(max(rad,1e-30))
  return M*mfac/f,orientation*beta*mfac/(x*x)
 vals=[rates(y) for y in ys]
 ts=trap([v[0] for v in vals],h);ps=trap([v[1] for v in vals],h)
 return ys,ts,ps,beta

def path_samples(M=1.,rho=4.,R=12.,orientation=1,n=600):
 if orientation not in (-1,1):raise ValueError('orientation must be +/-1')
 ys,ts,ps,beta=_regularized_half(M,rho,R,orientation,n);ht,hp=ts[-1],ps[-1]
 out=[]
 for i in range(n,0,-1):
  x=rho+ys[i]*ys[i];out.append({'branch':'incoming','t':ht-ts[i],'r':M*x,'theta':math.pi/2,'phi':hp-ps[i]})
 out.append({'branch':'turning','t':ht,'r':M*rho,'theta':math.pi/2,'phi':hp})
 for i in range(1,n+1):
  x=rho+ys[i]*ys[i];out.append({'branch':'outgoing','t':ht+ts[i],'r':M*x,'theta':math.pi/2,'phi':hp+ps[i]})
 return out

def _transport(M,points):
 T=m.eye()
 for a,b in zip(points,points[1:]):
  aa=[a['t'],a['r'],a['theta'],a['phi']];bb=[b['t'],b['r'],b['theta'],b['phi']]
  T=m.mm(m.segment_transport(M,aa,bb,1),T)
 return T

def _raw_matrices(M,rho,R,orientation,n):
 p=path_samples(M,rho,R,orientation,n);Tc=_transport(M,p);E=m.tetrad(M,M*R);Et=m.inverse_diag(E);Tt=m.mm(Et,m.mm(Tc,E))
 rev=_transport(M,list(reversed(p)))
 return p,Tc,Tt,rev

def raw_control(M=1.,rho=4.,R=12.,orientation=1,n=600):
 p,Tc,Tt,rev=_raw_matrices(M,rho,R,orientation,n);beta=turning_beta(rho);b=M*beta
 nr=[];er=[];lr=[]
 for z in p:
  x=z['r']/M;f=1-2/x;rad=max(0.,1-beta*beta*f/(x*x));sgn=-1 if z['branch']=='incoming' else 1 if z['branch']=='outgoing' else 0
  k=[1/f,sgn*math.sqrt(rad),0.,orientation*b/(z['r']*z['r'])]
  g=m.metric(M,z['r']);nr.append(abs(sum(g[i][j]*k[i]*k[j] for i in range(4) for j in range(4))))
  er.append(abs(f*k[0]-1));lr.append(abs(z['r']*z['r']*k[3]-orientation*b))
 eta=m.diag([-1,1,1,1]);metricres=m.norm(m.sub(m.mm(m.transpose(Tt),m.mm(eta,Tt)),eta))
 return {'M':M,'rho':rho,'R':R,'beta':beta,'orientation':orientation,'branches':['incoming','turning','outgoing'],'sample_count':len(p),'path_samples':p,'T_coordinate':Tc,'T_tetrad':Tt,'delta_t':p[-1]['t'],'delta_t_over_M':p[-1]['t']/M,'delta_phi':p[-1]['phi'],'turning_residual':abs(1-beta*beta*(1-2/rho)/(rho*rho)),'turning_match_residual':0.,'maximum_null_residual':max(nr),'maximum_energy_residual':max(er),'maximum_angular_momentum_residual':max(lr),'endpoint_metric_residual':metricres,'reverse_inverse_residual':m.norm(m.sub(m.mm(rev,Tc),m.eye())),'map_classification':'OPEN_PATH_ENDPOINT_TRANSPORT_NOT_HOLONOMY'}

def boundary_control():
 a=raw_control(R=8,n=400);b=raw_control(R=16,n=500)
 return {'R_values':[8,16],'delta_t_over_M_difference':abs(a['delta_t_over_M']-b['delta_t_over_M']),'transport_difference':m.norm(m.sub(a['T_tetrad'],b['T_tetrad'])),'classification':'FINITE_BOUNDARY_PROTOCOL_DIRECTION'}
def orientation_control():
 a=raw_control(orientation=1,n=500);b=raw_control(orientation=-1,n=500)
 return {'time_even_residual':abs(a['delta_t']-b['delta_t']),'phi_odd_residual':abs(a['delta_phi']+b['delta_phi']),'raw_transport_difference':m.norm(m.sub(a['T_tetrad'],b['T_tetrad'])),'norm_alias_residual':abs(m.norm(a['T_tetrad'])-m.norm(b['T_tetrad'])),'norm_alias_classification':'PROJECTED_NORM_ALIAS_NOT_RAW_MAP_EQUALITY'}
def rotation(angle):
 c=math.cos(angle);s=math.sin(angle);return [[1.,0.,0.,0.],[0.,c,-s,0.],[0.,s,c,0.],[0.,0.,0.,1.]]
def endpoint_control():
 T=raw_control(n=500)['T_tetrad'];Qs=rotation(.23);Qo=rotation(-.31);acted=m.mm(m.transpose(Qo),m.mm(T,Qs));recon=m.mm(Qo,m.mm(acted,m.transpose(Qs)))
 return {'acted_map_difference':m.norm(m.sub(acted,T)),'reconstruction_residual':m.norm(m.sub(recon,T)),'classification':'TOY_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION'}
def scale_control(scale=2.5):
 a=raw_control(M=1.,n=500);b=raw_control(M=scale,n=500);pa=a['path_samples'];pb=b['path_samples']
 pr=max(max(abs(pa[i][k]/(1 if k in ('theta','phi') else 1.)-pb[i][k]/(scale if k in ('t','r') else 1.)) for k in ('t','r','theta','phi')) for i in range(len(pa)))
 return {'scale':scale,'dimensionless_path_residual':pr,'delta_t_over_M_residual':abs(a['delta_t_over_M']-b['delta_t_over_M']),'delta_t_scaling_residual':abs(b['delta_t']-scale*a['delta_t']),'tetrad_transport_residual':m.norm(m.sub(a['T_tetrad'],b['T_tetrad'])),'coordinate_transport_difference':m.norm(m.sub(a['T_coordinate'],b['T_coordinate'])),'classification':'GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_ENDPOINT_CONVERSION'}
def _features(M,rho,R,n=360):
 z=raw_control(M,rho,R,n=n);return flatten(z['T_tetrad'])+[z['delta_t_over_M'],z['delta_phi']]
def _column(M,rho,R,key,h=2e-5):
 if key=='rho':a,b=_features(M,rho-h,R),_features(M,rho+h,R)
 elif key=='R':a,b=_features(M,rho,R-h),_features(M,rho,R+h)
 else:a,b=_features(M*math.exp(-h),rho,R),_features(M*math.exp(h),rho,R)
 return [(y-x)/(2*h) for x,y in zip(a,b)]
def _rank(cols,tol=1e-6):
 basis=[]
 for c in cols:
  v=c[:]
  for q in basis:
   dot=sum(x*y for x,y in zip(v,q));v=[x-dot*y for x,y in zip(v,q)]
  n=math.sqrt(sum(x*x for x in v))
  if n>tol:basis.append([x/n for x in v])
 return len(basis)
def rank_control():
 cols=[_column(1,4,12,k) for k in ('rho','R','log_M')];norms=[math.sqrt(sum(x*x for x in c)) for c in cols]
 return {'parameters':['rho','R','log_M'],'column_norms':norms,'log_M_column_norm':norms[2],'rank_shape_boundary':_rank(cols[:2]),'rank_with_log_M':_rank(cols),'scale_null_direction':[0,0,1],'independent_channels':False,'classification':'LOCAL_RANK_NOT_PHYSICAL_CHANNEL_INDEPENDENCE_OR_GLOBAL_INJECTIVITY'}
def collision_control():
 pairs=[]
 vals=[]
 for rho in (3.2,4.,6.):
  for R in (8.,12.,20.):
   if R>rho:vals.append((rho,R,_features(1,rho,R,n=220)))
 for i,a in enumerate(vals):
  for b in vals[i+1:]:
   d=math.sqrt(sum((x-y)**2 for x,y in zip(a[2],b[2])))
   if d<1e-5:pairs.append([a[:2],b[:2],d])
 return {'grid_size':len(vals),'bounded_collisions':pairs,'global_injectivity':'NOT_ESTABLISHED','classification':'BOUNDED_SEARCH_CANNOT_PROMOTE_LOCAL_RANK_TO_GLOBAL_INJECTIVITY'}
def build_result():
 return {'schema_version':1,'status':STATUS,'scope':SCOPE,'gate':GATE,'classification':CLASSIFICATION,'umch':'UNPROVEN','detection':'NO_POSITIVE_DETECTION_CLAIM','ell0_identified':False,'structural_dead_end':'NOT_DECLARED','normalization':{'killing_energy':1,'type':'PROJECT_AFFINE_ANCHOR'},'domain':{'scattering':'R>rho>3','critical':'EXCLUDED_LIMIT','capture':'OUT_OF_SCOPE'},'raw_records':[raw_control(rho=r,R=R,n=500) for r,R in ((3.2,8),(4,12),(6,20))],'boundary_control':boundary_control(),'orientation_control':orientation_control(),'endpoint_control':endpoint_control(),'scale_control':scale_control(),'rank_control':rank_control(),'collision_control':collision_control(),'source_scope':{'Schwarzschild2003Translation':'SCHWARZSCHILD_EXTERIOR_METRIC_CONTEXT_ONLY','Darwin1959GravityField':'SCHWARZSCHILD_NULL_TRAJECTORY_AND_CRITICAL_ORBIT_CONTEXT_ONLY'},'nonclaims':['NO_DETECTOR_READOUT','NO_COVARIANCE','NO_PHYSICAL_ENDPOINT_CALIBRATION','NO_ELL0_LAW','NO_UMCH_EVIDENCE','NO_DETECTION']}
def render():return json.dumps(build_result(),indent=2,sort_keys=True,ensure_ascii=False)+'\n'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();text=render()
 if args.check:
  if not OUT.exists() or OUT.read_text()!=text:print('artifact mismatch',file=sys.stderr);return 1
  print('schwarzschild null-scattering scale-gate artifact: OK');return 0
 OUT.write_text(text);print(OUT);return 0
if __name__=='__main__':raise SystemExit(main())
