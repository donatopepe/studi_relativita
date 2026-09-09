# Kerr equatorial photon-ring orientation/scale audit

## Status

```text
MODEL=KERR_EQUATORIAL_PHOTON_RING_4D_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE
```

Direct closure record: `DIRECT_REVIEW_NO_SUBAGENT`. Not independent review.

## Scope

This `4D_COMPARISON_BASELINE` checks exact subextremal Kerr equatorial circular null orbits. `Teo2003SphericalPhotonOrbits` supports radii, range, radial equation, and constant-radius conditions. Impact-parameter substitution, coordinate angular rate/period, sign collisions, scale audit, and rank are project derivations.

No transported screen, Jacobi/Sachs map, finite boundary, emitter/absorber, physical clock, receiver, covariance, or data enters this MVP.

## Deterministic anchor

```text
chi=0.6
x_pro=2.188914
x_retro=3.6298497
xi_pro/M=3.8384937
xi_retro/M=-6.3156493
Omega_pro*M=0.26051886
Omega_retro*M=-0.15833685
branch_minimum_gap=0.46362086
radial_residual=0.0
dimensionless_scale_residual=0.0
rank=1
scale_null_direction=[1.0,0.0]
```

`Omega_phi` and period are Boyer-Lindquist coordinate records, not detector-clock observables.

## Eight controls

All `8/8` preregistered controls pass:

1. radius formula and range;
2. strict nonzero-spin branch ordering;
3. Schwarzschild collision at `3M`;
4. independent radial-potential and angular-rate conformance;
5. simultaneous spin/orientation convention collision;
6. exact joint geometric dilation;
7. rank-one spin shape with exact scale-null direction;
8. fail-closed no-`ell0` gate.

## Bounded result

```text
KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
PHYSICAL_KERR_SOURCE_ABSORBER_ENDPOINT_TETRAD_SCREEN_TRANSPORT_AFFINE_FREQUENCY_CLOCK_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

Kerr frame dragging supplies orientation-sensitive dimensionless shape. It does not supply an internal dimensional standard. Thus `M`, `a`, absolute period, and `ell0` are not identified. This result neither confirms nor refutes an extra dimension or UMCH. Prior 5D tensor conformance, finite `S1` localization, Schwarzschild results, and `F_0` remain unchanged.
