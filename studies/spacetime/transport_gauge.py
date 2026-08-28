#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('transport-gauge-results.json')
def rotate_diag(a,b,t):
 c=math.cos(t);s=math.sin(t);return [[a*c*c+b*s*s,(a-b)*c*s],[(a-b)*c*s,a*s*s+b*c*c]]
def flatten(a):return [a[0][0],a[0][1],a[1][0],a[1][1]]
def project(a):
 v=flatten(a);n=math.sqrt(sum(x*x for x in v));return [round(x/n,12) for x in v]
def invariants(a):
 tr=a[0][0]+a[1][1];det=a[0][0]*a[1][1]-a[0][1]*a[1][0];disc=max(0,tr*tr-4*det);e=sorted([(tr-math.sqrt(disc))/2,(tr+math.sqrt(disc))/2]);return {'trace':round(tr,12),'determinant':round(det,12),'eigenvalues':[round(x,12) for x in e],'eigenvalue_ratio':None if abs(e[1])<1e-12 else round(e[0]/e[1],12)}
def compare(a,b):return 'APPARENT_NONRADIALITY_PURE_CONJUGATION' if invariants(a)==invariants(b) else 'SPECTRAL_SHAPE_EVOLUTION_GEOMETRIC_ONLY'
def ell0_gate(symbols):return 'ELL0_ABSENT_AFTER_TRANSPORT_QUOTIENT' if 'ell0' not in symbols else 'ELL0_REQUIRES_THEORY_FIXED_MAP'
def evaluate():
 a=rotate_diag(3,1,0);r=rotate_diag(3,1,.7);s=rotate_diag(4,1,.8)
 return {'study_id':'transport-gauge-quotient-v1','pure_rotation':{'projective_before':project(a),'projective_after':project(r),'invariants_before':invariants(a),'invariants_after':invariants(r),'decision':compare(a,r)},'spectral_change':{'invariants':invariants(s),'decision':compare(a,s)},'degenerate_rotation_blind':rotate_diag(2,2,1.1),'ell0_gate':ell0_gate(['operator','transport','scale']),'status':'TRANSPORT_GAUGE_QUOTIENT_REQUIRED_FOR_NONRADIALITY','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Finite-dimensional orthogonal basis toy only; no covariant spacetime transport, path dependence, calibration or boundary derivation.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Transport gauge artifact differs',file=sys.stderr);return 1
  print('Transport gauge artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
