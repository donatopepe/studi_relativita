#!/usr/bin/env python3
import argparse,json,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'turnover-shape-results.json'
AREA={'tidal','magnetic','holonomy'};OTHER={'clock','null','congruence'}
def exponent(channel,protocol_fixed,regular):
 if channel not in AREA|OTHER:raise ValueError(channel)
 if not regular:return None,'REGULAR_EXPANSION_UNAVAILABLE'
 if not protocol_fixed:return None,'PROTOCOL_GEOMETRY_REQUIRED'
 if channel in AREA:return 2,'DERIVED_REGULAR_SMALL_REGION_ONLY'
 return 2,'CONDITIONAL_FIXED_SHORT_BASELINE_PROTOCOL_ONLY'
def q_gate(mechanism):return 'NOT_DERIVED_FROM_CURRENT_GEOMETRIC_CORE' if mechanism is None else 'INDEPENDENT_MECHANISM_REQUIRED_AND_UNVALIDATED'
def evaluate():
 channels={c:{'p':exponent(c,True,True)[0],'status':exponent(c,True,True)[1]} for c in sorted(AREA|OTHER)}
 return {'study_id':'turnover-shape-derivation-gate-v1','channels':channels,'q_status':q_gate(None),'turnover_status':'BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM','conclusion':'NO_POSITIVE_DETECTION_CLAIM','scope':'p=2 follows only for declared regular small-region/short-baseline protocols; no universal channel law. Exponential q requires new independently justified mechanism.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Turnover shape results differ',file=sys.stderr);return 1
  print('Turnover shape results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
