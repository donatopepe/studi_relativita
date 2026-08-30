# Schwarzschild finite-scattering endpoint-clock phase audit — English

## Disposition

`SCHWARZSCHILD_STATIC_ENDPOINT_CLOCK_PHASE_ADDS_CROSS_CHANNEL_SHAPE_BUT_RETAINS_EXTERNAL_FREQUENCY_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_CLOCK_REALIZATION_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; maximum interpretation `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Review mode: `DIRECT_REVIEW_NO_SUBAGENT`.

## Preregistered object

Geometry is equatorial future-null Schwarzschild scattering between equal-radius static endpoints, with `M=1`, `rho=4`, `R=12`, one turning point and screen order `(polar,in-plane)`. Turning regularization is `r/M=rho+y^2`. Static endpoint elapsed proper time and declared toy-clock phase are

```text
Delta_tau_R=sqrt(1-2/R) Delta_t
Phi_clock=nu_s Delta_tau_R/M
nu_s=M omega_s
```

Primary joined record is `R_joint=(Phi_clock,P_frequency_converted)`. Full transported-screen `4x4` map remains intact; clock phase does not replace it. This is not called Shapiro excess delay because no independently matched flat reference path was specified.

## Deterministic controls

At `nu_s=0.2`:

```text
Delta_t/M=40.223422979930845
Delta_tau_R/M=36.718793510299655
Phi_clock=7.343803420273261
turning_integrand_limit=8.000000000000002
mesh_doubling_residual=3.061625987044181e-05
direct_cutoff_residual=0.029046157694665453
```

Frequency linearity and orientation-phase residuals are zero. Orientation scalar evenness does not erase raw screen labels `+1,-1`. Shrinking `R-rho` reduces phase and full-map identity residual: zero window is a protocol limit, not holonomy or evidence.

Under `M -> 1.7 M` at fixed `nu_s`, `omega_s -> omega_s/1.7`:

```text
dimensionless_time_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

Thus joined channel keeps exact geometric dilation blindness within numerical tolerance. Holding dimensional `omega_s=0.2` fixed instead changes `nu_s: 0.2 -> 0.34` and clock phase by `5.140662394191283`; classification remains `EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

Joint finite-difference audit:

```text
rank_shape_boundary=2
rank_with_log_M=2
log_M_column_norm=5.730937517383603e-09
scale_null_direction=[0,0,1]
global_injectivity=NOT_ESTABLISHED
```

Clock phase adds a shape/boundary component but no interior `log M` direction at fixed `nu_s`. Local rank does not prove global injectivity or statistical independence. No joint covariance exists.

## Scope and sources

`Schwarzschild2003Translation` supports Schwarzschild exterior geometry and static-clock context. `Darwin1959GravityField` supports null-geodesic scattering context. `Sachs1961` supports optical/Jacobi propagation context. These sources do not establish this complete finite-boundary endpoint-clock cross-map, a physical source clock or coherent spectrum, emission phase, absorber response, screen preparation, vector detector readout, joint covariance, an `ell0` law, UMCH evidence or detection.

Clock phase is a `PROJECT_DERIVATION` using a `TOY_EXTERNAL_CLOCK`. It is neither photon internal phase nor a derived source/absorber/detector observable. No source and observer frequencies were assigned independently on one geodesic.

## Decision

Negative counterexample passes. External frequency standard can compare geometric time to a clock, but does not become an interior Schwarzschild scale or identify `ell0`. Physical source, absorber, detector, covariance and other exact-geometry routes remain open, so no structural dead end is declared.
