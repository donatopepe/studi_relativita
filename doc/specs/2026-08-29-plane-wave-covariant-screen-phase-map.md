# Covariant rotating-screen phase-map correction in an exact plane wave

## Problem

The previous exact-plane-wave transport control correctly compared curvature operators `K` and `Q^T K Q` under a declared screen rotation, but its object called `P_transport` propagated `Q^T K Q` with the inertial Jacobi equation. That is not the phase-space propagator in rotating screen coordinates when `Q(u)` varies. Connection terms are required.

This iteration preserves the previous negative result and corrects the interpretation before using it further.

## Approaches

1. Keep propagating only `Q^T K Q`: rejected as a covariant rotating-coordinate map because it omits first-derivative and connection-potential terms.
2. Numerically differentiate `Q`: avoidable and less auditable for the analytic `SO(2)` connection.
3. Selected: derive exact rotating-screen first-order generator and independently verify endpoint graph transformation.

## Exact derivation

Let inertial screen displacement satisfy

`y''=-K(u)y`,

and set `y=Q(u)x`, with

`Q'=Q A`, `A=Q^T Q'= -omega(u) J`, `A'=-omega'(u)J`.

Then

`x''=-2 A x'-(Q^T K Q+A'+A^2)x`.

For `z_x=(x,x')`, retain the channel-native generator

`M_x=[[0,I],[-(Q^T K Q+A'+A^2),-2A]]`.

The phase-space state transformation is

`z_y=G(u)z_x`, `G(u)=[[Q,0],[Q A,Q]]`.

Thus the exact endpoint relation is

`P_x(u_o,u_s)=G(u_o)^-1 P_y(u_o,u_s) G(u_s)`.

## Counterexample-first controls

- `omega=0`: `P_x=P_y` and all connection terms vanish.
- Varying `omega`: direct integration of `M_x` must agree with endpoint graph transformation.
- Naive propagation using only `Q^T K Q` must differ from covariant `P_x`; this explicitly bounds the old interpretation.
- A constant common screen rotation must act by canonical similarity and preserve characteristic coefficients.
- Reanchoring the same physical `Q(u)` by a constant right basis rotation must change raw coordinates only, not the characteristic polynomial.
- Under `K_s=s^-2K(u/s)`, `omega_s=s^-1omega(u/s)`, `L_s=sL`, the dimensionless phase relation and characteristic polynomial remain scale-blind.
- Source/observer endpoint labels and `G_s,G_o` remain explicit; omitting endpoint angular velocity is prohibited.

## Classification and disposition

Classification: `EXACT_SPACETIME_COVARIANT_SCREEN_PHASE_MAP_CORRECTION_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_CONNECTION_TERMS_REQUIRED_NAIVE_TRANSPORTED_JACOBI_MAP_SUPERSEDED_NOT_ELL0`.

Correction disposition: the PR #76 finite-window operator result, invariant-average insufficiency, protocol mobility, and affine collision remain valid for `W_transport`. Its `P_transport` is relabelled `P_naive_conjugated_profile`; any claim that it was the rotating-coordinate Jacobi propagator is superseded. The corrected `P_covariant` obeys the endpoint graph law.

Open gate: `PHYSICAL_SCREEN_CONNECTION_ENDPOINT_ANGULAR_VELOCITY_AND_DETECTOR_PHASE_VARIABLES_NOT_DERIVED`.

Coley–McNutt–Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish this chosen rotating screen, detector phase variables, endpoint angular velocities, finite window/kernel, affine nuisance law, UMCH, `ell0`, or detection.

Physical tetrads, Fermi/parallel transport, detector displacement/derivative calibration, causal windows, and nontrivial spacetime paths remain open. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
