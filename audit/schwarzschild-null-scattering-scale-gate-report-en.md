# Audit — Schwarzschild finite-boundary null scattering (EN)

- Classification: `PROJECT_DERIVATION_AND_TOY_FINITE_BOUNDARY_CONTROL_WITH_NEGATIVE_GEOMETRIC_SCALE_IDENTIFIABILITY_RESULT`
- Status: `SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FINITE_WINDOW_OPEN_TRANSPORT_HAS_TURNING_AND_BOUNDARY_SHAPE_DIRECTIONS_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`
- Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_SCATTERING_WITH_ONE_TURNING_POINT_STATIC_ENDPOINT_TETRADS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_AND_NO_DETECTOR_READOUT`
- Gate: `PHYSICAL_SCATTERING_WINDOW_EMITTER_ABSORBER_TETRADS_AFFINE_FREQUENCY_STANDARD_SCREEN_JACOBI_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`
- `UMCH = UNPROVEN`
- `detection = NO_POSITIVE_DETECTION_CLAIM`
- `ell0_identified = false`; `structural_dead_end = NOT_DECLARED`

## Setup and raw records

For `R>rho>3`, the finite boundary and turning point are `r_b=MR`, `r_p=M rho`; project normalization `E=1` gives `beta=b/M=rho/sqrt(1-2/rho)`. `r/M=rho+y^2` regularizes the turning endpoint. Incoming and outgoing branches are matched explicitly.

The primary records are ordered path samples, `T_coordinate`, `T_tetrad`, and the boundary scattering record. Classification is `OPEN_PATH_ENDPOINT_TRANSPORT_NOT_HOLONOMY`. Static tetrads and unit Killing energy are project anchors, not detector calibration.

For displayed `(rho,R)=(3.2,8),(4,12),(6,20)`, maximum null residual is `1.2958384365546749e-15`; maximum endpoint metric residual is `7.936539086169608e-11`; maximum reverse inverse residual is `2.5981380717454544e-12`.

## Counterexample and identifiability results

Changing the finite boundary changes `delta_t/M` by `21.839598856801473` and `T_tetrad` by norm `1.2018984246738986`: `FINITE_BOUNDARY_PROTOCOL_DIRECTION`. Azimuthal orientation reversal has zero displayed time-even and phi-odd residuals, but raw transport differs by `2.9209203464700835`. Equal projected norms are `PROJECTED_NORM_ALIAS_NOT_RAW_MAP_EQUALITY`.

Toy endpoint actions change the map by `0.11335062941169595`; declared reconstruction residual is `2.4828267625947587e-16`. This is `TOY_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION`.

At geometric scale factor `2.5`, dimensionless path residual is `7.105427357601002e-15`, `delta_t/M` residual is `0.0`, and tetrad-transport residual is `7.107725939107331e-15`; coordinate transport changes by `20.361920261383094`. Result: `GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_ENDPOINT_CONVERSION`.

Joint feature audit:

- `rank_shape_boundary = 2`
- `rank_with_log_M = 2`
- `log_M_column_norm = 1.7391780828932144e-10`
- `scale_null_direction = [0, 0, 1]`
- `independent_channels = false`

Boundary rank is not an independent interior channel. No bounded grid collision was found; global injectivity remains `NOT_ESTABLISHED`.

## Source scope and nonclaims

`Schwarzschild2003Translation` supports Schwarzschild exterior metric context only. `Darwin1959GravityField` supports Schwarzschild null-trajectory and critical-orbit context only. Integration, transport, endpoint actions and rank are project derivations.

Explicit nonclaims: `NO_DETECTOR_READOUT`, `NO_COVARIANCE`, `NO_PHYSICAL_ENDPOINT_CALIBRATION`, `NO_ELL0_LAW`, `NO_UMCH_EVIDENCE`, `NO_DETECTION`. No `rho`, `R`, `beta`, dwell time or deflection is `ell0`.

## Review and closure

`DIRECT_REVIEW_NO_SUBAGENT`: explicit no-subagent instruction overrides automated closure review. Direct spec/code/artifact/report review plus focused/full tests and CI provide conformance evidence, not scientific evidence. Generic Sachs/Jacobi scattering and detector-derived readout remain open; no structural dead end is declared.
