#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'ell0-turnover-results.json'
def response(ell,A,ell0,p,q):
 x=float(ell)/float(ell0)
 if x<1 or min(A,ell0,p,q)<=0:raise ValueError('requires ell>=ell0 and positive parameters')
 return float(A)*x**float(p)*math.exp(-float(q)*(x-1))
def infer(ell1,y1,ell2,y2,p,q):
 if min(ell1,ell2,y1,y2,p,q)<=0 or ell1==ell2:raise ValueError('positive distinct scales/responses required')
 den=float(p)*math.log(float(ell1)/float(ell2))-math.log(float(y1)/float(y2))
 if den==0:raise ValueError('singular inversion')
 out=float(q)*(float(ell1)-float(ell2))/den
 if out<=0 or min(ell1,ell2)<out:raise ValueError('inconsistent ell0/domain')
 return out
def peak(ell0,p,q):return float(p)*float(ell0)/float(q)
def gate(shape_fixed,turnover_covered,frame_resolved):
 if not frame_resolved:return 'FRAME_UNRESOLVED'
 if not shape_fixed:return 'NON_IDENTIFIABLE_IF_SHAPE_FREE'
 if not turnover_covered:return 'PRACTICALLY_UNRESOLVED_NO_TURNOVER_COVERAGE'
 return 'IDENTIFIABLE_IN_PRINCIPLE'
def evaluate():
 A,e0,p,q=.3,2.,3.,1.;e1,e2=2.5,5.;y1=response(e1,A,e0,p,q);y2=response(e2,A,e0,p,q)
 return {'study_id':'ell0-turnover-identifiability-v1','family':'F_T=A*x^p*exp[-q*(x-1)]','fixed_shape':{'p':p,'q':q},'synthetic_control':{'ell':[e1,e2],'response':[y1,y2],'true_ell0':e0,'recovered_ell0':infer(e1,y1,e2,y2,p,q),'ell_peak':peak(e0,p,q)},'gates':{'fixed_shape_covered_resolved':gate(True,True,True),'free_shape':gate(False,True,True),'no_coverage':gate(True,False,True),'unresolved_frame':gate(True,True,False)},'status':'MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY','conclusion':'NO_POSITIVE_DETECTION_CLAIM','warning':'Synthetic algebra control only. F_T lacks independent physical derivation and is not adopted as UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('Turnover results differ',file=sys.stderr);return 1
  print('ell0 turnover results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
