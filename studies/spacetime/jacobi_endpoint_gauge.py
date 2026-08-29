#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-endpoint-gauge-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return [list(x) for x in zip(*a)]
def rot(t):return [[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]]
def reflection(t):return mm(rot(t),[[1,0],[0,-1]])
def endpoint_action(b,to,ts):return mm(mm(rot(to),b),transpose(rot(ts)))
def orthogonal_action(b,to,ts,ro=False,rs=False):
 qo=reflection(to) if ro else rot(to);qs=reflection(ts) if rs else rot(ts);return mm(mm(qo,b),transpose(qs))
def distance(a,b):return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def antisymmetric_scalar(a):return (a[0][1]-a[1][0])/2
def singular_values(a):
 ata=mm(transpose(a),a);t=ata[0][0]+ata[1][1];d=det2(ata);q=math.sqrt(max(0,t*t-4*d));return tuple(sorted((math.sqrt(max(0,(t-q)/2)),math.sqrt(max(0,(t+q)/2)))))
def grid_fit(b,target,common=False,orthogonal=False):
 best={'residual':float('inf'),'theta_observer':0.,'theta_source':0.,'observer_reflection':False,'source_reflection':False};n=720
 flags=[(False,False)] if not orthogonal else [(x,y) for x in (False,True) for y in (False,True)]
 for ro,rs in flags:
  for i in range(n):
   to=2*math.pi*i/n
   js=[i] if common else range(n)
   for j in js:
    ts=2*math.pi*j/n;c=orthogonal_action(b,to,ts,ro,rs);r=distance(c,target)
    if r<best['residual']:best={'residual':r,'theta_observer':to,'theta_source':ts,'observer_reflection':ro,'source_reflection':rs}
 return best
def fit_endpoint_rotations(b,target):
 if distance(target,transpose(b))<1e-12:
  phi=math.atan2(b[1][0]-b[0][1],b[0][0]+b[1][1]);c=endpoint_action(b,-phi,phi);return {'residual':distance(c,target),'theta_observer':-phi,'theta_source':phi,'observer_reflection':False,'source_reflection':False}
 return grid_fit(b,target)
def fit_common_rotation(b,target):return grid_fit(b,target,common=True)
def fit_endpoint_orthogonal(b,target):
 if distance(target,transpose(b))<1e-12:return fit_endpoint_rotations(b,target)
 return grid_fit(b,target,orthogonal=True)
def ell0_gate(symbols):return 'ENDPOINT_FRAME_QUOTIENT_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICALLY_LINKED_ENDPOINT_FRAMES'
def evaluate():
 b=[[.62,.11],[-.04,.39]];bt=transpose(b);ind=fit_endpoint_rotations(b,bt);common=fit_common_rotation(b,bt);rd=[[1,2],[0,0]]
 return {'study_id':'jacobi-endpoint-gauge-v1','vertex_block':b,'transpose':bt,'antisymmetric_forward':antisymmetric_scalar(b),'antisymmetric_transpose':antisymmetric_scalar(bt),'singular_values':singular_values(b),'determinant':det2(b),'independent_so2_fit':ind,'common_so2_fit':common,'rank_deficient_o2_fit':fit_endpoint_orthogonal(rd,transpose(rd)),'gauge_gate':'INDEPENDENT_SOURCE_OBSERVER_FRAMES_ACT_BY_LEFT_RIGHT_ORTHOGONAL_ACTION','orbit_gate':'TRANSPOSE_SHARES_SINGULAR_VALUES_AND_DETERMINANT_AND_IS_ENDPOINT_FRAME_EQUIVALENT','anchor_gate':'COMMON_ANCHORED_FRAME_RESTRICTION_REQUIRES_PHYSICAL_TRANSPORT_CERTIFICATE','ell0_gate':ell0_gate(['B','Qo','Qs','screen']),'status':'JACOBI_TRANSPOSE_REVERSAL_NONIDENTIFIABLE_UNDER_INDEPENDENT_ENDPOINT_FRAME_QUOTIENT','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Endpoint-frame quotient control; not a derived spacetime screen-transport law, detector calibration, data result, or UMCH mechanism.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi endpoint-gauge artifact differs',file=sys.stderr);return 1
  print('Jacobi endpoint-gauge artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
