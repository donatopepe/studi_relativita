#!/usr/bin/env python3
"""Run total or granular Kerr Jacobi scenario matrix with JSON evidence."""
from __future__ import annotations
import argparse,importlib.util,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'studies/spacetime/kerr-jacobi-scenarios.json'
MODULE=ROOT/'studies/spacetime/kerr_jacobi_tidal_gate.py'
SPEC=importlib.util.spec_from_file_location('kerr_jacobi_scenario_engine',MODULE);engine=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(engine)
def phase_conformance(case):
 p=engine.phase_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation'])
 residual=p['symplectic_residual'];return residual<3e-7,residual,3e-7
def schwarzschild_conformance(case):
 c=engine.schwarzschild_conformance(1.,case['rho'],case['R_source_over_M'],case['R_observer_over_M']);r=max(c.values());return r<3e-6,r,3e-6
def scale_conformance(case):
 c=engine.scale_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation'],case['scale_factor']);r=c['converted_phase_map_residual'];return r<3e-6,r,3e-6
def reversal_conformance(case):
 c=engine.reversal_composition_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation']);r=max(c.values());return r<3e-6,r,3e-6
HANDLERS={'phase_conformance':phase_conformance,'schwarzschild_conformance':schwarzschild_conformance,'scale_conformance':scale_conformance,'reversal_conformance':reversal_conformance}
def run(cases):
 results=[]
 for case in cases:
  handler=HANDLERS.get(case.get('handler'))
  if handler is None:results.append({'id':case['id'],'category':case['category'],'status':'BLOCKED','reason':'missing handler'});continue
  try:passed,residual,threshold=handler(case);results.append({'id':case['id'],'category':case['category'],'status':'PASS' if passed else 'FAIL','residual':residual,'threshold':threshold})
  except Exception as error:results.append({'id':case['id'],'category':case['category'],'status':'FAIL','reason':f'{type(error).__name__}: {error}'})
 summary={name:sum(item['status']==name for item in results)for name in ('PASS','FAIL','SKIP','BLOCKED')}
 return {'schema':'kerr-jacobi-scenario-report-v1','results':results,'summary':summary,'coverage':{'selected_ids':[x['id']for x in results],'selected_categories':sorted({x['category']for x in results})}}
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=('total','granular'),required=True);p.add_argument('--scenario');p.add_argument('--category',choices=('conformance','orientation','scale'));p.add_argument('--report-json');a=p.parse_args(argv);data=json.loads(MANIFEST.read_text(encoding='utf-8'));cases=data['scenarios']
 if a.mode=='granular':
  if bool(a.scenario)==bool(a.category):p.error('granular mode requires exactly one --scenario or --category')
  cases=[x for x in cases if x['id']==a.scenario] if a.scenario else [x for x in cases if x['category']==a.category]
  if not cases:p.error('selection matched no scenarios')
 elif a.scenario or a.category:p.error('total mode does not accept granular selectors')
 payload=run(cases);text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
 if a.report_json:pathlib.Path(a.report_json).write_text(text,encoding='utf-8')
 sys.stdout.write(text);return 0 if payload['summary']['FAIL']==payload['summary']['BLOCKED']==0 else 1
if __name__=='__main__':raise SystemExit(main())
