#!/usr/bin/env python3
import argparse,json,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;I=H/'vacuum-frame-cases.json';O=H/'vacuum-frame-results.json'
def resolve(unique_tmunu,anchor,transport,paths_fixed,unique,covered):
 if unique_tmunu:return 'MATTER_FRAME_RESOLVED','UNIQUE_TIMELIKE_TMUNU_EIGENVECTOR'
 if not anchor:return 'FRAME_UNRESOLVED','MISSING_COSMOLOGICAL_ANCHOR'
 if not transport:return 'FRAME_UNRESOLVED','MISSING_TRANSPORT_RULE'
 if not paths_fixed:return 'FRAME_UNRESOLVED','PATH_FAMILY_NOT_PREREGISTERED'
 if not unique:return 'FRAME_UNRESOLVED','CONTINUATION_NONUNIQUE'
 if not covered:return 'FRAME_UNRESOLVED','TARGET_NOT_COVERED'
 return 'CMB_CONTINUATION_RESOLVED','PREREGISTERED_UNIQUE_CONTINUATION'
def evaluate(d):
 r=[]
 for c in d['cases']:
  status,reason=resolve(**{k:v for k,v in c.items() if k!='name'});r.append({'name':c['name'],'status':status,'reason':reason,'confirmatory':False})
 return {'study_id':d['study_id'],'cases':r,'ell0_status':'NON_IDENTIFIABLE','conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Resolution is necessary, not sufficient. Certified vacuum case is a protocol fixture, not a physical derivation.'}
def render(d):return json.dumps(evaluate(d),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render(json.loads(I.read_text()))
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Vacuum frame results differ',file=sys.stderr);return 1
  print('Vacuum frame results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
