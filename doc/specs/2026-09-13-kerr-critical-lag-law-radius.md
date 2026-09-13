# Kerr critical latent-lag density-ratio radius

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Use bounded latent-lag probability law from prior milestone. Fix count `N=87`, full-window support fraction `f=1`, toy `rho=0.5`, and conservative risk ceiling `r*=0.05`. Worst-case risk minimizes

```text
beta(p)=sum_i p_i b_i
u/kappa <= p_i <= kappa*u
sum_i p_i=1,
```

where sorted coefficients satisfy `b_1<=...<=b_n`, `n=2N+1=175`. For kappa inside an active-set interval, let

```text
m=floor(n/(kappa+1)).
```

Worst LP puts upper probability `kappa/n` on first `m` coefficients, lower probability `1/(kappa*n)` on largest coefficients, and residual mass on one pivot. Algebra reduces exact profiled beta to

```text
beta_min(kappa)=A_m*kappa+B_m/kappa+C_m,
A_m=(sum_{i<=m} b_i-m*b_{m+1})/n,
B_m=sum_i b_i/n-sum_{i<=m} b_i/n-b_{m+1}+m*b_{m+1}/n,
C_m=b_{m+1}.
```

Set target beta from risk equality

```text
beta*= [M*alpha(N,rho)-tau^2*r*]/Q,
```

with marginal coefficient `M` and cross coefficient `Q`. Solve `A_m*kappa^2+(C_m-beta*)*kappa+B_m=0`, retaining root in fixed bracket `[2,4]` and its own active-set interval. Baseline expected root:

```text
kappa*=3.89024156496
m=35
risk_87(kappa*)=0.05.
```

Below root count 87 passes; above root count 87 fails and minimum count is 88. Other support fractions `[0,0.25,0.5]` do not cross even in unrestricted simplex limit and remain count 87.

## MVP-first gate

**Objective:** derive exact active-set critical radius for full-support count transition.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** critical-domain guardrails, active-set formula identity, bracket, analytic root, side classification, support contrast, basis/scale invariance, nonclaims.

## Eight controls

1. Domain fixes integer `N=87`, finite `rho=0.5`, fraction `f=1`, finite bracket `1<=lo<hi`; rejects invalid values and roots outside active-set interval.
2. Piecewise `A*kappa+B/kappa+C` agrees with greedy LP beta within `2e-10` at kappas `[2,3,3.8,4]`; active-set counts match generated extrema.
3. Risk at kappa 2 is below `0.05`; risk at kappa 4 is above; worst risk is strictly increasing over fixed grid `[2,2.5,3,3.5,4]`.
4. Analytic quadratic root agrees with 100-step bisection within `2e-10`, satisfies risk equality within `2e-10`, lies in `[3.89024156,3.89024157]`, and has active count 35.
5. At `kappa* +/- 1e-6`, lower side passes count 87 and upper side fails; count 88 passes both.
6. For fractions `[0,0.25,0.5]`, unrestricted worst risk at N=87 remains below `0.05`; only full support has finite transition in this toy.
7. Orthogonal channel rotation and common geometric scale preserve target/root/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels kappa threshold/toy gate as unmeasured, not confidence level.

## Scenarios

J135-J142 map one-to-one to controls. New category: `latent_lag_critical_radius`. Existing J01-J134 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_FULL_SUPPORT_LATENT_LAG_LAW_HAS_TOY_CRITICAL_DENSITY_RATIO_KAPPA_3P890241565_FOR_THE_COUNT_87_GATE_NOT_ELL0
MODEL_LEVEL_CRITICAL_LATENT_LAG_LAW_RADIUS_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Critical kappa is threshold in toy nuisance set, not statistical confidence, significance, measured tolerance or physical detection.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
