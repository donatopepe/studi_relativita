# Audit — mappa incrociata ad arco finito sulla sfera fotonica di Schwarzschild

Classificazione: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Stato: `SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_CONNECTION_JACOBI_CROSS_MAP_CAUSTIC_LANDMARKED_LOCALLY_ONE_SHAPE_DIRECTION_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Ambito: `FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_CONNECTION_AND_SCREEN_PHASE_MAP_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_ENDPOINT_BASES_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_FINITE_ARC_WINDOW_SELECTION_SOURCE_OBSERVER_TETRADS_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Contratto: `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; al massimo `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Risultato sottoposto ad audit

Anchor affine di progetto: `k=e_0+epsilon e_3`. Geometria: `r_ph=3M`, `L=3M alpha`, `Delta t=3 sqrt(3) M alpha`. L'artifact principale usa `M=1`, `alpha=pi/3`, quindi `L=pi`; il residuo nullo è `2.220446049250313e-16` e quello geodetico `2.7755575615628914e-17`.

Gli oggetti primari restano `T_arc` raw e la mappa completa `P_arc=[[A,B],[C,D]]`. L'oggetto di connessione è `OPEN_ARC_ENDPOINT_TRANSPORT_NOT_HOLONOMY`. Coefficienti caratteristici, blocchi di grafo e rango sono solo diagnostiche.

I residui esatto/numerico all'arco principale sono `8.973730906160965e-14` per il trasporto di connessione e `5.556515941082763e-14` per RK4 ottico. I residui Lorentz e simplettico sono `4.775249788392736e-16` e `2.5829094694428234e-15`; il determinante di fase è `1.0000000000000004`. I residui di semigruppo sono inferiori a `6e-15`.

Le caustiche vertex si trovano a `alpha=pi` e `alpha=2*pi`. In entrambe, il grafo vertex riporta `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`, mentre `P_arc` completa resta finita e invertibile. Il boundary toy nonvertex resta regolare. La caustica è un gate di dominio, non evidence.

L'orientazione cambia le entry raw della connessione, mentre i dati caratteristici collidono; la propagazione ottica diagonale collide sotto inversione dell'orientazione. Le azioni endpoint cambiano le entry raw. Senza tetradi endpoint fisiche, handedness e calibrazione screen, tali entry non sono invarianti del detector.

Il controllo affine con fattore `1.7` dà residuo di fase convertito `9.459807063569745e-15`. Il fattore geometrico `2.4` dà residui di connessione e fase convertita `4.685680459230494e-16` e `1.4001608167315755e-14`, mentre la lunghezza affine cambia di `4.3982297150257095` e la durata coordinata di `7.617957329783713`. Cecità affine e geometrica sono nuisance esatte distinte.

Per i parametri `(alpha,log_M)`, il cross-channel derivato ha `rank_joint=1`; la norma della colonna di scala è inferiore a `8e-11`, la convergenza di step inferiore a `2e-9`, e `independent_channels=false`. Ciò dice solo che questa famiglia esatta con geometria condivisa possiede una direzione locale di forma calibrata. Non prova iniettività globale, indipendenza statistica, identificabilità del detector o scala assoluta.

Il sottoblocco di fase ellittico collide sotto `alpha->alpha+2*pi`, ma fase completa iperbolica e feature congiunte non collidono nella coppia testata. A `alpha=2*pi`, il trasporto nullo futuro coincide esattamente con il precedente segmento fotonico; aggiungendo la chiusura precedente, l'olonomia coincide entro `6.2e-14`. La chiusura è `DERIVED_PAST_DIRECTED_STATIC_CLOSURE_CROSS_CHECK_ONLY`, non un altro canale indipendente.

## Fonti e limitazioni

`Darwin1959GravityField` supporta soltanto traiettoria Schwarzschild e contesto dell'orbita circolare critica. `Sachs1961` supporta soltanto il framework ottico nullo. Nessuna delle due fonti supporta trasporto ad arco aperto, selezione della finestra finita, tetradi endpoint, standard di frequenza affine di progetto, preparazione screen, continuazione attraverso caustiche, vector readout, detector, covariance, `ell0`, UMCH, evidence o detection.

Non sono stati introdotti dati reali, risposta del detector, covariance, calibrazione emitter/observer, standard assoluto, legge per `ell0`, bound, replica o detection.

Generic scattering ed endpoint freely falling restano route bounded aperte. Vector readout fisico e covariance restano blocker. Quindi non si dichiara alcun vicolo cieco strutturale né candidato di riformulazione.

## Eccezione di direct review

L'utente ha vietato esplicitamente l'uso di subagent. La direct review ha sostituito la closure review tramite subagent: spec, plan, implementazione, artifact canonico, teoria, report inglese e report italiano sono stati confrontati nella sessione. Questa eccezione di processo non riduce i gate scientifici e non crea evidence.
