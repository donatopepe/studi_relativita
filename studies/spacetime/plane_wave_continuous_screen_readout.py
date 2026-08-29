#!/usr/bin/env python3
"""Continuous canonical screen histories under a local gauge quotient."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;OUTPUT=HERE/'plane-wave-continuous-screen-readout-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
path=load('continuous_path','plane_wave_connection_path_cross_channel.py');base,full,cov,can=path.base,path.full,path.cov,path.can
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def diff(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def inv(a):
 n=len(a);w=[a[i][:]+[1. if i==j else 0. for j in range(n)] for i in range(n)]
 for c in range(n):
  p=max(range(c,n),key=lambda r:abs(w[r][c]));w[c],w[p]=w[p],w[c];v=w[c][c];w[c]=[x/v for x in w[c]]
  for r in range(n):
   if r!=c:
    f=w[r][c];w[r]=[w[r][j]-f*w[c][j] for j in range(2*n)]
 return [r[n:] for r in w]
def assemble(a,b,c,d):return [a[0]+b[0],a[1]+b[1],c[0]+d[0],c[1]+d[1]]
def lift(q):return assemble(q,base.zero(),base.zero(),q)
def h(a):return [[1.,0.,0.,0.],[0.,1.,0.,0.],[a[0][0],a[0][1],1.,0.],[a[1][0],a[1][1],0.,1.]]
def rk4(u,p,step,g):
 def add(a,b,f=1.):return [[a[i][j]+f*b[i][j] for j in range(4)] for i in range(4)]
 k1=mm(g(u),p);k2=mm(g(u+step/2),add(p,k1,step/2));k3=mm(g(u+step/2),add(p,k2,step/2));k4=mm(g(u+step),add(p,k3,step));return [[p[i][j]+step*(k1[i][j]+2*k2[i][j]+2*k3[i][j]+k4[i][j])/6 for j in range(4)] for i in range(4)]
def partial_inertial_history(kfun=base.base_k,length=.94,n=4000,samples=13):
 indices=[round(i*n/(samples-1)) for i in range(samples)];wanted=set(indices);out=[];p=[[1. if i==j else 0. for j in range(4)] for i in range(4)];u=-length/2;step=length/n
 if 0 in wanted:out.append((u,p))
 gen=lambda x:assemble(base.zero(),base.eye(),base.scale(kfun(x),-1),base.zero())
 for i in range(1,n+1):
  p=rk4(u,p,step,gen);u+=step
  if i in wanted:out.append((u,p))
 return out
def histories(length=.94,n=4000,samples=13,kfun=base.base_k,q1=None,q2=None,a1=None,a2=None):
 q1=q1 or path.qfun(1,length);q2=q2 or path.qfun(2,length);a1=a1 or path.afun(1,length);a2=a2 or path.afun(2,length);us=-length/2;cs1,cs2=lift(q1(us)),lift(q2(us));hs1,hs2=h(a1(us)),h(a2(us));rows=[]
 for u,pi in partial_inertial_history(kfun,length,n,samples):
  c1,c2=lift(q1(u)),lift(q2(u));pc1=mm(mm(inv(c1),pi),cs1);pc2=mm(mm(inv(c2),pi),cs2)
  pv1=mm(mm(inv(h(a1(u))),pc1),hs1);pv2=mm(mm(inv(h(a2(u))),pc2),hs2)
  g21=mm(inv(c2),c1);gsource=mm(inv(cs2),cs1);pred=mm(mm(g21,pc1),inv(gsource))
  rec1=mm(mm(c1,pc1),inv(cs1));rec2=mm(mm(c2,pc2),inv(cs2))
  rows.append({'u_over_L':u/length,'P_inertial':pi,'P_canonical_1':pc1,'P_canonical_2':pc2,'P_velocity_1':pv1,'P_velocity_2':pv2,'G_21':g21,'canonical_difference':diff(pc1,pc2),'velocity_difference':diff(pv1,pv2),'local_gauge_residual':diff(pc2,pred),'inertial_reconstruction_difference':diff(rec1,rec2)})
 return rows
def history_control(length=.94,n=4000,samples=13,**kwargs):
 rows=histories(length,n,samples,**kwargs);middle=rows[1:-1]
 return {'samples':rows,'maximum_intermediate_canonical_difference':max(r['canonical_difference'] for r in middle),'maximum_intermediate_velocity_difference':max(r['velocity_difference'] for r in middle),'endpoint_canonical_difference':rows[-1]['canonical_difference'],'endpoint_velocity_difference':rows[-1]['velocity_difference'],'maximum_local_gauge_residual':max(r['local_gauge_residual'] for r in rows),'maximum_inertial_reconstruction_difference':max(r['inertial_reconstruction_difference'] for r in rows)}
def zero_path_control(length=.94,n=4000,samples=13):
 q=path.qfun(1,length);a=path.afun(1,length);r=history_control(length,n,samples,q1=q,q2=q,a1=a,a2=a)
 return {'maximum_raw_history_difference':max(max(x['canonical_difference'],x['velocity_difference']) for x in r['samples'])}
def transformed_functions(r,length=.94,reflection=False):
 rt=path.tr(r);k=lambda u:mm(mm(rt,base.base_k(u)),r);qs=[];ass=[]
 for i in (1,2):
  q=path.qfun(i,length);a=path.afun(i,length);qs.append(lambda u,q=q:mm(mm(rt,q(u)),r));ass.append(lambda u,a=a:mm(mm(rt,a(u)),r))
 return k,qs,ass
def orientation_control(length=.94,n=4000,samples=13):
 raw=history_control(length,n,samples);r=path.rotation(.31);k,qs,ass=transformed_functions(r,length);moved=history_control(length,n,samples,kfun=k,q1=qs[0],q2=qs[1],a1=ass[0],a2=ass[1]);lr=lift(r)
 residual=max(diff(b['P_canonical_1'],mm(mm(inv(lr),a['P_canonical_1']),lr)) for a,b in zip(raw['samples'],moved['samples']))
 ref=[[1.,0.],[0.,-1.]];k,qs,ass=transformed_functions(ref,length);mir=history_control(length,n,samples,kfun=k,q1=qs[0],q2=qs[1],a1=ass[0],a2=ass[1]);a=raw['samples'][samples//2]['P_canonical_1'][0][1];b=mir['samples'][samples//2]['P_canonical_1'][0][1]
 return {'so2_history_covariance_residual':residual,'reflection_signed_component_residual':abs(a+b)}
def affine_control(length=.94,n=4000,samples=13,factor=1.47):
 raw=history_control(length,n,samples);kf=lambda u:base.scale(base.base_k(u/factor),1/factor**2);scaled=history_control(length*factor,n,samples,kfun=kf)
 d=[[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1/factor,0.],[0.,0.,0.,1/factor]];di=inv(d);vals=[]
 for a,b in zip(raw['samples'],scaled['samples']):
  normalized=lambda key:mm(mm(di,b[key]),d)
  vals.extend([diff(a['P_inertial'],normalized('P_inertial')),diff(a['P_canonical_1'],normalized('P_canonical_1')),diff(a['P_canonical_2'],normalized('P_canonical_2')),diff(a['P_velocity_1'],normalized('P_velocity_1')),diff(a['P_velocity_2'],normalized('P_velocity_2')),diff(a['G_21'],b['G_21'])])
 return {'factor':factor,'phase_unit_similarity':'D=diag(I,I/s), normalized scaled map D^-1 P_s D','maximum_dimensionless_residual':max(vals)}
def build(n=4000,samples=13):
 return {'classification':'EXACT_SPACETIME_CONTINUOUS_SCREEN_READOUT_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_PLANE_WAVE_CONTINUOUS_CANONICAL_SCREEN_HISTORY_LOCAL_GAUGE_EQUIVALENT_RAW_VELOCITY_HISTORY_CALIBRATION_DEPENDENT_NOT_ELL0','open_gate':'PHYSICAL_CONTINUOUS_TETRAD_READOUT_LOCAL_SCREEN_GAUGE_CAUSAL_SAMPLING_AND_ELL0_LAW_NOT_DERIVED','raw_objects':['K','omega_i','Q_i','A_i','P_inertial(u)','P_canonical_i(u)','P_velocity_i(u)','G_21(u)','L'],'history':history_control(n=n,samples=samples),'zero_path':zero_path_control(n=n,samples=samples),'orientation':orientation_control(n=n,samples=samples),'affine':affine_control(n=n,samples=samples),'caustic_scope':'SACHS_GRAPHS_ONLY_FULL_PHASE_MAP_RETAINED','ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','source_scope':'Coley-McNutt-Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; not continuous detector readout, local screen-gauge quotient, ell0, UMCH, or detection.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=text:print('Artifact differs.',file=sys.stderr);return 1
  print('Plane-wave continuous screen-readout artifact is current.');return 0
 if a.write:OUTPUT.write_text(text);print(OUTPUT);return 0
 print(text,end='');return 0
if __name__=='__main__':raise SystemExit(main())
