#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'operator-exact-results.json'
def analyze(eigs):
 e=sorted(float(x) for x in eigs);n=math.sqrt(sum(x*x for x in e));nz=[x for x in e if abs(x)>1e-12];proj=None if n==0 else [x/max(abs(y) for y in e) for x in e]
 return {'eigenvalues':e,'trace':sum(e),'rank':len(nz),'frobenius':n,'projective_spectrum':proj,'distinct_eigenvalues':len({round(x,12) for x in e})}
def compare_scales(a,b):
 pa=analyze(a)['projective_spectrum'];pb=analyze(b)['projective_spectrum']
 return 'PROJECTIVE_UNDEFINED_ZERO' if pa is None or pb is None else ('PROJECTIVE_SCALE_NON_IDENTIFIABLE' if pa==pb else 'PROJECTIVE_SHAPE_CHANGES_IN_TOY')
def evaluate():
 cases=[('MINKOWSKI',[0,0,0],[0,0,0]),('FLRW',[-1,-1,-1],[0,0,0]),('SCHWARZSCHILD',[-2,1,1],[0,0,0]),('VSI_TYPE_N_TOY',[-1,0,1],[-1,0,1])]
 out=[]
 for name,e,b in cases:out.append({'case':name,'electric':analyze(e),'magnetic':analyze(b),'scale_comparison':compare_scales(e,[4*x for x in e])})
 return {'study_id':'operator-native-exact-controls-v1','cases':out,'status':'PROJECTIVE_SCALE_NON_IDENTIFIABLE_IN_CURRENT_EXACT_CONTROLS','conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Fixed-curvature ell^2 controls validate operator spectra and geometry patterns only; no ell0 landmark.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Operator exact results differ',file=sys.stderr);return 1
  print('Operator exact controls are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
