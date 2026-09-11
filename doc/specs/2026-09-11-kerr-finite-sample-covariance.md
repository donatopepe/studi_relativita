# Kerr finite-sample covariance uncertainty

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model and source scope

This toy assumes four independent zero-mean Gaussian sample sets: signal and calibration under each branch. Covariance estimator uses known zero mean,

```text
S_hat=(1/N) sum_k x_k x_k^T.
```

For `x~N(0,C)`, direct fourth-moment/Wick contraction gives

```text
E||S_hat-C||_F^2=((tr C)^2+tr(C^2))/N.
```

No external empirical source is needed: identity is derived and checked componentwise in code. Independence lets MSEs add for estimated branch difference

```text
H_hat=(S_hat_+-B_hat_+)-(S_hat_--B_hat_-).
```

Use committed correlated-noise anchor, inside reference, minimum gains `[0.5,0.5]`, equal sample count per four covariance estimates, and branch-set separation `tau=18.797836635...`. Fixed sample counts: `[16,64,256]`.

Define RMS Frobenius error `epsilon_N=sqrt(E||H_hat-H||_F^2)`. Since operator norm is bounded by Frobenius norm, Markov gives conservative collision-scale excursion bound

```text
P(||error||_2 >= tau) <= epsilon_N^2/tau^2.
```

Predeclare risk ceiling `0.05`; exact smallest equal count meeting this bound is recorded. Counts and risk are toy design controls, not observed data significance.

## MVP-first gate

**Objective:** quantify exact covariance-estimation RMS and a conservative branch-separation risk bound.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** Wishart covariance identity, domain, branch RMS, sample-count scaling, safe count, unsafe count, basis/scale invariance, nonclaims.

## Eight controls

1. Componentwise Gaussian fourth-moment covariance identity and Frobenius MSE formula agree within `2e-10` for all four SPD covariances.
2. Domain rejects non-SPD/nonfinite covariance and nonpositive/noninteger sample counts.
3. Exact combined RMS at counts `[16,64,256]` is finite, positive and strictly decreasing.
4. RMS ratios obey inverse-square-root law: `epsilon_16/epsilon_64=2`, `epsilon_64/epsilon_256=2` within `2e-10`.
5. Smallest integer equal count with conservative risk bound `<=0.05` is exact and its predecessor fails.
6. `N=16` remains an authoritative unsafe negative (`risk_bound>0.05`); `N=64` passes only this model-level Markov gate.
7. Orthogonal basis rotation and common geometric scale conversion preserve normalized RMS/risk within `2e-10`.
8. Artifact preserves `L_identified=false`, `ell0_identified=false`, `L_equals_ell0=NOT_DERIVED`, no extra-dimension detection and no positive detection claim.

## Scenarios

J71-J78 map one-to-one to controls. New category: `finite_sample`. Existing J01-J70 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_GAUSSIAN_FINITE_SAMPLE_COVARIANCE_ERROR_FOLLOWS_EXACT_INVERSE_ROOT_COUNT_SCALING_AND_ONLY_A_CONSERVATIVE_TOY_COUNT_GATE_BOUNDS_BRANCH_COLLISION_SCALE_NOT_ELL0
MODEL_LEVEL_GAUSSIAN_COVARIANCE_UNCERTAINTY_NOT_EVIDENCE
PHYSICAL_KERR_SAMPLE_INDEPENDENCE_GAUSSIANITY_MEAN_ESTIMATION_CALIBRATION_MATCHING_DRIFT_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
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
