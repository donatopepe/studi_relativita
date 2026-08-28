#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('exact-window-separability-results.json');I=[[1,0,0],[0,1,0],[0,0,1]];S=[[-2,0,0],[0,1,0],[0,0,1]]
def avg(values,weights):
 d=sum(weights);return sum(x*w for x,w in zip(values,weights))/d
def response(ell,values,weights,pattern):
 c=ell*ell*avg(values,weights);return [[c*x for x in row] for row in pattern]
def project(a):
 v=[x for row in a for x in row];n=math.sqrt(sum(x*x for x in v));return None if n<1e-12 else [round(x/n,12) for x in v]
def schwarzschild_amp(r,mass=1):return mass/(r**3)
def ell0_gate(symbols):return 'SEPARABLE_EXACT_PATTERN_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_NONSEPARABLE_MAP'
def evaluate():
 f1=response(1,[1,2,3],[1,1,1],I);f2=response(2,[4,5],[1,3],I);s1=response(1,[schwarzschild_amp(r) for r in [2,3]],[1,1],S);s2=response(3,[schwarzschild_amp(r) for r in [4,5]],[2,1],S)
 return {'study_id':'exact-window-separability-v1','flrw':{'projective_window_a':project(f1),'projective_window_b':project(f2),'decision':'SEPARABLE_ISOTROPIC_RAY'},'schwarzschild_radial':{'projective_window_a':project(s1),'projective_window_b':project(s2),'decision':'SEPARABLE_PRINCIPAL_RAY'},'zero_average_projective':project(response(1,[1,-1],[1,1],I)),'ell0_gate':ell0_gate(['ell','window','curvature']),'status':'EXACT_PATTERN_WINDOW_AVERAGING_REMAINS_PROJECTIVELY_RADIAL','classification':'EXACT_PATTERN_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Symmetry-reduced scalar windows in fixed comoving/principal frames only; not arbitrary spacetime windows, transport, boundaries, or observations.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Exact window artifact differs',file=sys.stderr);return 1
  print('Exact window artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
