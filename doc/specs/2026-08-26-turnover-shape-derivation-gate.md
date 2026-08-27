# Turnover shape derivation gate

## Goal

Determine whether `p,q` in candidate `F_T=A x^p exp[-q(x-1)]` can be fixed independently from existing operational geometry, without fitting data or adding dynamics.

## Derived local scaling

Curvature has dimension `L^-2`. For a regular region with approximately constant curvature:

- tidal/magnetic normalization `ell^2 RMS(E/B)` has leading area scaling exponent 2;
- small-loop holonomy `||R Sigma||` has leading area scaling exponent 2;
- clock, null, and congruence residuals may have leading exponent 2 only after fixed geometry and regular short-baseline expansion; no universal exponent is asserted across arbitrary protocols.

Thus geometry can justify `p=2` for declared area-normalized channels in their controlled small-region regime. It does not justify a universal all-channel `p`.

## Exponential factor

Local GR curvature and finite-region Taylor/holonomy expansions supply powers and higher-order corrections. They do not by themselves supply `exp[-q ell/ell0]`, a universal decay coefficient `q`, or a turnover. Such factor requires an independently specified nonlocal kernel, screening law, correlation function, transfer function, or modified dynamics. Defining it by convenience is circular and not a physical derivation.

## Decision

- `p=2`: `DERIVED_FOR_AREA_NORMALIZED_REGULAR_SMALL_REGION_CHANNELS_ONLY`.
- `q`: `NOT_DERIVED_FROM_CURRENT_GEOMETRIC_CORE`.
- turnover unlock: `BLOCKED_PENDING_INDEPENDENT_NONLOCAL_MECHANISM`.

The mathematical inversion remains valid conditionally. This gate prevents treating synthetic fixed `p,q` as physical input.

## Acceptance

Deterministic dimensional/scaling controls, reason-coded channel decisions, bilingual audit, no data/detection/ell0 value. Core remains `UNPROVEN`.
