# Exact plane-wave joint window/full-map common-spectrum scale orbit

## Objective and classification

Attack surviving common-canonical route counterexample-first by joining finite-window tidal operator and full Jacobi similarity spectrum:

\[
J_K(L)=\left(LW_K(L),\chi_{P_K(L)}\right),
\qquad
W_K(L)=\int_{-L/2}^{L/2}w(u/L)K(u)\,du.
\]

Raw `W,A,B,C,D` remain primary. Characteristic coefficients are dependent diagnostics of `P`, not independent channels. Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Alternatives considered

1. **Trace-only landmark scan.** Easy, but scalarizes too early and a chosen level crossing depends on target and profile.
2. **Joint raw `W,P` under unrestricted independent endpoint calibration.** Already dominated by `Sp(4)xSp(4)` transitivity and does not test surviving common standard.
3. **Selected: joint dimensionless window operator plus full characteristic polynomial under common canonical calibration.** Preserves matrix window direction and all full-map similarity coefficients, while exposing an exact profile/affine scale orbit without fitted landmarks.

## Exact counterexample

For any `s>0`, define

\[
K_s(u)=s^{-2}K(u/s),\qquad L_s=sL,
\]

with scale-covariant kernel `w(u/L)`. Then

\[
L_sW_{K_s}(L_s)=LW_K(L).
\]

For Jacobi phase space, with

\[
T_s=\operatorname{diag}(s^{-1/2}I,s^{1/2}I),
\]

one has

\[
P_{K_s}(L_s)=T_s^{-1}P_K(L)T_s,
\]

so characteristic polynomial is identical. Therefore full joint curve is reparameterized exactly: each landmark at `L_*` moves to `sL_*` while `J` is unchanged.

Tests cover at least top-hat and triangular scale-covariant kernels, raw block scaling, canonical similarity, joint collision, nonradial window/profile sensitivity, and absence of `ell0`. Kernel shape remains fixed within each comparison; changing kernel is a separate nuisance already known to move responses.

## Interpretation

Expected status: `EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0`.

Open gate: `PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED`.

Result is stronger than testing one crossing: no landmark extracted solely from this joint object can identify absolute support scale along declared orbit. It does not prove no-go for observables carrying independently calibrated dimensional standards, non-scale-covariant causal boundaries, physically fixed profile laws, or other exact geometries. Coley–McNutt–Milson supports exact plane-wave geometry and geodesic deviation, not chosen window/kernel, common detector standard, profile dilation as observational nuisance, UMCH, `ell0`, or detection.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`. No structural dead end.
