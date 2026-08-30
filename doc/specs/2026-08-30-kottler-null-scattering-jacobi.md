# Kottler finite-boundary neutral-null scattering/Jacobi counterexample gate

Date: 2026-08-30  
Status: `RATIFIED_FOR_BOUNDED_IMPLEMENTATION`  
Authorization: repeated binding autonomous-loop instruction received after design presentation; conservative implementation authorized without subagents  
Primary object: channel-native optical profile and full `4x4` Jacobi phase map  

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
maximum_interpretation=CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

## 1. Question

Test a bounded nonradial exact-geometry control in Kottler (Schwarzschild–de Sitter) spacetime. Does a nonzero cosmological-curvature scale add an internally identifiable absolute scale to finite-boundary neutral-null Jacobi response, or only a dimensionless shape parameter plus an imported dimensional standard?

This is a counterexample-first continuation of Schwarzschild and Reissner–Nordström controls. It does not derive an UMCH law or identify `ell0`.

## 2. Alternatives considered

1. **Kottler finite-boundary null scattering — selected.** Sharp test of wrong-observable risk: the spacetime has nonzero Ricci curvature, but Einstein-space Ricci contraction along a null tangent vanishes, while the coordinate orbit equation loses explicit `Lambda`. Finite static boundaries and the full optical map retain enough structure to audit what survives.
2. **Kerr equatorial scattering — deferred.** Adds frame dragging and genuine orientation asymmetry, but tetrad/screen transport and endpoint-frame conventions create a wider sign and gauge surface before the current absolute-scale question is isolated.
3. **RN source/receiver microphysics — deferred.** Directly attacks an open physical gate, but no bounded canonical source, detector, calibrated-noise, or joint-covariance model is presently supplied; inventing one is forbidden.

## 3. Scope and domain

Use geometric units and the static Kottler chart

\[
 f(r)=1-\frac{2M}{r}-\frac{\Lambda r^2}{3},
 \qquad
 ds^2=f\,dt^2-f^{-1}dr^2-r^2d\Omega^2.
\]

Define dimensionless quantities

\[
 x=r/M,\quad \alpha=\Lambda M^2,\quad \beta=b/M,\quad
 f(x)=1-\frac2x-\frac{\alpha x^2}{3}.
\]

Bounded baseline domain:

```text
M>0
alpha>=0
rho>3
R>rho
f(r)>0 for every path sample in [rho M,R M]
neutral future-directed equatorial null ray
finite equal-radius static-chart endpoints
one radial turning point
unit Killing-energy normalization only as a declared toy control
screen_order=(polar,in-plane)
```

No asymptotic observer, detector, source spectrum, physical clock, or cosmological matching is implied. Negative `Lambda`, horizon-crossing windows, charged rays, multiple turning points, and nonstatic endpoint worldlines are out of scope.

## 4. Source scope

Rindler and Ishak, *Phys. Rev. D* **76**, 043006 (2007), arXiv:0709.2948, is the canonical anchor restricted to:

- Kottler metric and `f(r)` (their equations 1–2);
- exact equatorial null coordinate orbit equation `u''+u=3Mu^2` (their equation 7), in which `Lambda` is absent;
- distinction between coordinate path and locally measured angle.

The source does **not** establish this project's finite-window boundary choice, screen basis, direct Riemann projection, Jacobi integration, frequency conversion, rank audit, `ell0`, UMCH, covariance, evidence, or detection.

## 5. Classified mathematical contract

### `KNOWN_RESULT`

- Kottler metric above.
- Equatorial neutral-null coordinate orbit equation has no explicit `Lambda` after differentiation.
- Kottler is an Einstein space: `R_mn=Lambda g_mn`; hence `R_mn k^m k^n=0` for null `k`.

### `PROJECT_DERIVATION`

- Determine turning relation from
  \[
  (dr/d\lambda)^2=1-b^2f(r)/r^2,
  \qquad
  \beta=\rho/\sqrt{f(\rho)}.
  \]
- Regularize the turning point with `x=rho+y^2`.
- Reconstruct Christoffel and Riemann tensors directly from metric derivatives.
- Project
  \[
  \mathcal K_{AB}=R_{\mu\nu\rho\sigma}e_A^\mu k^\nu e_B^\rho k^\sigma
  \]
  in declared screen order.
