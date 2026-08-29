# Exact plane-wave full Jacobi-map quotient gate

## Objective

Extend the exact Brinkmann plane-wave cross-channel record from `(W,B)` to the full Jacobi phase-space propagator

\[
P(L)=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad
\binom{\xi_o}{\dot\xi_o}=P(L)\binom{\xi_s}{\dot\xi_s},
\]

using the same centered affine interval, parallel screen, self-adjoint optical tidal matrix, and fixed affine normalization. Test counterexample-first whether derivative blocks recover profile order after the physically general independent endpoint-frame quotient, and whether they break affine/profile scale degeneracy.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Candidate routes

1. **Only spectra/SVD of all four blocks.** Too coarse and not guaranteed to encode block relations.
2. **Full raw map with independent endpoint rotations.** Selected. Endpoint frames act by phase-space lifts `P -> diag(Q_o,Q_o) P diag(Q_s^T,Q_s^T)`. Reversal reciprocity must be tested on all blocks.
3. **Derived optical matrices `B^{-1}A` and `DB^{-1}`.** Selected where `B` is invertible. These preserve endpoint-local conjugacy classes and expose whether reversal swaps source and observer optical data rather than erasing all history.

## Exact claims to test

For continuous real symmetric `K(u)` and reversed profile `K_rev(u)=K(-u)`, reciprocity predicts

\[
P_{rev}=E P^T E
=\begin{pmatrix}D^T&B^T\\C^T&A^T\end{pmatrix},
\qquad E=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]

Therefore derivative blocks do add raw endpoint information: `A_rev=D^T`, `D_rev=A^T`, `C_rev=C^T`, `B_rev=B^T`. But an **unlabelled endpoint-swap quotient** erases reversal by construction. With labelled source and observer endpoints, source/observer optical conjugacy spectra can differ and reversal swaps them; this identifies profile orientation only conditionally on boundary labels, affine normalization, and endpoint calibration.

Under `L2=sL1`, `K2(u)=K1(u/s)/s^2`, block dimensions scale as

\[
A_2=A_1,\quad B_2=sB_1,\quad C_2=C_1/s,\quad D_2=D_1.
\]

Thus the dimensionless full map `[[A,B/L],[LC,D]]` is unchanged. Full derivative data do not restore absolute support scale and introduce no `ell0`.

## Required controls and limits

- Numerically verify full block reciprocity and symplectic residuals.
- Verify generic labelled endpoint optical spectra differ and reversal swaps them.
- Verify endpoint-swap quotient makes reversal records equivalent.
- Verify dimensionless full-map affine/profile rescaling identity.
- Preserve raw blocks in deterministic JSON; scalar spectra are dependent diagnostics.
- State that Coley–McNutt–Milson supports exact vacuum plane-wave/geodesic-deviation context only, not selected window, boundary, quotient, detector observability, UMCH, `ell0`, or detection.
- Produce semantically aligned English/Italian audits.

## Decision

Expected bounded result: full Jacobi derivative blocks conditionally retain labelled-endpoint profile orientation but remain reversal-blind after endpoint swap and affine-scale blind after dimensionless rescaling. This is not a structural dead end: physical endpoint labels/calibration, causal windows, full Sachs observables, and other exact geometries remain open.
