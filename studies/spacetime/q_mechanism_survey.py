#!/usr/bin/env python3
import argparse,json,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'q-mechanism-results.json'
def evaluate():
 return {'study_id':'independent-q-mechanism-survey-v1','classes':[{'name':'massive_propagation','independent_input':'mass m','matching':'q=m*ell0 in natural units','decision':'SECOND_SCALE_DEGENERACY_UNLESS_INDEPENDENTLY_FIXED'},{'name':'infinite_derivative_form_factor','independent_input':'action form factor and nonlocal scale M_s','matching':'q depends on M_s*ell0 and profile mapping','decision':'MODEL_DEPENDENT_NOT_RADIAL_EXPONENTIAL_BY_DEFAULT'},{'name':'covariant_curvature_form_factor','independent_input':'operator spectrum state boundary conditions masses','matching':'no universal scalar q','decision':'CONTEXT_DEPENDENT_NO_UNIVERSAL_Q'}],'status':'NO_MODEL_INDEPENDENT_Q_DERIVATION_FOUND','gate':'EXTERNAL_EVIDENCE_REQUIRED','conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Canonical classes show possible mechanisms but do not derive UMCH F_T or fixed q. No mechanism adopted.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('q mechanism results differ',file=sys.stderr);return 1
  print('q mechanism survey is current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
