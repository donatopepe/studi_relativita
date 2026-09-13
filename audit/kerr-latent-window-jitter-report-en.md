# Kerr latent window-jitter audit

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_LATENT_WINDOW_JITTER_FOURTH_MOMENT_CORRECTION_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controls `8/8`; scenario battery `126/126`.

```text
rho=0.5
radius_fractions=[0,0.25,0.5,1.0]
latent_beta_N64=[0.026034597,0.022629281,0.019211490,0.012671070]
kernel_beta_N64=[0.026034597,0.001901728,0.000297949,0.000000013]
latent_risk_N64=[0.067498804,0.067571613,0.067644690,0.067784531]
kernel_risk_N64=[0.067498804,0.068014792,0.068049082,0.068055452]
latent_counts=[87,87,87,87]
kernel_counts=[87,88,88,88]
```

```text
KERR_LATENT_WINDOW_JITTER_HAS_A_POSITIVE_FOURTH_MOMENT_JENSEN_CORRECTION_RELATIVE_TO_THE_GAUSSIAN_AVERAGED_KERNEL_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
PHYSICAL_KERR_LATENT_JITTER_DISTRIBUTION_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Exact law-of-total-covariance result. Positive fourth-moment Jensen correction means Gaussian averaged-kernel surrogate overstates erosion and changes one-count gate, but both leave `N=64` unsafe. Unconditional law is non-Gaussian mixture. No measured jitter law/noise model, significance, power, evidence or detection.
