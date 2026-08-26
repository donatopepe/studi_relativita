#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;DI=HERE/'operational-protocol-cases.json';DO=HERE/'operational-protocol-results.json'
def frame(has_unique_tmunu,has_unique_cmb_continuation):
 if has_unique_tmunu:return 'MATTER_FRAME_RESOLVED'
 if has_unique_cmb_continuation:return 'CMB_CONTINUATION_RESOLVED'
 return 'FRAME_UNRESOLVED'
def identifiability(frame_status,protocol_fixed,norm_family_fixed,likelihood_exists,nuisance_bounded):
 return 'IDENTIFIABLE_IN_PRINCIPLE' if frame_status!='FRAME_UNRESOLVED' and all([protocol_fixed,norm_family_fixed,likelihood_exists,nuisance_bounded]) else 'NON_IDENTIFIABLE'
def responses(curvature_scale,ell,clock_fraction,null_shear,congruence_residual):
 c=float(curvature_scale);l=float(ell)
 if l<=0:raise ValueError
 # Leading finite-loop holonomy proxy ||R Sigma|| with preregistered area ell^2.
 hol=abs(c)*l*l;raw=[0.,0.,hol,abs(float(clock_fraction)),abs(float(null_shear)),abs(float(congruence_residual))]
 return {'raw_vector':raw,'R_tidal':0.,'R_mag':0.,'R_hol':hol,'R_clock':raw[3],'R_null':raw[4],'R_cong':raw[5],'C_2':math.sqrt(sum(x*x for x in raw)),'C_infinity':max(raw),'approximation':'leading small-loop holonomy proxy; direct normalized residuals for other toy channels'}
def evaluate(d):
 cases=[{'name':c['name'],**responses(**{k:v for k,v in c.items() if k!='name'})} for c in d['cases']];i=d['identifiability_inputs'];status=identifiability(**i)
 return {'study_id':d['study_id'],'cases':cases,'frame_examples':{'matter':frame(True,False),'vacuum_unique':frame(False,True),'vacuum_ambiguous':frame(False,False)},'ell0_identifiability':status,'conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Toy protocols validate normalization/gates only; no real data, ell0 inference, or positive floor.'}
def render(d):return json.dumps(evaluate(d),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,default=DI);p.add_argument('--output',type=pathlib.Path,default=DO);p.add_argument('--check',action='store_true');a=p.parse_args();e=render(json.loads(a.input.read_text()))
 if a.check:
  if not a.output.exists() or a.output.read_text()!=e:print('Operational protocols differ',file=sys.stderr);return 1
  print('Operational protocols are current.');return 0
 a.output.write_text(e);print(f'Wrote {a.output}');return 0
if __name__=='__main__':raise SystemExit(main())
