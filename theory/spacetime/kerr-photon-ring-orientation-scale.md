# Kerr equatorial photon-ring orientation and scale

## Classification

- `KNOWN_RESULT`: `Teo2003SphericalPhotonOrbits` gives exact prograde/retrograde equatorial circular photon radii, their range, Kerr geodesic equations, radial potential, and constant-radius conditions.
- `PROJECT_DERIVATION`: impact-parameter substitution, independent `R=0` and `dR/dr=0` residuals, Boyer-Lindquist angular-rate record, signed convention map, joint dilation, and rank audit.
- `TOY_CONTROL`: exact subextremal Kerr exterior with circular equatorial null geodesics and no source/receiver or detector.
- `NEGATIVE_RESULT`: spin changes dimensionless branch shape, but exact joint `M,a` dilation leaves absolute scale and `ell0` unidentified.

## Exact orbit record

For `chi=|a|/M` and `0<=chi<1`,

```text
x_pro=2*[1+cos((2/3)*acos(-chi))]
x_retro=2*[1+cos((2/3)*acos(chi))]
r_ph=M*x_ph
```

with `1<=x_pro<=3<=x_retro<=4`. At `chi=0`, both radii collide at `3M`. For energy-normalized `xi=L_z/E` and equatorial Carter constant zero,

```text
Delta=r^2-2*M*r+a^2
R=[r^2+a^2-a*xi]^2-Delta*(xi-a)^2
```

Each generated branch is checked independently with `R=0` and `dR/dr=0`. Formula agreement alone is insufficient.

The retained `Omega_phi` and `Delta_t_per_2pi` form a Boyer-Lindquist coordinate period, not a physical clock. No endpoint worldline, redshift transfer, receiver, or calibration is included.

## Orientation and scale controls

Simultaneous spin and azimuthal reversal preserves relative orientation, radius, and unsigned period while reversing signed angular motion:

```text
SIMULTANEOUS_SPIN_ORIENTATION_REVERSAL_IS_CONVENTION_COLLISION_NOT_ELL0
```

At fixed `chi`,

```text
(M,a,r,xi,t) -> s*(M,a,r,xi,t)
Omega_phi -> Omega_phi/s
```

preserves all dimensionless branch features:

```text
JOINT_MA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE
```

The feature Jacobian over `[log_M,chi]` has rank one and exact scale-null direction `[1,0]`. This is dimensionless spin-shape rank, not physical global identifiability.

## Bounded result

All `8/8` preregistered controls pass.

```text
KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE
PHYSICAL_KERR_SOURCE_ABSORBER_ENDPOINT_TETRAD_SCREEN_TRANSPORT_AFFINE_FREQUENCY_CLOCK_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

This completes a `4D_COMPARISON_BASELINE`. It does not compare observed data to a 5D model, identify `M` internally, identify `ell0`, establish an extra dimension, or validate UMCH. Prior `R_op`, Schwarzschild controls, 5D tensor result, finite `S1` localization result, and `F_0` remain preserved.
