# Exact plane-wave common canonical spectrum

## Raw map and common standard

Retain raw full Jacobi map

\[
P=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in Sp(4,\mathbb R).
\]

Assume one shared canonical phase-space standard at source and observer. Calibration acts by

`P -> GPG^{-1}`.

The channel-native similarity object is the characteristic polynomial of `P`. For a four-dimensional symplectic map it is palindromic: determinant is one and first/third coefficients agree. Common conjugation preserves all coefficients.

## Exact collisions and surviving information

For profile reversal, reciprocity gives

`P_rev=E P^T E`.

Transpose and similarity preserve the characteristic polynomial, so the spectrum is reversal-blind even when raw maps differ.

Under `L2=sL1`, `K2(u)=K1(u/s)/s^2`, define canonical scaling

\[
T_s=\operatorname{diag}(s^{-1/2}I,s^{1/2}I).
\]

Then

\[
P_2=T_s^{-1}P_1T_s.
\]

Thus affine/profile scaling leaves the characteristic polynomial unchanged. Absolute support scale is absent.

Different exact tidal profiles can have different characteristic polynomials. Common-canonical spectrum is therefore profile-informative, unlike the quotient under independent endpoint `Sp(4)xSp(4)`. But this is conditional geometric information: reversal and affine scale lie in its null space, and profile parameters can move spectral landmarks.

## Ledger

Status: `EXACT_PLANE_WAVE_COMMON_CANONICAL_SPECTRUM_PROFILE_INFORMATIVE_REVERSAL_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Open gate: `PHYSICAL_COMMON_CANONICAL_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

Raw `A`, `B`, `C`, `D` remain primary. Characteristic coefficients are dependent diagnostics, not independent channels. Coley–McNutt–Milson (2012) supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Common canonical detector standard, finite-window spectral protocol, profile law, UMCH, `ell0`, and detection are project derivations or claims, not source-established.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`. Physical common standards, causal windows, transport, full Sachs observables, profile-scale laws, and other exact geometries remain open. This is not a structural dead end.
