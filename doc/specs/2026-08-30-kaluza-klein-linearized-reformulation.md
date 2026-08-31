# Linearized compact Kaluza–Klein gravity reformulation candidate

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Design sections and complete specification approved by human on 2026-08-30. This specification records a candidate change of scientific core. Ratification authorizes implementation planning through the writing-plans gate, not implementation itself.

Because this route may replace the current primary core, any eventual implementation PR must remain unmerged pending a separate human ratification of the complete reformulation ledger.

Global guardrails:

```text
HIGHER_DIMENSIONAL_GRAVITY_CORE=REFORMULATION_CANDIDATE_UNRATIFIED
MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
Detection=NO_POSITIVE_DETECTION_CLAIM
Maximum interpretation=MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

## Candidate core statement

The observed four-dimensional gravitational interaction could be a projection or effective sector of a higher-dimensional geometry.

First bounded realization:

\[
\mathcal M_5=\mathbb R^{1,3}\times S^1,
\qquad y\sim y+2\pi L,
\]

with one compact spatial dimension of radius `L`, a full Fourier/Kaluza–Klein tower, and a static weak-field linearized calculation.

This is a hypothesis and toy-control programme, not a claim that the physical universe has five dimensions. `L` is a compactification radius in the candidate model. It is not automatically the UMCH scale `ell0`.

## Relation to the existing programme

This design selects higher-dimensional effective gravity as the new primary reformulation candidate. Existing four-dimensional UMCH work is not deleted or rewritten. It must be frozen and preserved as historical scientific work, including:

- the ratified channel-native operational response object;
- scalar projections and `F_0`;
- pointwise no-go results;
- turnover and `q` demotion;
- exact plane-wave, Schwarzschild, Reissner–Nordström, and Kottler controls;
- all negative identifiability results, contradiction history, source scopes, and provenance.

UMCH becomes a possible secondary consequence only. A compact dimension does not imply a universal curvature floor. Recovering such a floor would require a separate derivation from higher-dimensional dynamics to a preregistered operational response law.

The pending Kerr orbit-level draft is not part of this bounded increment and remains deferred. No structural dead end is declared for the four-dimensional route.

## Alternatives considered

1. **General unspecified projection from `D>4`.** Rejected for the first increment because it is too underdetermined to produce a sharp counterexample or deterministic test.
2. **Compact fifth dimension with zero mode only.** Retained as a null projection but rejected as the candidate core because it makes `L` locally invisible in the first static control.
3. **Full compact Kaluza–Klein tower with a linearized first increment — selected.** It exposes mode projection, source/probe dependence, short/long-distance limits, finite-window response, and scale degeneracy while avoiding premature nonlinear or cosmological claims.
4. **Braneworld/bulk model.** Deferred because brane action, bulk dynamics, junction conditions, and localization add unsupported structure before the compact-circle control is understood.
5. **Full nonlinear five-dimensional gravity.** Deferred until the linearized source, projection, window, convergence, and identifiability gates pass.

## Bounded question

For static linearized gravity on `R^(1,3) x S^1`, do localized source and probe profiles generate a finite-window tidal-matrix shape from nonzero Kaluza–Klein modes that is absent under uniform-circle projection, while source size, window size, and joint geometric dilation prevent unsupported identification of an absolute compactification scale or `ell0`?

## Declared domain

The first increment is restricted to:

- one compact spatial circle `S^1`;
- static weak fields and linear perturbations about the flat product background;
- nonrelativistic source and probe records;
- positive compactification radius `L>0`;
- observation windows outside singular support for point sources;
- explicitly normalized source and probe profiles;
- deterministic, noiseless model controls;
- no cosmological expansion, radion stabilization, quantum corrections, nonlinear backreaction, emission, absorption, detector transfer, or calibrated covariance.

Any gauge convention, normalization of the five-dimensional coupling, relation to an effective four-dimensional coupling, and treatment of tensor/vector/scalar sectors must be derived and source-scoped before becoming test authority.

## Mode and profile contract

The periodic dependence is represented as

\[
G_{AB}(x,y)=\sum_{n\in\mathbb Z}G_{AB}^{(n)}(x)e^{iny/L}.
\]

The familiar scale `|n|/L` is a candidate mode scale only; its exact mass and normalization convention must be verified from canonical sources before implementation.

Circle profiles:

1. **Localized source/probe:** ideal delta profile at a declared circle location, or a regulator whose delta limit is certified.
2. **Uniform source/probe:** normalized profile `1/(2*pi*L)` around the circle.

The source–probe coupling to each mode must be computed from profile overlaps rather than assumed. Expected projection controls are:

```text
localized source x localized probe -> zero mode plus nonzero KK modes
localized source x uniform probe   -> zero mode only
uniform source   x localized probe -> zero mode only
uniform source   x uniform probe   -> zero mode only
```

Relative positions of localized source and probe around `S^1` must be retained if they enter the mode phases. Coincidence on the circle may be the baseline but cannot silently replace the general preparation label.

A missing nonzero-mode response under a uniform profile is a protocol projection, not proof that the extra dimension is absent.

## Three-dimensional source contract

Each circle-profile case is crossed with:

1. **Point source:** analytic reference with singular support excluded from windows.
2. **Uniform compact sphere:** radius `R_s`, constant density inside its support, zero outside, fixed total mass.
3. **Gaussian source:** declared width `sigma`, explicit normalization and width convention, fixed total mass.

Required limits:

\[
R_s\to0,
\qquad \sigma\to0,
\]

must recover the point-source result away from the origin under the same coupling and circle profiles.

`R_s` and `sigma` are source-preparation scales. They are neither `L` nor `ell0`.

## Primary response object

Potential and acceleration are auxiliary. The primary local weak-field record is the full spatial tidal Hessian

\[
T_{ij}(x)=\partial_i\partial_j\Phi(x),
\]

subject to the sign and metric-perturbation convention established by the sourced linearized derivation.

For a spherically symmetric pointwise response,

\[
T_{ij}
=T_\perp(r)(\delta_{ij}-\hat r_i\hat r_j)
+T_\parallel(r)\hat r_i\hat r_j.
\]

The implementation must preserve the matrix and its eigenspaces. Norms, traces, eigenvalue ratios, and other scalarizations are secondary and cannot replace the raw matrix.

This Hessian is a weak-field tidal control linked to relative acceleration. It is not automatically the complete five-dimensional Riemann tensor, a detector record, or the full channel-native UMCH response.

## Finite-window operator

The primary bounded record is a transported finite-window tidal matrix

\[
\mathcal T[\Omega,W,x_0]
=\int_\Omega W(x)\,
\mathcal P_{x\to x_0}T(x)\mathcal P_{x\to x_0}^{-1}\,d\mu(x),
\]

where the baseline linearized flat-background transport, measure, kernel normalization, and reference point are explicit.

Two window families are required:

1. **Radial shell:** centered at `r_c`, finite width `Delta r`, with a declared radial weight. This is the analytic symmetry control.
2. **Oriented three-dimensional region:** declared shape, center, dimensions, orientation, boundary, and kernel. This tests matrix response, boundary dependence, and rotational equivalence.

Required records include:

```text
T_window_matrix
T_parallel
T_perpendicular
Phi_auxiliary
grad_Phi_auxiliary
source_3d_profile
source_size
source_S1_profile
probe_S1_profile
source_probe_relative_S1_position
L
window_family
window_geometry
window_orientation
window_kernel
transport_convention
mode_truncation_or_closed_form
convergence_certificate
```

Transport, averaging, differentiation, scalarization, and source convolution are not assumed interchangeable. Any equality among them must be proved within declared assumptions.

The zero-window limit must recover the pointwise matrix at regular points.

## Counterexample-first controls

### Uniform-circle null projection

Any uniform source or uniform probe must eliminate nonzero Fourier modes according to the derived overlap. Failure is a falsification of the implementation or declared coupling.

### Four-dimensional/decoupling limit

At fixed nonzero observation distance, the verified compactification limit must recover the four-dimensional zero-mode response. The precise statement may be `L->0`, `r/L->infinity`, or an equivalent sourced limit, but it must be fixed from the exact expression before testing.

### Short-distance control

If canonical theory predicts a five-dimensional short-distance law, the localized/localized point-source case must recover it in its valid domain. No short-distance coefficient or power may be preregistered from memory; source verification is mandatory.

### Finite-source limits

Uniform-sphere and Gaussian results must converge to the point-source control away from singular support as their sizes vanish.

### Matrix conformance

The tidal record must be symmetric. Radial/transverse components must reconstruct the matrix. Rotationally equivalent windows and source configurations must agree after the declared basis transformation.

### Tower convergence

A truncated sum is not authoritative without a convergence certificate. Required controls include increasing truncation, residual bounds or comparison to a verified closed form, and stress cases near the compactification and source scales.

### Boundary and ordering controls

Changing window shape or kernel may change the response. Such changes are boundary/protocol dependence unless an invariant quotient is derived. Averaging before differentiation must be compared with differentiating before averaging where both are defined.

## Scale and identifiability gates

Potential features may depend on

\[
\frac rL,
\qquad \frac{R_s}{L},
\qquad \frac{\sigma}{L},
\qquad \frac{\ell_\Omega}{L},
\]

and on source/probe profile overlaps.

The first implementation must test whether changes in `L` can be imitated by source size, Gaussian width, window scale, normalization, or profile preparation. If so, report:

```text
L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION
```

A joint geometric dilation of all lengths must be derived and tested. If it preserves all dimensionless shapes, report:

```text
JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE
```

Rank analysis must use preregistered dimensionless features and declared parameters. More modes, matrix entries, samples, windows, or source profiles do not imply physical rank, statistical independence, or global identifiability.

A known external source size, compactification standard, absolute clock, or coupling would be imported calibration. It would not by itself identify an interior UMCH scale.

No result may set

\[
L=\ell_0
\]

without a separate derived law mapping compactified geometry to the operational UMCH response and its universal lower-curvature claim.

## Source programme

Before implementation, canonical sources must verify and delimit:

- linearized gravity on `R^(1,3) x S^1`;
- Fourier/Kaluza–Klein decomposition and normalization;
- static compact-circle Green function or equivalent mode sum;
- effective four-dimensional long-distance limit;
- five-dimensional short-distance behavior, if used;
- coupling of modes to source and probe profiles;
- relation between five- and four-dimensional gravitational couplings;
- gauge and tensor/scalar/vector content relevant to the tidal Hessian.

Search summaries and AI-generated prose are not sources. Each bibliography entry needs DOI/arXiv/publisher or institutional provenance, exact supported topic, inspected equations/pages or sections, and explicit exclusions.

No source automatically supports finite-window protocol, source/probe preparation, identifiability, detector physics, `L=ell0`, UMCH, or detection.

## Falsification and stop conditions

The bounded implementation fails if any of these remains unresolved:

1. uniform-circle profiles fail to remove nonzero modes;
2. verified four-dimensional limit fails;
3. verified short-distance limit fails, if claimed;
4. finite-source point limits fail away from singular support;
5. tidal matrix symmetry or radial/transverse reconstruction fails;
6. mode sum lacks convergence certification;
7. dimensional scaling fails;
8. zero-window limit fails;
9. equivalent orientations disagree without geometric cause;
10. source, probe, boundary, gauge, or normalization dependence is mislabeled intrinsic geometry;
11. canonical sources do not establish the formula scope;
12. a physical rank or detection claim is made without detector, noise, covariance, and independent data.

Ambiguous source support, unresolved gauge normalization, or absence of a bounded reproducible Green-function calculation requires stopping before implementation claims.

## Expected classifications

Possible bounded result:

```text
LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE_BUT_UNIFORM_PROFILE_PROJECTION_SOURCE_WINDOW_DEGENERACY_AND_JOINT_5D_DILATION_PREVENT_ABSOLUTE_SCALE_OR_ELL0_IDENTIFICATION
```

Null/projection classifications:

```text
UNIFORM_S1_SOURCE_OR_PROBE_PROJECTS_NONZERO_KK_MODES_NOT_ABSENCE_OF_EXTRA_DIMENSION
SOURCE_PROFILE_AND_WINDOW_SHAPE_ARE_PREPARATION_NUISANCES_NOT_INTRINSIC_GEOMETRY
JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE
L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION
```

Physical gate:

```text
NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

