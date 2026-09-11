# Kerr estimated-mean covariance penalty

Using an estimated mean before covariance costs exactly one degree of freedom. For unbiased centered Gaussian covariance, centered Wishart degrees are:

```text
degrees_of_freedom=[15,63,255]
penalty=[1.0666667,1.015873,1.0039216]
```

Penalty is exact `N/(N-1)` relative to known-mean MSE. RMS becomes:

```text
rms=[7.8472642,3.8290729,1.9032411]
```

Conservative toy risk gate shifts by one sample:

```text
minimum_count=54
risk_54=0.049321491
risk_53=0.050269981
risk_16=0.17426927
```

`N=16` stays negative; `N=64` remains conditional pass. This is not empirical power or significance.

All `8/8` controls and `86/86` scenarios pass.

```text
KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_ESTIMATED_MEAN_COVARIANCE_PENALTY_NOT_EVIDENCE
PHYSICAL_KERR_UNKNOWN_MEAN_NON_GAUSSIANITY_SAMPLE_DEPENDENCE_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
