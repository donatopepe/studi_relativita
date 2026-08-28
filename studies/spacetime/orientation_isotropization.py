#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('orientation-isotropization-results.json');A=[[3,0],[0,1]];B=[[1,0],[0,3]]
def average(w):return [[w*A[i][j]+(1-w)*B[i][j] for j in range(2)] for i in range(2)]
def eigenvalues(a):
 tr=a[0][0]+a[1][1];det=a[0][0]*a[1][1]-a[0][1]*a[1][0];d=math.sqrt(max(0,tr*tr-4*det));return [round((tr-d)/2,12),round((tr+d)/2,12)]
def projective_spectrum(a):
 e=eigenvalues(a);n=math.sqrt(sum(x*x for x in e));return [round(x/n,12) for x in e]
def weight_profile(ell,target):return .5+.25*(ell-target)/(ell+target)
def ell0_gate(symbols):return 'ORIENTATION_PROTOCOL_SCALE_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_ORIENTATION_MEASURE'
def evaluate():
 return {'study_id':'orientation-isotropization-v1','operator':A,'rotated_operator':B,'weights':[{'w':w,'operator':average(w),'eigenvalues':eigenvalues(average(w)),'projective_spectrum':projective_spectrum(average(w))} for w in [0,0.25,0.5,0.75,1]],'movable_targets':[{'target':x,'weight_at_target':weight_profile(x,x)} for x in [1,4,9]],'isotropy_gate':'MULTIPLICITY_CHANGE_FROM_ORIENTATION_MIXTURE','ell0_gate':ell0_gate(['ell','weight','A']),'status':'ORIENTATION_WEIGHT_LANDMARK_PROTOCOL_MOVABLE_NOT_ELL0','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'2x2 rotated-mixture toy; orientation weights are protocol nuisance, not derived spacetime measure, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Orientation isotropization artifact differs',file=sys.stderr);return 1
  print('Orientation isotropization artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
