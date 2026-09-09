# Audit Kerr a frontiera finita con endpoint ZAMO

## Stato

```text
MODEL=KERR_EQUATORIAL_FINITE_BOUNDARY_4D_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_KERR_ENDPOINT_CONFORMANCE_NOT_EVIDENCE
```

Chiusura diretta: `DIRECT_REVIEW_NO_SUBAGENT`. Non è revisione indipendente.

## Perimetro

Cammini nulli futuri equatoriali di Kerr vanno dall'endpoint sorgente a un punto di inversione esterno e poi all'endpoint osservatore. `GrallaLupsasca2020KerrNullGeodesics` sostiene equazioni del cammino e struttura d'inversione. Costruzione ZAMO agli endpoint e controlli di residuo/rango sono derivazioni del progetto.

## Ancora deterministica

```text
chi=0.6
rho=4.5
R_source/M=12.0
R_observer/M=12.0
Delta_t_plus/M=33.987089
Delta_t_minus/M=41.551191
Delta_phi_plus=3.4663312
Delta_phi_minus=-4.2673873
omega_plus=1.0911117
omega_minus=1.1004156
orientation_shape_difference=7.7337185
rank=4
scale_null_direction=[1.0,0.0,0.0,0.0,0.0]
dimensionless_scale_residual=0.0
```

Direzioni locali e frequenze relative ZAMO sono matematicamente coerenti. ZAMO resta osservatore endpoint dichiarato, non sorgente fisica o rivelatore.

## Controlli e risultato

Tutti gli `8/8` controlli passano: radice d'inversione, cammino/convergenza, ortonormalità tetrade, ricostruzione nulla agli endpoint, orientazione/inversione, collisione Schwarzschild, dilatazione congiunta e rango/no-`ell0`.

```text
KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS_TO_LOCAL_DIRECTION_AND_RELATIVE_FREQUENCY_SHAPE_BUT_WITHOUT_PHYSICAL_ENDPOINT_STANDARDS_OR_SCREEN_TRANSPORT_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
PHYSICAL_KERR_EMITTER_ABSORBER_WORLDLINES_CLOCKS_AFFINE_FREQUENCY_STANDARD_PARALLEL_SCREEN_JACOBI_PREPARATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Le tetradi risolvono coerenza coordinate-locale, non osservabilità fisica. Restano mancanti worldline e orologi di emettitore/assorbitore, parallel screen transport, preparazione Jacobi, ricevitore/covarianza/dati, comparatore 5D e legge per `ell0`. Nessuna evidenza o detection.
