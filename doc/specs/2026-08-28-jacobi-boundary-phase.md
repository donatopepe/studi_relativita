# Jacobi boundary-phase caustic gate

## Question

Does constant positive optical curvature alone fix first positive zero when general source boundary data are allowed?

## Control

For `d''+lambda d=0`, `lambda>0`, general scalar solution is `d(s)=d0 cos(omega s)+(v0/omega) sin(omega s)`, `omega=sqrt(lambda)`. Existing conjugate-point control uses vertex data `d0=0,v0=1`, yielding `pi/omega` as first positive zero after source.

This is exact ODE algebra within constant diagonal toy, not arbitrary-spacetime optics or observation.

## Counterexamples and gates

- General `(d0,v0)` introduces phase and moves first positive zero within an oscillation period.
- For any target in `(0,pi/omega)`, choose `v0=-omega d0/tan(omega target)`.
- Overall common scaling of `(d0,v0)` leaves zeros unchanged; boundary phase, not amplitude, controls location.
- Zero initial data is trivial solution and not a usable Jacobi channel.
- Thus caustic is geometric only after vertex/source boundary contract and affine normalization are fixed.
- `ell0` remains absent.

## Decision

Status `JACOBI_CAUSTIC_BOUNDARY_PHASE_MOVABLE_NOT_ELL0`. No reformulation: exact varying-matrix and physical source/observer boundary routes remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
