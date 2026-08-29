# Exact plane-wave endpoint shear-calibration quotient

## Objective

Attack the conditional labelled-endpoint route left by the full Jacobi-map control. Keep the same exact Brinkmann plane-wave profile, centered affine interval, parallel screen, raw symplectic propagator

\[
P=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\]

and source/observer labels. Add only endpoint-local canonical shear calibrations and test whether spectra of `B^{-1}A` and `DB^{-1}` remain identifiable.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Bounded nuisance model

For symmetric two-by-two matrices `H_s,H_o`, use

\[
S(H)=\begin{pmatrix}I&0\\H&I\end{pmatrix},\qquad S(H)^T\Omega S(H)=\Omega.
\]

The calibrated map is

\[
P'=S(H_o)P S(H_s)^{-1}.
\]

This models endpoint-local mixing of displacement into derivative while preserving endpoint labels and symplectic structure. It is a project nuisance model, not a detector model derived from the canonical plane-wave source.

## Exact predictions

Block algebra gives

\[
A'=A-BH_s,\quad B'=B,\quad
C'=C+H_oA-(D+H_oB)H_s,\quad D'=D+H_oB.
\]

Therefore

\[
B^{-1}A'=B^{-1}A-H_s,\qquad D'(B')^{-1}=DB^{-1}+H_o.
\]

Independent free symmetric endpoint shears can move both endpoint optical matrices and their spectra arbitrarily within this additive nuisance action. Scalar choices `H_s=h_s I`, `H_o=h_o I` shift eigenvalues without changing eigenvalue gaps; general symmetric shears can also change gaps and eigenframes. Labels alone are insufficient without independently fixed derivative/displacement calibration.

Affine/profile rescaling remains exact and no `ell0` occurs.

## Falsification and stop conditions

Tests must fail if endpoint shear is not symplectic, block formulas disagree with direct multiplication, optical matrices do not obey additive transformations, spectral landmarks remain invariant under general shears, or deterministic output changes.

This result does not prove every full-map invariant is erased: `B` is unchanged by these shears, endpoint rotations and other calibration mixing require a joint quotient, and physical detector calibration remains open. Therefore this is not a structural dead end.

Expected status: `EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0`.

Open gate: `PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED`.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.
