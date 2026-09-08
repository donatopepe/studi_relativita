# Linearized five-dimensional tensor conformance for the compact-circle tidal control

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human approved the recommendation to defer Kerr and make the next MVP a five-dimensional linearized tensor-conformance check on 2026-09-02. The 2026-09-09 source/convention review corrected the dust metric ratios, separated compact-index curvature from nonzero-mode curvature, and aligned the eight-control list. This complete specification is ratified for implementation planning. Implementation remains gated by a completed sibling TDD plan.

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

Kerr remains preserved as:

```text
DEFERRED_4D_ROTATING_BASELINE_FOR_FUTURE_5D_COMPARISON
```

## MVP-first gate

**Objective:** determine whether the existing scalar Hessian is exactly the observable-coordinate projection `R_0i0j` of a declared static linearized five-dimensional Einstein metric, while exposing additional spatial and compact-direction curvature components that the scalar record omitted.

**Metric and threshold:** correctness over eight preregistered source/tensor controls; threshold `8/8` under declared analytic or numerical tolerances.

**Cases and order:** sourced `d=5` harmonic-gauge metric ratios, gauge residual, linearized Ricci/Einstein conformance including regular vacuum samples, `R_0i0j`–Hessian identity, compact-index/nonzero-mode separation, exact-uniform zero-mode limit, source-stress dependence, and joint scaling/rank gate.

**MVP:** static dust source with only `T_00=rho`, signature `(-,+,+,+,+)`, flat `R^(1,3) x S1` background, harmonic gauge, existing compact-circle point potential and exact localized/uniform circle profiles, one ordinary-space radial-shell window. No finite wrapped widths, general source profiles, full nonlinear theory, radion stabilization, electromagnetic sector, detector, covariance, or data.

**Escalation condition:** add tensor/vector/radion dynamics or physical source stress only if this declared dust/harmonic-gauge baseline fails a named field-equation or curvature-conformance control that cannot be resolved by convention tracing.

## Alternatives considered

1. **Static dust tensor conformance — selected.** Smallest test linking existing Newtonian scalar response to five-dimensional metric curvature and field equations.
2. **Full dynamical KK tensor/vector/scalar decomposition — deferred.** Adds time dependence, residual gauge, polarizations, mode constraints, and source sectors before static conformance is known.
3. **Radion stabilization — deferred.** Requires a compactification potential/background source not derived by current programme.
4. **Kerr orbit control — deferred.** Useful later as a 4D rotating baseline, but does not attack the current 5D tensor-interpretation gate.

## Canonical conventions

Primary source candidate: Sean P. Robinson, *Normalization conventions for Newton's constant and the Planck scale in arbitrary spacetime dimension*, arXiv `gr-qc/0609060`. Before implementation, exact metadata and equations `(1)`, `(2a,b)`, `(4)`, `(5a,b)`, `(6a,b)`, `(7a,b)`, `(9)`–`(15)` must be verified and narrowly logged.

Secondary context candidate: Atondo-Rubio et al., *Linearized Five Dimensional Kaluza-Klein Theory as a Gauge Theory*, arXiv `hep-th/0609133`, equations `(4)`–`(19)` for linearized metric/curvature/field-equation conventions and `(20)`–`(41)` only as scoped KK decomposition context. Its cylinder ansatz and `h_44=0` specialization must not be imported into the localized compact-circle source calculation.

Declared conventions:

```text
d=5 total spacetime dimensions
indices A,B=0,1,2,3,4
ordinary spatial indices i,j=1,2,3
compact spatial index y=4
eta_AB=diag(-1,+1,+1,+1,+1)
g_AB=eta_AB+h_AB
partial_A h^A_B=(1/2) partial_B h^A_A
bar_h_AB=h_AB-(1/2) eta_AB h^C_C
h_AB=bar_h_AB-(1/(d-2)) eta_AB bar_h^C_C
```

Linearized Einstein convention:

\[
\partial^2\bar h_{AB}=-\mathcal K_5^2 T_{AB},
\]

with static dust

\[
T_{00}=\rho,\qquad T_{0I}=T_{IJ}=0,
\qquad I,J=1,2,3,4.
\]

Define Newtonian potential

\[
\Phi=-\frac12h_{00}.
\]

The source-specific relation between `mathcal K_5`, five-dimensional Newtonian constant, the compact-circle effective `G4`, and the existing unit-amplitude potential must be recorded but factored out of dimensionless shape tests. No coupling convention is silently identified with a physical measured standard.

## Static metric ansatz derived from trace reversal

For regular static solutions with only `bar_h_00` nonzero, inversion of trace reversal in `d=5` gives a metric proportional to one scalar potential. Under the declared sign convention, the project must derive and test the exact component ratios rather than hard-code them from prose.

Equations `(6a,b)`, `(7a-c)`, and `(11)` of the primary source fix, for `d=5`,

