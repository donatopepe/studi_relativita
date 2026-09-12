# Kerr AR(1) temporal-dependence penalty

For separable Gaussian AR(1) samples with estimated mean, centered quadratic-form/Wishart contraction gives exact finite-N factor `alpha=tr(H T H T)/tr(H T)^2`. Iid limit recovers `1/(N-1)`.

At fixed toy correlation:

```text
rho=0.5
rms=[9.7334408,4.9038744,2.4524884]
minimum_count=88
risk_88=0.049511371
risk_87=0.050080099
risk_64=0.068055453
```

Thus `N=64`, safe in iid estimated-mean toy, fails under rho 0.5. Dependence penalty increases monotonically over `[0,0.25,0.5,0.75]`. Near unit correlation remains severe:

```text
rho_0.99_effective_df_64=2.9130205
```

All `8/8` controls and `94/94` scenarios pass. AR(1), stationarity, separability and rho are not measured.

```text
KERR_GAUSSIAN_AR1_TEMPORAL_DEPENDENCE_REDUCES_EFFECTIVE_COVARIANCE_INFORMATION_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_AR1_COVARIANCE_PENALTY_NOT_EVIDENCE
PHYSICAL_KERR_TEMPORAL_CORRELATION_MODEL_STATIONARITY_GAUSSIANITY_CROSS_STREAM_DEPENDENCE_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
