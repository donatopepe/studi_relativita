#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('sphere-transport-mixture-results.json')
def holonomy_angle(K,area):return K*area
def mixed_eigenvalues(l1,l2,alpha):
 c=.5*(l1+l2);d=.5*abs(l1-l2)*abs(math.cos(alpha));return (c-d,c+d)
def ell0_gate(symbols):return 'SPHERE_TRANSPORT_MIXTURE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_DERIVED_PATH_AND_SCALE_LAW'
def evaluate():
 cases=[]
 for a in [0,math.pi/4,math.pi/2,math.pi-.3,.3]:cases.append({'area_unit_sphere':a,'holonomy_angle':holonomy_angle(1,a),'mixed_eigenvalues':mixed_eigenvalues(3,1,a)})
 return {'study_id':'sphere-transport-mixture-v1','geometry':'unit two-sphere','known_relation':'alpha=integral K dA = area modulo 2pi for constant K=1','operator':'D=diag(3,1)','mixture':'(D+Q(alpha) D Q(alpha)^T)/2','eigenvalue_formula':'2 +- |cos(alpha)|','cases':cases,'isotropy_gate':'ALPHA_EQUALS_PI_OVER_TWO_MOD_PI','alias_gate':'MIXTURE_SPECTRUM_EVEN_AND_PI_PERIODIC_IN_HOLONOMY_ANGLE','path_gate':'SPECTRAL_SHAPE_DEPENDS_ON_ENCLOSED_PATH_AREA','ell0_gate':ell0_gate(['K','area']),'status':'SPHERE_HOLONOMY_MIXTURE_SPECTRAL_SHAPE_PATH_AREA_NOT_ELL0','classification':'KNOWN_RESULT_PLUS_PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact two-sphere tangent geometry with equal two-path mixture; not four-dimensional spacetime, physical path measure, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Sphere transport-mixture artifact differs',file=sys.stderr);return 1
  print('Sphere transport-mixture artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
