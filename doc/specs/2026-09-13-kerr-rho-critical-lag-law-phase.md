# Kerr rho-critical latent-lag-law phase window

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Fix full-window latent-lag support, count `N=87`, risk ceiling `0.05`, and vary AR(1) correlation `rho`. Let

```text
r_uniform(rho)=risk at kappa=1
r_unrestricted(rho)=risk with all lag probability on minimum beta_d.
```

Worst risk increases with density-ratio radius from uniform toward unrestricted limit. Two rho boundaries define three regimes:

```text
rho_low:  r_unrestricted(rho_low)=0.05
rho_high: r_uniform(rho_high)=0.05.
```

Fixed search bracket `[0.49,0.51]`. Baseline expected:

```text
rho_low=0.499243438917
rho_high=0.501157235677.
```

Regimes:

1. `rho<rho_low`: count 87 passes even under unrestricted lag law (`ALWAYS_SAFE_OVER_LAG_LAW_SIMPLEX`, toy gate only).
2. `rho_low<rho<rho_high`: finite critical kappa exists (`FINITE_KAPPA_SENSITIVE`).
3. `rho>rho_high`: count 87 fails already under uniform lag law (`ALWAYS_UNSAFE_FROM_UNIFORM_ONWARD`).

At fixed sensitive rho cases `[0.4995,0.5,0.5005,0.501]`, finite critical kappas should be approximately `[12.485595532,3.890241565,2.001949812,1.172518080]`, strictly decreasing with rho. At rho `0.5`, prior kappa result is recovered.

## MVP-first gate

**Objective:** derive exact rho phase window for lag-law sensitivity.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** rho-domain guardrails, monotonic-risk identity, unrestricted boundary, uniform boundary, phase classification, kappa path, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N=87`, finite `0<=rho<1`, full support and finite rho bracket `0<=lo<hi<1`; rejects invalid values and non-straddling brackets.
2. Both `r_uniform` and `r_unrestricted` are finite, positive and strictly increasing on rho grid `[0.49,0.495,0.5,0.505,0.51]`; unrestricted risk is never lower than uniform risk.
3. Bisection root of unrestricted risk lies in `[0.49924343,0.49924345]`, residual below `2e-10`, and sides classify below/above correctly.
4. Bisection root of uniform risk lies in `[0.50115723,0.50115724]`, residual below `2e-10`, and sides classify below/above correctly.
5. Fixed rho cases `0.495`, `0.5`, `0.505` classify as always-safe, finite-kappa-sensitive and always-unsafe respectively; boundary ordering is strict.
6. Critical kappas at `[0.4995,0.5,0.5005,0.501]` agree with fixed values within `2e-9`, decrease strictly, and rho 0.5 recovers `3.890241565`.
7. Orthogonal channel rotation and common geometric scale preserve both rho boundaries and fixed-rho kappa within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels rho window/toy gate as unmeasured, not confidence or stationarity evidence.

## Scenarios

J143-J150 map one-to-one to controls. New category: `latent_lag_rho_phase`. Existing J01-J142 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW_RHO_0P499243439_TO_0P501157236_NOT_ELL0
MODEL_LEVEL_RHO_CRITICAL_LATENT_LAG_LAW_PHASE_NOT_EVIDENCE
PHYSICAL_KERR_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Rho phase window is boundary of toy assumptions, not confidence interval, measured stationarity/correlation, significance or physical detection.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
