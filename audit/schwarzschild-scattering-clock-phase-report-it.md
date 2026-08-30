# Audit della fase di clock agli estremi nello scattering finito di Schwarzschild — Italiano

## Disposizione

`SCHWARZSCHILD_STATIC_ENDPOINT_CLOCK_PHASE_ADDS_CROSS_CHANNEL_SHAPE_BUT_RETAINS_EXTERNAL_FREQUENCY_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_CLOCK_REALIZATION_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Autorità: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; interpretazione massima `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Modalità di review: `DIRECT_REVIEW_NO_SUBAGENT`.

## Oggetto preregistrato

La geometria è scattering equatoriale futuro-nullo di Schwarzschild tra estremi statici allo stesso raggio, con `M=1`, `rho=4`, `R=12`, un punto di inversione e ordine screen `(polar,in-plane)`. La regolarizzazione è `r/M=rho+y^2`. Il tempo proprio trascorso sul clock statico all'estremo e la fase dichiarata del clock toy sono

```text
Delta_tau_R=sqrt(1-2/R) Delta_t
Phi_clock=nu_s Delta_tau_R/M
nu_s=M omega_s
```

Il record congiunto primario è `R_joint=(Phi_clock,P_frequency_converted)`. La mappa completa `4x4` dello screen trasportato resta intatta; la fase di clock non la sostituisce. Non chiamiamo il risultato ritardo di Shapiro in eccesso, perché non è stato specificato un cammino piatto indipendente e abbinato.

## Controlli deterministici

Per `nu_s=0.2`:

```text
Delta_t/M=40.223422979930845
Delta_tau_R/M=36.718793510299655
Phi_clock=7.343803420273261
turning_integrand_limit=8.000000000000002
mesh_doubling_residual=3.061625987044181e-05
direct_cutoff_residual=0.029046157694665453
```

I residui di linearità in frequenza e parità orientativa della fase sono nulli. La parità dello scalare non cancella le label raw dello screen `+1,-1`. Riducendo `R-rho` diminuiscono fase e residuo della mappa dall'identità: la finestra nulla è limite di protocollo, non holonomy o evidenza.

Sotto `M -> 1.7 M` a `nu_s` fisso, `omega_s -> omega_s/1.7`:

```text
dimensionless_time_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

Il canale congiunto conserva quindi la cecità alla dilatazione geometrica entro la tolleranza numerica. Tenere invece fissa la frequenza dimensionale `omega_s=0.2` cambia `nu_s: 0.2 -> 0.34` e la fase di `5.140662394191283`; la classificazione resta `EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

Audit con differenze finite:

```text
rank_shape_boundary=2
rank_with_log_M=2
log_M_column_norm=5.730937517383603e-09
scale_null_direction=[0,0,1]
global_injectivity=NOT_ESTABLISHED
```

La fase aggiunge una componente di forma/bordo ma nessuna direzione interna `log M` a `nu_s` fisso. Il rango locale non dimostra iniettività globale o indipendenza statistica. Manca una covariance congiunta.

## Scope e fonti

`Schwarzschild2003Translation` sostiene geometria esterna di Schwarzschild e contesto dei clock statici. `Darwin1959GravityField` sostiene il contesto delle geodetiche nulle di scattering. `Sachs1961` sostiene il contesto della propagazione ottica/Jacobi. Queste fonti non stabiliscono il cross-map completo a estremi finiti, un clock fisico della source o spettro coerente, fase di emissione, risposta dell'absorber, preparazione dello screen, readout vettoriale del detector, covariance congiunta, legge per `ell0`, evidenza UMCH o detection.

La fase di clock è `PROJECT_DERIVATION` con `TOY_EXTERNAL_CLOCK`. Non è fase interna del fotone né osservabile derivato di source/absorber/detector. Frequenze source e observer non sono state assegnate indipendentemente sulla stessa geodetica.

## Decisione

Il counterexample negativo passa. Lo standard esterno di frequenza può confrontare tempo geometrico e clock, ma non diventa scala interna di Schwarzschild e non identifica `ell0`. Restano aperte route fisiche per source, absorber, detector, covariance e altre geometrie esatte; nessun vicolo cieco strutturale è dichiarato.
