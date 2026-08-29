# Exact plane-wave screen-transport/window/Jacobi order control

## Question

In the exact Brinkmann plane-wave tidal channel, does a scale-dependent screen rotation inside a finite window create intrinsic operator nonradiality, and does averaging before versus after transport retain equivalent Jacobi information?

## Approaches considered

1. **Constant endpoint rotation only.** Pure conjugation is already covered and cannot test transport variation within support.
2. **Abstract two-matrix toy.** Already demonstrates noncommutation but lacks connection-derived plane-wave curvature.
3. **Selected: prescribed screen connection over exact curvature profile.** Use exact plane-wave tidal matrix `K(u)` and a declared `SO(2)` screen connection `omega(u)J`. Parallel transport to window center gives `Q(u)`. Compare raw coordinate average, transport-to-center average, average of local invariants, and Jacobi maps generated from raw versus transported profiles.

The screen connection is a project protocol input, not derived from a detector or from the canonical source. This study tests order dependence in an exact spacetime curvature profile, not a physical screen prescription.

## Objects and conventions

For centered support `[-L/2,L/2]`, kernel `w_L(u)`, and

\[
Q'(u)=-\omega(u)JQ(u),\qquad Q(0)=I,
\]

retain

\[
W_{\rm raw}=\int w_L K\,du,
\qquad
W_{\rm tr}=\int w_L Q^TKQ\,du,
\]

local invariant averages `(average trace, average determinant, average Frobenius norm squared)`, and full phase-space propagators

\[
P_{\rm raw}[K],\qquad P_{\rm tr}[Q^TKQ].
\]

Top-hat and triangular kernels remain explicit. `W_raw`, `W_tr`, and invariant averages are not treated as independent channels.

## Counterexample-first tests

- `omega=0` must collapse raw and transported profiles, windows, and propagators.
- Nonconstant `omega` must generally make averaging and transport noncommutative: `W_raw != W_tr` and `P_raw != P_tr`.
- Pointwise trace, determinant, eigenvalues, and Frobenius norm must be preserved under orthogonal transport; their window averages cannot reconstruct `W_tr` or `P_tr`.
- A constant common change of center screen basis must conjugate `W_tr` and induce canonical similarity of `P_tr`; spectra/characteristic polynomial remain fixed.
- Under affine/profile/connection scaling
  \[
  K_s(u)=s^{-2}K(u/s),\quad \omega_s(u)=s^{-1}\omega(u/s),\quad L_s=sL,
  \]
  dimensionless `LW_tr` and characteristic polynomial of `P_tr` collide. Transport order does not recover absolute scale.
- Different transport profiles at fixed curvature and support can move matrix entries and Jacobi spectrum; this is protocol dependence, not `ell0`.

## Interpretation

Classification: `EXACT_SPACETIME_TRANSPORT_WINDOW_JACOBI_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Expected status: `EXACT_PLANE_WAVE_SCREEN_TRANSPORT_AVERAGE_ORDER_OPERATOR_AND_JACOBI_PROTOCOL_DEPENDENT_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SCREEN_CONNECTION_PATH_KERNEL_AND_COMMON_ENDPOINT_STANDARD_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish the chosen screen connection, finite-window kernel, transport path/anchor, endpoint detector standard, affine/profile/connection scaling law, UMCH, `ell0`, or detection.

Physical Fermi/parallel screen transport derived from source/observer tetrads, causal support, independent calibration, nontrivial spacetime paths, and other geometries remain open. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
