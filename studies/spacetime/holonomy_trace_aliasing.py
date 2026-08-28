#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('holonomy-trace-aliasing-results.json')
def rotation(phi):return [[math.cos(phi),-math.sin(phi)],[math.sin(phi),math.cos(phi)]]
def trace(phi):return 2*math.cos(phi)
def principal_phase(t):
 if t < -2 or t > 2:raise ValueError('rotation trace must lie in [-2,2]')
 return math.acos(max(-1,min(1,t/2)))
def branches(t,nmax):
 p=principal_phase(t);return sorted(set(round(s*p+2*math.pi*n,12) for n in range(-nmax,nmax+1) for s in [-1,1]))
def phase(curvature,area):return curvature*area
def ell0_gate(symbols):return 'HOLONOMY_PHASE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_BRANCH_FIXED_LOOP_LAW'
def evaluate():
 p=.7;t=trace(p)
 return {'study_id':'holonomy-trace-aliasing-v1','holonomy':'SO(2) rotation H(phi)','trace_formula':'T(phi)=2 cos(phi)','reference_phase':p,'reference_trace':t,'branches_n2':branches(t,2),'collision_gate':'TRACE_EVEN_AND_TWO_PI_PERIODIC','local_gate':'INJECTIVE_ONLY_ON_PREREGISTERED_MONOTONE_BRANCH','conditioning_gate':'TRACE_DERIVATIVE_ZERO_AT_BRANCH_ENDPOINTS','amplitude_area_gate':'PHASE_EQUALS_CURVATURE_TIMES_AREA_MULTIPLICATIVE_DEGENERACY','ell0_gate':ell0_gate(['phi','k','area']),'status':'FINITE_HOLONOMY_TRACE_PERIODIC_BRANCH_NONIDENTIFIABLE','classification':'EXACT_GROUP_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact SO(2) matrix algebra; no connection-derived spacetime loop, non-Abelian transport, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Holonomy trace-aliasing artifact differs',file=sys.stderr);return 1
  print('Holonomy trace-aliasing artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
