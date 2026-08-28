# Finite-window operator shape control

## Question

Can curvature variation across a finite window generate nonradial operator evolution, and does that alone identify `ell0`?

## Construction

Use deterministic diagonal trace-free toy operators. A windowed response has the form

`R(ell) = ell^2 [f(ell) A + g(ell) B]`.

This is a project derivation/toy control, not a GR solution or UMCH evidence.

## Counterexamples first

- If all sampled tensor profiles are separable, `R(ell)=s(ell)A`, projective direction is constant.
- If two non-collinear operator profiles have changing relative weights, projective direction changes.
- Yet if the construction contains only geometric scale `ell`, profile coefficients, and window choice, `ell0` is absent. Nonradial evolution is geometry/profile information, not an `ell0` landmark.
- Free profile coefficients and window nuisance can mimic shape unless independently fixed.

## Decision

Record `NONRADIAL_GEOMETRIC_SHAPE_NOT_ELL0_LANDMARK`. This is useful negative progress: nonradiality is necessary for projective scale information but insufficient for universal-scale identification. No core reformulation: route not at structural dead end because transport, boundary, holonomy/Jacobi and cross-channel structures remain untested.

Core remains `UNPROVEN`; conclusion `NO_POSITIVE_DETECTION_CLAIM`.
