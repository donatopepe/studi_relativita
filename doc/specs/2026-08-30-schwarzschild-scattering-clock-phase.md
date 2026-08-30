# Schwarzschild finite-scattering endpoint-clock phase cross-channel gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end remains `NOT_DECLARED`.

Question: for the audited finite-boundary equatorial Schwarzschild null-scattering ray with equal-radius static endpoints, `R>rho>3`, one turning point, and source-local toy frequency, does joining endpoint-clock elapsed phase to the corrected transported-screen Jacobi map create an interior absolute-scale direction, or does the joint record retain exact Schwarzschild dilation blindness when the dimensionless source frequency `nu_s=M omega_s` is fixed?

Classifications:

- Schwarzschild exterior metric, Killing time, static proper time, null first integrals, gravitational frequency transfer and Sachs/Jacobi framework: `KNOWN_RESULT` within cited source scope;
- regularized finite-scattering Killing-time integral, endpoint proper elapsed time, clock phase, phase/Jacobi cross-map and rank audit: `PROJECT_DERIVATION`;
- ideal static boundary clock, continuous monochromatic source phase, equal-radius endpoints and declared source-local frequency: `TOY_CONTROL`, not emitter, absorber or detector dynamics;
- persistence of geometric dilation blindness, rank loss or cross-channel collinearity: `NEGATIVE_RESULT` if tests pass;
- physical clock realization, source spectrum/coherence, emission event, absorber response, screen preparation, vector readout, joint covariance and an `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this complete finite-boundary cross-channel protocol, detector response, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Use coordinate travel time as direct observable.** Rejected: Schwarzschild `t` alone is coordinate-labelled. Retain it only as intermediate; primary clock quantity is static-endpoint proper elapsed time `Delta tau_R=sqrt(f_R) Delta t`.
2. **Call the elapsed quantity a Shapiro delay.** Rejected: no independently matched flat reference path is preregistered here. Report finite endpoint elapsed time and phase, not an excess-delay claim.
3. **Join endpoint-clock phase to full Jacobi map.** Selected. It preserves channel-native clock and optical records, tests cross-channel rank directly, and exposes external-clock calibration without scalarizing the full phase map.

## Geometry and preregistered equations

Use `G=c=1`, `x=r/M`, turning radius `rho=r_min/M`, endpoint radius `R=r_endpoint/M`, and

```text
f(x)=1-2/x
beta=b/M=rho/sqrt(f(rho))
x=rho+y^2
q(x)=1-beta^2 f(x)/x^2
```

For future-null unit-Killing-energy project normalization,

```text
dt/dr = 1/[f(x) sqrt(q(x))]
Delta t/M = 2 int_0^sqrt(R-rho) 2y/[f(rho+y^2) sqrt(q(rho+y^2))] dy
Delta tau_R/M = sqrt(f(R)) Delta t/M
```

The `y=0` integrand is evaluated by its analytic finite limit. With source-local angular frequency `omega_s` and `nu_s=M omega_s`, endpoint-clock phase is

```text
Phi_clock = omega_s Delta tau_R = nu_s Delta tau_R/M.
```

Equal-radius endpoints imply equal local source/observer frequency on the same null geodesic. `Phi_clock` counts the declared static boundary clock during propagation; it is not a derived source spectrum, photon internal phase, absorber action or detector output.

The optical object remains the corrected full transported-screen map in `(polar,in-plane)` order. Rate coordinates use the source-frequency normalization and are converted exactly as in the frequency-transfer audit. Primary joint record:

```text
R_joint = (Phi_clock, P_frequency_converted)
```

No norm or scalarized Jacobi summary replaces `P`.

## Counterexample-first tests

1. **Turning regularity:** doubled half-path integral is finite and converges under mesh doubling.
2. **Independent integration check:** compare regularized `y` quadrature against a direct radial quadrature with a controlled endpoint cutoff and convergence trend; do not claim equality at finite cutoff.
3. **Orientation parity:** clock phase is invariant under screen handedness while raw optical screen bookkeeping retains declared orientation.
4. **Frequency linearity:** at fixed geometry, `Phi_clock` scales linearly with `nu_s`; optical maps at distinct affine normalization agree only after declared rate conversion.
5. **Geometric dilation:** under `M -> sM`, `omega_s -> omega_s/s` so `nu_s` stays fixed. Require invariant `Delta t/M`, `Delta tau_R/M`, `Phi_clock`, and converted full map within numerical tolerance.
6. **External-standard control:** holding dimensional `omega_s` fixed changes `nu_s` and `Phi_clock`; classify this as an external clock-standard direction, not an interior geometric scale.
7. **Joint rank:** finite-difference the raw feature vector consisting of `Phi_clock` plus flattened converted `4x4` phase map with respect to `(rho,R,log M)` at fixed `nu_s`. Report shape/boundary rank, rank with `log M`, column norm, singular values and null direction. Local rank does not establish global injectivity or statistical independence.
8. **Boundary limit:** `R -> rho+` forces elapsed time and clock phase toward zero while full map approaches identity; this is a protocol zero-window limit, not evidence.

## Deterministic artifact contract

Produce `studies/spacetime/schwarzschild-scattering-clock-phase-results.json` containing:

- exact status, scope, classification and gate labels;
- declared geometry, screen order, affine/frequency normalization and endpoint clock convention;
- regularized elapsed-time convergence and direct-cutoff cross-check;
- clock phase, frequency linearity, orientation parity and zero-window controls;
- fixed-`nu_s` dilation and fixed-`omega_s` external-standard controls;
- full joint-rank diagnostics and `global_injectivity=NOT_ESTABLISHED`;
- `ell0_identified=false`, `UMCH=UNPROVEN`, `NO_POSITIVE_DETECTION_CLAIM`, `structural_dead_end=NOT_DECLARED`.

`--check` must fail on artifact drift.

## Reports, source scope and gates

Add semantically aligned English/Italian audits and one theory note. Source scope remains bounded to existing canonical entries `Schwarzschild2003Translation`, `Darwin1959GravityField`, and `Sachs1961`; add no citation unless exact support is verified. Reports must state what sources do not establish.

Passing gives at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Expected negative status if all controls pass:

```text
SCHWARZSCHILD_STATIC_ENDPOINT_CLOCK_PHASE_ADDS_CROSS_CHANNEL_SHAPE_BUT_RETAINS_EXTERNAL_FREQUENCY_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0
```

Expected unresolved gate:

```text
PHYSICAL_CLOCK_REALIZATION_SOURCE_COHERENCE_EMISSION_ABSORPTION_SCREEN_PREPARATION_VECTOR_READOUT_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

A numerical mismatch blocks disposition and triggers bounded correction; it does not support UMCH. Structural dead end is not declared because physical source/absorber/detector dynamics, covariance, other endpoint motions and other exact geometries remain open routes.

## Autonomous ratification

Binding autonomous loop preauthorizes conservative negative-control continuation without a conversational approval pause. This design is therefore ratified for implementation exactly as written. Any hypothesis-contract change, positive evidence claim, `ell0` value, structural-dead-end declaration or reformulation remains outside this ratification.
