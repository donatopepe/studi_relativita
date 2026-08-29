# Exact plane-wave Sachs twist from non-vertex boundary data

## Question

Previous vertex control leaves only twist invariant under symmetric observer endpoint shear, but twist is zero. Test whether non-vertex rotating congruence boundary data create connection-propagated twist, and whether that recovers profile scale or `ell0`.

## Objects and boundary

Propagate a Jacobi matrix `X` and derivative `V` through the same exact symmetric plane-wave tidal profile:

\[
X''=-K(u)X,
\qquad X(u_s)=I,
\qquad V(u_s)=S_0=\theta_0 I+\sigma_0+\omega_0J.
\]

Away from `det X=0`, define `S=VX^{-1}` and retain raw `X,V,S`. Boundary parameters are declared nuisance candidates, not source-derived detector values.

## Alternatives

1. Treat nonzero twist as positive new channel: rejected before identifiability checks.
2. Restrict to vertex data: already proves twist-free subclass only.
3. Selected: vary rotating non-vertex boundary, derive exact evolution, then test boundary mobility, affine/profile scaling, screen orientation, and profile sensitivity.

## Counterexample-first expectations

For symmetric `K`, antisymmetric part of Riccati equation obeys homogeneous transport. In two screen dimensions, twist is expected to follow

\[
\omega(u)\det X(u)=\omega_0\det X(u_s),
\]

up to sign convention. Therefore nonzero endpoint twist may mainly encode initial congruence boundary data and area expansion. Varying `omega_0` can move endpoint twist without changing spacetime profile.

Common `SO(2)` preserves oriented twist; common `O(2)` reflection flips it. Under affine/profile dilation, dimensionful optical matrix scales as `S_s=S/s` if boundary `S_{0,s}=S_0/s`; hence `LS`, dimensionless boundary `LS_0`, and twist-area law collide.

Different profiles at fixed boundary may still change raw `X,V,S`, so this test is not expected to erase all profile information. It targets absolute-scale and boundary identifiability.

## Ledger

Classification: `EXACT_SPACETIME_SACHS_BOUNDARY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Expected status: `EXACT_PLANE_WAVE_NONVERTEX_TWIST_BOUNDARY_PROPAGATED_ORIENTATION_AND_AFFINE_SCALE_CONDITIONAL_NOT_ELL0`.

Open gate: `PHYSICAL_ROTATING_CONGRUENCE_BOUNDARY_PARITY_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation, not chosen rotating boundary data, detector congruence, parity anchor, profile-scale nuisance, UMCH, `ell0`, or detection.

Causal source preparation, detector-defined boundary covariance, physical screen handedness, caustic continuation, independently calibrated scale, and other exact geometries remain open. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
