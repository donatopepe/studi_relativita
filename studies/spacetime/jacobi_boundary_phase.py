#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-boundary-phase-results.json')
def solution(lam,d0,v0,s):
 if lam<=0:raise ValueError
 w=math.sqrt(lam);return d0*math.cos(w*s)+(v0/w)*math.sin(w*s)
def first_positive_zero(lam,d0,v0):
 if lam<=0 or (d0==0 and v0==0):raise ValueError
 w=math.sqrt(lam);phi=math.atan2(-w*d0,v0);n=math.floor(-phi/math.pi)+1;s=(phi+n*math.pi)/w
 if s<=1e-12:s+=math.pi/w
 return s
def velocity_for_zero(lam,d0,target):
 if lam<=0 or target<=0:raise ValueError
 w=math.sqrt(lam);q=math.sin(w*target)
 if abs(q)<1e-12:raise ValueError
 return -w*d0*math.cos(w*target)/q
def ell0_gate(symbols):return 'BOUNDARY_PHASE_GEOMETRIC_ZERO_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_BOUNDARY_CONTRACT'
def evaluate():
 lam=4
 return {'study_id':'jacobi-boundary-phase-v1','lambda':lam,'vertex_first_positive_zero':first_positive_zero(lam,0,1),'movable_targets':[{'target':x,'required_v0_for_d0_1':velocity_for_zero(lam,1,x),'recovered_zero':first_positive_zero(lam,1,velocity_for_zero(lam,1,x))} for x in [.2,.7,1.2]],'amplitude_scale_collision':[first_positive_zero(lam,1,-3),first_positive_zero(lam,5,-15)],'trivial_boundary_gate':'ZERO_INITIAL_DATA_TRIVIAL_CHANNEL_REJECTED','ell0_gate':ell0_gate(['lambda','d0','v0']),'status':'JACOBI_CAUSTIC_BOUNDARY_PHASE_MOVABLE_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact constant-positive scalar ODE only; no varying optical matrix, covariant screen transport, observation, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi boundary-phase artifact differs',file=sys.stderr);return 1
  print('Jacobi boundary-phase artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
