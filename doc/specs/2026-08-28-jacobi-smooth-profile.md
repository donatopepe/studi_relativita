# Smooth Jacobi profile moment gate

## Question

Does fixed integrated smooth optical strength determine observer endpoint at weak focusing?

## Project derivation

For scalar Jacobi equation

`d''(s)+epsilon f(s)d(s)=0`, `d(0)=0`, `d'(0)=1`, on `[0,S]`, variation around epsilon zero gives

`d(S)=S-epsilon int_0^S (S-t)t f(t) dt+O(epsilon^2)`.

Thus first-order endpoint depends on weighted moment, not only integrated strength `int f`. Choose normalized smooth profiles

`f_a(t)=1/S`,

`f_b(t)=6t(S-t)/S^3`.

Both integrate to one, but weighted moments are `S^2/6` and `S^2/5`; endpoint shifts differ by `epsilon S^2/30`. Reflection `f(t)->f(S-t)` preserves this scalar vertex-observer kernel; profile location degeneracy remains for symmetric pairs.

## Gates

Integrated focusing is insufficient even for smooth nonnegative profiles. Weighted first-order moment is sufficient only at first perturbative order, not exact finite epsilon. Affine normalization and boundaries are fixed here. `ell0` is absent.

## Decision

Status `JACOBI_SMOOTH_EQUAL_INTEGRAL_DIFFERENT_WEIGHTED_ENDPOINT_NOT_ELL0`. No structural dead end: exact smooth matrix optical profiles and spacetime-derived Sachs systems remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
