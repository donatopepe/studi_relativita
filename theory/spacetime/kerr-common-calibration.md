# Kerr common-calibration robustness

A common calibration applies the same positive diagonal gain and isotropic noise to both Kerr branch covariances. For bounded invertible gains, covariance difference obeys exact congruence and cannot collide.

Deterministic grids show bounded robustness:

```text
bounded_min_KL=4.0094352
bounded_anchor=[0.5,0.5,1.0]
identity_residual=0.0
scale_residual=0.0
```

Grid sizes `5`, `9`, `17` return same boundary minimum. Bounds are toy assumptions, not physical priors.

The asymptotic counterexamples remain:

```text
attenuation_KL=[4.0094352,0.15069819,2.8033078e-05]
noise_KL=[6.4635633,0.15069819,2.8033078e-05]
```

Common attenuation toward zero or common unbounded noise drives information separation toward zero. Hence bounded common calibration is robust, but unbounded common nuisance is not.

All `8/8` controls and `30/30` scenarios pass.

```text
KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION_BUT_COMMON_ATTENUATION_OR_UNBOUNDED_NOISE_DRIVES_SEPARATION_TO_ZERO_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_COMMON_CALIBRATION_ROBUSTNESS_NOT_EVIDENCE
PHYSICAL_KERR_CALIBRATION_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
