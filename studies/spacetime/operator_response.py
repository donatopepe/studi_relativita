#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'operator-response-results.json'
def channels(x,A,c1,c2,p1,p2):return [float(A)*float(c1)*float(x)**float(p1),float(A)*float(c2)*float(x)**float(p2)]
def infer_x_from_ratio(r1,r2,c1,c2,p1,p2):
 d=float(p1)-float(p2)
 if min(abs(r1),abs(r2),abs(c1),abs(c2))==0 or d==0:raise ValueError('nonzero channels and distinct exponents required')
 x=((float(r1)/float(r2))*(float(c2)/float(c1)))**(1/d)
 if not math.isfinite(x) or x<=0:raise ValueError('invalid projective inversion')
 return x
def infer_ell0(ell,*args):return float(ell)/infer_x_from_ratio(*args)
def identifiability(v1,v2):
 if len(v1)!=len(v2) or not v1:raise ValueError
 # proportional response directions cannot encode scale projectively
 ratios=[]
 for a,b in zip(v1,v2):
  if a==0:
   if b!=0:return 'PROJECTIVE_IDENTIFIABLE_IN_PRINCIPLE_TOY'
  else:ratios.append(b/a)
 return 'PROJECTIVE_NON_IDENTIFIABLE_COLLINEAR' if ratios and max(ratios)-min(ratios)==0 else 'PROJECTIVE_IDENTIFIABLE_IN_PRINCIPLE_TOY'
def evaluate():
 x,A,c1,c2,p1,p2=3.,2.,2.,1.,2.,1.;r=channels(x,A,c1,c2,p1,p2)
 return {'study_id':'operator-response-projective-identifiability-v1','primary_object':'CHANNEL_NATIVE_TENSOR_OPERATOR_RESPONSE_SECTION','synthetic_projective_control':{'x':x,'raw_channels':r,'recovered_x':infer_x_from_ratio(r[0],r[1],c1,c2,p1,p2),'note':'Synthetic amplitudes/exponents only; no physical channel derivation.'},'counterexample':{'status':identifiability([1,2],[2,4]),'note':'All channel objects scale along same ray; normalization cannot identify scale.'},'status':'OPERATOR_IDENTIFIABILITY_NOT_YET_PHYSICALLY_DERIVED','scalar_turnover_branch':'SECONDARY_PROJECTION_SPECIFIC','conclusion':'NO_POSITIVE_DETECTION_CLAIM'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Operator response results differ',file=sys.stderr);return 1
  print('Operator response results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
