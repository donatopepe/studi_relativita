# Exact plane-wave non-vertex Sachs twist boundary

## Raw congruence object

Propagate raw `X,V` from non-vertex boundary `X=I`, `V=S_0` through exact symmetric plane-wave tidal matrix. Away from a caustic define `S=VX^{-1}`. Retain `X,V,S,S_0`; expansion, shear, and twist are dependent decompositions.

For symmetric curvature `K`, antisymmetric Riccati evolution implies conserved twist-area product

`twist(u) det X(u)=twist(u_s) det X(u_s)`.

Nonzero endpoint twist is therefore curvature-propagated within this fixed inertial screen but inherits rotating congruence boundary. Changing boundary twist at fixed profile changes endpoint twist. It is not a profile-only observable.

A later rotating-screen control distinguishes canonical graph `R=P X^{-1}` from velocity Sachs graph `S_rot=X'X^{-1}=R-A`, where `A=Q^TQ'`. Thus the inertial twist-area conservation stated here remains valid in its declared screen, while a varying screen adds a connection-dependent term to velocity-coordinate twist. See `plane-wave-covariant-sachs-screen.md`.

## Orientation and scale quotient

Common oriented screen rotation `SO(2)` preserves twist. A common `O(2)` reflection flips its sign, so oriented interpretation requires physical handedness.

Under affine/profile scaling `K_s(u)=s^{-2}K(u/s)`, `L_s=sL`, scale boundary as `S_{0,s}=S_0/s`. Then `X_s=X`, `V_s=V/s`, `S_s=S/s`; dimensionless `X,LV,LS` and twist-area relation collide. Different profiles remain distinguishable at fixed boundary, but neither absolute scale nor `ell0` follows.

Singular `X` returns `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`; no continuation is assumed.

## Ledger

Classification: `EXACT_SPACETIME_SACHS_BOUNDARY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_NONVERTEX_TWIST_BOUNDARY_PROPAGATED_ORIENTATION_AND_AFFINE_SCALE_CONDITIONAL_NOT_ELL0`.

Open gate: `PHYSICAL_ROTATING_CONGRUENCE_BOUNDARY_PARITY_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Chosen `S_0`, rotating detector congruence, parity anchor, affine/profile nuisance, UMCH, `ell0`, and detection are not source-established.

Physical boundary preparation/covariance, screen handedness, caustic continuation, causal support, detector calibration, independent dimensional standards, and other geometries remain open. This is not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
