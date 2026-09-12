# Kerr bounded pairing-lag erosion

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Signal and calibration streams retain identical marginal AR(1) covariance, but shared receiver-noise clocks differ by nonnegative integer lag `L`:

```text
T_rho[t,s]=rho^|t-s|
K_L[t,s]=rho^|t-s-L|
H=I-11^T/N
alpha=tr(H T H T)/tr(H T)^2
beta=tr(H K_L H K_L^T)/tr(H T)^2.
```

For each branch pair, Gaussian cross-Wishart contraction gives

```text
MSE_pair(N,rho,L)
 = alpha*[q(C_S)+q(C_B)] - 2*beta*q(N_noise),
q(A)=(tr A)^2+tr(A A^T).
```

Two branch pairs remain independent, so their terms add. `L=0` exactly recovers synchronous paired milestone. Fixed `rho=0.5`, counts `[16,64,256]`, lag fractions `f=[0,0.25,0.5,1.0]`, and deterministic integer rule `L=round_half_up(f*N)=floor(f*N+0.5)`. Same risk ceiling `0.05` and branch-set threshold.

Baseline preregistration expects timing erosion: normalized cancellation factor `beta/alpha` decreases strictly with lag fraction. Fractions `0`, `0.25`, `0.5` retain minimum count `87`, but one-window lag `f=1.0` restores independent count `88`. `N=64` remains unsafe in every case.

## MVP-first gate

**Objective:** derive exact finite-N lag erosion and count-gate transition.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** lag domain, cross-time trace identity, synchronous limit, fixed lag-fraction risk, monotonic erosion, count-gate transition, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, finite `0<=rho<1`, finite `0<=f<=1`; rejects invalid values and validates `L<=N` under fixed rounding.
2. Direct dense evaluation of `tr(H K_L H K_L^T)` agrees with bounded explicit-sum evaluation within `2e-10` for `(N,L)=(8,2),(16,8),(32,32)` at rho `0.5`.
3. Fraction `f=0` recovers synchronous paired MSE/risk/count `87` within `2e-10`.
4. Risks at counts `[16,64,256]` are finite, positive and strictly decreasing for every fixed fraction.
5. At each fixed count, `beta/alpha` strictly decreases and risk strictly increases over fractions `[0,0.25,0.5,1.0]`.
6. Minimum counts are `[87,87,87,88]`; each predecessor fails, and `N=64` fails for all fractions.
7. Orthogonal channel rotation and common geometric scale preserve normalized MSE/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J103-J110 map one-to-one to controls. New category: `pairing_lag`. Existing J01-J102 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_A_ONE_WINDOW_LAG_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_PAIRING_LAG_EROSION_NOT_EVIDENCE
PHYSICAL_KERR_PAIRING_LAG_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Lag fractions, AR(1), shared-noise identity and synchronized acquisition are toy assumptions, not measured receiver behavior.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