\[
h_{00}=\frac{2}{3}\bar h_{00}=-2\Phi,
\qquad h_{11}=h_{22}=h_{33}=h_{44}=\frac{1}{3}\bar h_{00}=-\Phi,
\qquad h_{0I}=h_{IJ}=0\quad(I\ne J).
\]

These ratios must still be recovered by algebraic inversion in the implementation rather than hard-coded from prose. Any disagreement with direct trace reversal or the sourced equations is a stop condition.

The compact component `h_44` is part of the five-dimensional metric perturbation. It must not be called a stabilized physical radion. It is a static scalar metric component generated by the declared dust ansatz.

## Linearized curvature and field-equation record

Compute the full linearized Riemann tensor directly from metric second derivatives:

\[
R^{(1)}_{ABCD}
=\frac12\left(
\partial_C\partial_B h_{AD}
+\partial_D\partial_A h_{BC}
-\partial_D\partial_B h_{AC}
-\partial_C\partial_A h_{BD}
\right),
\]

with exact sign/order source-scoped before use. Contract to raw

```text
Riemann_5D
Ricci_5D
Ricci_scalar_5D
Einstein_5D
harmonic_gauge_residual
```

At regular points away from singular support, compare to vacuum field equations. At a smooth source-control point, use a declared analytic smooth density/potential pair or distribution-free mode identity; do not numerically differentiate through a point singularity or invent delta-function values.

## Primary conformance map

For static `h_0i=0`, derive expected observable-coordinate components:

\[
R_{0i0j}=\partial_i\partial_j\Phi
\]

under the declared Riemann sign convention. Compare raw `3x3` block against the existing point tidal Hessian and radial-shell average.

This identity validates only the ordinary-space temporal tidal block of the declared linearized metric. It does not make the prior scalar Hessian the complete five-dimensional curvature record.

Additional raw components include compact-index curvature. Preserve

\[
R_{0404},\qquad R_{0i04},\qquad R_{i4j4},
\]

where present. For the localized profile, `y` derivatives can populate all three classes. For the exact uniform zero mode, all `y` derivatives and nonzero KK modes vanish, so `R_{0404}` and `R_{0i04}` vanish; however `R_{i4j4}=\tfrac12\partial_i\partial_j\Phi` under this dust ansatz can remain nonzero through ordinary-space derivatives of `h_{44}`. The null control therefore removes nonzero-mode/`y`-derivative structure, not every component carrying index `4`.

No individual tensor component, trace, eigenvalue, or count of nonzero entries is automatically an independent observable or an `ell0` channel.

## Finite-window scope

Reuse only the existing normalized ordinary-space radial shell. At each shell point, compare:

1. average of direct `R_0i0j` block;
2. existing average of scalar Hessian.

They must agree under the common flat-background radial eigenframe. No oriented box, screen transport, source convolution, finite wrapped width, clock, or detector is added.

## Eight counterexample-first controls

### 1. `d=5` trace-reversal ratios

Starting from a symbolic or deterministic numeric `bar_h_00`, invert trace reversal and recover every diagonal/off-diagonal metric component. Falsify on any incorrect factor or sign.

### 2. Harmonic-gauge residual

Evaluate

\[
\partial_A h^A{}_B-\frac12\partial_B h^A{}_A
\]

for localized mode samples and exact uniform profile. Maximum residual must remain below preregistered tolerance.

### 3. Linearized Ricci/Einstein conformance

Direct contractions from `Riemann_5D` must agree with independently evaluated linearized Einstein operator. At regular vacuum samples outside source, `Ricci_5D`, Ricci scalar and Einstein tensor must vanish within derivative tolerance even though Riemann components need not vanish.

### 4. Ordinary-space tidal identity

Direct raw block `R_0i0j` must match existing raw Hessian `T_ij` pointwise and after radial-shell averaging:

```text
SCALAR_HESSIAN_EQUALS_R0I0J_ONLY_UNDER_DECLARED_STATIC_LINEARIZED_CONVENTIONS
```

### 5. Compact-index/nonzero-mode separation

Localized profile must produce nonzero `y`-derivative curvature at generic `r/L` and `y/L`, including at least one of `R_0404` or `R_0i04`. Record `R_i4j4` separately because it can contain both ordinary-space derivatives of `h_44` and `y`-derivative terms. This demonstrates incompleteness of a record containing only `R_0i0j`, not evidence or an independent detector channel:

```text
ORDINARY_SPACE_TIDAL_BLOCK_OMITS_COMPACT_INDEX_CURVATURE_NOT_EXTRA_OBSERVATIONAL_RANK
```

### 6. Exact-uniform circle null

Uniform source/probe zero-mode case must remove all `y` derivatives and nonzero KK structure: `R_0404=R_0i04=0` within tolerance. Remaining ordinary-space `R_0i0j` must match the 4D-shaped zero-mode Hessian under the same imported amplitude convention. `R_i4j4` is retained and may be nonzero because the sourced dust ansatz has an ordinary-space-dependent `h_44`; it must not be mislabeled as surviving KK-mode structure.

### 7. Source and convention dependence

