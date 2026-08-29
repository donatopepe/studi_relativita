# Exact plane-wave finite-window/non-vertex Sachs joint quotient

## Question

Can joining a dimensionless finite-window tidal matrix with rotating-congruence Sachs data remove boundary and affine/profile degeneracies?

## Primary joint object

Retain raw channel-native objects

\[
\mathcal J_K(L,S_0)=\bigl(LW_K(L),X(L),LV(L),LS(L),LS_0\bigr),
\qquad S=VX^{-1},
\]

plus declared kernel, centered support, parallel screen, and non-vertex boundary. Twist-area is a dependent diagnostic, not an independent channel.

## Alternatives

1. Join only scalar twist and window norm: rejected because it discards matrices and creates false channel independence.
2. Hold boundary fixed under affine scaling: dimensionally inconsistent because `S_0` has units `1/L`.
3. Selected: test raw joint object with top-hat and triangular kernels under dimensionally correct affine/profile/boundary orbit, then test boundary mobility at fixed curvature window.

## Counterexample-first derivation

For

\[
K_s(u)=s^{-2}K(u/s),\quad L_s=sL,\quad S_{0,s}=S_0/s,
\]

and scale-covariant kernel,

\[
L_sW_{K_s}(L_s)=LW_K(L),
\quad X_s=X,
\quad L_sV_s=LV,
\quad L_sS_s=LS,
\quad L_sS_{0,s}=LS_0.
\]

Thus entire declared raw joint object collides. A landmark coordinate extracted only from it moves `L_* -> sL_*`.

At fixed `K,L,kernel`, varying boundary twist changes `X,V,S` and endpoint twist while finite-window matrix is unchanged. Therefore cross-channel joining does not by itself separate profile geometry from congruence preparation.

Different profile shapes at fixed boundary can remain distinguishable. Result is not a no-go against detector-derived boundary standards, causal non-scale-covariant support, or independent dimensional calibration.

## Ledger

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_SACHS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Expected status: `EXACT_PLANE_WAVE_WINDOW_SACHS_TWIST_JOINT_PROFILE_AND_BOUNDARY_CONDITIONAL_AFFINE_ORBIT_NOT_ELL0`.

Open gate: `PHYSICAL_CAUSAL_WINDOW_ROTATING_BOUNDARY_COMMON_SCREEN_AND_ELL0_LAW_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation, not chosen finite window/kernel, rotating boundary, common detector screen, profile/boundary scaling nuisance, UMCH, `ell0`, or detection.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`. Not a structural dead end.
