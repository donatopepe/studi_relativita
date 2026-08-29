# Exact plane-wave common canonical spectrum gate

## Objective

Follow the surviving route after independent `Sp(4)xSp(4)` transitivity: assume one common physically shared canonical calibration, so

\[
P\mapsto GPG^{-1},\qquad G\in Sp(4,\mathbb R).
\]

Test whether similarity invariants of the exact full Jacobi map provide an absolute support-scale landmark or `ell0`, counterexample-first.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Candidate observable

Use the channel-native characteristic polynomial of the dimensionless phase-space map, not four independent block scalars. In four dimensions, record trace, determinant, and characteristic coefficients. Symplecticity constrains determinant to one and reciprocal eigenvalue structure, but trace can vary with profile and window.

## Exact nuisance tests

1. **Common canonical calibration.** Similarity preserves characteristic polynomial exactly.
2. **Profile reversal.** Reciprocity gives `P_rev=E P^T E`; transpose and similarity preserve characteristic polynomial, so full-map spectrum is reversal-blind.
3. **Affine/profile scaling.** For `L2=sL1`, `K2(u)=K1(u/s)/s^2`, normalized maps are related by the canonical scaling

\[
T_s=\operatorname{diag}(s^{-1/2}I,s^{1/2}I),
\qquad P_2=T_s^{-1}P_1T_s.
\]

Hence the characteristic polynomial is unchanged and absolute `L` is nonidentifiable.
4. **Profile amplitude/frequency.** Trace crossings or extrema may move under profile parameters. A numerical exact-plane-wave family must demonstrate that any candidate spectral landmark belongs to geometry/profile unless a law ties profile to `ell0`.

## Expected interpretation

Common calibration preserves nontrivial profile information, unlike independent endpoint calibration. But reversal and affine scaling remain exact collisions. Characteristic landmarks can diagnose exact optical geometry conditionally; they do not identify absolute support scale or `ell0` without a physical profile/scale law.

Expected status: `EXACT_PLANE_WAVE_COMMON_CANONICAL_SPECTRUM_PROFILE_INFORMATIVE_REVERSAL_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_COMMON_CANONICAL_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

The canonical source supports exact plane-wave geometry and geodesic deviation, not common detector calibration, finite-window spectrum protocol, UMCH, `ell0`, or detection. Other exact geometries, physically selected windows, causal support, detector standards, and cross-channel laws remain open. This is not a structural dead end.

UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.
