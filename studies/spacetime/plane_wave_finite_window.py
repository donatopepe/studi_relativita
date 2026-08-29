#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('plane-wave-finite-window-results.json')
def profile(u,mode):
 if mode=='fixed':a=1+.15*u;theta=.23
 elif mode=='odd':a=1;theta=1.1*u
 elif mode=='asymmetric':a=1+.15*u;theta=.31+1.1*u+.28*u*u
 else:raise ValueError(mode)
 c=math.cos(2*theta);s=math.sin(2*theta);return [[a*c,a*s],[a*s,-a*c]]
def trace(a):return a[0][0]+a[1][1]
def add(a,b,c=1):return [[a[i][j]+c*b[i][j] for j in range(2)] for i in range(2)]
def scale(a,c):return [[c*x for x in r] for r in a]
def norm(a):return math.sqrt(sum(x*x for r in a for x in r))
def project(a):
 n=norm(a);return None if n<1e-14 else scale(a,1/n)
def projective_distance(a,b):
 x=project(a);y=project(b)
 if x is None or y is None:return float('inf')
 d1=norm(add(x,y,-1));d2=norm(add(x,y,1));return min(d1,d2)
def weight(x,L,kernel):
 if kernel=='top_hat':return 1.
 if kernel=='triangular':return max(0.,1-2*abs(x)/L)
 raise ValueError(kernel)
def window(L,mode,center=0.,kernel='top_hat',n=4000):
 h=L/n;out=[[0.,0.],[0.,0.]]
 for i in range(n+1):
  x=-L/2+i*h;w=weight(x,L,kernel)*(0.5 if i in (0,n) else 1);out=add(out,profile(center+x,mode),w*h)
 return out
def ell0_gate(symbols):return 'EXACT_PLANE_WAVE_NONRADIALITY_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_INDEPENDENT_PHYSICAL_MAP'
def matrix(a):return [[round(x,12) for x in r] for r in a]
def evaluate():
 fixed=[window(x,'fixed') for x in (.4,1.1)];odd=[window(x,'odd') for x in (.4,1.1)];asym=[window(x,'asymmetric') for x in (.4,1.1)]
 return {'study_id':'exact-plane-wave-finite-window-v1','geometry':'EXACT_VACUUM_BRINKMANN_PLANE_WAVE_DECLARED_PROFILE','source':'ColeyMcNuttMilson2012 DOI 10.1088/0264-9381/29/23/235023 arXiv:1210.0746','fixed_polarization':{'windows':[matrix(x) for x in fixed],'projective_distance':projective_distance(*fixed)},'centered_odd_rotation':{'windows':[matrix(x) for x in odd],'projective_distance':projective_distance(*odd)},'asymmetric_rotation':{'windows':[matrix(x) for x in asym],'projective_distance':projective_distance(*asym)},'center_shift_distance':projective_distance(window(.9,'odd'),window(.9,'odd',center=.25)),'kernel_distance':projective_distance(window(1.,'asymmetric'),window(1.,'asymmetric',kernel='triangular')),'transport_gate':'BRINKMANN_PARALLEL_SCREEN_DECLARED','window_gate':'CENTER_AND_KERNEL_MOVE_PROJECTIVE_DIRECTION','ell0_gate':ell0_gate(['L','omega','phase','center','kernel']),'status':'EXACT_PLANE_WAVE_FINITE_WINDOW_NONRADIAL_GEOMETRY_PROTOCOL_NOT_ELL0','classification':'EXACT_SPACETIME_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Declared exact vacuum plane-wave profile and numerical quadrature; profile/window scales are geometry and protocol, not ell0 or UMCH evidence.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Plane-wave window artifact differs',file=sys.stderr);return 1
  print('Plane-wave window artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
