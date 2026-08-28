# Exact-pattern finite-window separability gate

## Question

Does finite-window averaging alone make fixed-symmetry exact operator patterns nonradial?

## Controls

Use declared symmetry-reduced profiles:

- FLRW tidal operator on comoving homogeneous slices: `E(t)=k(t) I`.
- Schwarzschild electric Weyl operator in a radially transported principal frame: `E(r)=m/r^3 diag(-2,1,1)`.

A scalar normalized window average of either profile is scalar coefficient times one fixed matrix. Multiplication by area normalization `ell^2` therefore stays on one projective ray whenever averaged coefficient is nonzero.

This is algebraic use of standard exact-pattern forms already present in project. It is not a new GR derivation, observational model, or claim about arbitrary windows/transport.

## Counterexample gate

- Curvature amplitude varying across window is insufficient for nonradiality when operator pattern is separable.
- Sign-changing average can pass through zero, where projective direction is undefined, without producing an injective `ell0` landmark.
- Nonradial response requires symmetry breaking, multiple non-collinear patterns, transport mixing not removed by quotient, channel structure, or boundary terms.
- `ell0` remains absent.

## Decision

Status `EXACT_PATTERN_WINDOW_AVERAGING_REMAINS_PROJECTIVELY_RADIAL`. No reformulation: nonsymmetric exact geometries and derived transport/boundary maps remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
