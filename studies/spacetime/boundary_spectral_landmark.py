#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('boundary-spectral-landmark-results.json')
def operator(ell,a,c,beta):return [a*ell*ell+beta,c*ell*ell]
def project(v):
 n=math.sqrt(sum(x*x for x in v));return None if n==0 else [round(x/n,12) for x in v]
def crossing(a,c,beta):
 q=beta/(c-a) if c!=a else -1
 return math.sqrt(q) if q>0 else None
def beta_for_crossing(a,c,ell_cross):return (c-a)*ell_cross*ell_cross
def ell0_gate(symbols):return 'BOUNDARY_GEOMETRIC_SCALE_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_CROSSING_LINK'
def evaluate():
 a,c,beta=1,2,4
 return {'study_id':'boundary-spectral-landmark-v1','family':{'a':a,'c':c,'beta':beta,'projective_at_ell1':project(operator(1,a,c,beta)),'projective_at_ell2':project(operator(2,a,c,beta)),'crossing':crossing(a,c,beta)},'movable_crossings':[{'target':x,'required_beta':beta_for_crossing(a,c,x),'recovered':crossing(a,c,beta_for_crossing(a,c,x))} for x in [1,3,7]],'no_crossing_case':crossing(2,1,4),'ell0_gate':ell0_gate(['ell','a','c','beta']),'status':'BOUNDARY_SPECTRAL_LANDMARK_MOVABLE_NOT_ELL0','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Additive diagonal boundary toy only; beta is not derived from GR, protocol, observation, or UMCH.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Boundary landmark artifact differs',file=sys.stderr);return 1
  print('Boundary landmark artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
