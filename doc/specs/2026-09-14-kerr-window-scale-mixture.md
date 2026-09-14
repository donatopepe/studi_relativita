# Kerr window-scale mixture covariance floor

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Retain full-support latent-lag model at toy `rho=0.5`. For each branch pair and centered observation window, draw one positive latent amplitude-squared scale `W`, independent between branch pairs and independent of lag/conditional Gaussian samples:

```text
E[W]=1
Var(W)=cv^2
E[W^2]=1+cv^2.
```

Both signal and calibration covariance estimates in same branch pair are multiplied by common W. Conditional difference estimator has mean `W*Delta_b`, where `Delta_b=C_S,b-C_B,b`. Law of total covariance gives exact two-pair MSE

```text
MSE_scale(N,cv)
 =(1+cv^2)*MSE_latent_gaussian(N)
 +cv^2*sum_b ||Delta_b||_F^2.
```

Second term does not decay with N. Fixed coefficient and normalized floor:

```text
Delta_coefficient=304.907367059628
floor_risk(cv)=0.862883522363*cv^2.
```

Fixed CV cases `[0,0.1,0.2,0.25]`, counts `[64,87,256]`, risk ceiling `0.05`. Baseline expected minimum counts `[87,106,292,None]`; CV 0.25 has floor above ceiling and no finite count. Critical CV solves floor equality:

```text
cv*=0.240718192810.
```

This scale is one latent nuisance per entire window, not iid per-sample elliptical scaling. Only first two moments enter this exact total-MSE identity because conditional estimator mean is linear in W and conditional variance scales as W squared.

## MVP-first gate

**Objective:** derive exact non-decaying risk floor from window-level scale mixture.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** scale-mixture domain, total-MSE identity, zero-variance limit, risk floor, fixed-CV counts, critical CV, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, finite `cv>=0`, normalized moments `E[W]=1`, `E[W^2]=1+cv^2`; rejects invalid values and negative/nonfinite variance.
2. Direct law-of-total-covariance decomposition per branch agrees with compact combined formula within `2e-10` for `N=[16,64]`, `cv=[0.1,0.2]`.
3. `cv=0` exactly recovers latent Gaussian full-support risk/count 87 within `2e-10`.
4. Risks converge monotonically from above to exact floor `0.862883522363*cv^2`; fixed large-N residual obeys analytic decaying term.
5. Minimum counts at CV `[0,0.1,0.2,0.25]` are `[87,106,292,None]`; predecessors fail for finite cases; N64 fails all cases.
6. Critical CV lies in `[0.24071819,0.24071820]`, floor equals `0.05` within `2e-10`; below admits finite count, at/above cannot pass finite N because positive sampling term remains.
7. Orthogonal channel rotation and common geometric scale preserve normalized MSE/floor/critical CV within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels CV/floor as toy non-Gaussian nuisance, not measured variability or sample prescription.

## Scenarios

J159-J166 map one-to-one to controls. New category: `window_scale_mixture`. Existing J01-J158 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_WINDOW_LEVEL_SCALE_MIXTURE_CREATES_NONDECAYING_COVARIANCE_RISK_FLOOR_AND_CV_0P240718193_PRECLUDES_ANY_FINITE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_WINDOW_SCALE_MIXTURE_FLOOR_NOT_EVIDENCE
PHYSICAL_KERR_WINDOW_SCALE_DISTRIBUTION_NON_GAUSSIANITY_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

CV and window-scale law are toy assumptions, not measured receiver/source variability, confidence, significance or detection.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
