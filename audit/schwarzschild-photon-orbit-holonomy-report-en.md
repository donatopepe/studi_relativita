# Audit: Schwarzschild photon-orbit holonomy

## Verdict

`SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Detection: `NO_POSITIVE_DETECTION_CLAIM`. Structural dead end: `NOT_DECLARED`.

## Reproducible result

For `M=1`, future null photon orbit has `r_ph=3`, `Delta tau=18.84955592`, null/geodesic residuals below `2e-15` and `3e-16`. Algebraic and numerical loop transport agree within `8e-10`. Raw Lorentz holonomy is nontrivial with nonidentity norm `148.8621186`.

Future null photon orbit plus past-directed static closure has order-dependent transport. Segment exchange differs by `464.9166525`; path ordering is not an independent channel. Azimuthal orientation changes raw anchored matrix but collides in characteristic coefficients. Common tetrad conjugacy also changes raw entries while preserving those coefficients.

Batched two-winding boundary differs from two repeated complete loops because static closure placement differs. winding is a discrete protocol label, not continuous geometric rank. geometric scale blindness survives `(M,r,Delta t,Delta tau)->s(M,r,Delta t,Delta tau)`; proper duration changes while dimensionless timing and holonomy remain fixed.

## Interpretation boundary

No emitter, absorber, vector readout, oriented tetrad calibration, covariance or absolute standard is derived. Photon sphere `r=3M` is a background-mass landmark, not an `ell0` landmark. `Darwin1959GravityField` supports Schwarzschild null trajectories and critical circular-orbit context only, not finite closure, detector protocol, UMCH or detection.
