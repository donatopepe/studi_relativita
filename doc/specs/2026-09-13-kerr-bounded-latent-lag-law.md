# Kerr bounded latent-lag law robustness

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Retain one latent integer lag `D` per centered window and conditional Gaussian fixed-lag kernels. Replace known uniform lag law on support `{-J,...,J}` by unknown probability vector `p` in density-ratio box around uniform `u=1/(2J+1)`:

```text
sum_d p_d=1
u/kappa <= p_d <= kappa*u
kappa in [1,2,4].
```

No symmetry of probabilities is imposed; support remains symmetric. Conditional covariance-estimator mean stays lag-independent, so

```text
beta(p)=sum_d p_d beta_d
beta_d=tr(H K_d H K_d^T)/tr(H T)^2.
```

Risk decreases linearly with `beta(p)`. Worst risk therefore minimizes `beta(p)` over bounded simplex; best risk maximizes it. Exact extrema come from starting all probabilities at lower bound and greedily allocating remaining mass, up to upper bound, in ascending/descending `beta_d` order. This is exact finite-dimensional linear programming, not numerical optimization.

Fixed `rho=0.5`, counts `[16,64,256]`, fractions `f=[0,0.25,0.5,1.0]` with `J=floor(f*N+0.5)`, kappas `[1,2,4]`, same risk ceiling `0.05`. Baseline expects uniform recovery at kappa 1; envelopes widen monotonically. Worst-case minimum counts at kappa 2 remain `[87,87,87,87]`; at kappa 4 become `[87,87,87,88]`. Best-case counts remain `[87,87,87,87]`. `N=64` remains unsafe everywhere.

## MVP-first gate

**Objective:** derive exact bounded-law risk envelope and count robustness.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** probability-box domain, linear-program extremum identity, uniform limit, fixed-box envelope, monotonic widening, count-gate transition, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, finite `0<=rho<1`, finite `0<=f<=1`, finite `kappa>=1`; generated extremal probabilities are nonnegative, sum to one and obey bounds. Invalid values rejected.
2. Greedy extrema agree with exhaustive vertex enumeration within `2e-10` for fixed small coefficient vectors and `(N,f,kappa)=(8,0.25,2)`.
3. `kappa=1` exactly recovers uniform latent beta/risk/count within `2e-10`.
4. At kappas `[1,2,4]`, best/uniform/worst risk ordering holds at counts `[16,64,256]` and every fixed fraction.
5. Risk-envelope width is nondecreasing with kappa at every fixed count/fraction; zero-support width remains zero.
6. Worst counts are `[87,87,87,87]` at kappa 2 and `[87,87,87,88]` at kappa 4; best counts stay `[87,87,87,87]`; predecessors fail and `N=64` is always unsafe.
7. Orthogonal channel rotation and common geometric scale preserve normalized extrema/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels density-ratio bounds/toy lag law as unmeasured.

## Scenarios

J127-J134 map one-to-one to controls. New category: `latent_lag_law_robustness`. Existing J01-J126 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_LATENT_LAG_LAW_DENSITY_RATIO_BOUNDS_GIVE_EXACT_RISK_ENVELOPES_BUT_KAPPA_4_CAN_RESTORE_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_LATENT_LAG_LAW_ROBUSTNESS_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_LAG_LAW_BOUNDS_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Density-ratio bounds, lag support/law, conditional Gaussianity, branch-pair independence, AR(1), shared-noise identity and timing are toy assumptions, not measured behavior.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
