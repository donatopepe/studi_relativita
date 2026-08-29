# Exact plane-wave full Jacobi-map quotient

## Channel-native propagator

For the exact Brinkmann plane-wave optical tidal matrix `K(u)`, retain the full phase-space propagator

\[
P(L)=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
(\xi_o,\dot\xi_o)^T=P(L)(\xi_s,\dot\xi_s)^T,
\]

on a centered affine interval with parallel screen and fixed affine normalization. `B` is the vertex displacement block already studied; `A`, `C`, and `D` retain derivative/boundary response. The numerical control verifies the symplectic identity `P^T Omega P=Omega`.

For a real symmetric profile and `K_rev(u)=K(-u)`, exact reciprocity is

`P_rev=E P^T E`,

so

\[
A_{rev}=D^T,\quad B_{rev}=B^T,\quad C_{rev}=C^T,\quad D_{rev}=A^T.
\]

## Labelled endpoints versus endpoint swap

Where `B` is invertible, define endpoint-local optical matrices `B^{-1}A` and `DB^{-1}`. Their conjugacy spectra are generally different for the asymmetric exact profile. Reversal swaps source and observer spectra. Therefore the full map retains conditional profile-order information if source and observer are physically labelled and calibrated.

If the nuisance quotient permits endpoint swap, the reversal map is exactly identified with the forward map by `P -> E P^T E`. Order is then nonidentifiable. This quotient differs from independent endpoint rotations: the latter act by phase-space lifts of `SO(2) x SO(2)`, while endpoint swap exchanges boundary roles.

## Affine/profile scaling

For `L2=sL1`, `K2(u)=K1(u/s)/s^2`,

\[
A_2=A_1,\quad B_2=sB_1,\quad C_2=C_1/s,\quad D_2=D_1.
\]

Hence `[[A,B/L],[LC,D]]` is unchanged. Derivative blocks do not restore absolute support scale. No `ell0` occurs.

## Ledger

Status: `EXACT_PLANE_WAVE_FULL_JACOBI_LABELLED_ENDPOINT_ORDER_CONDITIONAL_SWAP_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0`.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Open gate: `PHYSICAL_ENDPOINT_LABELS_AND_CALIBRATION_NOT_DERIVED`.

Raw `A`, `B`, `C`, `D` remain primary; endpoint spectra are dependent diagnostics. Brinkmann parallel-screen coordinates and chosen vertex/full-map boundary convention do not derive source/observer labels, tetrad calibration, measured derivative component, causal support, detector response, or leakage model. UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.

Canonical source scope is exact vacuum plane waves and curvature-driven geodesic deviation. Full-map protocol, boundary labels, endpoint-swap quotient, finite window, detector observability, UMCH, `ell0`, and detection are project derivations or claims, not established by that source.
