# Kerr finite-boundary Jacobi tidal gate

`BoeroMoreschi2020KerrOpticalScalars` supplies exact Kerr vacuum optical curvature and geodesic-deviation scope. On the PR #109 transported equatorial screen:

```text
K_screen=diag(-A,+A)
A=3*M*(xi-a)^2/r^5
```

The `chi=0` profile and phase map conform to the independent Schwarzschild implementation. Full `FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS` remains primary; graph diagnostics are conditional.

Baseline phase map includes:

```text
P_00=-1.8555935
P_02=-8.7010491
P_11=7.4061706
P_13=95.431407
orientation_phase_difference=297.70811
Schwarzschild_phase_residual=2.6279542e-06
scale_residual=0.0
scenario_battery=6/6
```

Unlike identity screen quotient, Jacobi evolution retains orientation-sensitive focusing/shear. All `8/8` controls pass, including symplecticity, reversal/turning composition, source-preparation distinction and scale conversion.

```text
KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION_SENSITIVE_FOCUSING_AND_SHEAR_BEYOND_IDENTITY_SCREEN_QUOTIENT_BUT_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0
MODEL_LEVEL_KERR_JACOBI_CONFORMANCE_NOT_EVIDENCE
PHYSICAL_KERR_JACOBI_SOURCE_SIZE_PROFILE_SCREEN_PREPARATION_POLARIZATION_ANALYZER_CAUSTIC_CONTINUATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

No physical source, analyzer, receiver, data, 5D Kerr comparator or `ell0` law is derived.