Maximum interpretation:

```text
MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

## Deliverables after final spec ratification

The implementation plan may propose:

- canonical-source ledger and bibliography entries;
- test-first derivation and deterministic implementation;
- point, sphere, and Gaussian source controls;
- localized/uniform source–probe matrix;
- radial-shell and oriented-3D finite-window operators;
- convergence, limits, orientation, dimensional scaling, and rank tests;
- deterministic JSON artifact with `.8g` numeric formatting and near-zero canonicalization only for `abs(value)<1e-7`;
- bilingual English/Italian theory and audit reports with identical equations, values, labels, claims, and limitations;
- complete change ledger freezing the previous primary core and recording the new candidate status;
- full unittest discovery, artifact regeneration comparison, extraction/inventory checks, `git diff --check`, PR CI, and review record.

Because this is a primary-core reformulation, the resulting PR must not auto-merge. It must be labeled `REFORMULATION_CANDIDATE_UNRATIFIED` and await explicit human scientific ratification.

## Explicit exclusions

This specification does not derive or claim:

- existence or detection of an extra dimension;
- a fundamental value or bound for `L`;
- `L=ell0`;
- a universal minimum curvature;
- nonlinear five-dimensional field equations beyond sourced background assumptions;
- radion stabilization or compactification mechanism;
- realistic matter localization;
- physical source emission or probe preparation;
- clock, detector, receiver, calibrated noise, covariance, or real data;
- cosmological, black-hole, quantum-gravity, or Standard Model phenomenology;
- positive evidence for UMCH or the higher-dimensional candidate.

## Human decisions recorded

Approved during design dialogue:

- primary reformulation rather than subordinate UMCH mechanism;
- compact fifth dimension rather than generic projection or braneworld;
- full KK tower with a linearized first increment;
- localized source candidate plus uniform-circle null control;
- point, uniform-sphere, and Gaussian three-dimensional sources;
- localized and uniform probes;
- full tidal matrix as primary local response;
- radial shell and oriented three-dimensional finite windows;
- counterexample-first source/profile/window/scale identifiability programme;
- preservation of the old programme and no unsupported detection or `ell0` claim.

Final whole-spec ratification was received on 2026-08-30. The next required gate is `/skill:writing-plans`; implementation remains unauthorized until that plan is complete.
