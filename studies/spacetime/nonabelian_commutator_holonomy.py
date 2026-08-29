#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
O=pathlib.Path(__file__).with_name('nonabelian-commutator-holonomy-results.json')
def shear_a(a):return [[1.0,float(a)],[0.0,1.0]]
def shear_b(b):return [[1.0,0.0],[float(b),1.0]]
def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def commutator(a,b):return mul(mul(mul(shear_a(a),shear_b(b)),shear_a(-a)),shear_b(-b))
def trace(x):return x[0][0]+x[1][1]
def det(x):return x[0][0]*x[1][1]-x[0][1]*x[1][0]
def scaled_trace(ell,kappa,rho,p,q):
 if ell<=0 or p+q<=0:raise ValueError('positive scale and exponent sum required')
 return 2+(kappa*rho)**2*ell**(2*(p+q))
def threshold(tau,product,p,q):
 if tau<=2 or product==0 or p+q<=0:raise ValueError('tau>2, nonzero product, positive exponent sum required')
 return ((tau-2)/(product*product))**(1/(2*(p+q)))
def ell0_gate(symbols):return 'NONABELIAN_PRODUCT_PHASE_GEOMETRIC_NOT_ELL0' if 'ell0' not in symbols else 'ELL0_REQUIRES_PHYSICAL_CONNECTION_AND_LOOP_LAW'
def evaluate():
 cases=[]
 for a,b in [(.2,.3),(1,-2),(-.5,-.7)]:
  c=commutator(a,b);cases.append({'a':a,'b':b,'commutator':c,'trace':trace(c),'determinant':det(c),'trace_formula':2+(a*b)**2})
 return {'study_id':'nonabelian-commutator-holonomy-v1','group':'SL(2,R) exact shear toy','commutator':'A(a) B(b) A(a)^-1 B(b)^-1','trace':'2+(ab)^2','determinant':1,'cases':cases,'product_gate':'A_B_FACTOR_ALLOCATION_NONIDENTIFIABLE_FROM_TRACE','sign_gate':'TRACE_ERASES_PRODUCT_SIGN','scale_gate':'FREE_PRODUCT_AMPLITUDE_MOVES_TRACE_THRESHOLD','exponent_gate':'ONLY_P_PLUS_Q_ENTERS_SCALE_EXPONENT','ell0_gate':ell0_gate(['a','b','ell']),'status':'NONABELIAN_COMMUTATOR_TRACE_PRODUCT_DEGENERACY_NOT_ELL0','classification':'EXACT_GROUP_TOY_CONTROL_AND_NEGATIVE_RESULT','conclusion':'NO_POSITIVE_DETECTION_CLAIM','limitation':'Exact non-Abelian group toy, not holonomy derived from a four-dimensional spacetime connection, physical loop family, data, or UMCH law.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=render()
 if a.check:
  if not O.exists() or O.read_text()!=s:print('Non-Abelian commutator artifact differs',file=sys.stderr);return 1
  print('Non-Abelian commutator artifact is current.');return 0
 O.write_text(s);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
