# Finite source–probe localization on compact `S1`

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human ratified the complete specification on 2026-08-31. Human selected the finite-localization route, distinct finite source/probe widths, coincident and separated circle centers, and a pointlike three-dimensional source. Human also authorized automatic selection of explicitly recommended options; therefore this MVP selects the already recommended radial-shell window and all conservative recommendations below. Ratification authorizes implementation planning; implementation remains gated by the completed sibling plan.

Global state remains:

```text
HIGHER_DIMENSIONAL_GRAVITY_DIRECTION=HUMAN_RATIFIED_RESEARCH_DIRECTION
MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
Maximum interpretation=MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

## MVP-first gate

**Objective:** determine whether finite source and probe localization widths on the compact circle add separately identifiable tidal information or collapse to a combined preparation nuisance in the existing static scalar KK control.

**Metric and threshold:** correctness over ten preregistered analytic/numerical controls; threshold `10/10` controls passing under declared tolerances before any result is accepted.

**Fixed cases and order:** normalization, analytic Fourier coefficients, localized limit, broad-width zero-mode limit, exact uniform control, circle periodicity, static orientation-sign collision, source–probe exchange, equal-combined-width collision, joint scale/rank gate.

**MVP:** pointlike source in ordinary three-space, wrapped-Gaussian source and probe profiles on `S1`, existing scalar mode sum and raw tidal matrix, and existing radial-shell finite window only. No new framework, general spectral API, oriented 3D window rerun, physical localization field, radion, nonlinear 5D dynamics, detector, or data.

**Escalation condition:** add a more general profile family or physical localization dynamics only if this direct wrapped-Gaussian baseline fails a named source, convergence, symmetry, or identifiability control that cannot be corrected within the declared model.

## Bounded question

For static linearized scalar gravity on

\[
\mathcal M_5=\mathbb R^{1,3}\times S^1,
\qquad y\sim y+2\pi L,
\]

do normalized finite source/probe widths `w_s` and `w_p` create independently recoverable structure in the point and radial-shell tidal matrices, or does the response depend only on a combined dimensionless width and even relative circle separation, leaving exact collisions and absolute-scale blindness?

## Alternatives considered

1. **Direct wrapped-Gaussian overlap extension — selected.** Smallest change to the verified compact-circle mode sum. It isolates finite localization and attacks identifiability before adding dynamics.
2. **General arbitrary-profile spectral API — deferred.** More flexible but unnecessary before one analytic profile establishes baseline behavior and exact collisions.
3. **Gauge-fixed tensor/vector/radion perturbations — deferred.** More physical but introduces gauge, couplings, stabilization, and additional degrees of freedom before the preparation degeneracy is measured.
4. **Physical localization mechanism — deferred.** A brane/domain-wall action could derive profiles, but inventing one now would add unsupported parameters and dynamics.
5. **Repeat point/sphere/Gaussian 3D sources and oriented-box windows — rejected for this MVP.** Those controls already passed in the previous increment and would multiply cases without isolating the new `S1` widths.

## Wrapped-Gaussian profile contract

Use a normalized periodic Gaussian on the circle,

\[
\rho(y;y_0,w,L)
=\frac{1}{\sqrt{2\pi}w}
\sum_{k\in\mathbb Z}
\exp\!\left[-\frac{(y-y_0+2\pi kL)^2}{2w^2}\right],
\]

for `w>0`, integrated over any fundamental interval of length `2*pi*L`. The `w->0+` limit is distributional and recovers a localized profile. Exact uniform preparation remains a separate normalized profile `1/(2*pi*L)`; no finite Gaussian width may be mislabeled exactly uniform.

Before implementation, DLMF §1.8(iv), especially Poisson summation (1.8.14), and DLMF §20.2(i), especially the theta-3 Fourier series (20.2.3), must be inspected and source-scoped. Under the declared Fourier convention, the expected project derivation is

\[
\widehat\rho_n
=\int_{0}^{2\pi L}\rho(y)e^{-iny/L}\,dy
=\exp\!\left[-\frac{n^2w^2}{2L^2}\right]e^{-iny_0/L}.
\]

This coefficient is not test authority until independently derived from the normalized image sum and verified against direct quadrature.

The source and probe records remain separate:

```text
source_mode_coefficient=(Re rho_s_n, Im rho_s_n)
probe_mode_coefficient=(Re rho_p_n, Im rho_p_n)
combined_complex_overlap=rho_s_n*conjugate(rho_p_n)
static_real_mode_weight=Re(combined_complex_overlap)
```

With `Delta_y=y_p-y_s`, expected static real weight is

\[
w_n^{\rm static}
=\exp\!\left[-\frac{n^2(w_s^2+w_p^2)}{2L^2}\right]
\cos\!\left(\frac{n\Delta y}{L}\right).
\]

This is a project derivation from the sourced Fourier identities, not a claim of physical matter localization.

## Potential and primary response

For a point source in ordinary three-space, use the existing unit-amplitude static mode convention:

\[
f(r)=\frac1r\left[1+2\sum_{n=1}^{\infty}
w_n^{\rm static}e^{-nr/L}\right],
\qquad \Phi=-A f.
\]

The primary pointwise record remains the full raw Hessian

\[
T_{ij}=\partial_i\partial_j\Phi
=T_\perp(\delta_{ij}-\hat r_i\hat r_j)
+T_\parallel\hat r_i\hat r_j.
\]

Potential and radial gradient remain auxiliary. Norms, traces, ratios, and rank features are secondary.

The only finite-window MVP is the existing normalized radial shell centered at `r_c` with width `Delta r`, excluding singular support. Its raw averaged matrix remains primary. The zero-width limit must recover the pointwise response.

## Raw record

Each run preserves:

```text
L
r_or_shell_center
shell_width
w_s
w_p
y_s
y_p
Delta_y
source_profile=wrapped_gaussian|localized_limit|uniform
probe_profile=wrapped_gaussian|localized_limit|uniform
source_mode_coefficients
probe_mode_coefficients
combined_complex_overlaps
static_real_mode_weights
mode_truncation
convergence_certificate
T_point_matrix
T_shell_matrix
T_parallel
T_perpendicular
potential_auxiliary
gradient_auxiliary
```

Complex coefficient records are mathematical preparation records, not independently measured channels. The static real tidal response uses their real combined projection.

## Counterexample-first controls

### 1. Normalization

Direct deterministic quadrature over a fundamental interval must agree with unit normalization for multiple `w/L` and centers, including a profile crossing the interval boundary.

### 2. Fourier coefficient conformance

Direct quadrature of real and imaginary Fourier coefficients must agree with the analytic coefficient for several modes, widths, and centers. This test must not call the production analytic coefficient helper as its reference.

### 3. Localized limit

At fixed finite tower tolerance and regular `r>0`, `w_s,w_p->0+` must converge to the previous localized/localized mode sum and tidal matrix.

### 4. Broad-width and exact-uniform controls

As either `w_s/L` or `w_p/L` grows, every nonzero-mode overlap must tend to zero and the response must converge to the zero mode. Exact uniform preparation must still set all nonzero coefficients exactly to zero.

Classification:

```text
BROAD_WRAPPED_GAUSSIAN_APPROACHES_ZERO_MODE_BUT_FINITE_WIDTH_IS_NOT_EXACT_UNIFORM
```

### 5. Periodicity

The complete coefficient/tidal record must respect

\[
\Delta y\sim\Delta y+2\pi mL,
\qquad m\in\mathbb Z,
\]

up to the declared complex phase convention.

### 6. Orientation-sign collision

Under `Delta_y->-Delta_y`, complex combined overlaps are conjugated, while their static real weights and tidal matrices remain unchanged. Therefore only the static response has the exact collision:

```text
S1_RELATIVE_ORIENTATION_SIGN_COLLISION_IN_STATIC_REAL_RESPONSE_NOT_COMPACTIFICATION_SCALE
```

No claim is made that a future phase-sensitive protocol must share this collision.

### 7. Source–probe exchange

The transformation

\[
(w_s,w_p,\Delta y)\mapsto(w_p,w_s,-\Delta y)
\]

must conjugate the combined complex overlap and preserve static real tidal matrices.

### 8. Combined-width collision

For every mode, static attenuation depends on

\[
u=\frac{w_s^2+w_p^2}{L^2}.
\]

Distinct width pairs with equal `u` and equal `Delta_y/L` must produce identical mode weights, point matrices, and radial-shell matrices:

```text
SOURCE_PROBE_LOCALIZATION_WIDTHS_COLLIDE_UNDER_COMBINED_MODE_OVERLAP
```

This is an exact model collision, not statistical independence or a physical detector claim.

### 9. Joint dilation

The transformation

\[
(L,r,\Delta r,w_s,w_p,\Delta y)
\mapsto
s(L,r,\Delta r,w_s,w_p,\Delta y)
\]

must preserve dimensionless overlaps and the appropriately converted dimensionless tidal matrices:

```text
JOINT_5D_LOCALIZATION_GEOMETRIC_DILATION_NOT_ABSOLUTE_SCALE
```

### 10. Rank and global collisions

Preregister parameters

\[
(\log L,\alpha_s,\alpha_p,\theta)
=\left(\log L,\frac{w_s}{L},\frac{w_p}{L},\frac{\Delta y}{L}\right).
\]

At a generic nonzero-width, non-special-angle baseline, use dimensionless point and shell matrix features at fixed `r/L` and `Delta r/L`. Expected null directions are:

```text
absolute_scale_null=[1,0,0,0]
combined_width_tangent_null=[0,alpha_p,-alpha_s,0]
```

Local feature rank is at most two under this static wrapped-Gaussian model. Globally, `theta` has sign and `2*pi` periodic collisions. More modes or radii do not remove a collision built into the same combined overlap.

## Deterministic baseline

Numerical baseline values are toy inputs selected only after the equations and sources are frozen. Recommended dimensionless baseline:

```text
L=1
r/L=2
shell_width/L=0.3
alpha_s=0.25
alpha_p=0.4
theta=0.7
scale_factor=2.5
```

A second equal-`u` pair must be derived deterministically, remain nonnegative, and be recorded. Values are not estimates of physical localization, `L`, or `ell0`.

Numeric artifact rules remain `.8g`; canonicalize to `0.0` only when `abs(value)<1e-7`.

## Source programme

Required canonical/institutional source:

- NIST Digital Library of Mathematical Functions, DOI `10.18434/M3167`, §1.8(iv) equation (1.8.14) for Poisson summation and §20.2(i) equation (20.2.3) for theta-3 Fourier series.

The verification log must state exact inspected equations and exclusions. DLMF supports mathematical Fourier/theta identities only. It does not establish:

- a Kaluza–Klein matter-localization mechanism;
- source or detector preparation;
- gravitational coupling to finite profiles;
- the project static potential or Hessian;
- finite-window averaging;
- physical `L`, localization widths, covariance, data, `ell0`, UMCH, evidence, or detection.

Existing `Liu2003CompactifiedPotential`, `FloratosLeontaris1999`, and `KehagiasSfetsos2000` remain scoped to compact-circle potential, KK tower, and asymptotic/spectral context.

## Expected bounded result

If all ten controls pass, expected classification is:

```text
FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE_BUT_STATIC_RESPONSE_IDENTIFIES_ONLY_COMBINED_WIDTH_AND_EVEN_PERIODIC_SEPARATION_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Maximum interpretation remains:

