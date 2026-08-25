#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;DI=HERE/'threshold-cases.json';DO=HERE/'threshold-results.json'
def threshold(family,x,p):
 x=float(x)
 if x<1:raise ValueError('x=ell/ell0 must be >=1')
 if family=='F_0':return 0.
 if family=='F_P':return float(p['A'])*x**(-float(p['p']))
 if family=='F_E':return float(p['A'])*math.exp(-float(p['q'])*(x-1))
 if family=='F_PE':return float(p['A_inf'])+float(p['A_1'])*x**(-float(p['p']))
 raise ValueError(family)
def classify(response,floor,frame_status,identifiable):
 if frame_status!='FRAME_RESOLVED':return 'FRAME_UNRESOLVED'
 if not identifiable:return 'NON_IDENTIFIABLE'
 if float(response)==0 and float(floor)>0:return 'CONTRADICTED'
 if float(response)>=float(floor)>0:return 'SUPPORTED_WITHIN_DATA_RANGE'
 return 'UPPER_BOUND_ONLY'
def evaluate(d):
 vals={k:[threshold(k,x,p) for x in d['x_samples']] for k,p in d['families'].items()}
 checks=[{**c,'status':classify(c['response'],c['threshold'],c['frame_status'],c['identifiable'])} for c in d['synthetic_checks']]
 return {'study_id':d['study_id'],'norm':d['norm'],'families':vals,'synthetic_checks':checks,'conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Threshold arithmetic and status logic only; no real-universe data or ell0 estimate.'}
def render(d):return json.dumps(evaluate(d),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,default=DI);p.add_argument('--output',type=pathlib.Path,default=DO);p.add_argument('--check',action='store_true');a=p.parse_args();e=render(json.loads(a.input.read_text()))
 if a.check:
  if not a.output.exists() or a.output.read_text()!=e:print('Thresholds differ',file=sys.stderr);return 1
  print('Spacetime thresholds are current.');return 0
 a.output.write_text(e);print(f'Wrote {a.output}');return 0
if __name__=='__main__':raise SystemExit(main())
