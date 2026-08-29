# Exact plane-wave Sachs optical matrix

## Connection-derived object

For vertex Jacobi boundary data and away from a caustic, retain raw full-map blocks `B` and `D` and derive

`S=DB^{-1}`.

Decompose `S` into expansion `theta=tr(S)/2`, symmetric trace-free shear, and antisymmetric twist. No abstract optical profile is inserted. Screen transport uses the declared parallel Brinkmann screen; this is mathematical control, not derived detector tetrad.

The numerical propagation verifies the Riccati equation in the sign convention used by the repository, `S'=-K-S^2`. Singular `B` returns `CAUSTIC_OR_VERTEX_BLOCK_SINGULAR`; no inverse or caustic continuation is inferred.

## Quotients and exact obstruction

Under common `SO(2)` screen rotation, `S -> Q S Q^T`: expansion, shear norm, and oriented twist coefficient are invariant, while shear components rotate.

Observer lower canonical shear calibration gives

`S -> S+H_o`, with symmetric `H_o`.

It moves expansion and shear but preserves antisymmetric twist. Yet for this symmetric tidal equation with vertex boundary, `S` remains symmetric away from caustics, so twist is numerically zero. Thus bounded calibration leaves only a twist invariant that carries no information in this exact class.

Reversal exchanges labelled source/observer optical matrices. Under `K_s(u)=s^{-2}K(u/s)`, `L_s=sL`, one has `S_s=S/s`; dimensionless `LS` and its optical decomposition collide. Absolute affine/profile scale and `ell0` remain absent.

## Ledger

Classification: `EXACT_SPACETIME_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_SACHS_EXPANSION_SHEAR_CALIBRATION_MOVABLE_TWIST_ZERO_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SACHS_ENDPOINT_CALIBRATION_TWIST_SOURCE_AND_ELL0_LAW_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Selected vertex/Sachs detector protocol, endpoint `H_o`, common screen standard, profile scaling as nuisance, UMCH, `ell0`, and detection are not source-established.

Rotating or non-vertex congruences, physical screen transport, caustic continuation, causal windows, detector-derived calibration, independent dimensional standards, and other exact geometries remain open. This is not a structural dead end.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.
