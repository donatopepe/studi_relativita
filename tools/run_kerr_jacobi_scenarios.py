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
PROFILE_MODULE=ROOT/'studies/spacetime/kerr_composite_calibration.py'
PROFILE_SPEC=importlib.util.spec_from_file_location('kerr_composite_calibration_scenario_engine',PROFILE_MODULE);profile=importlib.util.module_from_spec(PROFILE_SPEC);PROFILE_SPEC.loader.exec_module(profile)
CALCHANNEL_MODULE=ROOT/'studies/spacetime/kerr_calibration_channel.py'
CALCHANNEL_SPEC=importlib.util.spec_from_file_location('kerr_calibration_channel_scenario_engine',CALCHANNEL_MODULE);calchannel=importlib.util.module_from_spec(CALCHANNEL_SPEC);CALCHANNEL_SPEC.loader.exec_module(calchannel)
REFERENCE_MODULE=ROOT/'studies/spacetime/kerr_calibration_reference_correction.py'
REFERENCE_SPEC=importlib.util.spec_from_file_location('kerr_calibration_reference_correction_scenario_engine',REFERENCE_MODULE);reference=importlib.util.module_from_spec(REFERENCE_SPEC);REFERENCE_SPEC.loader.exec_module(reference)
DRIFT_MODULE=ROOT/'studies/spacetime/kerr_reference_drift.py'
DRIFT_SPEC=importlib.util.spec_from_file_location('kerr_reference_drift_scenario_engine',DRIFT_MODULE);drift=importlib.util.module_from_spec(DRIFT_SPEC);DRIFT_SPEC.loader.exec_module(drift)
MISMATCH_MODULE=ROOT/'studies/spacetime/kerr_correlated_noise_mismatch.py'
MISMATCH_SPEC=importlib.util.spec_from_file_location('kerr_correlated_noise_mismatch_scenario_engine',MISMATCH_MODULE);mismatch=importlib.util.module_from_spec(MISMATCH_SPEC);MISMATCH_SPEC.loader.exec_module(mismatch)
SAMPLE_MODULE=ROOT/'studies/spacetime/kerr_finite_sample_covariance.py'
SAMPLE_SPEC=importlib.util.spec_from_file_location('kerr_finite_sample_covariance_scenario_engine',SAMPLE_MODULE);sample=importlib.util.module_from_spec(SAMPLE_SPEC);SAMPLE_SPEC.loader.exec_module(sample)
MEAN_MODULE=ROOT/'studies/spacetime/kerr_estimated_mean_covariance.py'
MEAN_SPEC=importlib.util.spec_from_file_location('kerr_estimated_mean_covariance_scenario_engine',MEAN_MODULE);mean=importlib.util.module_from_spec(MEAN_SPEC);MEAN_SPEC.loader.exec_module(mean)
AR1_MODULE=ROOT/'studies/spacetime/kerr_ar1_temporal_dependence.py'
AR1_SPEC=importlib.util.spec_from_file_location('kerr_ar1_temporal_dependence_scenario_engine',AR1_MODULE);ar1=importlib.util.module_from_spec(AR1_SPEC);AR1_SPEC.loader.exec_module(ar1)
PAIRED_MODULE=ROOT/'studies/spacetime/kerr_paired_stream_common_noise.py'
PAIRED_SPEC=importlib.util.spec_from_file_location('kerr_paired_stream_scenario_engine',PAIRED_MODULE);paired=importlib.util.module_from_spec(PAIRED_SPEC);PAIRED_SPEC.loader.exec_module(paired)
LAG_MODULE=ROOT/'studies/spacetime/kerr_bounded_pairing_lag.py'
LAG_SPEC=importlib.util.spec_from_file_location('kerr_pairing_lag_scenario_engine',LAG_MODULE);lag=importlib.util.module_from_spec(LAG_SPEC);LAG_SPEC.loader.exec_module(lag)
JITTER_MODULE=ROOT/'studies/spacetime/kerr_bounded_pairing_jitter.py'
JITTER_SPEC=importlib.util.spec_from_file_location('kerr_pairing_jitter_scenario_engine',JITTER_MODULE);jitter=importlib.util.module_from_spec(JITTER_SPEC);JITTER_SPEC.loader.exec_module(jitter)
LATENT_MODULE=ROOT/'studies/spacetime/kerr_latent_window_jitter.py'
LATENT_SPEC=importlib.util.spec_from_file_location('kerr_latent_jitter_scenario_engine',LATENT_MODULE);latent=importlib.util.module_from_spec(LATENT_SPEC);LATENT_SPEC.loader.exec_module(latent)
LAGLAW_MODULE=ROOT/'studies/spacetime/kerr_bounded_latent_lag_law.py'
LAGLAW_SPEC=importlib.util.spec_from_file_location('kerr_lag_law_scenario_engine',LAGLAW_MODULE);laglaw=importlib.util.module_from_spec(LAGLAW_SPEC);LAGLAW_SPEC.loader.exec_module(laglaw)
CRITICAL_MODULE=ROOT/'studies/spacetime/kerr_critical_lag_law_radius.py'
CRITICAL_SPEC=importlib.util.spec_from_file_location('kerr_critical_lag_law_scenario_engine',CRITICAL_MODULE);critical=importlib.util.module_from_spec(CRITICAL_SPEC);CRITICAL_SPEC.loader.exec_module(critical)
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
def profile_control(case):return profile.scenario_control(case['handler'],case)
def calibration_channel_control(case):return calchannel.scenario_control(case['handler'],case)
def reference_control(case):return reference.scenario_control(case['handler'],case)
def drift_control(case):return drift.scenario_control(case['handler'],case)
def mismatch_control(case):return mismatch.scenario_control(case['handler'],case)
def sample_control(case):return sample.scenario_control(case['handler'],case)
def mean_control(case):return mean.scenario_control(case['handler'],case)
def ar1_control(case):return ar1.scenario_control(case['handler'],case)
def paired_control(case):return paired.scenario_control(case['handler']),0.,1.
def lag_control(case):return lag.scenario_control(case['handler']),0.,1.
def jitter_control(case):return jitter.scenario_control(case['handler']),0.,1.
def latent_control(case):return latent.scenario_control(case['handler']),0.,1.
def laglaw_control(case):return laglaw.scenario_control(case['handler']),0.,1.
def critical_control(case):return critical.scenario_control(case['handler']),0.,1.
HANDLERS={'phase_conformance':phase_conformance,'schwarzschild_conformance':schwarzschild_conformance,'scale_conformance':scale_conformance,'reversal_conformance':reversal_conformance,'source_covariance_domain':source_covariance_domain,'covariance_conformance':covariance_conformance,'width_homogeneity':width_homogeneity,'source_orientation_survival':source_orientation_survival,'analyzer_extrema':analyzer_extrema,'analyzer_collision':analyzer_collision,'source_analyzer_scale':source_analyzer_scale,**{name:receiver_control for name in ('receiver_covariance','likelihood_normalization','KL_conformance','noise_monotonicity','expected_LLR','receiver_basis','calibration_collision','receiver_scale')},**{name:common_control for name in ('common_identity','bounded_domain','bounded_minimum','refinement','boundary','attenuation','unbounded_noise','common_scale')},**{name:profile_control for name in ('profile_overlap','profile_domain','profile_minimum','profile_refinement','profile_boundary','profile_collision','profile_basis_scale','profile_nonclaims')},**{name:calibration_channel_control for name in ('calibration_joint_map','calibration_domain','calibration_noncollision','calibration_fisher','calibration_precision','calibration_weak_limit','calibration_unknown_reference','calibration_scale')},**{name:reference_control for name in ('reference_criterion','reference_inside','reference_noncollision','reference_outside_collision','reference_fisher','reference_unknown_collision','reference_weak_precision','reference_scale')},**{name:drift_control for name in ('drift_geometry','drift_box','drift_margin','drift_endpoint','drift_outside_collision','drift_fisher','drift_scale','drift_nonclaims')},**{name:mismatch_control for name in ('mismatch_spd','mismatch_cancellation','mismatch_cones','mismatch_threshold','mismatch_safe','mismatch_collision','mismatch_basis_scale','mismatch_nonclaims')},**{name:sample_control for name in ('sample_identity','sample_domain','sample_rms','sample_scaling','sample_safe_count','sample_unsafe','sample_basis_scale','sample_nonclaims')},**{name:mean_control for name in ('mean_identity','mean_domain','mean_penalty','mean_rms','mean_safe_count','mean_unsafe','mean_basis_scale','mean_nonclaims')},**{name:ar1_control for name in ('ar1_domain','ar1_identity','ar1_iid','ar1_rms','ar1_monotonicity','ar1_safe_count','ar1_basis_scale','ar1_nonclaims')},**{name:paired_control for name in ('paired_domain','paired_identity','paired_coefficient','paired_rms','paired_safe_count','paired_zero_shared','paired_basis_scale','paired_nonclaims')},**{name:lag_control for name in ('lag_domain','lag_identity','lag_synchronous','lag_risk','lag_monotonicity','lag_count_transition','lag_basis_scale','lag_nonclaims')},**{name:jitter_control for name in ('jitter_domain','jitter_identity','jitter_zero','jitter_risk','jitter_monotonicity','jitter_count_transition','jitter_basis_scale','jitter_nonclaims')},**{name:latent_control for name in ('latent_domain','latent_identity','latent_zero','latent_jensen','latent_risk','latent_count_contrast','latent_basis_scale','latent_nonclaims')},**{name:laglaw_control for name in ('laglaw_domain','laglaw_extrema','laglaw_uniform','laglaw_envelope','laglaw_widening','laglaw_count_transition','laglaw_basis_scale','laglaw_nonclaims')},**{name:critical_control for name in ('critical_domain','critical_active_set','critical_bracket','critical_root','critical_sides','critical_support','critical_basis_scale','critical_nonclaims')}}
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
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=('total','granular'),required=True);p.add_argument('--scenario');p.add_argument('--category',choices=('conformance','orientation','scale','preparation','analyzer','receiver','likelihood','noise','calibration','robustness','asymptotic','profiling','calibration_channel','reference_placement','reference_drift','calibration_mismatch','finite_sample','estimated_mean','temporal_dependence','cross_stream_dependence','pairing_lag','pairing_jitter','latent_pairing_jitter','latent_lag_law_robustness','latent_lag_critical_radius'));p.add_argument('--report-json');a=p.parse_args(argv);data=json.loads(MANIFEST.read_text(encoding='utf-8'));cases=data['scenarios']
 if a.mode=='granular':
  if bool(a.scenario)==bool(a.category):p.error('granular mode requires exactly one --scenario or --category')
  cases=[x for x in cases if x['id']==a.scenario] if a.scenario else [x for x in cases if x['category']==a.category]
  if not cases:p.error('selection matched no scenarios')
 elif a.scenario or a.category:p.error('total mode does not accept granular selectors')
 payload=run(cases);text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
 if a.report_json:pathlib.Path(a.report_json).write_text(text,encoding='utf-8')
 sys.stdout.write(text);return 0 if payload['summary']['FAIL']==payload['summary']['BLOCKED']==0 else 1
if __name__=='__main__':raise SystemExit(main())
