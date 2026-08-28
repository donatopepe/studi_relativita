#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('jacobi-spectrum-results.json')
def eigenvalue(lam,s):
 if lam>0:return math.sin(math.sqrt(lam)*s)/math.sqrt(lam)
 if lam<0:return math.sinh(math.sqrt(-lam)*s)/math.sqrt(-lam)
 return float(s)
def first_caustic(lam):return math.pi/math.sqrt(lam) if lam>0 else None
def phase(lam,s):return math.sqrt(abs(lam))*s
def affine_gate(fixed):return 'AFFINE_NORMALIZATION_FIXED' if fixed else 'AFFINE_OPTICAL_SCALE_DEGENERACY'
def ell0_gate(symbols):return 'GEOMETRIC_FOCUSING_SCALE_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_THEORY_LINK'
def evaluate():
 vals=[4,0,-1];s=1
 return {'study_id':'constant-optical-jacobi-spectrum-v1','channels':[{'optical_eigenvalue':x,'jacobi_eigenvalue_at_s1':eigenvalue(x,s),'first_caustic':first_caustic(x)} for x in vals],'phase_collision':{'phase_lambda4_s3':phase(4,3),'phase_lambda1_s6':phase(1,6)},'affine_gate':affine_gate(False),'ell0_gate':ell0_gate(['affine','optical_eigenvalue','source_boundary_data']),'status':'JACOBI_CAUSTIC_GEOMETRIC_LANDMARK_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Constant diagonal optical-tidal ODE control only; no arbitrary-spacetime Jacobi map, observation, or UMCH scale law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Jacobi spectrum artifact differs',file=sys.stderr);return 1
  print('Jacobi spectrum artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