Compare dust trace structure with at least one preregistered alternative diagonal stress label algebraically, without adopting it physically. Show that spatial/compact metric ratios depend on source stress and dimension even if `h_00` is held fixed:

```text
TENSOR_COMPLETION_DEPENDS_ON_SOURCE_STRESS_AND_DECLARED_LINEARIZED_CONVENTIONS_NOT_SCALAR_POTENTIAL_ALONE
```

This control must not invent an equation of state; alternative stress entries are symbolic counterexample inputs.

### 8. Joint scaling and rank

Under

\[
(L,r,y,\lambda_{\rm window})\mapsto
s(L,r,y,\lambda_{\rm window}),
\]

appropriately converted dimensionless full-curvature and `R_0i0j` records must remain invariant. At fixed dimensionless protocol, `log L` remains a null direction. Extra tensor components do not identify absolute scale:

```text
LINEARIZED_5D_TENSOR_COMPLETION_RETAINS_JOINT_GEOMETRIC_SCALE_NULL_NOT_ELL0
```

## Raw output contract

```text
metric_perturbation_5D
trace_reversed_metric_5D
harmonic_gauge_residual
Riemann_5D
Ricci_5D
Ricci_scalar_5D
Einstein_5D
R_0i0j
R_0404
R_0i04
R_i4j4
scalar_Hessian_reference
point_conformance_residual
shell_R_0i0j
shell_Hessian_reference
shell_conformance_residual
source_stress_label
source_stress_parameters
gauge_convention
Riemann_convention
coupling_normalization
profile_label
mode_or_exact_expression
convergence_certificate
```

Full tensors or bounded nonzero-entry maps remain primary. Norms and rank features are secondary.

## Deterministic baseline

Use dimensionless toy inputs after source/convention freeze:

```text
L=1
r/L=2
y/L=0.7
shell_width/L=0.3
scale_factor=2.5
unit_effective_potential_amplitude=true
```

Also test exact uniform profile. Values are not physical estimates or bounds.

Artifact rendering remains `.8g`; canonicalize numeric noise to `0.0` only for `abs(value)<1e-7`, while preserving nonzero thresholds.

## Source boundaries

Canonical sources may establish linearized Einstein equations, harmonic gauge, trace reversal, Newtonian limit, geodesic-deviation relation, linearized Riemann conventions, and KK decomposition context. They do not automatically establish:

- current compact-circle source/probe profiles;
- point/radial-shell protocol;
- physical localization or stress tensor;
- radion stabilization;
- coupling calibration;
- independent observability of tensor components;
- covariance/noise/data;
- `L`, `ell0`, UMCH, evidence, or detection.

Every source entry must state equations/sections inspected and explicit exclusions. Search summaries and AI prose are not authority.

## Expected bounded result

If all eight controls pass:

```text
DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J_BUT_ADDS_SOURCE_AND_GAUGE_DEPENDENT_COMPACT_CURVATURE_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Maximum interpretation:

```text
MODEL_LEVEL_LINEARIZED_TENSOR_CONFORMANCE_NOT_EVIDENCE
```

Physical gate:

```text
PHYSICAL_5D_SOURCE_STRESS_LOCALIZATION_DYNAMICS_GAUGE_INVARIANT_OBSERVABLE_RADION_STABILIZATION_COUPLING_CALIBRATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

## Falsification and stop conditions

Stop or report failed conformance if:

1. canonical-source conventions remain ambiguous;
2. trace-reversal ratios or harmonic gauge fail;
3. independently constructed curvature and Einstein operators disagree, or vacuum Ricci fails to vanish at regular samples;
4. `R_0i0j` does not match scalar Hessian after traced signs/conventions;
5. localized generic samples lack the preregistered `y`-derivative curvature;
6. uniform profile retains `y` derivatives/nonzero KK modes or is incorrectly required to erase ordinary-space `R_i4j4`;
7. source-stress dependence or shell-average equality fails;
8. joint scaling fails;
9. full tensor entries are presented as independent measured channels;
10. physical stress, stabilization, coupling, `L`, `ell0`, evidence, or detection is invented.

## Deliverables after ratification

- sibling TDD plan;
- source tests and narrow bibliography/log additions;
- a smallest standard-library tensor-conformance module reusing existing compact-circle potential derivatives where safe;
- tests for exactly eight measured controls;
- deterministic JSON artifact;
- aligned EN/IT audit reports and theory note;
- roadmap/ledger update preserving earlier scalar and finite-localization results plus `F_0`;
- `DIRECT_REVIEW_NO_SUBAGENT` record;
- focused/full suites, artifact checks, extraction/inventory, CI and Hermes;
- conservative PR and auto-merge only if source conventions are unambiguous and all local/CI checks are green.

## Explicit exclusions

No nonlinear 5D solution, physical radion, stabilization mechanism, electromagnetic mode, realistic source stress, brane, detector, real data, value/bound for `L`, `L=ell0`, universal curvature floor, evidence, or detection is derived.
