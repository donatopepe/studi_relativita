# Kerr finite Gaussian source and analyzer

The verified dimensionless Jacobi map propagates a zero-mean Gaussian toy preparation by

```text
Sigma_observer=P_bar Sigma_source P_bar^T
```

with source widths `(0.08,0.12,0.015,0.02)`. Raw phase-space and position covariance remain primary. Ideal analyzer variance is `a(theta)^T Gamma a(theta)`.

Orientation survives fixed preparation:

```text
Gamma_plus_diag=[0.039071011,4.432721]
Gamma_minus_diag=[0.19373503,79.624068]
orientation_difference=75.191347
```

But width homogeneity proves overall preparation scale is nuisance. Analyzer variance extrema equal covariance eigenvalues. Their intervals overlap, producing scalar collision:

```text
collision_target=2.313228
collision_angles=[0.16408671,0.80300266]
collision_residual=0.0
scale_residual=0.0
```

Thus full covariance distinguishes fixed branches, while one branch-dependent unknown analyzer scalar does not. Common-basis covariance passes. All `8/8` controls and `14/14` scenarios pass.

```text
KERR_JACOBI_ORIENTATION_SHAPE_SURVIVES_FIXED_FINITE_GAUSSIAN_SOURCE_AND_ANALYZER_SCAN_BUT_SOURCE_WIDTH_HOMOGENEITY_AND_ANALYZER_COLLISIONS_PREVENT_INDEPENDENT_BRANCH_OR_ABSOLUTE_SCALE_IDENTIFICATION_NOT_ELL0
PHYSICAL_KERR_SOURCE_DYNAMICS_EMISSION_INTENSITY_POLARIZATION_ANALYZER_HARDWARE_RECEIVER_TRANSFER_CALIBRATED_NOISE_LIKELIHOOD_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

`MODEL_LEVEL_KERR_SOURCE_ANALYZER_CONTROL_NOT_EVIDENCE`; analyzer is mathematical label, not hardware.
