#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
OUT=pathlib.Path(__file__).with_name('einstein-static-spatial-holonomy-results.json')
ETA=[[-1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]]
I4=[[1. if i==j else 0. for j in range(4)] for i in range(4)]

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def transpose(a):return [list(x) for x in zip(*a)]
def add(a,b,s=1.):return [[a[i][j]+s*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def norm(a):return math.sqrt(sum(x*x for row in a for x in row))
def vecdiff(a,b):return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def rotation(plane,angle):
 i,j=plane;c=math.cos(angle);s=math.sin(angle);h=[row[:] for row in I4];h[i][i]=c;h[j][j]=c;h[i][j]=-s;h[j][i]=s;return h
def generator(plane,angle):
 i,j=plane;w=[[0.]*4 for _ in range(4)];w[i][j]=-angle;w[j][i]=angle;return w
def right_triangle(alpha,beta,R=1.):
 if R<=0 or not(0<alpha<math.pi/2 and 0<beta<math.pi/2):raise ValueError('R positive and angular legs in (0,pi/2) required')
 c=math.acos(math.cos(alpha)*math.cos(beta));sc=math.sin(c)
 A=math.acos(max(-1.,min(1.,math.cos(alpha)*math.sin(beta)/sc)))
 B=math.acos(max(-1.,min(1.,math.sin(alpha)*math.cos(beta)/sc)))
 E=A+B-math.pi/2;return {'alpha':alpha,'beta':beta,'c_angle':c,'A':A,'B':B,'excess':E,'area':R*R*E,'proper_side_lengths':[R*alpha,R*beta,R*c]}
def loop(plane=(1,2),alpha=.43,beta=.71,R=3.2,orientation=1):
 if orientation not in (-1,1):raise ValueError('orientation must be +/-1')
 t=right_triangle(alpha,beta,R);e=orientation*t['excess'];return {'triangle':t,'signed_excess':e,'W':generator(plane,e),'H':rotation(plane,e),'plane':list(plane),'orientation':orientation}
def jacobi(theta):return [[math.cos(theta),math.sin(theta)],[-math.sin(theta),math.cos(theta)]]
def characteristic(e):
 c=math.cos(e)
 # (lambda-1)^2(lambda^2-2c lambda+1)
 return [1.,-2.*(1.+c),2.+4.*c,-2.*(1.+c),1.]
def geometry_control():
 l=loop();h=l['H'];return {'metric_compatibility_residual':norm(add(mm(mm(transpose(h),ETA),h),ETA,-1)),'fixed_time_residual':vecdiff([h[i][0] for i in range(4)],[1.,0.,0.,0.]),'nonidentity_norm':norm(add(h,I4,-1))}
def reversal_control():
 a=loop();b=loop(orientation=-1);return {'inverse_residual':norm(add(mm(a['H'],b['H']),I4,-1)),'signed_excess_residual':abs(a['signed_excess']+b['signed_excess'])}
def nonabelian_control():
 a=loop((1,2),.43,.71);b=loop((2,3),.57,.62);ab=mm(a['H'],b['H']);ba=mm(b['H'],a['H']);comm=mm(mm(mm(a['H'],b['H']),transpose(a['H'])),transpose(b['H']))
 return {'commutator_residual':norm(add(comm,I4,-1)),'ordered_product_difference':norm(add(ab,ba,-1)),'H_12_H_23':ab,'H_23_H_12':ba,'commutator':comm}
def cross_channel_control():
 l=loop();t=l['triangle'];return {'holonomy_from_window_residual':norm(add(l['H'],rotation(tuple(l['plane']),l['signed_excess']),-1)),'excess_minus_area_curvature_residual':abs(l['signed_excess']-t['area']/3.2**2),'holonomy_independent_channel':False,'exact_map':'W_T=E J_ij; H_ij=exp(W_T)'}
def spectrum_control():
 a=loop();b=loop(orientation=-1);return {'trace':tr(a['H']),'spectrum':['1','1','exp(+iE)','exp(-iE)'],'characteristic_coefficients':characteristic(a['signed_excess']),'sign_trace_collision':abs(tr(a['H'])-tr(b['H'])),'raw_sign_difference':norm(add(a['H'],b['H'],-1))}
def anchor_control():
 l=loop();q=mm(rotation((1,3),.39),rotation((2,3),-.21));qc=mm(mm(q,l['H']),transpose(q));wq=mm(mm(q,l['W']),transpose(q));e=l['signed_excess']
 # Rodrigues series closes through W^2 for a simple rotation
 ew=add(add(I4,wq,math.sin(e)/e),mm(wq,wq),(1-math.cos(e))/(e*e))
 return {'common_conjugacy_residual':norm(add(qc,ew,-1)),'characteristic_collision':vecdiff(characteristic(e),characteristic(-e))}
def beta_for_excess(alpha,target):
 lo=1e-10;hi=math.pi/2-1e-10
 if not(right_triangle(alpha,lo)['excess']<target<right_triangle(alpha,hi)['excess']):raise ValueError('target excess not bracketed')
 for _ in range(90):
  mid=(lo+hi)/2
  if right_triangle(alpha,mid)['excess']<target:lo=mid
  else:hi=mid
 return (lo+hi)/2
def shape_collision_control():
 R=3.2;t1=right_triangle(.43,.71,R);b2=beta_for_excess(.58,t1['excess']);t2=right_triangle(.58,b2,R);h1=rotation((1,2),t1['excess']);h2=rotation((1,2),t2['excess'])
 return {'shape_1':t1,'shape_2':t2,'excess_collision':abs(t1['excess']-t2['excess']),'holonomy_collision':norm(add(h1,h2,-1)),'boundary_length_difference':vecdiff(t1['proper_side_lengths'],t2['proper_side_lengths']),'labelled_jacobi_difference':norm(add(jacobi(t1['alpha']),jacobi(t2['alpha']),-1))}
def scale_control():
 s=1.47;R=3.2;a=.43;b=.71;t1=right_triangle(a,b,R);t2=right_triangle(a,b,s*R);h1=rotation((1,2),t1['excess']);h2=rotation((1,2),t2['excess']);j1=jacobi(a);j2=jacobi(t2['proper_side_lengths'][0]/(s*R))
 residuals=[abs(t1['excess']-t2['excess']),norm(add(h1,h2,-1)),norm(add(j1,j2,-1)),abs(t1['area']/R**2-t2['area']/(s*R)**2)]
 return {'scale_factor':s,'maximum_dimensionless_residual':max(residuals),'proper_length_difference':vecdiff(t1['proper_side_lengths'],t2['proper_side_lengths'])}
def flat_control():
 def n(R):
  t=right_triangle(.7/R,1.1/R,R);return norm(add(rotation((1,2),t['excess']),I4,-1))
 return {'finite_radius_nonidentity_norm':n(3.2),'large_radius_nonidentity_norm':n(100.)}
def build():
 l1=loop();l2=loop((2,3),.57,.62);shape=shape_collision_control();nonab=nonabelian_control();scale=scale_control();flat=flat_control()
 return {'study_id':'einstein-static-spatial-holonomy-v1','classification':'EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','status':'EXACT_EINSTEIN_STATIC_SPATIAL_LEVI_CIVITA_HOLONOMY_NONABELIAN_RAW_ORDER_DEPENDENT_WINDOW_EXPONENTIAL_AND_CURVATURE_RADIUS_SCALE_BLIND_NOT_ELL0','scope':'FOUR_DIMENSIONAL_PRODUCT_SPACETIME_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_SPACELIKE_GEODESIC_TRIANGLES_NOT_DETECTOR_DERIVED','physical_gate':'PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED','geometry_control':geometry_control(),'reversal_control':reversal_control(),'nonabelian_control':nonab,'cross_channel_control':cross_channel_control(),'spectrum_control':spectrum_control(),'anchor_control':anchor_control(),'shape_collision_control':shape,'scale_control':scale,'flat_control':flat,'raw_record':{'R':3.2,'eta':ETA,'tetrad':['e0','e1','e2','e3'],'loop_planes':[l1['plane'],l2['plane']],'orientation':[l1['orientation'],l2['orientation']],'alpha_i':[l1['triangle']['alpha'],l2['triangle']['alpha']],'beta_i':[l1['triangle']['beta'],l2['triangle']['beta']],'c_i':[l1['triangle']['c_angle'],l2['triangle']['c_angle']],'proper_side_lengths':[l1['triangle']['proper_side_lengths'],l2['triangle']['proper_side_lengths']],'area_i':[l1['triangle']['area'],l2['triangle']['area']],'E_i':[l1['signed_excess'],l2['signed_excess']],'W_T_i':[l1['W'],l2['W']],'H_i':[l1['H'],l2['H']],'ordered_products':[nonab['H_12_H_23'],nonab['H_23_H_12']],'commutator':nonab['commutator'],'spectrum_i':[spectrum_control()['spectrum'],['1','1','exp(+iE2)','exp(-iE2)']],'chi_i':[characteristic(l1['signed_excess']),characteristic(l2['signed_excess'])],'segment_Jacobi_i':[jacobi(l1['triangle']['alpha']),jacobi(l2['triangle']['alpha'])],'shape_collision':shape,'scale_factor':scale['scale_factor'],'flat_control':flat},'ell0_identified':False,'umch_status':'UNPROVEN','positive_detection_claim':False,'structural_dead_end':'NOT_DECLARED'}
def render():return json.dumps(build(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not OUT.exists() or OUT.read_text()!=s:print('Einstein-static spatial holonomy artifact differs',file=sys.stderr);return 1
  print('Einstein-static spatial holonomy artifact verified');return 0
 OUT.write_text(s);print(f'Wrote {OUT}');return 0
if __name__=='__main__':raise SystemExit(main())