```text
MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

Physical gate:

```text
PHYSICAL_5D_LOCALIZATION_DYNAMICS_GAUGE_FIXED_TENSOR_COUPLING_RADION_STABILIZATION_SOURCE_PROBE_PREPARATION_PHASE_SENSITIVE_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

## Falsification and stop conditions

Stop or classify implementation as failed if:

1. image-sum normalization or coefficient quadrature disagrees with sourced Fourier derivation;
2. localized or exact-uniform limits fail;
3. mode/tidal tower lacks convergence certification;
4. periodicity, conjugation, source–probe exchange, or equal-`u` collision fails;
5. shell zero-width or joint-scaling conformance fails;
6. generic rank exceeds the dependence allowed by the same analytic overlap without a traced coding or feature-definition cause;
7. a finite width is called exactly uniform;
8. phase labels are mislabeled as physical phase-sensitive observations;
9. source scope is ambiguous;
10. any value of `L`, `w_s`, `w_p`, or `ell0`, extra-dimension evidence, or detection is inferred.

## Deliverables after final ratification

- sibling implementation plan;
- source-test RED then DLMF bibliography/log update;
- missing/extended-API RED tests;
- smallest extension of `studies/spacetime/kaluza_klein_linearized_tidal.py` or one tightly scoped sibling module if direct extension would obscure old artifact compatibility;
- deterministic JSON artifact;
- bilingual EN/IT audit reports and one theory note;
- roadmap and unified-ledger updates that preserve old result;
- direct closure review labeled `DIRECT_REVIEW_NO_SUBAGENT`;
- focused tests, full discovery, extraction/inventory, deterministic checks, `git diff --check`, GitHub tests/LaTeX CI;
- conservative PR eligible for merge only after all checks are green. No positive evidence or detection language.

## Explicit exclusions

This increment does not derive physical branes, domain walls, localization potentials, tensor/vector/radion dynamics, stabilization, nonlinear 5D gravity, a detector, real data, an absolute value or bound for `L`, `L=ell0`, a universal curvature floor, or evidence for an extra dimension.
