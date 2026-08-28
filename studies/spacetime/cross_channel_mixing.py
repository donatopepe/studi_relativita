#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('cross-channel-mixing-results.json')
def response(x):
 if x<=0:raise ValueError('x must be positive')
 return [x,x*x]
def mv(a,v):return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv(a):
 d=det(a)
 if d==0:raise ValueError('mixing matrix must be invertible')
 return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def collision_matrix(x,z):
 if x<=0 or z<=0:raise ValueError('candidates must be positive')
 return [[z/x,0],[0,(z/x)**2]]
def projective_recover(y):
 if y[0]==0:raise ValueError('first channel must be nonzero')
 return y[1]/y[0]
def ell0_gate(symbols):return 'MIXING_QUOTIENT_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_FIXED_PHYSICAL_MIXING_MAP'
def evaluate():
 collisions=[]
 for x,z in [(1,2),(2,5),(.5,3)]:
  M=collision_matrix(x,z);collisions.append({'source_x':x,'target_z':z,'matrix':M,'determinant':det(M),'observed':mv(M,response(x)),'target_response':response(z)})
 return {'study_id':'cross-channel-mixing-v1','latent_map':'r(x)=(x,x^2), x>0','latent_gate':'PROJECTIVE_RATIO_RECOVERS_X_WHEN_BASIS_FIXED','collisions':collisions,'known_mixing_gate':'KNOWN_INVERTIBLE_MIXING_REVERSIBLE','free_mixing_gate':'UNKNOWN_DIAGONAL_SUBGROUP_ALREADY_CREATES_ALL_POSITIVE_COLLISIONS','ell0_gate':ell0_gate(['x','M']),'status':'CROSS_CHANNEL_INJECTIVITY_DESTROYED_BY_FREE_MIXING_GROUP','classification':'TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Synthetic dimensionless map; no channel-native units, physical leakage, spacetime transport, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Cross-channel mixing artifact differs',file=sys.stderr);return 1
  print('Cross-channel mixing artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
