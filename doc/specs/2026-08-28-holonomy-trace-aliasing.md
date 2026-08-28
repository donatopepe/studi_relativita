# Finite-holonomy trace aliasing gate

## Question

Can conjugacy-invariant trace of finite rotational holonomy identify curvature-area phase globally?

## Exact compact-group control

Use planar rotation holonomy

`H(phi)=[[cos phi,-sin phi],[sin phi,cos phi]]`,

with trace `T(phi)=2 cos phi`, determinant one and eigenvalues `exp(+-i phi)`. Trace is conjugacy invariant but periodic and even:

`T(phi)=T(-phi)=T(phi+2pi n)`.

Thus global inversion from trace gives branches `phi=+-arccos(T/2)+2pi n`. Local injectivity holds only on preregistered branch such as `[0,pi]`; endpoints have derivative zero and poor conditioning. If `phi=k A`, unknown curvature amplitude `k` and loop area `A` are multiplicatively confounded.

This is exact SO(2) matrix holonomy algebra, not a connection-derived spacetime loop.

## Gates

- Conjugacy invariance does not imply global injectivity.
- Orientation reversal is invisible to trace.
- Winding/branch must be fixed independently.
- Full matrix retains signed sine only after frame/orientation convention; eigenvalue unordered set still identifies `+-phi`.
- `ell0` is absent.

## Decision

Status `FINITE_HOLONOMY_TRACE_PERIODIC_BRANCH_NONIDENTIFIABLE`. No reformulation: connection-derived non-Abelian loop families remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
