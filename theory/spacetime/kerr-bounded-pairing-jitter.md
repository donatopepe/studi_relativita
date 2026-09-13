# Kerr bounded pairing-jitter erosion

Declare jointly Gaussian signal/calibration noise with mixture-kernel cross-time covariance averaged over symmetric integer offsets:

```text
K_J[t,s]=(1/(2J+1))*sum_{d=-J}^J rho^|t-s-d|
beta_J=tr(H K_J H K_J^T)/tr(H T)^2
MSE=alpha*sum[q(C_S)+q(C_B)]-4*beta_J*q(N_noise).
```

Fixed `rho=0.5`, counts `[16,64,256]`, radii `[0,1,2,4,8,16]`. At N=64:

```text
beta_over_alpha=[1.0,0.789485810,0.623302468,0.404555012,0.204269692,0.073046173]
risk_64=[0.067498804,0.067615986,0.067708492,0.067830258,0.067941746,0.068014792]
minimum_counts=[87,87,87,87,87,88]
```

Support averaging erodes cancellation monotonically. Radius 16 restores independent-stream count 88; smaller fixed radii retain 87 only because original paired gain was one sample. `N=64` remains unsafe throughout. All `8/8` controls and `118/118` scenarios pass.

This model averages lag kernels inside one Gaussian covariance. We do not claim equivalence to latent window-level random covariance mixing, generally non-Gaussian and requiring extra fourth-moment terms. Jitter distribution, Gaussianity, AR(1), shared-noise identity and timing are not measured.

```text
KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_RADIUS_16_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_PAIRING_JITTER_EROSION_NOT_EVIDENCE
PHYSICAL_KERR_PAIRING_JITTER_DISTRIBUTION_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
