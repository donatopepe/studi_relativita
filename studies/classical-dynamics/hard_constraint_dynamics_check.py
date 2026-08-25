#!/usr/bin/env python3
"""Smooth-branch and transition audit for fixed normalized hard constraint."""

from __future__ import annotations
import argparse, json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent
DEFAULT_INPUT=HERE/'hard-constraint-dynamics-cases.json'
DEFAULT_OUTPUT=HERE/'hard-constraint-dynamics-results.json'
TOL=1e-12

def classify(kappa,kappa0,multiplier):
    kappa,kappa0,multiplier=map(float,(kappa,kappa0,multiplier))
    if kappa0<=0 or multiplier<0: raise ValueError('positive kappa0 and nonnegative multiplier required')
    g=1-kappa/kappa0; residual=multiplier*g
    if g>TOL or abs(residual)>TOL: state='KKT_INFEASIBLE'
    elif abs(g)<=TOL: state='ACTIVE_BOUNDARY_BRANCH'
    else: state='INACTIVE_FREE_BRANCH'
    return {'g':g,'complementarity_residual':residual,'classification':state}

def effective_lagrangian_coefficients(multiplier,kappa0):
    multiplier,kappa0=float(multiplier),float(kappa0)
    if multiplier<0 or kappa0<=0: raise ValueError
    # L/(mc)=-1+lambda-(lambda/kappa0) kappa
    return {'constant_mc_coefficient':-1+multiplier,'kappa_mc_length_coefficient':-multiplier/kappa0,'L_kappakappa':0.0,'classification':'LINEAR_CURVATURE_DEGENERATE_SECTOR'}

def transition_audit(lambda_left,lambda_right,lambda_prime_left,lambda_prime_right):
    values=list(map(float,(lambda_left,lambda_right,lambda_prime_left,lambda_prime_right)))
    jump=values[1]-values[0]; derivative_jump=values[3]-values[2]
    state='NO_MULTIPLIER_JUMP_DETECTED' if abs(jump)<=TOL and abs(derivative_jump)<=TOL else 'DISTRIBUTIONAL_MATCHING_REQUIRED'
    return {'lambda_jump':jump,'lambda_prime_jump':derivative_jump,'classification':state,'matching_rule_derived':False}

def evaluate(data):
    return {'study_id':data['study_id'],'source_formula_ids':data['source_formula_ids'],'derived_scope':'SMOOTH_BRANCHES_ONLY','branches':[{**x,**classify(x['kappa'],x['kappa0'],x['multiplier'])} for x in data['branch_cases']], 'active_effective_lagrangian':effective_lagrangian_coefficients(.5,1), 'transitions':[{**x,**transition_audit(x['lambda_left'],x['lambda_right'],x['lambda_prime_left'],x['lambda_prime_right'])} for x in data['transition_cases']], 'global_well_posedness_derived':False,'warning':'Smooth interval specialization does not derive active-set matching, global existence, uniqueness, stability, or observability.'}
def render(data): return json.dumps(evaluate(data),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser(); p.add_argument('--input',type=pathlib.Path,default=DEFAULT_INPUT); p.add_argument('--output',type=pathlib.Path,default=DEFAULT_OUTPUT); p.add_argument('--check',action='store_true'); a=p.parse_args(); expected=render(json.loads(a.input.read_text()))
 if a.check:
  if not a.output.exists() or a.output.read_text()!=expected: print('Hard dynamics result differs',file=sys.stderr); return 1
  print('Hard-constraint dynamics result is current.'); return 0
 a.output.write_text(expected); print(f'Wrote {a.output}'); return 0
if __name__=='__main__': raise SystemExit(main())
