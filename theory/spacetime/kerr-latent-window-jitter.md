# Kerr latent window-jitter fourth-moment correction

Draw one uniform latent lag `D` per centered window. Conditional on `D=d`, pair is Gaussian with `K_d[t,s]=rho^|t-s-d|`. Conditional covariance-estimator mean is lag-independent, so law of total covariance gives exact average conditional Wick factor:

```text
beta_latent=E_D[tr(H K_D H K_D^T)]/tr(H T)^2
MSE_latent=alpha*sum[q(C_S)+q(C_B)]-4*beta_latent*q(N_noise).
```

Gaussian averaged-kernel surrogate instead uses

```text
beta_kernel=tr(H E[K_D] H E[K_D]^T)/tr(H T)^2.
```

Convexity yields positive Jensen correction `beta_latent-beta_kernel`; because term is subtracted, latent mixture has lower estimator MSE than averaged-kernel surrogate.

At fixed `rho=0.5`, fractions `[0,0.25,0.5,1.0]` and N=64:

```text
latent_beta=[0.026034597,0.022629281,0.019211490,0.012671070]
kernel_beta=[0.026034597,0.001901728,0.000297949,0.000000013]
latent_risk_64=[0.067498804,0.067571613,0.067644690,0.067784531]
kernel_risk_64=[0.067498804,0.068014792,0.068049082,0.068055452]
latent_counts=[87,87,87,87]
kernel_counts=[87,88,88,88]
```

Fourth-moment correction reverses averaged-kernel one-count transition, but does not solve burden: `N=64` remains unsafe in both models. All `8/8` controls and `126/126` scenarios pass. Unconditional sample law is non-Gaussian mixture; latent lag law, conditional Gaussianity, AR(1), shared-noise identity and timing are unmeasured.

```text
KERR_LATENT_WINDOW_JITTER_HAS_A_POSITIVE_FOURTH_MOMENT_JENSEN_CORRECTION_RELATIVE_TO_THE_GAUSSIAN_AVERAGED_KERNEL_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
MODEL_LEVEL_LATENT_WINDOW_JITTER_FOURTH_MOMENT_CORRECTION_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_JITTER_DISTRIBUTION_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
