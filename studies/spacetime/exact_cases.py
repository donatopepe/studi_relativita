#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;DI=HERE/'exact-cases.json';DO=HERE/'exact-case-results.json'
def pack(case,ell,tidal,mag=0,frame_status='FRAME_RESOLVED',status='DEFINITION_TEST_ONLY',**extra):
 raw=[tidal,mag,0.,0.,0.,0.];return {'case':case,'ell':ell,'raw_vector':raw,'R_tidal':tidal,'R_mag':mag,'C_2':math.sqrt(sum(x*x for x in raw)),'C_infinity':max(abs(x) for x in raw),'frame_status':frame_status,'status':status,**extra}
def minkowski(ell): return pack('MINKOWSKI',float(ell),0,status='NULL_CONTROL')
def flrw(ell,addot_over_a,frame):
 ell=float(ell);a=float(addot_over_a);return pack('FLRW',ell,ell**2*math.sqrt(3*a*a),frame_status='FRAME_RESOLVED' if frame else 'FRAME_UNRESOLVED',status='DEFINITION_TEST_ONLY' if frame else 'NOT_CONFIRMATORY',assumption='orthonormal comoving E_ij=-(addot/a)delta_ij; magnetic zero')
def schwarzschild(ell,mu_over_r3,frame):
 ell=float(ell);q=float(mu_over_r3);e=[-2*q,q,q];fs='FRAME_RESOLVED' if frame else 'FRAME_UNRESOLVED';return pack('SCHWARZSCHILD',ell,ell**2*math.sqrt(sum(x*x for x in e)),frame_status=fs,status='DEFINITION_TEST_ONLY' if frame else 'NOT_CONFIRMATORY',tidal_eigenvalues=e,assumption='static orthonormal frame; magnetic zero')
def vsi_wave(ell,wave_amplitude_per_l2,frame):
 ell=float(ell);h=float(wave_amplitude_per_l2);x=ell**2*abs(h);fs='FRAME_RESOLVED' if frame else 'FRAME_UNRESOLVED';return pack('VSI_WAVE',ell,x,x,frame_status=fs,status='DEFINITION_TEST_ONLY' if frame else 'NOT_CONFIRMATORY',polynomial_scalar_invariants_zero=True,assumption='toy type-N equal normalized electric/magnetic amplitudes; not observational model')
def evaluate(d):
 out=[]
 for c in d['cases']:
  k=c['case'];args={x:y for x,y in c.items() if x!='case'};out.append({'MINKOWSKI':minkowski,'FLRW':flrw,'SCHWARZSCHILD':schwarzschild,'VSI_WAVE':vsi_wave}[k](**args))
 return {'study_id':d['study_id'],'normalization':d['normalization'],'cases':out,'warning':'Exact/toy cases validate response behavior only; they do not establish a positive floor in realized universe.'}
def render(d):return json.dumps(evaluate(d),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,default=DI);p.add_argument('--output',type=pathlib.Path,default=DO);p.add_argument('--check',action='store_true');a=p.parse_args();e=render(json.loads(a.input.read_text()))
 if a.check:
  if not a.output.exists() or a.output.read_text()!=e:print('Exact cases differ',file=sys.stderr);return 1
  print('Spacetime exact cases are current.');return 0
 a.output.write_text(e);print(f'Wrote {a.output}');return 0
if __name__=='__main__':raise SystemExit(main())
