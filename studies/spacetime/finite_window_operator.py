#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('finite-window-operator-results.json')
def response(ell,a,f,b=None,g=0):
 out=[ell*ell*f*x for x in a]
 if b is not None:out=[out[i]+ell*ell*g*b[i] for i in range(len(a))]
 return out
def project(v):
 n=math.sqrt(sum(x*x for x in v));return None if n==0 else [round(x/n,12) for x in v]
def compare(a,b):return 'PROJECTIVE_SCALE_NON_IDENTIFIABLE_SEPARABLE_WINDOW' if project(a)==project(b) else 'NONRADIAL_PROFILE_DEPENDENT_SHAPE_ONLY'
def identifiability(symbols):return 'ELL0_NOT_PRESENT_IN_GEOMETRIC_WINDOW_CONTROL' if 'ell0' not in symbols else 'ELL0_REQUIRES_THEORY_FIXED_MAP'
def evaluate():
 sep=[response(1,[1,2,3],1),response(2,[1,2,3],4)]
 mix=[response(1,[1,-1,0],1,[0,1,-1],0),response(2,[1,-1,0],1,[0,1,-1],1)]
 return {'study_id':'finite-window-operator-v1','separable':{'projective':[project(x) for x in sep],'decision':compare(*sep)},'mixed_profiles':{'projective':[project(x) for x in mix],'decision':compare(*mix)},'identifiability':identifiability(['ell','profile_coefficients','window']),'status':'NONRADIAL_GEOMETRIC_SHAPE_NOT_ELL0_LANDMARK','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Noncollinear profiles are prescribed toys, not derived exact-geometry windows; nuisance profiles/window can mimic shape.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Finite-window artifact differs',file=sys.stderr);return 1
  print('Finite-window artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