- Propagate the full phase map
  \[
  P'=\begin{pmatrix}0&I\\-\mathcal K&0\end{pmatrix}P,
  \qquad P(0)=I_4.
  \]
- Treat graph objects only where required blocks are invertible.

### `TOY_CONTROL`

Finite equal-radius endpoints, static-chart Killing normalization, numerical screen preparation, positive/negative orientation labels, and endpoint frequency-conversion similarity are mathematical controls, not detector derivations.

### `NEGATIVE_RESULT` targets

- `NULL_RICCI_FOCUSING_IN_EINSTEIN_SPACE_NOT_ZERO_SPACETIME_RICCI` if direct contraction is numerically zero while spacetime Ricci is nonzero.
- `KOTTLER_COORDINATE_ORBIT_LAMBDA_CANCELLATION_NOT_OPERATOR_SCALE_IDENTIFICATION` if coordinate path cancellation coexists with boundary/normalization dependence.
- `JOINT_M_LAMBDA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE` under
  \[
  (M,r,b,\lambda,\Lambda)\mapsto(sM,sr,sb,s\lambda,\Lambda/s^2),
  \]
  which fixes `alpha=Lambda M^2`.
- `FIXED_EXTERNAL_LAMBDA_IS_IMPORTED_DIMENSIONAL_STANDARD_NOT_ELL0` if holding dimensional `Lambda` externally known makes `M` recoverable from `alpha`.

### `OPEN_PROBLEM`

Physical cosmological matching, source/emitter, absorber, endpoint tetrad/screen preparation, absolute-frequency realization, receiver transfer, calibrated noise, joint covariance, and any geometry-to-`ell/ell0` law remain underived.

## 6. Counterexample-first tests

Tests must fail before implementation and then cover:

1. domain and static-patch rejection;
2. path and turning residuals;
3. screen orthonormality and null orthogonality;
4. direct Riemann projection versus profile used by integrator;
5. nonzero spacetime Ricci diagnostics but vanishing null Ricci optical trace;
6. `alpha=0` conformance with existing Schwarzschild scattering;
7. `M=0` is not taken through dimensionless `x=r/M`; pure de Sitter is a separate analytic null-focusing control;
8. zero-window identity;
9. orientation reversal comparison without claiming physical endpoint calibration;
10. full-map symplectic/conformance residuals;
11. joint dilation after declared frequency conversion;
12. local Jacobian rank in `(log M, alpha)` with exact scale-null representative;
13. fixed-dimensional-`Lambda` audit explicitly labeled imported standard;
14. deterministic `.8g` JSON rendering and bilingual report parity.

Passing tolerances establishes only implementation conformance.

## 7. Primary record

Preserve, append-only:

```text
R_Kottler=(path_samples,screen_samples,K_raw,Ricci_tensor,
           null_Ricci_trace,K_tracefree,P_full,graph_validity,
           orientation_control,Schwarzschild_limit,
           geometric_dilation,fixed_Lambda_control,rank_control)
```

Ricci tensor, null Ricci contraction, and trace-free optical profile are parts of one curvature record, not statistically independent channels. More matrix entries or local rank do not imply physical or global identifiability.

## 8. Decision rule

Expected bounded classification if all tests pass:

```text
KOTTLER_LAMBDA_ADDS_STATIC_BOUNDARY_AND_DIMENSIONLESS_OPTICAL_SHAPE_BUT_NULL_RICCI_FOCUSING_COORDINATE_ORBIT_CANCELLATION_AND_JOINT_MLAMBDA_DILATION_DO_NOT_IDENTIFY_ELL0
```

This wording must be narrowed if direct projection shows no `alpha` dependence after the declared conversion. Any dependence on fixed dimensional `Lambda` must be reported as an external standard, never an internally derived scale or `ell0`.

Structural-dead-end criteria are not met: Kerr orientation/frame-dragging controls and physical source/receiver derivations remain open. No reformulation candidate is authorized by this increment.

## 9. Deliverables and review

After ratification: implementation plan, source tests and verification log, numerical tests, deterministic artifact, theory note, bilingual EN/IT audits, roadmap update, focused and cross-control suites, full discovery, artifact/tool checks, `git diff --check`, direct closure review, PR, green `tests`/`latex`, conservative merge only if unambiguous, post-merge CI, Hermes Inbox note, and cleanup.

Because subagents are forbidden, review status is `DIRECT_REVIEW_NO_SUBAGENT`, never independent review.
