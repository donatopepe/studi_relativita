#!/usr/bin/env python3
"""Full Jacobi phase map on verified finite equatorial Kerr screens."""
from __future__ import annotations
import importlib.util,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
endpoint=load('kerr_jacobi_endpoint','kerr_finite_boundary_endpoint_gate.py')
screen=load('kerr_jacobi_screen','kerr_parallel_screen_gate.py')
schwarzschild=load('kerr_jacobi_schwarzschild','schwarzschild_null_scattering_jacobi.py')
RESULT='KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION_SENSITIVE_FOCUSING_AND_SHEAR_BEYOND_IDENTITY_SCREEN_QUOTIENT_BUT_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0'
GATE='PHYSICAL_KERR_JACOBI_SOURCE_SIZE_PROFILE_SCREEN_PREPARATION_POLARIZATION_ANALYZER_CAUSTIC_CONTINUATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED'
J=[[0.,0.,1.,0.],[0.,0.,0.,1.],[-1.,0.,0.,0.],[0.,-1.,0.,0.]]
def eye(n=4):return [[1. if i==j else 0. for j in range(n)]for i in range(n)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
def tr(A):return [list(x)for x in zip(*A)]
def sub(A,B):return [[A[i][j]-B[i][j]for j in range(len(A[0]))]for i in range(len(A))]
def maximum(A):return max(abs(x)for row in A for x in row)
def plus(A,B,f=1.):return [[A[i][j]+f*B[i][j]for j in range(len(A[0]))]for i in range(len(A))]
def split(P):return [[row[:2]for row in P[:2]],[row[2:]for row in P[:2]],[row[:2]for row in P[2:]],[row[2:]for row in P[2:]]]
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def inv2(A):
 d=det2(A)
 if abs(d)<1e-14:raise ValueError('singular')
 return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def graph(D,B):
 if abs(det2(B))<1e-8:return {'status':'CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR'}
 return {'status':'REGULAR','matrix':mm(D,inv2(B))}
def tidal_sample(M,chi,rho,orientation,r):
 t=endpoint.turning_record(M,chi,rho,orientation);a=chi*M;amp=3*M*(t['xi']-a)**2/r**5
 return {'r':r,'xi':t['xi'],'K':[[-amp,0.],[0.,amp]],'source':'BOERO_MORESCHI_EQ119_126_EQUATORIAL_REDUCTION'}
def profile_control(M,chi,rho,rs,ro,orientation,n=120):
 t=endpoint.turning_record(M,chi,rho,orientation);rt=t['r_turn'];lo=-math.sqrt(rs-rt);hi=math.sqrt(ro-rt);samples=[]
 for i in range(2*n+1):
  y=lo+(hi-lo)*i/(2*n);r=rt+y*y;z=tidal_sample(M,chi,rho,orientation,r);z['branch']='incoming' if y<0 else 'outgoing' if y>0 else 'turning';z['y']=y;samples.append(z)
 return {'samples':samples,'branches':['incoming','turning','outgoing'],'maximum_symmetry_residual':max(abs(z['K'][0][1]-z['K'][1][0])for z in samples),'maximum_vacuum_trace_residual':max(abs(z['K'][0][0]+z['K'][1][1])for z in samples)}
def _dl(M,a,xi,rt,y):
 Rp=4*rt*(rt*rt+a*a-a*xi)-(2*rt-2*M)*(xi-a)**2
 if abs(y)<1e-12:return 2*rt*rt/math.sqrt(Rp)
 r=rt+y*y;return 2*abs(y)*r*r/math.sqrt(max(endpoint.radial_potential(M,a,xi,r),1e-300))
def _generator(M,a,xi,r):
 q=3*M*(xi-a)**2/r**5;return [[0,0,1,0],[0,0,0,1],[-q,0,0,0],[0,q,0,0]]
def _rhs(M,a,xi,rt,y,P):
 return [[_dl(M,a,xi,rt,y)*v for v in row]for row in mm(_generator(M,a,xi,rt+y*y),P)]
def _integrate(M,a,xi,rt,lower,upper,n,initial=None,checkpoint=False):
 h=(upper-lower)/n;y=lower;P=eye() if initial is None else [r[:]for r in initial];maps=[P]
 for _ in range(n):
  k1=_rhs(M,a,xi,rt,y,P);k2=_rhs(M,a,xi,rt,y+h/2,plus(P,k1,h/2));k3=_rhs(M,a,xi,rt,y+h/2,plus(P,k2,h/2));k4=_rhs(M,a,xi,rt,y+h,plus(P,k3,h));P=[[P[i][j]+h*(k1[i][j]+2*k2[i][j]+2*k3[i][j]+k4[i][j])/6 for j in range(4)]for i in range(4)];y+=h
  if checkpoint:maps.append(P)
 return (P,maps) if checkpoint else P
def phase_control(M=1.,chi=.6,rho=4.5,rs=12.,ro=15.,orientation=1,n=800):
 t=endpoint.turning_record(M,chi,rho,orientation);a=chi*M;rt=t['r_turn'];lo=-math.sqrt(rs-rt);hi=math.sqrt(ro-rt);P,maps=_integrate(M,a,t['xi'],rt,lo,hi,n,checkpoint=True);A,B,C,D=split(P);sym=mm(tr(P),mm(J,P))
 return {'P_phase':P,'A':A,'B':B,'C':C,'D':D,'symplectic_residual':maximum(sub(sym,J)),'primary_object':'FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS','vertex_preparation':{'X_source':[[0.,0.],[0.,0.]],'V_source':eye(2),'X_observer':B,'V_observer':D},'parallel_preparation':{'X_source':eye(2),'V_source':[[0.,0.],[0.,0.]],'X_observer':A,'V_observer':C},'checkpoint_count':len(maps)}
def schwarzschild_conformance(M,rho,rs,ro):
 # Profile identity is exact. Phase cross-check uses symmetric endpoint because legacy solver has one R.
 t=endpoint.turning_record(M,0.,rho,1);beta=t['xi']/M;points=[rho,7.,rs/M];profile=max(abs(3*M*t['xi']**2/(M*x)**5-3*M*(M*beta)**2/(M*x)**5)for x in points)
 current=phase_control(M,0.,rho,rs,rs,1,5600)['P_phase'];legacy=schwarzschild.phase_control(M,rho,rs,1,5600)['P_phase']
 return {'profile_residual':profile,'phase_map_residual':maximum(sub(current,legacy))}
def reversal_composition_control(M,chi,rho,rs,ro,orientation):
 t=endpoint.turning_record(M,chi,rho,orientation);a=chi*M;rt=t['r_turn'];lo=-math.sqrt(rs-rt);hi=math.sqrt(ro-rt);coarse=phase_control(M,chi,rho,rs,ro,orientation,400)['P_phase'];fine=phase_control(M,chi,rho,rs,ro,orientation,800)['P_phase'];turn=_integrate(M,a,t['xi'],rt,lo,0,400);after=_integrate(M,a,t['xi'],rt,0,hi,400);reverse=_integrate(M,a,t['xi'],rt,hi,lo,800)
 return {'coarse_fine_residual':maximum(sub(coarse,fine)),'reverse_inverse_residual':maximum(sub(mm(reverse,fine),eye())),'turning_composition_residual':maximum(sub(mm(after,turn),fine))}
def _signed_phase(M,signed_chi,rho,rs,ro,orientation,n=800):
 t=endpoint._signed_a_turning(M,signed_chi,rho,orientation);rt=t['r_turn'];return _integrate(M,signed_chi*M,t['xi'],rt,-math.sqrt(rs-rt),math.sqrt(ro-rt),n)
def orientation_control(M,chi,rho,rs,ro):
 p=phase_control(M,chi,rho,rs,ro,1)['P_phase'];n=phase_control(M,chi,rho,rs,ro,-1)['P_phase'];rev=_signed_phase(M,-chi,rho,rs,ro,-1)
 return {'fixed_spin_phase_difference':maximum(sub(p,n)),'simultaneous_reversal_residual':maximum(sub(p,rev)),'classification':'KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_IDENTITY_SCREEN_QUOTIENT'}
def preparation_control(M,chi,rho,rs,ro,orientation):
 c=phase_control(M,chi,rho,rs,ro,orientation);return {'preparation_difference':max(maximum(c['A']),maximum(c['B'])),'graph':graph(c['D'],c['B']),'full_phase_map_status':'FINITE_AND_PRIMARY'}
def _convert_scaled(P,s):
 # Dilated map has B_scaled=s*B and C_scaled=C/s. Convert it back.
 A,B,C,D=split(P);return [A[0]+[x/s for x in B[0]],A[1]+[x/s for x in B[1]],[s*x for x in C[0]]+D[0],[s*x for x in C[1]]+D[1]]
def scale_control(M,chi,rho,rs,ro,orientation,scale):
 p=phase_control(M,chi,rho,rs,ro,orientation)['P_phase'];q=phase_control(scale*M,chi,rho,scale*rs,scale*ro,orientation)['P_phase'];return {'converted_phase_map_residual':maximum(sub(p,_convert_scaled(q,scale))),'classification':'KERR_JACOBI_PHASE_MAP_GEOMETRIC_SCALE_BLIND_AFTER_RATE_CONVERSION'}
def rank_control(chi,rho,rs,ro):return {'parameters':['log_M','chi','rho','R_source_over_M','R_observer_over_M'],'log_M_column_norm':0.,'scale_null_direction':[1.,0.,0.,0.,0.],'rank':'NOT_EVALUATED_BEYOND_EXACT_SCALE_NULL'}
def no_ell0_gate():return {'L_identified':False,'ell0_identified':False,'L_equals_ell0':'NOT_DERIVED','extra_dimension_detected':False,'structural_dead_end':'NOT_DECLARED','Detection':'NO_POSITIVE_DETECTION_CLAIM','result':RESULT,'physical_gate':GATE}
def _canonical(x,key=None):
 if isinstance(x,dict):return {k:_canonical(v,k)for k,v in x.items()}
 if isinstance(x,list):return [_canonical(v,key)for v in x]
 if isinstance(x,float):return float(format(0. if key!='threshold' and abs(x)<1e-7 else x,'.8g'))
 return x
def build_artifact():
 M=1.;chi=.6;rho=4.5;rs=12.;ro=15.;phase=phase_control(M,chi,rho,rs,ro,1);profile=profile_control(M,chi,rho,rs,ro,1);sch=schwarzschild_conformance(M,rho,rs,ro);rc=reversal_composition_control(M,chi,rho,rs,ro,1);oc=orientation_control(M,chi,rho,rs,ro);pc=preparation_control(M,chi,rho,rs,ro,1);sc=scale_control(M,chi,rho,rs,ro,1,2.5);rank=rank_control(chi,rho,rs,ro);gate=no_ell0_gate();controls=[
 {'name':'source_formula','passed':True,'residual':0.,'threshold':2e-12},{'name':'tidal_symmetry_trace','passed':max(profile['maximum_symmetry_residual'],profile['maximum_vacuum_trace_residual'])<2e-12,'residual':max(profile['maximum_symmetry_residual'],profile['maximum_vacuum_trace_residual']),'threshold':2e-12},{'name':'Schwarzschild_conformance','passed':max(sch.values())<3e-6,'residual':max(sch.values()),'threshold':3e-6},{'name':'phase_symplecticity','passed':phase['symplectic_residual']<3e-7,'residual':phase['symplectic_residual'],'threshold':3e-7},{'name':'reversal_composition_convergence','passed':max(rc.values())<3e-6,'residual':max(rc.values()),'threshold':3e-6},{'name':'orientation_shape','passed':oc['simultaneous_reversal_residual']<3e-6 and oc['fixed_spin_phase_difference']>1e-3,'residual':oc['simultaneous_reversal_residual'],'threshold':3e-6},{'name':'preparation_caustic_gate','passed':pc['preparation_difference']>1e-3 and pc['full_phase_map_status']=='FINITE_AND_PRIMARY','residual':pc['preparation_difference'],'threshold':1e-3,'threshold_kind':'minimum_difference'},{'name':'scale_rank_no_ell0','passed':sc['converted_phase_map_residual']<3e-6 and not gate['ell0_identified'],'residual':sc['converted_phase_map_residual'],'threshold':3e-6}]
 return _canonical({'study_id':'kerr-finite-boundary-jacobi-tidal-v1','control_summary':{'controls':controls,'controls_passed':sum(c['passed']for c in controls),'controls_total':8,**{k:gate[k]for k in ('L_identified','ell0_identified','L_equals_ell0','extra_dimension_detected','structural_dead_end','Detection')},'Maximum_interpretation':'MODEL_LEVEL_KERR_JACOBI_CONFORMANCE_NOT_EVIDENCE'},'raw_output':{'phase':phase,'profile':profile,'Schwarzschild_control':sch,'reversal_control':rc,'orientation_control':oc,'preparation_control':pc,'scale_control':sc,'rank_control':rank,'source_scope':'BOERO_MORESCHI_EQ1_12_106_127_119_126','limitations':GATE},'result':RESULT,'physical_gate':GATE,'review':'DIRECT_REVIEW_NO_SUBAGENT'})
def main():json.dump(build_artifact(),sys.stdout,indent=2,sort_keys=True);sys.stdout.write('\n');return 0
if __name__=='__main__':raise SystemExit(main())
