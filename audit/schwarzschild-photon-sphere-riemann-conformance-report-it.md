# Audit di conformità full-Riemann sulla sfera fotonica di Schwarzschild — Italiano

## Decisione

`classification=FULL_FOUR_DIMENSIONAL_RIEMANN_CROSS_CONFORMANCE_AND_NEGATIVE_AFFINE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_FULL_RIEMANN_CONFIRMS_LEGACY_PROFILE_AFTER_SCREEN_ORDER_AND_AFFINE_NORMALIZATION_NOT_ELL0`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_ABSOLUTE_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

`review=DIRECT_REVIEW_NO_SUBAGENT`

UMCH resta `UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; la detection resta `NO_POSITIVE_DETECTION_CLAIM`. Superare il gate significa al massimo `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Risultato counterexample-first

Il conflitto sospettato con il profilo scattering corretto era una trappola di normalizzazione/ordine, non una falsificazione del profilo circolare legacy. La ricostruzione diretta del Riemann di Schwarzschild quadridimensionale usa derivate centrate sia in `r` sia in `theta`, poi proietta entrambi i canali sullo screen esplicito `(polar,radial)`. Per frequenza circolare locale unitaria,

`K_circular=diag(-1,+1)/(9M^2)`.

I mismatch coarse e fine sono `3.455052488702422e-08` e `2.308480787357262e-09`; il mismatch fine col legacy è ancora `2.308480787357262e-09`. Gli elementi polare e radiale sono entrambi proiezioni dirette; la traccia di vuoto è solo un check. Quindi il profilo legacy della PR #90 è confermato, non falsificato, dopo aver convertito la vecchia presentazione `(radial,polar)` nell'ordine esplicito `(polar,radial)`.

Il limite scattering della PR #95 è

`K_scattering=diag(-1,+1)/(3M^2)`

per l'anchor di progetto `E_infinity=1`. A `r=3M` la sua frequenza locale nel tetrade statico è `sqrt(3)`, mentre il controllo circolare pone la frequenza locale a uno. Poiché le matrici tidali ottiche scalano quadraticamente con la frequenza affine, dividere per `3` produce la matrice circolare. Il residuo convertito è `1.962615573354719e-17`; quello non convertito è `0.31426968052735443`.

Quindi il cross-control ingenuo è `FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON`. I due profili precedenti sono mutuamente conformi solo dopo ordine screen e conversione della frequenza affine espliciti.

## Interpretazione e fonti

`FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY`; le riduzioni a grafo restano condizionate all'invertibilità del blocco richiesto. Questa conformità non aggiunge uno standard assoluto né una direzione `ell0`.

`Schwarzschild2003Translation` supporta solo il contesto metrico; `Darwin1959GravityField` supporta traiettorie nulle e contesto dell'orbita critica; `Sachs1961` supporta il framework ottico nullo/Jacobi. Queste fonti non stabiliscono preparazione screen, boundary source/observer, calibrazione o readout del detector, covariance, `ell0`, UMCH, evidenza o detection del progetto.
