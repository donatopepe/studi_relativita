# Audit — scattering nullo Schwarzschild a boundary finito (IT)

- Classificazione: `PROJECT_DERIVATION_AND_TOY_FINITE_BOUNDARY_CONTROL_WITH_NEGATIVE_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT`
- Stato: `SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FINITE_WINDOW_OPEN_TRANSPORT_HAS_TURNING_AND_BOUNDARY_SHAPE_DIRECTIONS_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`
- Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_SCATTERING_WITH_ONE_TURNING_POINT_STATIC_ENDPOINT_TETRADS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_AND_NO_DETECTOR_READOUT`
- Gate: `PHYSICAL_SCATTERING_WINDOW_EMITTER_ABSORBER_TETRADS_AFFINE_FREQUENCY_STANDARD_SCREEN_JACOBI_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`
- `UMCH = UNPROVEN`
- `detection = NO_POSITIVE_DETECTION_CLAIM`
- `ell0_identified = false`; `structural_dead_end = NOT_DECLARED`

## Setup e record raw

Per `R>rho>3`, boundary finito e turning point sono `r_b=MR`, `r_p=M rho`; la normalizzazione di progetto `E=1` dà `beta=b/M=rho/sqrt(1-2/rho)`. `r/M=rho+y^2` regolarizza l'endpoint di turning. I branch incoming e outgoing sono matched esplicitamente.

I record primari sono campioni ordinati del path, `T_coordinate`, `T_tetrad` e il record di scattering al boundary. La classificazione è `OPEN_PATH_ENDPOINT_TRANSPORT_NOT_HOLONOMY`. Tetradi statiche ed energia di Killing unitaria sono anchor di progetto, non calibrazione detector.

Per `(rho,R)=(3.2,8),(4,12),(6,20)`, il massimo residuo nullo è `1.2958384365546749e-15`; il massimo residuo metrico endpoint è `7.936539086169608e-11`; il massimo residuo reverse inverse è `2.5981380717454544e-12`.

## Risultati counterexample e identificabilità

Cambiare boundary finito cambia `delta_t/M` di `21.839598856801473` e `T_tetrad` di norma `1.2018984246738986`: `FINITE_BOUNDARY_PROTOCOL_DIRECTION`. L'inversione dell'orientazione azimutale ha residui time-even e phi-odd mostrati nulli, ma il trasporto raw differisce di `2.9209203464700835`. Norme proiettate uguali sono `PROJECTED_NORM_ALIAS_NOT_RAW_MAP_EQUALITY`.

Azioni endpoint toy cambiano la mappa di `0.11335062941169595`; il residuo di ricostruzione dichiarata è `2.4828267625947587e-16`. Questo è `TOY_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION`.

Con fattore di scala geometrica `2.5`, il residuo del path dimensionless è `7.105427357601002e-15`, il residuo `delta_t/M` è `0.0` e quello del trasporto in tetrade è `7.107725939107331e-15`; il trasporto coordinato cambia di `20.361920261383094`. Risultato: `GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_ENDPOINT_CONVERSION`.

Audit joint delle feature:

- `rank_shape_boundary = 2`
- `rank_with_log_M = 2`
- `log_M_column_norm = 1.7391780828932144e-10`
- `scale_null_direction = [0, 0, 1]`
- `independent_channels = false`

Il rango di boundary non è un canale interno indipendente. Nessuna collisione è stata trovata nella griglia bounded; l'iniettività globale resta `NOT_ESTABLISHED`.

## Scope fonti e nonclaim

`Schwarzschild2003Translation` supporta solo il contesto della metrica esterna Schwarzschild. `Darwin1959GravityField` supporta solo il contesto di traiettorie nulle Schwarzschild e orbita critica. Integrazione, trasporto, azioni endpoint e rango sono derivazioni di progetto.

Nonclaim espliciti: `NO_DETECTOR_READOUT`, `NO_COVARIANCE`, `NO_PHYSICAL_ENDPOINT_CALIBRATION`, `NO_ELL0_LAW`, `NO_UMCH_EVIDENCE`, `NO_DETECTION`. Nessun `rho`, `R`, `beta`, dwell time o deflection è `ell0`.

## Review e chiusura

`DIRECT_REVIEW_NO_SUBAGENT`: l'istruzione esplicita no-subagent prevale sulla closure review automatica. Review diretta spec/code/artifact/report più test focused/full e CI forniscono evidenza di conformità, non evidenza scientifica. Sachs/Jacobi scattering generico e readout detector-derived restano aperti; nessun structural dead end è dichiarato.
