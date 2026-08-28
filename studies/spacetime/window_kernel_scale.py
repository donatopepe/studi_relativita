#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('window-kernel-scale-results.json')
def response(ell,kappa):
 if ell<=0 or kappa<=0:raise ValueError('ell and kappa must be positive')
 return [[1,0],[0,kappa*kappa*ell*ell/3]]
def crossing(kappa):
 if kappa<=0:raise ValueError('kappa must be positive')
 return math.sqrt(3)/kappa
def kappa_for_crossing(ell_target):
 if ell_target<=0:raise ValueError('target must be positive')
 return math.sqrt(3)/ell_target
def physical_half_width(ell,kappa):return ell*kappa
def ell0_gate(symbols):return 'KERNEL_SCALE_CONVENTION_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_FIXED_COVARIANT_KERNEL_LAW'
def evaluate():
 cases=[]
 for k in [.5,1,4]:
  x=crossing(k);cases.append({'kappa':k,'reported_crossing':x,'physical_half_width':physical_half_width(x,k),'operator_at_crossing':response(x,k)})
 targets=[]
 for x in [.5,2,5]:targets.append({'target':x,'required_kappa':kappa_for_crossing(x),'recovered':crossing(kappa_for_crossing(x))})
 return {'study_id':'window-kernel-scale-v1','profile':'K(s)=diag(1,s^2)','window':'normalized top-hat [-kappa ell,kappa ell]','average':'diag(1,kappa^2 ell^2/3)','cases':cases,'movable_targets':targets,'reparameterization_gate':'PHYSICAL_HALF_WIDTH_CROSSING_FIXED_REPORTED_ELL_CONVENTIONAL','ell0_gate':ell0_gate(['ell','kappa']),'status':'FINITE_WINDOW_SPECTRAL_LANDMARK_KERNEL_DILATION_MOVABLE_NOT_ELL0','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Synthetic 1D operator profile and top-hat kernel; no covariant spacetime region, transport, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Window kernel-scale artifact differs',file=sys.stderr);return 1
  print('Window kernel-scale artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
