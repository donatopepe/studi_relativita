#!/usr/bin/env python3
import argparse,json,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'inference-protocol-results.json'
def domain(scales,ell0):
 if not scales or min(scales)<=0 or ell0<=0:raise ValueError('positive scales and ell0 required')
 return 'DOMAIN_CONSISTENT' if ell0<=min(scales) else 'DOMAIN_INCONSISTENT'
def gate(frame,domain_ok,family_fixed,dependence,likelihood,nuisance,identifiable,replicated):
 if not frame:return 'FRAME_UNRESOLVED'
 if not domain_ok:return 'DOMAIN_INCONSISTENT'
 if not family_fixed:return 'EXPLORATORY_FAMILY_SELECTION'
 if not dependence:return 'DEPENDENCE_UNRESOLVED'
 if not likelihood:return 'LIKELIHOOD_UNRESOLVED'
 if not nuisance:return 'NUISANCE_UNBOUNDED'
 if not identifiable:return 'NON_IDENTIFIABLE'
 if not replicated:return 'REPLICATION_MISSING'
 return 'CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE'
def evaluate():
 base={'frame':True,'domain_ok':True,'family_fixed':True,'dependence':True,'likelihood':True,'nuisance':True,'identifiable':True,'replicated':True}
 cases=[]
 for name,change in [('eligible',{}),('unresolved_frame',{'frame':False}),('bad_domain',{'domain_ok':False}),('exploratory',{'family_fixed':False}),('dependence_missing',{'dependence':False}),('likelihood_missing',{'likelihood':False}),('nuisance_unbounded',{'nuisance':False}),('nonidentifiable',{'identifiable':False}),('unreplicated',{'replicated':False})]:cases.append({'name':name,'status':gate(**{**base,**change})})
 return {'study_id':'inference-protocol-gate-v1','domain_controls':{'consistent':domain([1,2,4],.5),'inconsistent':domain([1,2,4],1.1)},'cases':cases,'conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Gate eligibility is not evidence. No data are analyzed.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Inference protocol results differ',file=sys.stderr);return 1
  print('Inference protocol results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
