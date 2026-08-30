# Schwarzschild photon-sphere finite arc with freely falling endpoint frames

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: when the raw open photon-sphere arc maps from PR #91 are expressed in independently specified radial freely falling endpoint tetrads rather than project-static endpoint bases, does endpoint motion add a physically independent shape/scale direction, or is it an endpoint boost nuisance unless emitter/observer preparation and readout are calibrated?

Classifications:

- Schwarzschild geometry and photon-sphere trajectory: `KNOWN_RESULT` in the bounded source scope already verified;
- radial timelike geodesic first integral and orthonormal boosted tetrad: `PROJECT_DERIVATION` checked directly against normalization and geodesic equations;
- endpoint-frame actions on raw connection and optical phase maps: `PROJECT_DERIVATION` / `TOY_CONTROL`;
- quotient collisions, rank loss and scale blindness: `NEGATIVE_RESULT` if tests pass;
- physical release history, endpoint synchronization, source/observer preparation, detector action, covariance and `ell0` law: `OPEN_PROBLEM`.

No source establishes this endpoint protocol, detector calibration, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Generic nonradial scattering.** Adds turning points, capture/scatter branch matching and asymptotic screen calibration together. Strong but too many new dependencies for the next bounded counterexample.
2. **Freely falling endpoint frames on the exact photon-sphere arc — selected.** Keeps exact raw interior generators and varies only endpoint observers. This isolates whether removal of static endpoint bases changes physical rank.
3. **Detector-derived emitter/absorber action.** Scientifically required later, but cannot be invented from geometry alone.

Selected design is minimal and counterexample-first. Endpoint frames are radial timelike geodesics characterized locally by signed specific energy `E>=sqrt(f(3M))` and radial sign `sigma in {-1,+1}`. These labels are toy preparation variables, not observables derived by this study.

## Geometry and endpoint frames

At `r=3M`, `f=1/3`. A radial timelike geodesic has

```text
u^t = E/f,
u^r = sigma sqrt(E^2-f),
g(u,u)=-1.
```

Relative to the static orthonormal tetrad, write

```text
gamma = E/sqrt(f),
beta = sigma sqrt(1-f/E^2),
B(beta) = [[gamma,-gamma beta],[-gamma beta,gamma]]
```

in the timelike/radial plane, with polar and azimuthal axes unchanged. Direct coordinate acceleration residuals must verify the local geodesic equation. `E=1` is an optional marginally-bound toy anchor; no physical release event is inferred.

The future photon arc remains

```text
r=3M,
k=e_0+orientation e_3,
L(alpha)=3M alpha,
Delta t=3 sqrt(3) M alpha.
```

## Raw endpoint actions

Let `T_arc` be the static-tetrad endpoint transport from PR #91. For independently specified source and observer free-fall frames `B_s,B_o`, preserve

```text
T_ff = B_o^{-1} T_arc B_s.
```

For optical phase variables, radial boosts change measured null frequency while leaving the chosen radial/polar screen axes as a declared mathematical screen. Let

```text
omega(beta)=gamma
```

for `k=e_0+orientation e_3`, because radial boost is orthogonal to the azimuthal ray. The phase-rate endpoint conversion is

```text
D(omega)=diag(I,I/omega),
P_ff = D(omega_o)^{-1} P_arc D(omega_s).
```

This is a project conversion, not a detector response. Connection and phase objects remain separate raw records.

## Preregistered counterexamples and tests

Check at `alpha in {0,pi/3,pi,3pi/2,2pi}` and endpoint energies/signs including static limit `E=sqrt(f)`, marginally bound `E=1`, unequal energies and reversed radial signs.

1. **Frame validity:** normalization, orthonormality, Lorentz compatibility and radial geodesic residuals.
2. **Endpoint covariance:** free-fall maps equal explicit left/right endpoint actions; reconstructing static maps recovers PR #91 raw objects.
3. **Zero-window distinction:** unequal source/observer frames give an endpoint comparison map at `alpha=0`; this is not interior curvature response and must not be called holonomy.
4. **Composition:** composition works only when the intermediate endpoint frame and phase-rate convention match. Deliberate mismatch yields a nonzero residual until the transition action is inserted.
5. **Caustics:** endpoint actions do not remove vertex caustics; full phase map remains finite and invertible.
6. **Endpoint quotient:** independently variable endpoint boosts can change raw entries without changing static-reconstructed interior maps. Raw multiplicity is not extra physical rank absent calibrated endpoint preparation.
7. **Affine/geometric scale:** affine-rate and Schwarzschild dilation controls remain separate and blind after declared conversion.
8. **Joint rank:** for fixed endpoint preparation, dimensionless features versus `(alpha,log M)` retain one shape direction and a zero scale column. If endpoint energy is allowed to vary, any extra local direction must be labelled `ENDPOINT_PREPARATION_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.
9. **Global collisions:** test orientation/sign and periodic optical subblock collisions; local rank must not be promoted to global injectivity.
10. **Closed-loop provenance:** `alpha=2pi` future-null segment may be compared with prior controls, but free-fall endpoint frames do not derive a physical closure.

## Deterministic artifact and authority

Create:

- `studies/spacetime/schwarzschild_photon_arc_freefall_endpoints.py`;
- `studies/spacetime/schwarzschild-photon-arc-freefall-endpoints-results.json`;
- focused scientific, source and report tests;
- theory note and semantically aligned English/Italian audits;
- roadmap and bounded source-verification updates.

Raw matrices precede derived features in the artifact. Record exact status, scope, gate, source limits, residuals, collisions, rank, nuisance labels and negative result. Preserve `ell0_identified=false`, `independent_channels=false`, `structural_dead_end=NOT_DECLARED` and `NO_POSITIVE_DETECTION_CLAIM`.

## Expected bounded verdict

If tests pass:

```text
SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_FREEFALL_ENDPOINT_FRAMES_EXPOSE_PREPARATION_DIRECTIONS_BUT_RETAIN_ONE_INTERIOR_SHAPE_DIRECTION_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0
```

Scope:

```text
FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_WITH_LOCAL_RADIAL_GEODESIC_ENDPOINT_TETRADS_PROJECT_PHASE_RATE_CONVERSION_TOY_PREPARATION_LABELS_AND_NO_DETECTOR_READOUT
```

Gate:

```text
PHYSICAL_RELEASE_HISTORY_FINITE_ARC_WINDOW_SOURCE_OBSERVER_SYNCHRONIZATION_SCREEN_PREPARATION_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

Passing yields at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Generic nonradial scattering and physical detector/readout derivation remain open, so structural-dead-end criteria do not pass.
