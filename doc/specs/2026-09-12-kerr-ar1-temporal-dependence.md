# Kerr AR(1) temporal-dependence covariance penalty

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

For each of four signal/calibration sample sets, assume zero-mean jointly Gaussian observations with separable covariance

```text
Cov(x_t,x_s)=T_rho[t,s] C,
T_rho[t,s]=rho^|t-s|,
0<=rho<1.
```

Mean is estimated and removed. Let `H=I-11^T/N`, `d=tr(H T_rho)`, and unbiased centered covariance

```text
S_hat=X^T H X/d.
```

Gaussian quadratic-form contraction gives exact

```text
E||S_hat-C||_F^2 = alpha(N,rho)*((tr C)^2+tr(C^2)),
alpha=tr(H T_rho H T_rho)/tr(H T_rho)^2.
```

At `rho=0`, `alpha=1/(N-1)`, exactly recovering estimated-mean milestone. Four sample sets remain independent of each other. Fixed rho set `[0,0.25,0.5,0.75]`, counts `[16,64,256]`, risk ceiling `0.05`, same committed covariances and branch-set separation.

## MVP-first gate

**Objective:** derive exact AR(1) finite-N penalty and conservative count gate.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** AR(1) domain, centered quadratic-form identity, iid limit, fixed-rho RMS, monotonicity, corrected safe count, basis/scale invariance, nonclaims.

## Eight controls

1. Domain rejects `N<2`, noninteger N, nonfinite rho and rho outside `[0,1)`.
2. Direct dense matrix evaluation of `tr(H T H T)` agrees with bounded closed sums within `2e-10` for fixed cases.
3. `rho=0` recovers exact `1/(N-1)` centered-Wishart factor within `2e-10`.
4. RMS at rho `0.5` and counts `[16,64,256]` is finite, positive and strictly decreasing.
5. At each fixed N, alpha and RMS are strictly increasing over rho `[0,0.25,0.5,0.75]`.
6. Smallest integer count at rho `0.5` meeting risk `<=0.05` is `88`; predecessor fails; `N=64` is authoritative unsafe negative.
7. Orthogonal basis rotation and common geometric scale preserve normalized MSE/risk within `2e-10`; near-unit rho `0.99` retains very low effective covariance degrees and is recorded as negative limit.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J87-J94 map one-to-one to controls. New category: `temporal_dependence`. Existing J01-J86 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_GAUSSIAN_AR1_TEMPORAL_DEPENDENCE_REDUCES_EFFECTIVE_COVARIANCE_INFORMATION_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_AR1_COVARIANCE_PENALTY_NOT_EVIDENCE
PHYSICAL_KERR_TEMPORAL_CORRELATION_MODEL_STATIONARITY_GAUSSIANITY_CROSS_STREAM_DEPENDENCE_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

AR(1), rho and independence assumptions are toy, not measured time-series properties.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
