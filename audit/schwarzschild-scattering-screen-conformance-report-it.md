# Audit — conformità screen/Riemann dello scattering Schwarzschild (IT)

- Stato: `SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0`
- Gate: `PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`
- `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`
- Detection: `NO_POSITIVE_DETECTION_CLAIM`
- Interpretazione massima: `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`
- Review: `DIRECT_REVIEW_NO_SUBAGENT`

## Formule di progetto falsificata e corretta

La proiezione indipendente del Riemann quattro-dimensionale a differenze finite, incluse le derivate metriche radiali e polari, falsifica la precedente formula di progetto `diag(+1,-1) M b^2/r^5`. La formula corretta per `X''=K X`, nell'ordine `(polar,in-plane)`, è `diag(-1,+1) 3 M b^2/r^5`.

A `rho=3.000001`, i valori al turning tendono a `diag(-1,+1)/3`, non al precedente `diag(+1,-1)/9`. Questo è un `NEGATIVE_RESULT` bounded contro l'implementazione di progetto, preservato esplicitamente.

## Controlli raw di trasporto e ricostruzione

Lo screen in-plane ha derivata raw non nulla `0.1767889727337515`, in gran parte null gauge. Il residuo quotient esplicito converge da `7.965045099585612e-05` (`n=60`) a `1.9939515283841326e-05` (`n=120`); la rotazione screen fine è `1.851520265341161e-05`. Gli endpoint usano diagnostici one-sided separati.

Il mismatch del profilo Riemann converge da `2.2914168372714706e-08` a `1.8971899374401116e-09`; residuo fine di simmetria `0.0`, residuo di traccia vacuum `1.3529229958564315e-09`, residuo di profilo tra orientazioni `0.0`.

La phase map corretta resta simplettica e cieca alla scala:

```text
symplectic_residual = 5.684341886080802e-14
reverse_inverse_residual = 1.000444171950221e-11
turning_composition_residual = 5.684341886080802e-14
dimensionless_profile_residual = 4.163336342344337e-17
converted_phase_map_residual = 3.410605131648481e-13
rank_shape_boundary = 2
rank_with_log_M = 2
log_M_column_norm = 5.724578281939044e-09
scale_null_direction = [0,0,1]
global_injectivity = NOT_ESTABLISHED
```

## Classificazione e limiti delle fonti

`Schwarzschild2003Translation`, `Darwin1959GravityField` e `Sachs1961` supportano solo il contesto metrico/geodetico nullo/Jacobi `KNOWN_RESULT`. Quotient null-gauge, ricostruzione a differenze finite, correzione del profilo e nuovo calcolo della phase map sono `PROJECT_DERIVATION`. Boundary finito, tetrade statica, energia di Killing unitaria, handedness e step schedule sono `TOY_CONTROL`. Source fisica, realizzazione endpoint, standard assoluto, vector readout del detector, covariance e legge `ell0` restano `OPEN_PROBLEM`.

Queste fonti do not establish il protocollo boundary di progetto, la calibrazione detector, la covariance, `ell0`, UMCH, evidence o detection. La correzione non identifica `ell0` e non attiva una riformulazione.
