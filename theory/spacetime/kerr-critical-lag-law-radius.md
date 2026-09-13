# Kerr critical latent-lag density-ratio radius

At full-window support and count `N=87`, worst bounded-simplex beta is piecewise analytic. Within active-set region of `m` smallest coefficients,

```text
beta_min(kappa)=A_m*kappa+B_m/kappa+C_m.
```

Equating worst risk to toy ceiling `0.05` gives quadratic root. Fixed rho `0.5` result:

```text
kappa_star=3.890241564958
active_count=35
active_interval=[3.861111111111,4.0]
risk_87(kappa_star)=0.05
analytic_bisection_residual=3.05e-13
```

At `kappa_star-1e-6`, count 87 passes with risk `0.0499999999834`; at `kappa_star+1e-6`, it fails with `0.0500000000166`, while count 88 passes. Sub-full support fractions `[0,0.25,0.5]` remain below ceiling even in unrestricted simplex limit; only full support has finite transition in this toy.

All `8/8` controls and `142/142` scenarios pass. `kappa_star` is boundary of assumed nuisance set, not confidence level, significance, measured hardware tolerance or evidence.

```text
KERR_FULL_SUPPORT_LATENT_LAG_LAW_HAS_TOY_CRITICAL_DENSITY_RATIO_KAPPA_3P890241565_FOR_THE_COUNT_87_GATE_NOT_ELL0
MODEL_LEVEL_CRITICAL_LATENT_LAG_LAW_RADIUS_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
