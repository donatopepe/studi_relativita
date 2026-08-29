#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('cross-channel-gain-bounds-results.json')
def validate(R,C,gmin,gmax):
 if min(R,C,gmin,gmax)<=0 or gmin>gmax:raise ValueError('positive ordered inputs required')
def feasible_interval(R,C,gmin,gmax,delta):
 validate(R,C,gmin,gmax)
 if delta==0:raise ValueError('delta must be nonzero for x interval')
 a=(R/(C*gmin))**(1/delta);b=(R/(C*gmax))**(1/delta)
 return (min(a,b),max(a,b))
def required_gain(R,C,x,delta):
 if min(R,C,x)<=0:raise ValueError('positive inputs required')
 return R/(C*x**delta)
def equal_delta_gate(R,C,gmin,gmax):
 validate(R,C,gmin,gmax);q=R/C
 return 'X_ABSENT_EQUAL_HOMOGENEITY' if gmin<=q<=gmax else 'GAIN_BOUNDS_INCONSISTENT'
def ell0_gate(symbols):return 'BOUNDED_GAIN_SET_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_X_AND_PROSPECTIVE_GAIN_BOUNDS'
def evaluate():
 cases=[]
 for d in [2,1,-1,-2]:
  lo,hi=feasible_interval(9,1,1,9,d);mid=(lo+hi)/2;cases.append({'delta':d,'interval':[lo,hi],'midpoint':mid,'required_gain_at_midpoint':required_gain(9,1,mid,d)})
 return {'study_id':'cross-channel-gain-bounds-v1','model':'R=gamma C x^delta','gain_bounds':[1,9],'cases':cases,'sharpness_gate':'EVERY_INTERVAL_CANDIDATE_ATTAINABLE_BY_ADMISSIBLE_GAIN','point_gate':'POINT_ONLY_IF_GAIN_INTERVAL_COLLAPSES','equal_homogeneity_feasible':equal_delta_gate(4,2,1,3),'equal_homogeneity_inconsistent':equal_delta_gate(8,2,1,3),'ell0_gate':ell0_gate(['x','gamma']),'status':'CROSS_CHANNEL_BOUNDED_GAIN_SHARP_SET_IDENTIFICATION_ONLY','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Positive synthetic power-ratio model; no physical channel law, calibrated prospective bounds, data, or UMCH scale derivation.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Cross-channel gain-bounds artifact differs',file=sys.stderr);return 1
  print('Cross-channel gain-bounds artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
