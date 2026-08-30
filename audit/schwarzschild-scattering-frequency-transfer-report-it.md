# Audit — trasferimento di frequenza statica nello scattering Schwarzschild

## Contratto

Stato:

`SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate:

`PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

Ambito: scattering Schwarzschild equatoriale nullo futuro con boundary finiti, `R>rho>3`, un turning point, tetradi endpoint statiche, frequenza locale sorgente toy, screen trasportato corretto `(polar,in-plane)`, phase map completa, nessun detector.

Classificazioni: metrica/redshift/ottica nulla sono `KNOWN_RESULT` nello scope limitato delle fonti; audit di trasferimento/mappa/rango è `PROJECT_DERIVATION`; clock statico ideale è `TOY_CONTROL`; cecità di scala preservata è `NEGATIVE_RESULT`; sorgente/assorbitore/readout/covarianza/legge `ell0` fisici restano `OPEN_PROBLEM`.

## Risultato counterexample-first

La frequenza statica soddisfa

`omega(r)=E_infinity/sqrt(1-2M/r)`.

Frequenze endpoint indipendenti sono rifiutate se non rispettano l'energia di Killing conservata. Sorgente e osservatore allo stesso raggio hanno uguale frequenza locale. Il profilo primario corretto resta

`diag(-1,+1) 3 M b^2/r^5`

per `E_infinity=1`. Per scala tangente sorgente `a`, `K_a=a^2 K_1`; con `D_a=diag(I,aI)`,

`P_a=D_a P_1 D_a^-1`.

A `M=1`, `rho=4`, `R=12`, `omega_s=0.2`:

```text
tangent_scale=0.18257418583505539
profile_quadratic_ratio=0.03333333333333334
raw_rate_map_difference=1086.2506743368622
converted_phase_map_residual=6.821210263296962e-12
```

Le entry raw nelle coordinate di phase rate cambiano, ma la conversione affine esplicita riconcilia le mappe. La phase map completa resta primaria.

A `nu_s=M omega_s` fisso, la dilatazione Schwarzschild di `1.7` dà residuo convertito `1.7280399333685637e-11`. L'audit di rango dà `rank_shape_boundary=2`, `rank_with_log_M=2`, `log_M_column_norm=4.270886111708851e-10`, direzione nulla di scala `[0,0,1]` e iniettività globale `NOT_ESTABLISHED`.

Tenere fissa la frequenza dimensionale della sorgente cambia `M omega_s` e l'output. Disposizione:

`EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

È calibrazione tramite clock importato, non scala intrinseca di curvatura o `ell0`.

## Scope delle fonti

`Schwarzschild2003Translation` supporta il contesto metrico; `Darwin1959GravityField` supporta traiettorie nulle/contesto dell'orbita critica; `Sachs1961` supporta il framework ottico nullo/Jacobi. Non stabiliscono il protocollo endpoint completo, clock o spettro sorgente fisici, risposta dell'assorbitore, detector, covarianza, `ell0`, UMCH, evidenza o detection.

## Review e stato finale

Review diretta di diff/spec perché l'utente ha vietato subagent: `DIRECT_REVIEW_NO_SUBAGENT`.

`UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; massimo `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.
