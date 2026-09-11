# Kerr correlated-noise mismatch threshold

Arbitrary full SPD shared noise between signal and calibration observations cancels in their covariance difference. Correlated anchor:

```text
noise_eigenvalues=[0.35790627,0.74209373]
cancellation_residual=8.8817842e-16
```

With inside reference, branch difference matrices occupy opposite definite cones. Collision requires differential signal/calibration mismatch equal full branch difference, not merely one zero eigenvalue. Exact bounded-gain full branch-set operator distance is:

```text
tau=18.797837
safe_bound=15.038269
remaining_separation=3.7595673
```

At full threshold, observable matrices coincide while underlying observed covariances remain SPD:

```text
threshold_collision=1.3322676e-15
minimum_observed_eigenvalue=0.39954509
```

All `8/8` controls and `70/70` scenarios pass. Shared noise cancellation is exact only if same noise enters signal and calibration. Differential mismatch threshold is toy model, not measured hardware tolerance.

```text
KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION_BUT_DIFFERENTIAL_MISMATCH_AT_THE_EXACT_CONE_MARGIN_RESTORES_COLLISION_NOT_ELL0
MODEL_LEVEL_CORRELATED_NOISE_MISMATCH_THRESHOLD_NOT_EVIDENCE
PHYSICAL_KERR_SIGNAL_CALIBRATION_NOISE_MATCHING_DRIFT_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
