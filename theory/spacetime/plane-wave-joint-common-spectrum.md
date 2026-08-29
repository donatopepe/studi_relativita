# Exact plane-wave joint window/full-map common spectrum

## Channel-native object

Retain raw finite-window operator `W` and full Jacobi blocks `A`, `B`, `C`, `D`. Under a physically shared canonical endpoint standard, use characteristic polynomial of

\[
P=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\]

as dependent similarity diagnostic, not separate evidence. Joint dimensionless object is

\[
J_K(L)=\left(LW_K(L),\chi_{P_K(L)}\right).
\]

Both top-hat and triangular kernels are tested with fixed centered support and vertex Jacobi boundary data.

## Exact profile/affine orbit

For `s>0`, define

`K_s(u)=s^{-2}K(u/s)` and `L_s=sL`.

For any scale-covariant kernel `w(u/L)`, direct substitution gives

\[
L_sW_{K_s}(L_s)=LW_K(L).
\]

With `T_s=diag(s^{-1/2}I,s^{1/2}I)`, Jacobi blocks scale as

\[
A_s=A,\quad B_s=sB,\quad C_s=C/s,\quad D_s=D,
\]

and

\[
P_{K_s}(L_s)=T_s^{-1}P_K(L)T_s.
\]

Hence characteristic polynomial and entire joint object collide exactly. Same response landmark coordinate moves from `L_*` to `sL_*`. Different profiles can still change both window matrix and spectrum, so joint object is conditionally profile-informative but not absolute-scale-identifying.

## Ledger and scope

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0`.

Open gate: `PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED`.

Coley–McNutt–Milson (2012) supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Chosen finite window, top-hat/triangular kernels, common detector standard, profile dilation as nuisance, UMCH, `ell0`, and detection are not source-established.

This exact orbit does not cover independently calibrated dimensional standards, non-scale-covariant causal boundaries, physically fixed profile-scale laws, detector-derived calibration, or other geometries. These routes remain open; this is not a structural dead end.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.
