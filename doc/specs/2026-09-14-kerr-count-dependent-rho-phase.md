# Kerr count-dependent rho phase window

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Retain full-window latent-lag support and risk ceiling `0.05`. For each finite count `N`, define

```text
rho_low(N):  unrestricted-lag-law risk = 0.05
rho_high(N): uniform-lag-law risk = 0.05.
```

At `rho=0`, count 53 is unsafe even for uniform law (`0.0500676203`) and unrestricted law (`0.0502699814`), while count 54 is safe (`0.0491228897`, `0.0493214912`). Thus N=54 is first count with nonnegative-rho phase window. Fixed counts/order:

```text
N=[53,54,64,87,128,256].
```

Expected boundaries for N>=54:

```text
rho_low =[0.084265333564,0.309816339325,0.499243438917,0.649991897137,0.814628675425]
rho_high=[0.095873875058,0.313101631950,0.501157235677,0.651271982688,0.815322224235]
width   =[0.011608541494,0.003285292625,0.001913796761,0.001280085551,0.000693548809]
```

Both boundaries increase strictly with count; width decreases strictly. N=53 is `ALWAYS_UNSAFE_FROM_RHO_ZERO`; N>=54 has always-safe, finite-kappa-sensitive and uniform-unsafe rho phases. N=87 must recover prior milestone exactly.

## MVP-first gate

**Objective:** derive count dependence of rho-sensitive lag-law phase.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** count-domain guardrails, iid threshold, root identity, fixed-count boundaries, ordering, width contraction, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, full support, finite `0<=rho<1` and valid root bracket; rejects bool/noninteger/invalid counts and non-straddling roots.
2. At rho zero, N=53 uniform/unrestricted risks exceed `0.05`, N=54 risks are below, and 54 is first safe count by direct scan.
3. Generic count-root bisection at N=87 agrees with prior rho roots within `2e-10`; risk residuals and side classification are below `2e-10`.
4. Roots for counts `[54,64,87,128,256]` agree with fixed boundary arrays within `2e-10`; N=53 records no finite nonnegative-rho window.
5. Lower and upper boundary sequences are strictly increasing with count and satisfy `rho_low<rho_high` at each finite case.
6. Window widths agree with fixed array within `2e-10` and strictly decrease; N=54 width is largest, N=256 smallest.
7. Orthogonal channel rotation and common geometric scale preserve N=54/N=256 boundaries and N=87 recovery within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels count/rho phases as toy gate, not sample-size prescription, confidence or stationarity evidence.

## Scenarios

J151-J158 map one-to-one to controls. New category: `latent_lag_count_phase`. Existing J01-J150 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_LATENT_LAG_LAW_RHO_SENSITIVITY_WINDOW_MOVES_UPWARD_AND_NARROWS_WITH_TOY_SAMPLE_COUNT_WHILE_N53_IS_UNSAFE_ALREADY_AT_IID_NOT_ELL0
MODEL_LEVEL_COUNT_DEPENDENT_RHO_PHASE_NOT_EVIDENCE
PHYSICAL_KERR_SAMPLE_COUNT_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Count and rho phase boundaries are toy consequences of Markov gate and committed receiver covariances, not experimental sample-size advice, confidence, significance or detection.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
