# Kerr bounded pairing-lag erosion

For signal/calibration clocks separated by lag `L`, shared-noise cross-time covariance is `K_L[t,s]=rho^|t-s-L|`. Centering changes cancellation factor from synchronous `alpha` to

```text
beta(N,rho,L)=tr(H K_L H K_L^T)/tr(H T)^2.
```

Thus two branch-pair MSE is marginal AR(1) MSE minus `4 beta q(N_noise)`. Fixed `rho=0.5`, counts `[16,64,256]`, fractions `[0,0.25,0.5,1.0]`, with `L=floor(f*N+0.5)`.

At `N=64`, cancellation ratios and risks are

```text
fraction=[0,0.25,0.5,1.0]
beta_over_alpha=[1.0,0.740204882,0.482882271,0.004159271]
risk_64=[0.067498804,0.067643419,0.067786657,0.068053137]
minimum_counts=[87,87,87,88]
```

Cancellation erodes monotonically. One-window lag nearly removes it and restores independent-stream gate 88. Intermediate fractions retain gate 87 only because synchronous benefit was already one sample. `N=64` remains unsafe throughout. All `8/8` controls and `110/110` scenarios pass. Lag, pairing, Gaussian AR(1) and common-noise identity are not measured.

```text
KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_A_ONE_WINDOW_LAG_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_PAIRING_LAG_EROSION_NOT_EVIDENCE
PHYSICAL_KERR_PAIRING_LAG_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
