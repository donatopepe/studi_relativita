# Audit: olonomia dell'orbita fotonica di Schwarzschild

## Verdetto

`SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

Ambito: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Rilevazione: `NO_POSITIVE_DETECTION_CLAIM`. Vicolo cieco strutturale: `NOT_DECLARED`.

## Risultato riproducibile

Per `M=1`, l'orbita fotonica nulla futura ha `r_ph=3`, `Delta tau=18.84955592`, residui di nullità/geodetico minori di `2e-15` e `3e-16`. Il trasporto algebrico e quello numerico del loop concordano entro `8e-10`. L'olonomia di Lorentz raw è non banale, con norma di non identità `148.8621186`.

L'orbita fotonica nulla futura più la chiusura statica orientata al passato ha trasporto dipendente dall'ordine. Lo scambio dei segmenti differisce di `464.9166525`; il path ordering non è un canale indipendente. L'orientazione azimutale cambia la matrice raw ancorata ma collide nei coefficienti caratteristici. Anche la coniugazione comune della tetrade cambia le entrate raw preservando quei coefficienti.

Il boundary batched a due winding differisce da due loop completi ripetuti perché cambia la posizione della chiusura statica. Il winding è una label discreta di protocollo, non rango geometrico continuo. La cecità alla scala geometrica sopravvive a `(M,r,Delta t,Delta tau)->s(M,r,Delta t,Delta tau)`; la durata propria cambia mentre timing adimensionale e olonomia restano fissi.

## Confine interpretativo

Non sono derivati emettitore, assorbitore, readout vettoriale, calibrazione di tetrade orientata, covarianza o standard assoluto. La sfera fotonica `r=3M` è un landmark della massa di fondo, non di `ell0`. `Darwin1959GravityField` supporta solo il contesto delle traiettorie nulle di Schwarzschild e dell'orbita circolare critica, non chiusura finita, protocollo di rivelatore, UMCH o detection.
