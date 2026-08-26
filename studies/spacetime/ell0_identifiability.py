#!/usr/bin/env python3
import argparse,json,math,pathlib,sys
H=pathlib.Path(__file__).resolve().parent;O=H/'ell0-identifiability-results.json'
def power(ells,A,ell0,p):return [float(A)*(float(e)/float(ell0))**(-float(p)) for e in ells]
def exponential(ells,A,q,ell0):return [float(A)*math.exp(-float(q)*(float(e)/float(ell0)-1)) for e in ells]
def plateau_power(ells,A_inf,A1,ell0,p):return [float(A_inf)+x for x in power(ells,A1,ell0,p)]
def gate(family,amplitude_calibrated,shape_calibrated):
 if family=='F_0':return 'ELL0_ABSENT_FROM_NULL_MODEL'
 if family in ('F_P','F_PE') and amplitude_calibrated:return 'IDENTIFIABLE_IN_PRINCIPLE_WITH_EXTERNAL_CALIBRATION'
 if family=='F_E' and amplitude_calibrated and shape_calibrated:return 'IDENTIFIABLE_IN_PRINCIPLE_WITH_EXTERNAL_CALIBRATION'
 return 'ELL0_STRUCTURALLY_NON_IDENTIFIABLE'
def evaluate():
 return {'study_id':'ell0-structural-identifiability-v1','families':{'F_0':gate('F_0',True,True),'F_P':gate('F_P',False,False),'F_E':gate('F_E',False,False),'F_PE':gate('F_PE',False,False)},'identified_combinations':{'F_P':['A*ell0^p','p'],'F_E':['A*exp(q)','q/ell0'],'F_PE':['A_inf','A_1*ell0^p','p'],'F_0':[]},'status':'ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES','conclusion':'NO_POSITIVE_DETECTION_CLAIM','scope':'Exact reparameterization result for current free-parameter families; external calibration could change the gate.'}
def render():return json.dumps(evaluate(),indent=2,sort_keys=True)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();e=render()
 if a.check:
  if not O.exists() or O.read_text()!=e:print('ell0 results differ',file=sys.stderr);return 1
  print('ell0 identifiability results are current.');return 0
 O.write_text(e);print(f'Wrote {O}');return 0
if __name__=='__main__':raise SystemExit(main())
