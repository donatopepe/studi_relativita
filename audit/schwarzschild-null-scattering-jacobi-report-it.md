# Audit — mappa di Jacobi dello scattering Schwarzschild a boundary finito (IT)

- Classificazione: `PROJECT_DERIVATION_AND_TOY_SCREEN_BOUNDARY_CONTROL_WITH_NEGATIVE_AFFINE_AND_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT`
- Stato: `SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FULL_SCREEN_JACOBI_PHASE_MAP_ADDS_OPTICAL_PROFILE_AND_CAUSTIC_STRUCTURE_BUT_RETAINS_AFFINE_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`
- Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_ONE_TURNING_POINT_PARALLEL_SCREEN_FULL_JACOBI_PHASE_MAP_STATIC_ENDPOINTS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_NO_DETECTOR`
- Gate: `PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`
- `UMCH = UNPROVEN`; `ell0_identified = false`
- `detection = NO_POSITIVE_DETECTION_CLAIM`; `structural_dead_end = NOT_DECLARED`

## Oggetto raw e controlli

Il dominio del path è `R>rho>3`, con branch incoming, turning e outgoing ed energia di Killing unitaria come anchor affine di progetto. Nello screen trasportato dichiarato, `K=diag(+1,-1) 3 M b^2/r^5`. L'oggetto primario è `FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS`; i diagnostici graph sono guarded quando `B` è singolare.

Residui artifact: ortonormalità screen `4.440892098500626e-16`, traccia vacuum `0.0`, simplettico `1.7053025658242404e-13`, reverse inverse `7.275957614183426e-12`, composizione al turning `1.7053025658242404e-13`. Il conteggio globale delle caustiche è `NOT_ESTABLISHED`.

Le preparazioni vertex e parallel restano dati source toy distinti. Le azioni endpoint ricostruiscono la mappa interna ma sono `TOY_ORIENTED_SCREEN_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION`.

## Scala e rango

Per fattore geometrico `2.5`, il residuo del profilo dimensionless è `6.938893903907228e-17`; il residuo della phase map convertita è `6.394884621840902e-14`. Classificazione: `GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_PHASE_RATE_AND_ENDPOINT_CONVERSION`.

```text
rank_shape_boundary = 2
rank_with_log_M = 2
log_M_column_norm = 4.317417286094902e-09
scale_null_direction = [0, 0, 1]
independent_channels = false
global_injectivity = NOT_ESTABLISHED
```

Il rango shape/boundary non è scala interna né indipendenza statistica. Non esiste una legge `ell0`.

## Fonti, limiti e review

- `Schwarzschild2003Translation`: solo contesto metrico.
- `Darwin1959GravityField`: solo contesto di traiettorie nulle e orbita critica.
- `Sachs1961`: solo framework ottico nullo/Jacobi.
- Profilo, convenzione screen, integrazione phase, azioni endpoint, scala e rango sono derivazioni di progetto/controlli toy.

Limiti espliciti: `NO_DETECTOR_READOUT`, `NO_COVARIANCE`, `NO_ELL0_LAW`. Le fonti non stabiliscono calibrazione del protocollo, detector, covariance, `ell0`, UMCH, evidence o detection.

Modalità review: `DIRECT_REVIEW_NO_SUBAGENT`, richiesta dalla policy esplicita senza subagent. Interpretazione massima: `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Source/readout/covariance detector-derived generici restano aperti; nessun structural dead end dichiarato.
