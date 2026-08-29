#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('sphere-harmonic-channels-results.json')
def channels(alpha):return (math.cos(alpha),math.cos(2*alpha))
def gap_pair(alpha):return (abs(math.cos(alpha)),math.cos(2*alpha))
def principal_phase(y1):
 if y1 < -1 or y1 > 1:raise ValueError('cosine channel must lie in [-1,1]')
 return math.acos(max(-1,min(1,y1)))
def phase_jacobian_rank(alpha,tol=1e-12):return 1 if math.hypot(math.sin(alpha),2*math.sin(2*alpha))>tol else 0
def scaled_channels(ell,r,eta):
 if min(ell,r,eta)<=0:raise ValueError('positive geometry inputs required')
 return channels(eta*ell*ell/(r*r))
def ell0_gate(symbols):return 'HARMONIC_PHASE_CHANNELS_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_INDEPENDENT_CHANNEL_LAW'
def evaluate():
 cases=[]
 for a in [0,.3,1,math.pi/2,math.pi]:cases.append({'alpha':a,'channels':channels(a),'gap_pair':gap_pair(a),'jacobian_rank':phase_jacobian_rank(a)})
 return {'study_id':'sphere-harmonic-channels-v1','phase':'alpha=eta ell^2/r^2','channels':['y1=cos(alpha)','y2=cos(2alpha)'],'dependence':'y2=2 y1^2-1','cases':cases,'rank_gate':'JOINT_CHANNEL_MAP_ALGEBRAIC_CURVE_RANK_AT_MOST_ONE','global_gate':'SIGN_AND_TWO_PI_PHASE_ALIASING','gap_gate':'ABS_COS_AND_COS2_PI_PERIODIC_REDUNDANCY','geometry_gate':'ONLY_ETA_OVER_R_SQUARED_ENTERS_PHASE','ell0_gate':ell0_gate(['alpha','eta','r']),'status':'SPHERE_CROSS_CHANNEL_HARMONIC_ALGEBRAIC_DEPENDENCE_NOT_ELL0','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Synthetic conjugacy-invariant harmonics of exact sphere holonomy phase; no independent physical channels, calibration, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Sphere harmonic-channel artifact differs',file=sys.stderr);return 1
  print('Sphere harmonic-channel artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
