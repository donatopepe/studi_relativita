#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('sphere-window-pathscale-results.json')
def validate(r,eta):
 if r<=0 or eta<=0:raise ValueError('positive radius and path-shape coefficient required')
def angle(ell,r,eta):
 validate(r,eta)
 if ell<0:raise ValueError('nonnegative scale required')
 return eta*ell*ell/(r*r)
def gap(ell,r,eta,local_gap):
 if local_gap<0:raise ValueError('nonnegative local gap required')
 return local_gap*abs(math.cos(angle(ell,r,eta)))
def first_isotropy(r,eta):validate(r,eta);return r*math.sqrt(math.pi/(2*eta))
def ell0_gate(symbols):return 'CURVATURE_RADIUS_PATH_LANDMARK_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_INDEPENDENT_UNIVERSAL_SCALE_LAW'
def evaluate():
 r=2;cases=[]
 for eta in [.5,1,2]:
  e=first_isotropy(r,eta);cases.append({'eta':eta,'first_isotropy_ell':e,'physical_area_at_isotropy':eta*e*e,'gap_at_isotropy':gap(e,r,eta,2)})
 return {'study_id':'sphere-window-pathscale-v1','geometry':'radius-r two-sphere K=1/r^2','path_area':'A(ell)=eta ell^2','holonomy_angle':'alpha=eta ell^2/r^2','spectral_gap':'Delta |cos(eta ell^2/r^2)|','first_isotropy':'ell_iso=r sqrt(pi/(2 eta))','first_isotropy_area':'A_iso=pi r^2/2','cases':cases,'shape_gate':'ETA_MOVES_REPORTED_ELL_LANDMARK','confounding_gate':'ONLY_ETA_OVER_R_SQUARED_ENTERS_PHASE','branch_gate':'ABSOLUTE_COSINE_MULTIBRANCH_ALIASING','ell0_gate':ell0_gate(['r','eta','ell']),'status':'SPHERE_WINDOW_NONRADIAL_LANDMARK_CURVATURE_RADIUS_PATH_SHAPE_NOT_ELL0','classification':'KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact two-sphere and prescribed area law; no four-dimensional spacetime window, physical path selection, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Sphere window-pathscale artifact differs',file=sys.stderr);return 1
  print('Sphere window-pathscale artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
