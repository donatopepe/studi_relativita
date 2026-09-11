# Kerr finite-sample covariance uncertainty

For known-zero-mean Gaussian samples, direct Wishart/Wick contraction gives exact covariance-estimator Frobenius MSE. Four independent signal/calibration estimates add:

```text
total_coefficient=923.69333
counts=[16,64,256]
rms=[7.5980809,3.7990405,1.8995202]
```

Inverse-root scaling is exact. Comparing operator error to toy branch-set separation through Frobenius domination and Markov bound yields:

```text
minimum_count=53
risk_53=0.049321491
risk_52=0.050269981
risk_16=0.16337744
risk_64=0.04084436
```

`N=16` is authoritative unsafe negative for declared 0.05 bound; `N=64` passes only conservative model-level gate. This is not detection significance, power, measured sampling, or data evidence.

All `8/8` controls and `78/78` scenarios pass.

```text
KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING_AND_ONLY_A_CONSERVATIVE_TOY_COUNT_GATE_BOUNDS_BRANCH_COLLISION_SCALE_NOT_ELL0
MODEL_LEVEL_GAUSSIAN_COVARIANCE_UNCERTAINTY_NOT_EVIDENCE
PHYSICAL_KERR_SAMPLE_INDEPENDENCE_GAUSSIANITY_MEAN_ESTIMATION_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
