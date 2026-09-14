# Kerr window-scale mixture covariance floor

Let one positive latent covariance scale W multiply both signal and calibration estimates in each branch-pair window, with `E[W]=1`, `Var(W)=cv^2`. Law of total covariance gives

```text
MSE_scale=(1+cv^2)*MSE_latent_gaussian+cv^2*sum_b||C_S,b-C_B,b||_F^2.
```

Committed branch contrasts give

```text
Delta_coefficient=304.907367059628
floor_risk(cv)=0.862883522363*cv^2
critical_cv=0.240718192810.
```

At toy rho 0.5/full lag support:

```text
cv=[0,0.1,0.2,0.25]
minimum_counts=[87,106,292,None]
floors=[0,0.008628835224,0.034515340895,0.053930220148]
```

CV 0.25 exceeds ceiling asymptotically, creating nondecaying risk floor, so no finite count passes. At critical CV, floor equals 0.05 and positive finite-N sampling term keeps every finite count above ceiling. All `8/8` controls and `166/166` scenarios pass.

This is one common scale per entire covariance window, not iid per-sample elliptical scaling. CV/law remain unmeasured toy nuisances; count gate is not sample-size advice or evidence.

```text
KERR_WINDOW_LEVEL_SCALE_MIXTURE_CREATES_NONDECAYING_COVARIANCE_RISK_FLOOR_AND_CV_0P240718193_PRECLUDES_ANY_FINITE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_WINDOW_SCALE_MIXTURE_FLOOR_NOT_EVIDENCE
PHYSICAL_KERR_WINDOW_SCALE_DISTRIBUTION_NON_GAUSSIANITY_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
