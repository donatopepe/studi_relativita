# Exact plane-wave endpoint shear-calibration quotient

## Raw channel and nuisance

Retain the exact Brinkmann plane-wave Jacobi propagator

\[
P=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\]

with labelled source and observer endpoints. Test endpoint-local canonical shears

\[
S(H)=\begin{pmatrix}I&0\\H&I\end{pmatrix},\qquad H=H^T,
\]

which mix displacement into derivative and preserve `S(H)^T Omega S(H)=Omega`. The calibrated raw map is

`P'=S(H_o)P S(H_s)^{-1}`.

Direct multiplication gives

\[
A'=A-BH_s,\quad B'=B,\quad D'=D+H_oB,
\]
\[
C'=C+H_oA-(D+H_oB)H_s.
\]

This action preserves endpoint labels and symplecticity. It is a bounded project nuisance model, not a physical detector calibration derived from the plane-wave source.

## Endpoint optical spectra

Where `B` is invertible,

\[
(B')^{-1}A'=B^{-1}A-H_s,
\qquad
D'(B')^{-1}=DB^{-1}+H_o.
\]

Thus independent free symmetric endpoint shears move source and observer optical matrices. General shears change spectra, gaps, and eigenframes. Scalar shears shift both eigenvalues while preserving gaps. Labelled endpoint optical spectra therefore do not remain identified unless phase-space calibration is independently fixed.

This quotient does not erase every full-map invariant: `B` is unchanged. It is not a proof against joint invariants under a physically derived restricted calibration group. Endpoint rotations, transport, leakage, detector response, and measured derivative variables remain open.

Under affine/profile scaling, `H` has dimension `1/L`; scaling it accordingly preserves the dimensionless calibrated map. Absolute scale remains unidentified and no `ell0` occurs.

## Ledger

Status: `EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0`.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Open gate: `PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED`.

Raw `A`, `B`, `C`, `D` remain primary. Coley–McNutt–Milson (2012) supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Endpoint shear nuisance, calibration group, detector response, UMCH, `ell0`, and detection are project derivations or claims, not source-established.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`. Other calibration groups, full Sachs observables, causal windows, transport, and exact geometries remain open, so this is not a structural dead end.
