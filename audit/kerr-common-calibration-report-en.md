# Kerr common-calibration robustness audit

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_COMMON_CALIBRATION_ROBUSTNESS_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controls `8/8`; scenario battery `30/30`.

```text
bounded_min_KL=4.0094352
bounded_anchor=[0.5,0.5,1.0]
attenuation_KL=[4.0094352,0.15069819,2.8033078e-05]
noise_KL=[6.4635633,0.15069819,2.8033078e-05]
identity_residual=0.0
scale_residual=0.0
```

```text
KERR_BRANCH_COVARIANCES_REMAIN_INFORMATION_DISTINCT_UNDER_COMMON_BOUNDED_INVERTIBLE_CALIBRATION_BUT_COMMON_ATTENUATION_OR_UNBOUNDED_NOISE_DRIVES_SEPARATION_TO_ZERO_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
PHYSICAL_KERR_CALIBRATION_BOUNDS_PRIORS_HARDWARE_NOISE_SPECTRUM_SYSTEMATICS_SAMPLING_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Common bounded invertible calibration cannot create exact covariance collision. Unbounded attenuation/noise removes information asymptotically. Bounds are not measured priors.
