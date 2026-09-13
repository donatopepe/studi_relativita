# Kerr rho-critical latent-lag-law phase window

For full-window support and N=87, worst risk ranges from uniform lag law to unrestricted simplex. Solving their crossings with toy ceiling 0.05 gives

```text
rho_low=0.499243438917   (unrestricted risk crossing)
rho_high=0.501157235677 (uniform risk crossing)
window_width=0.001913796761
```

Three regimes follow:

```text
rho<rho_low: ALWAYS_SAFE_OVER_LAG_LAW_SIMPLEX
rho_low<rho<rho_high: FINITE_KAPPA_SENSITIVE
rho>rho_high: ALWAYS_UNSAFE_FROM_UNIFORM_ONWARD
```

Inside window, critical density-ratio radius falls sharply:

```text
rho=[0.4995,0.5,0.5005,0.501]
kappa_star=[12.485595532,3.890241565,2.001949812,1.172518080]
```

Both uniform and unrestricted risks increase monotonically over fixed rho grid. All `8/8` controls and `150/150` scenarios pass. Narrow phase window is consequence of toy count/risk/receiver choices, not physical tolerance, confidence interval, stationarity evidence or detection.

```text
KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW_RHO_0P499243439_TO_0P501157236_NOT_ELL0
MODEL_LEVEL_RHO_CRITICAL_LATENT_LAG_LAW_PHASE_NOT_EVIDENCE
PHYSICAL_KERR_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
