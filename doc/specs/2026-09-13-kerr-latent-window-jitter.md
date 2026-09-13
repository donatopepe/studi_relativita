# Kerr latent window-jitter mixture

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

One latent integer lag `D` is drawn per centered observation window, uniformly on `{-J,...,J}` and independently between branch pairs. Conditional on `D=d`, signal/calibration samples are jointly Gaussian with fixed-lag cross-time kernel

```text
P(D=d)=1/(2J+1)
K_d[t,s]=rho^|t-s-d|
E[Sx-Sy | D=d]=C_S-C_B.
```

Conditional estimator mean is independent of `d`; therefore law of total covariance has zero between-lag mean term. Exact unconditional covariance-estimator MSE is average conditional Wick MSE:

```text
beta_latent=E_D[tr(H K_D H K_D^T)]/tr(H T)^2
MSE_latent=alpha*sum[q(C_S)+q(C_B)]-4*beta_latent*q(N_noise).
```

For Gaussian averaged-kernel milestone,

```text
beta_kernel=tr(H E[K_D] H E[K_D]^T)/tr(H T)^2.
```

Convexity gives `beta_latent>=beta_kernel`, with strict Jensen gap for nonzero support. Because cross term is subtracted, latent window mixing retains more cancellation and has lower estimator MSE than replacing random lag by averaged Gaussian kernel. No generic Gaussianity claim is made for unconditional sample law.

Fixed `rho=0.5`, counts `[16,64,256]`, fractional radii `f=[0,0.25,0.5,1.0]`, deterministic `J=floor(f*N+0.5)`, same risk ceiling `0.05`. Baseline expects latent minimum counts `[87,87,87,87]`, while Gaussian averaged-kernel counts are `[87,88,88,88]`. `N=64` remains unsafe for both.

## MVP-first gate

**Objective:** derive exact latent-mixture fourth-moment correction and compare with averaged-kernel surrogate.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** latent-mixture domain, conditional fourth-moment identity, zero-support limit, Jensen gap, fixed-fraction risk, count-gate contrast, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, finite `0<=rho<1`, finite `0<=f<=1`; rejects invalid values and verifies uniform weights sum to one.
2. Explicit average over conditional componentwise Wick contractions agrees with compact `beta_latent` formula within `2e-10` for `(N,f)=(8,0.25),(16,0.5),(32,1.0)`.
3. Fraction `f=0` exactly recovers synchronous paired MSE/risk/count 87 within `2e-10`.
4. Jensen gaps `beta_latent-beta_kernel` are zero at `f=0` and strictly positive at nonzero fractions for counts `[16,64,256]`; latent risk is correspondingly lower.
5. Latent risks at counts `[16,64,256]` are finite, positive and strictly decreasing for each fraction, and strictly increase with fraction at each count.
6. Latent minimum counts are `[87,87,87,87]`; averaged-kernel counts are `[87,88,88,88]`; each predecessor fails and `N=64` fails for both models.
7. Orthogonal channel rotation and common geometric scale preserve normalized latent MSE/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims and labels unconditional mixture non-Gaussian/not evidence.

## Scenarios

J119-J126 map one-to-one to controls. New category: `latent_pairing_jitter`. Existing J01-J118 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_LATENT_WINDOW_JITTER_HAS_A_POSITIVE_FOURTH_MOMENT_JENSEN_CORRECTION_RELATIVE_TO_THE_GAUSSIAN_AVERAGED_KERNEL_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
MODEL_LEVEL_LATENT_WINDOW_JITTER_FOURTH_MOMENT_CORRECTION_NOT_EVIDENCE
PHYSICAL_KERR_LATENT_JITTER_DISTRIBUTION_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Latent lag law, conditional Gaussianity, branch-pair independence, AR(1), shared-noise identity and acquisition timing are toy assumptions, not measured behavior.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
