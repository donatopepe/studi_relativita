# Kerr estimated-mean covariance penalty

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Prior finite-sample gate used known zero mean and estimator `(1/N) sum x x^T`. Realistic covariance estimation usually removes sample mean and uses unbiased estimator

```text
S_hat=(1/(N-1)) sum_k (x_k-x_bar)(x_k-x_bar)^T.
```

For iid Gaussian vectors, `(N-1)S_hat` is centered Wishart with degrees of freedom `nu=N-1`. Therefore

```text
E||S_hat-C||_F^2=((tr C)^2+tr(C^2))/(N-1).
```

Relative to known-mean MSE at same `N`, exact penalty is `N/(N-1)`. Four covariance estimates remain independent and use same committed covariances/branch-set separation. Fixed counts `[16,64,256]`, risk ceiling `0.05`.

## MVP-first gate

**Objective:** quantify one lost degree of freedom and corrected conservative sample-count gate.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** centered-Wishart identity, domain, known/estimated relation, RMS sequence, corrected safe count, unsafe count, basis/scale invariance, nonclaims.

## Eight controls

1. Centered-Wishart componentwise contraction agrees with Frobenius MSE formula within `2e-10` for all four SPD covariances.
2. Domain rejects `N<2`, noninteger counts and non-SPD/nonfinite covariance.
3. Estimated/known mean MSE ratio equals `N/(N-1)` for `[16,64,256]` within `2e-10`.
4. Estimated-mean combined RMS at `[16,64,256]` is finite, positive and strictly decreasing with exact `sqrt((N2-1)/(N1-1))` ratios.
5. Smallest integer count meeting conservative risk `<=0.05` is `54`; predecessor `53` fails.
6. `N=16` remains unsafe and `N=64` remains safe only under this model-level Markov gate.
7. Orthogonal basis rotation and common geometric scale preserve normalized MSE/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J79-J86 map one-to-one to controls. New category: `estimated_mean`. Existing J01-J78 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_GAUSSIAN_ESTIMATED_MEAN_COSTS_EXACTLY_ONE_COVARIANCE_DEGREE_OF_FREEDOM_AND_RAISES_ONLY_THE_CONSERVATIVE_TOY_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_ESTIMATED_MEAN_COVARIANCE_PENALTY_NOT_EVIDENCE
PHYSICAL_KERR_UNKNOWN_MEAN_NON_GAUSSIANITY_SAMPLE_DEPENDENCE_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
