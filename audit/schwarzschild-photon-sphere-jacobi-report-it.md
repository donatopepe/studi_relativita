# Audit Jacobi sulla sfera fotonica di Schwarzschild — Italiano

## Decisione

`classification=EXACT_NONRADIAL_NULL_SCREEN_JACOBI_PHASE_MAP_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

`scope=FOUR_DIMENSIONAL_SCHWARZSCHILD_NULL_SCREEN_JACOBI_PHASE_MAP_ON_FUTURE_PHOTON_SPHERE_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_BOUNDARIES_AND_NO_DETECTOR_READOUT`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

UMCH è `UNPROVEN`. Lo stato detection è `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`. Superare questo audit significa al massimo `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Controlli esatti e numerici

La normalizzazione di progetto è `STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR`. Per `M=1`, `r_ph=3`, `L=18.84955592`; il residuo nullo è `2.220446049e-16` e quello geodetico `2.775557562e-17`.

La curvatura della connessione quadridimensionale dà `K=diag(0.1111111111,-0.1111111111)` nell'ordine originale `(radial,polar)` e nella convenzione dichiarata `X''=KX`. Il residuo originale della differenza finita radiale è `1.23788757e-11`; la traccia screen è zero. Un audit full-Riemann successivo calcola entrambi i canali usando derivate `r` e `theta` e conferma `diag(-1,+1)/(9M^2)` nell'ordine esplicito `(polar,radial)` con mismatch fine `2.308480787357262e-09`; risolve inoltre l'apparente conflitto di fattore tre con lo scattering tramite conversione della frequenza affine. Il residuo fra phase map esatta e numerica è `3.070206877e-12`; quello simplettico è `2.057951833e-11`.

Il raw `P_phase=[[A,B],[C,D]]` è primario. Coefficienti caratteristici e surrogato spettrale sono solo diagnostiche del quotient.

## Controesempi e limitazioni

Il boundary vertex ha punti coniugati `9.424777961` e `18.84955592`; all'endpoint `abs(det B)=2.140247132e-12`. Quindi `S_vertex` è `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`, mentre la full phase map resta finita/invertibile. La preparazione toy nonvertex resta regolare: il boundary conta.

L'inversione dell'orientation circolare è invisibile nei raw in questo controllo diagonalizzato con screen parallelo. Le rotazioni endpoint dello screen cambiano gli elementi raw. La conversione affine delle rate e l'orbita di scala Schwarzschild preservano il contenuto adimensionale della phase map mentre cambia la lunghezza dimensionale. Non segue alcun `ell0`.

Holonomy e phase map Jacobi condividono percorso e geometria: nessun canale indipendente senza covariance/readout del detector. Il winding è `DISCRETE_PROTOCOL_LABEL`; `Jacobian_joint=NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN`.

Mancano: preparazione fisica dello screen source/observer endpoint, standard affine-frequency, continuazione attraverso caustic, tetrade orientata, vector readout, azione detector, covariance, calibrazione, legge `ell0`, evidence e protocollo di detection.

## Classificazione e fonti

Sfera fotonica: risultato noto. Proiezione della connessione e phase map: derivazione di progetto. Boundary vertex/nonvertex: controlli toy. Caustic, quotient e cecità di scala: risultati negativi. Readout fisico: problema aperto.

`Darwin1959GravityField` supporta il contesto delle traiettorie Schwarzschild e dell'orbita circolare critica. `Sachs1961` supporta il contesto ottico nullo. Nessuna fonte stabilisce screen endpoint, normalizzazione affine, mappa finite-window, readout della caustic, detector, covariance, `ell0`, UMCH, evidence o detection.

## Review diretta di conformità

La review è stata eseguita direttamente perché la policy esplicita del progetto vieta subagent per questo task. Sono stati controllati allineamento spec/raw-key, convenzione dei segni, entrambe le proiezioni Riemann screen con differenze finite indipendenti, primarietà della full map, gate di invertibilità dei grafi, azione endpoint, conversioni affine/geometrica, scope delle fonti e label machine bilingui. Nessuna claim positiva e nessun trigger di vicolo cieco strutturale.
