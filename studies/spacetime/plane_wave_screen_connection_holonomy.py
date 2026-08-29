#!/usr/bin/env python3
"""Prescribed SO(2) screen-connection holonomy in an exact plane-wave control."""
import argparse,importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;OUTPUT=HERE/'plane-wave-screen-connection-holonomy-results.json'
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
path=load('holonomy_path','plane_wave_connection_path_cross_channel.py');base=path.base
I=[[1.,0.],[0.,1.]];J=[[0.,-1.],[1.,0.]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(r) for r in zip(*a)]
def diff(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def rot(theta):return [[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]]
def inv2(a):return tr(a)
def phase(q):return [[q[0][0],q[0][1],0.,0.],[q[1][0],q[1][1],0.,0.],[0.,0.,q[0][0],q[0][1]],[0.,0.,q[1][0],q[1][1]]]
def inv4(a):
 n=4;w=[a[i][:]+[1. if i==j else 0. for j in range(n)] for i in range(n)]
 for c in range(n):
  p=max(range(c,n),key=lambda r:abs(w[r][c]));w[c],w[p]=w[p],w[c];v=w[c][c];w[c]=[x/v for x in w[c]]
  for r in range(n):
   if r!=c:
    f=w[r][c];w[r]=[w[r][j]-f*w[c][j] for j in range(2*n)]
 return [r[n:] for r in w]
def rk4_transport(u,q,h,afun):
 def add(a,b,f):return [[a[i][j]+f*b[i][j] for j in range(2)] for i in range(2)]
 f=lambda x,y:mm(afun(x),y);k1=f(u,q);k2=f(u+h/2,add(q,k1,h/2));k3=f(u+h/2,add(q,k2,h/2));k4=f(u+h,add(q,k3,h));return [[q[i][j]+h*(k1[i][j]+2*k2[i][j]+2*k3[i][j]+k4[i][j])/6 for j in range(2)] for i in range(2)]
def sampled_transport(afun,length=.94,n=6000,samples=15):
 wanted=set(round(i*n/(samples-1)) for i in range(samples));u=-length/2;h=length/n;q=[r[:] for r in I];theta=0.;out=[]
 if 0 in wanted:out.append({'u_over_L':-.5,'angle':0.,'ordered':q,'analytic':rot(0.),'ordered_analytic_residual':0.})
 for i in range(1,n+1):
  a0=afun(u)[1][0];a1=afun(u+h/2)[1][0];a2=afun(u+h)[1][0];q=rk4_transport(u,q,h,afun);theta+=h*(a0+4*a1+a2)/6;u+=h
  if i in wanted:out.append({'u_over_L':u/length,'angle':theta,'ordered':q,'analytic':rot(theta),'ordered_analytic_residual':diff(q,rot(theta))})
 return out
def endpoint_matched_control(length=.94,n=6000,samples=15):
 h1=sampled_transport(path.afun(1,length),length,n,samples);h2=sampled_transport(path.afun(2,length),length,n,samples);rows=[]
 for a,b in zip(h1,h2):rows.append({'u_over_L':a['u_over_L'],'angle_1':a['angle'],'angle_2':b['angle'],'U_1':a['ordered'],'U_2':b['ordered'],'holonomy_difference':diff(a['ordered'],b['ordered']),'trace_1':a['ordered'][0][0]+a['ordered'][1][1],'trace_2':b['ordered'][0][0]+b['ordered'][1][1],'ordered_analytic_residual_1':a['ordered_analytic_residual'],'ordered_analytic_residual_2':b['ordered_analytic_residual']})
 u1,u2=h1[-1]['ordered'],h2[-1]['ordered'];relative=mm(inv2(u2),u1);pc1=path.canonical_endpoint_map(path.qfun(1,length),length,n);pc2=path.canonical_endpoint_map(path.qfun(2,length),length,n);canonical_loop=mm(pc2,inv4(pc1))
 return {'samples':rows,'maximum_ordered_analytic_residual':max(max(x['ordered_analytic_residual_1'],x['ordered_analytic_residual_2']) for x in rows),'maximum_intermediate_holonomy_difference':max(x['holonomy_difference'] for x in rows[1:-1]),'endpoint_holonomy_difference':rows[-1]['holonomy_difference'],'relative_endpoint_holonomy':relative,'relative_endpoint_identity_residual':diff(relative,I),'canonical_endpoint_loop':canonical_loop,'canonical_endpoint_loop_identity_residual':diff(canonical_loop,[[1. if i==j else 0. for j in range(4)] for i in range(4)])}
def alias_control(theta=.73):
 plus,minus,winding=rot(theta),rot(-theta),rot(theta+2*math.pi)
 return {'theta':theta,'plus_matrix':plus,'minus_matrix':minus,'winding_matrix':winding,'plus_spectrum':[[math.cos(theta),math.sin(theta)],[math.cos(theta),-math.sin(theta)]],'raw_sign_matrix_difference':diff(plus,minus),'sign_trace_residual':abs((plus[0][0]+plus[1][1])-(minus[0][0]+minus[1][1])),'winding_matrix_residual':diff(plus,winding),'winding_trace_residual':abs((plus[0][0]+plus[1][1])-(winding[0][0]+winding[1][1]))}
def zero_connection_control(length=.94,n=6000,samples=15):
 h=sampled_transport(lambda u:[[0.,0.],[0.,0.]],length,n,samples);return {'samples':h,'maximum_identity_residual':max(diff(x['ordered'],I) for x in h)}
def orientation_control(length=.94,n=6000,samples=15):
 raw=endpoint_matched_control(length,n,samples);r=rot(.31);rt=tr(r);cov=max(diff(mm(mm(rt,x['U_1']),r),x['U_1']) for x in raw['samples']);f=[[1.,0.],[0.,-1.]];u=raw['samples'][samples//2]['U_1'];ref=mm(mm(f,u),f);expected=tr(u)
 return {'so2_covariance_residual':cov,'reflection_matrix_residual':diff(ref,expected),'reflection_trace_residual':abs((ref[0][0]+ref[1][1])-(u[0][0]+u[1][1])),'oriented_angle_reversal_residual':abs(math.atan2(ref[1][0],ref[0][0])+math.atan2(u[1][0],u[0][0]))}
def affine_control(length=.94,n=6000,samples=15,factor=1.47):
 raw=endpoint_matched_control(length,n,samples);a1=lambda u:[[x/factor for x in row] for row in path.afun(1,length)(u/factor)];a2=lambda u:[[x/factor for x in row] for row in path.afun(2,length)(u/factor)];h1=sampled_transport(a1,length*factor,n,samples);h2=sampled_transport(a2,length*factor,n,samples);vals=[]
 for x,y,z in zip(raw['samples'],h1,h2):vals.extend([diff(x['U_1'],y['ordered']),diff(x['U_2'],z['ordered']),abs(x['angle_1']-y['angle']),abs(x['angle_2']-z['angle'])])
 return {'factor':factor,'maximum_dimensionless_residual':max(vals)}
def build(n=6000,samples=15):
 return {'classification':'EXACT_SPACETIME_SCREEN_CONNECTION_HOLONOMY_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_PLANE_WAVE_SO2_SCREEN_HOLONOMY_ENDPOINT_MATCHED_AND_TRACE_SIGN_WINDING_ALIASED_CANONICAL_LOOP_NOT_INDEPENDENT_NOT_ELL0','open_gate':'PHYSICAL_SPACETIME_CONNECTION_LOOP_FAMILY_ANCHOR_BRANCH_PARITY_READOUT_AND_ELL0_LAW_NOT_DERIVED','raw_objects':['omega_i','A_i','U_i(u)','theta_i(u)','trace_i(u)','spectrum_i(u)','H_21','P_canonical_loop','L'],'endpoint_matched':endpoint_matched_control(n=n,samples=samples),'alias':alias_control(),'zero_connection':zero_connection_control(n=n,samples=samples),'orientation':orientation_control(n=n,samples=samples),'affine':affine_control(n=n,samples=samples),'connection_scope':'PRESCRIBED_SO2_SCREEN_CONNECTION_NOT_FOUR_DIMENSIONAL_LEVI_CIVITA_LOOP','ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED','source_scope':'Coley-McNutt-Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; not prescribed screen connection, loop/readout protocol, branch, ell0, UMCH, or detection.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
 if a.check:
  if not OUTPUT.exists() or OUTPUT.read_text()!=text:print('Artifact differs.',file=sys.stderr);return 1
  print('Plane-wave screen-connection holonomy artifact is current.');return 0
 if a.write:OUTPUT.write_text(text);print(OUTPUT);return 0
 print(text,end='');return 0
if __name__=='__main__':raise SystemExit(main())
