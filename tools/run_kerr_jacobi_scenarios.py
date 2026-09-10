#!/usr/bin/env python3
"""Run total or granular Kerr Jacobi scenario matrix with JSON evidence."""
from __future__ import annotations
import argparse,importlib.util,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'studies/spacetime/kerr-jacobi-scenarios.json'
MODULE=ROOT/'studies/spacetime/kerr_jacobi_tidal_gate.py'
SPEC=importlib.util.spec_from_file_location('kerr_jacobi_scenario_engine',MODULE);engine=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(engine)
SOURCE_MODULE=ROOT/'studies/spacetime/kerr_finite_source_analyzer.py'
SOURCE_SPEC=importlib.util.spec_from_file_location('kerr_source_analyzer_scenario_engine',SOURCE_MODULE);source=importlib.util.module_from_spec(SOURCE_SPEC);SOURCE_SPEC.loader.exec_module(source)
RECEIVER_MODULE=ROOT/'studies/spacetime/kerr_receiver_likelihood.py'
RECEIVER_SPEC=importlib.util.spec_from_file_location('kerr_receiver_scenario_engine',RECEIVER_MODULE);receiver=importlib.util.module_from_spec(RECEIVER_SPEC);RECEIVER_SPEC.loader.exec_module(receiver)
COMMON_MODULE=ROOT/'studies/spacetime/kerr_common_calibration.py'
COMMON_SPEC=importlib.util.spec_from_file_location('kerr_common_calibration_scenario_engine',COMMON_MODULE);common=importlib.util.module_from_spec(COMMON_SPEC);COMMON_SPEC.loader.exec_module(common)
def phase_conformance(case):
 p=engine.phase_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation'])
 residual=p['symplectic_residual'];return residual<3e-7,residual,3e-7
def schwarzschild_conformance(case):
 c=engine.schwarzschild_conformance(1.,case['rho'],case['R_source_over_M'],case['R_observer_over_M']);r=max(c.values());return r<3e-6,r,3e-6
def scale_conformance(case):
 c=engine.scale_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation'],case['scale_factor']);r=c['converted_phase_map_residual'];return r<3e-6,r,3e-6
def reversal_conformance(case):
 c=engine.reversal_composition_control(1.,case['chi'],case['rho'],case['R_source_over_M'],case['R_observer_over_M'],case['orientation']);r=max(c.values());return r<3e-6,r,3e-6
def source_covariance_domain(case):return source.scenario_control('source_covariance_domain',case)
def covariance_conformance(case):return source.scenario_control('covariance_conformance',case)
def width_homogeneity(case):return source.scenario_control('width_homogeneity',case)
def source_orientation_survival(case):return source.scenario_control('orientation_survival',case)
def analyzer_extrema(case):return source.scenario_control('analyzer_extrema',case)
def analyzer_collision(case):return source.scenario_control('analyzer_collision',case)
def source_analyzer_scale(case):return source.scenario_control('scale',case)
def receiver_control(case):return receiver.scenario_control(case['handler'],case)
def common_control(case):return common.scenario_control(case['handler'],case)
HANDLERS={'phase_conformance':phase_conformance,'schwarzschild_conformance':schwarzschild_conformance,'scale_conformance':scale_conformance,'reversal_conformance':reversal_conformance,'source_covariance_domain':source_covariance_domain,'covariance_conformance':covariance_conformance,'width_homogeneity':width_homogeneity,'source_orientation_survival':source_orientation_survival,'analyzer_extrema':analyzer_extrema,'analyzer_collision':analyzer_collision,'source_analyzer_scale':source_analyzer_scale,**{name:receiver_control for name in ('receiver_covariance','likelihood_normalization','KL_conformance','noise_monotonicity','expected_LLR','receiver_basis','calibration_collision','receiver_scale')},**{name:common_control for name in ('common_identity','bounded_domain','bounded_minimum','refinement','boundary','attenuation','unbounded_noise','common_scale')}}
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
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=('total','granular'),required=True);p.add_argument('--scenario');p.add_argument('--category',choices=('conformance','orientation','scale','preparation','analyzer','receiver','likelihood','noise','calibration','robustness','asymptotic'));p.add_argument('--report-json');a=p.parse_args(argv);data=json.loads(MANIFEST.read_text(encoding='utf-8'));cases=data['scenarios']
 if a.mode=='granular':
  if bool(a.scenario)==bool(a.category):p.error('granular mode requires exactly one --scenario or --category')
  cases=[x for x in cases if x['id']==a.scenario] if a.scenario else [x for x in cases if x['category']==a.category]
  if not cases:p.error('selection matched no scenarios')
 elif a.scenario or a.category:p.error('total mode does not accept granular selectors')
 payload=run(cases);text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
 if a.report_json:pathlib.Path(a.report_json).write_text(text,encoding='utf-8')
 sys.stdout.write(text);return 0 if payload['summary']['FAIL']==payload['summary']['BLOCKED']==0 else 1
if __name__=='__main__':raise SystemExit(main())
