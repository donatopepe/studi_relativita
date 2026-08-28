#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('cross-channel-nuisance-results.json')
def observe(x,A,c1,c2,p1,p2,g1,g2):return [g1*A*c1*x**p1,g2*A*c2*x**p2]
def infer_x(obs,c1,c2,p1,p2,gain_ratio):
 d=p1-p2
 if d==0 or min(obs[0],obs[1],c1,c2,gain_ratio)<=0:raise ValueError
 return ((obs[0]/obs[1])*(c2/c1)/gain_ratio)**(1/d)
def required_gain_ratio(obs,c1,c2,p1,p2,x):return (obs[0]/obs[1])*(c2/c1)*x**(p2-p1)
def gate(p1,p2,gain_ratio):
 if p1==p2:return 'X_NON_IDENTIFIABLE_EQUAL_EXPONENTS'
 return 'X_STRUCTURALLY_NON_IDENTIFIABLE_FREE_GAIN_RATIO' if gain_ratio is None else 'X_IDENTIFIABLE_IF_GAIN_RATIO_AND_SHAPE_FIXED'
def x_interval(ratio,c1,c2,p1,p2,gmin,gmax):
 d=p1-p2
 if d<=0 or min(ratio,c1,c2,gmin,gmax)<=0 or gmin>gmax:raise ValueError
 vals=[((ratio*c2/c1)/g)**(1/d) for g in (gmin,gmax)];return [min(vals),max(vals)]
def evaluate():
 common=observe(3,2,2,1,2,1,5,5);ratio=common[0]/common[1]
 return {'study_id':'cross-channel-calibration-nuisance-v1','common_gain':{'observed':common,'recovered_x':infer_x(common,2,1,2,1,1),'gate':gate(2,1,1)},'free_independent_gain':{'gate':gate(2,1,None),'required_gain_ratio_for_x7':required_gain_ratio(common,2,1,2,1,7)},'bounded_gain_ratio':{'bounds':[.5,2],'x_interval':x_interval(ratio,2,1,2,1,.5,2),'gate':'SET_IDENTIFIED_ONLY'},'equal_exponents':{'gate':gate(1,1,1)},'status':'CROSS_CHANNEL_IDENTIFIABILITY_REQUIRES_CALIBRATION_QUOTIENT','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Synthetic channels and calibration groups only; no physical exponents, coefficients, likelihood or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Cross-channel nuisance artifact differs',file=sys.stderr);return 1
  print('Cross-channel nuisance artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
