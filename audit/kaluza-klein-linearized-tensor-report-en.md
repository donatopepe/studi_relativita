# Linearized 5D tensor-conformance audit

## Status

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
MODEL_LEVEL_LINEARIZED_TENSOR_CONFORMANCE_NOT_EVIDENCE
```

Direct closure record: `DIRECT_REVIEW_NO_SUBAGENT`. Not independent review.

## Scope and conventions

This MVP embeds the existing exact compact-circle scalar potential into the sourced static `d=5` dust metric, in harmonic gauge and signature `(-,+,+,+,+)`. `Robinson2006Normalization` fixes trace reversal, Newtonian potential, and sign conventions. `AtondoRubio2008Linearized5D` supports linearized curvature context only; its cylinder ansatz and `h_44=0` specialization are excluded.

The complete raw `Riemann_5D`, contractions, `R_0i0j`, compact-index blocks, scalar-Hessian reference, and radial-shell averages are retained in the deterministic artifact.

## Deterministic baseline

```text
L=1.0
r/L=2.0
y/L=0.7
shell_width/L=0.3
scale_factor=2.5
R_0101=-0.50548011
R_0202=0.20349714
R_0404=0.098485837
R_0104=-0.24481889
shell_R_0101=-0.51149219
point_conformance_residual=0.0
shell_conformance_residual=0.0
uniform_R_0404=0.0
uniform_R_1414=-0.125
source_ratio_residual=0.5
dimensionless_full_curvature_residual=0.0
```

Values use unit effective potential amplitude. They are model-level dimensionless controls, not measurements or bounds.

## Eight controls

All `8/8` preregistered controls pass:

1. sourced `d=5` dust trace reversal;
2. harmonic-gauge residual;
3. independent Riemann contraction, Einstein-operator conformance, and regular-vacuum Ricci null;
4. point and shell `R_0i0j` equality with the prior scalar Hessian;
5. localized compact-index/nonzero-mode separation;
6. exact uniform zero mode removes `y` derivatives but not ordinary-space `R_i4j4`;
7. symbolic diagonal-stress counterexample changes tensor completion at fixed `h_00`;
8. joint dilation preserves dimensionless curvature and leaves `log L` null.

## Bounded result

```text
DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J_BUT_ADDS_COMPACT_INDEX_CURVATURE_WHILE_TENSOR_COMPLETION_REMAINS_SOURCE_DEPENDENT_AND_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
PHYSICAL_5D_SOURCE_STRESS_LOCALIZATION_DYNAMICS_GAUGE_INVARIANT_OBSERVABLE_RADION_STABILIZATION_COUPLING_CALIBRATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

Passing conformance repairs the scalar-to-tensor interpretation only inside declared static conventions. It does not make raw components independent gauge-invariant observables and does not identify `L`, derive `L=ell0`, validate UMCH, or detect an extra dimension. Prior scalar, finite-localization, and `F_0` records remain preserved.
