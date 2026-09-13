# Kerr bounded latent-lag law audit

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_BOUNDED_LATENT_LAG_LAW_ROBUSTNESS_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controls `8/8`; scenario battery `134/134`.

```text
rho=0.5
radius_fractions=[0,0.25,0.5,1.0]
kappas=[1,2,4]
kappa_2_worst_counts=[87,87,87,87]
kappa_2_best_counts=[87,87,87,87]
kappa_4_worst_counts=[87,87,87,88]
kappa_4_best_counts=[87,87,87,87]
kappa_4_full_support_worst_risk_N64=0.067950561
kappa_4_full_support_best_risk_N64=0.067612376
```

```text
KERR_LATENT_LAG_LAW_DENSITY_RATIO_BOUNDS_GIVE_EXACT_RISK_ENVELOPES_BUT_KAPPA_4_CAN_RESTORE_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
PHYSICAL_KERR_LATENT_LAG_LAW_BOUNDS_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Exact bounded-simplex linear program. Kappa 2 preserves uniform count 87; kappa 4 can restore worst-case count 88 at full support. `N=64` remains unsafe across envelope. Bounds and lag law are unmeasured toys; no significance, power, evidence or detection.
