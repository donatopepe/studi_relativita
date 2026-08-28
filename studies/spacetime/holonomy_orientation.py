#!/usr/bin/env python3
import argparse,json,pathlib,sys
O=pathlib.Path(__file__).with_name('holonomy-orientation-results.json')
def observe(matrix,curvature,ell):return [ell*ell*sum(a*b for a,b in zip(row,curvature)) for row in matrix]
def matrix_rank(a,tol=1e-12):
 a=[list(map(float,r)) for r in a];m=len(a);n=len(a[0]) if m else 0;r=0
 for c in range(n):
  p=next((i for i in range(r,m) if abs(a[i][c])>tol),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(m):
   if i!=r:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def rank_gate(matrix,n):return 'SCALED_OPERATOR_TOMOGRAPHY_IDENTIFIABLE' if matrix_rank(matrix)==n else 'OPERATOR_TOMOGRAPHY_NON_IDENTIFIABLE_RANK_DEFICIENT'
def scale_gate(curvature_independently_fixed):return 'KNOWN_ELL_GEOMETRIC_AMPLITUDE_RECOVERABLE' if curvature_independently_fixed else 'ELL_CURVATURE_AMPLITUDE_DEGENERACY'
def evaluate():
 deficient=[[1,0,0],[0,1,0]];full=[[1,0,0],[0,1,0],[0,0,1]]
 return {'study_id':'holonomy-orientation-tomography-v1','rank_deficient':{'rank':matrix_rank(deficient),'gate':rank_gate(deficient,3),'collision':[observe(deficient,[2,3,4],1),observe(deficient,[2,3,9],1)]},'full_rank':{'rank':matrix_rank(full),'gate':rank_gate(full,3),'record':observe(full,[2,3,4],2)},'scale_gate':scale_gate(False),'ell0_gate':'ELL0_NOT_PRESENT_WITHOUT_THEORY_FIXED_LANDMARK','status':'HOLONOMY_TOMOGRAPHY_RANK_CONDITIONAL_ELL0_ABSENT','classification':'PROJECT_DERIVATION_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Leading linearized loop model only; finite-loop path ordering, transport, noise and boundary nuisance excluded.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Holonomy orientation artifact differs',file=sys.stderr);return 1
  print('Holonomy orientation artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
