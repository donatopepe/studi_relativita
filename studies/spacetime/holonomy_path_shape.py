#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('holonomy-path-shape-results.json')
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0];return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def trace(a):return a[0][0]+a[1][1]
def loop(ell,rho):return mm([[1,ell],[0,1]],[[1,0],[-rho*ell,1]])
def loop_trace(ell,rho):return trace(loop(ell,rho))
def crossing(tau,rho):
 q=(2-tau)/rho if rho!=0 else -1
 return math.sqrt(q) if q>0 else None
def rho_for_crossing(tau,ell_cross):return (2-tau)/(ell_cross*ell_cross)
def ell0_gate(symbols):return 'PATH_SHAPE_GEOMETRIC_SCALE_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_FIXED_LOOP_FAMILY'
def evaluate():
 tau=1
 return {'study_id':'holonomy-path-shape-v1','target_trace':tau,'movable_crossings':[{'target':x,'required_rho':rho_for_crossing(tau,x),'recovered':crossing(tau,rho_for_crossing(tau,x))} for x in [1,2,5]],'zero_shape_crossing':crossing(tau,0),'trace_gate':'CONJUGACY_INVARIANT_BUT_PATH_NUISANCE_DEPENDENT','ell0_gate':ell0_gate(['ell','rho','tau']),'status':'HOLONOMY_TRACE_LANDMARK_PATH_SHAPE_MOVABLE_NOT_ELL0','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'2x2 shear-product toy; rho is free path-shape protocol, not connection-derived geometry, observation, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Holonomy path-shape artifact differs',file=sys.stderr);return 1
  print('Holonomy path-shape artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
