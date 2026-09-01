# Finite `S1` source–probe localization audit

## Status

```text
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

Review: `DIRECT_REVIEW_NO_SUBAGENT`; not independent review.

## MVP and source scope

Metric threshold is `10/10`; all ten preregistered controls pass. Model keeps pointlike ordinary-space source, wrapped-Gaussian source/probe profiles on compact `S1`, raw complex Fourier coefficients/overlaps, static real mode weights, raw point tidal matrix, and existing radial shell only.

`NISTDLMF` §1.8(iv) (1.8.14) and §20.2(i) (20.2.3) support Poisson summation and theta-3 Fourier identities. Wrapped-profile normalization, source/probe overlap, gravitational mode sum, Hessian, shell and rank are `PROJECT_DERIVATION`/`TOY_CONTROL`. DLMF does not support physical localization or gravity claims.

## Deterministic baseline

```text
L=1.0
r_over_L=2.0
shell_width_over_L=0.3
alpha_s=0.25
alpha_p=0.4
theta=0.7
equal_u_pair=[0.1,0.46097722]
T_parallel=-0.48757452
T_perpendicular=0.19602073
T_shell_parallel=-0.4940744
T_shell_perpendicular=0.1988726
rank=2
absolute_scale_null=[1.0,0.0,0.0,0.0]
combined_width_tangent_null=[0.0,0.4,-0.25,0.0]
dimensionless_point_matrix_residual=0.0
dimensionless_shell_matrix_residual=0.0
```

## Counterexamples

```text
BROAD_WRAPPED_GAUSSIAN_APPROACHES_ZERO_MODE_BUT_FINITE_WIDTH_IS_NOT_EXACT_UNIFORM
S1_RELATIVE_ORIENTATION_SIGN_COLLISION_IN_STATIC_REAL_RESPONSE_NOT_COMPACTIFICATION_SCALE
SOURCE_PROBE_LOCALIZATION_WIDTHS_COLLIDE_UNDER_COMBINED_MODE_OVERLAP
JOINT_5D_LOCALIZATION_GEOMETRIC_DILATION_NOT_ABSOLUTE_SCALE
```

Complex overlaps distinguish orientation through conjugation, but static real tidal records are even in relative separation. Distinct source/probe width pairs collide when `(w_s^2+w_p^2)/L^2` is equal. More modes from the same overlap do not remove these exact collisions.

## Result

```text
FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE_BUT_STATIC_RESPONSE_IDENTIFIES_ONLY_COMBINED_WIDTH_AND_EVEN_PERIODIC_SEPARATION_WHILE_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Passing model controls is not evidence for an extra dimension, physical localization, `L`, `ell0`, or UMCH.

```text
PHYSICAL_5D_LOCALIZATION_DYNAMICS_GAUGE_FIXED_TENSOR_COUPLING_RADION_STABILIZATION_SOURCE_PROBE_PREPARATION_PHASE_SENSITIVE_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```
