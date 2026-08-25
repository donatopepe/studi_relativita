#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent; DEFAULT_INPUT=HERE/'hard-constraint-gate-cases.json'; DEFAULT_OUTPUT=HERE/'hard-constraint-gate-results.json'
def geodesic_intersection(kappa0): return 'GEODESICS_INCLUDED_AT_LIMIT_SET' if float(kappa0)==0 else 'EMPTY_INTERSECTION'
def limit_path(name,kappa0,kappa=1):
 k0=float(kappa0); k=float(kappa)
 if name=='fixed-positive-curvature': return {'classification':'EVENTUALLY_FEASIBLE' if k>=k0 else 'INFEASIBLE'}
 if name=='geodesic': return {'classification':'INFEASIBLE_FOR_EVERY_POSITIVE_KAPPA0' if k0>0 else 'FEASIBLE_AT_ZERO'}
 if name=='active-boundary': return {'classification':'MULTIPLIER_COEFFICIENT_SINGULAR_UNLESS_LAMBDA_SCALES','lambda_over_kappa0':'diverges for fixed nonzero lambda'}
 raise ValueError(name)
def evaluate(d):
 failed=[k for k,v in d['required_checks'].items() if v.startswith('FAIL')]
 return {'study_id':d['study_id'],'required_checks':d['required_checks'],'failed_required_checks':failed,'candidate_a_state':'CONTRADICTED_UNDER_ASSUMPTIONS','candidate_b_state':d['candidate_b_prior_state'],'combined_result':'CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B','paper_iii_gate':'BLOCKED','all_umch_falsified':False,'paths':[limit_path('fixed-positive-curvature',1e-6),limit_path('geodesic',1e-6),limit_path('active-boundary',1e-6)],'decision_basis':'Fixed A lacks transition rules/global well-posedness, excludes geodesic data for every positive kappa0, has singular normalized multiplier coefficient unless scaled, and lacks observable mapping.','warning':'Conditional result covers only fixed A and fixed B under timelike pointwise definition.'}
def render(d): return json.dumps(evaluate(d),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,default=DEFAULT_INPUT);p.add_argument('--output',type=pathlib.Path,default=DEFAULT_OUTPUT);p.add_argument('--check',action='store_true');a=p.parse_args();e=render(json.loads(a.input.read_text()))
 if a.check:
  if not a.output.exists() or a.output.read_text()!=e: print('Hard gate differs',file=sys.stderr);return 1
  print('Hard-constraint gate decision is current.');return 0
 a.output.write_text(e);print(f'Wrote {a.output}');return 0
if __name__=='__main__':raise SystemExit(main())
