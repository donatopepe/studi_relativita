# Kerr bounded pairing-jitter erosion

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Each paired acquisition has an unobserved integer timing offset `D`, independent of Gaussian amplitudes and uniformly distributed on bounded symmetric support `{-J,...,J}`. Marginal stream covariance remains AR(1), while shared-noise cross-time covariance becomes mixture

```text
P(D=d)=1/(2J+1),  d=-J,...,J
K_J[t,s]=(1/(2J+1))*sum_{d=-J}^J rho^|t-s-d|
H=I-11^T/N
alpha=tr(H T H T)/tr(H T)^2
beta_J=tr(H K_J H K_J^T)/tr(H T)^2.
```

Gaussian cross-Wishart contraction applies conditionally to this declared joint Gaussian covariance model, giving total two-branch-pair MSE

```text
MSE_jitter=alpha*sum[q(C_S)+q(C_B)]-4*beta_J*q(N_noise),
q(A)=(tr A)^2+tr(A A^T).
```

Fixed `rho=0.5`, counts `[16,64,256]`, integer jitter radii `J=[0,1,2,4,8,16]`, same risk ceiling `0.05` and branch-set threshold. Evaluation domain requires `0<=J<=N` for each reported finite window; minimum-count search begins at `max(2,J)`.

Baseline preregistration expects support averaging to erase cross-time structure faster than a known fixed lag. At N=64, `beta_J/alpha` should decrease strictly over fixed radii. Minimum count should remain 87 through J=8, then return to independent count 88 at J=16. `N=64` remains unsafe for all supports.

## MVP-first gate

**Objective:** derive exact bounded uniform-jitter erosion and count transition.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** jitter domain, mixture covariance identity, zero-jitter limit, fixed-support risk, monotonic erosion, count-gate transition, basis/scale invariance, nonclaims.

## Eight controls

1. Domain accepts integer `N>=2`, integer `0<=J<=N`, finite `0<=rho<1`; rejects invalid values and verifies mixture symmetry.
2. Direct averaging of fixed-lag matrices agrees elementwise with explicit mixture covariance within `2e-10` for `(N,J)=(8,1),(16,4),(32,16)` at rho `0.5`; dense and explicit centered traces agree.
3. Radius `J=0` recovers synchronous paired MSE/risk/count 87 within `2e-10`.
4. Risks at counts `[16,64,256]` are finite, positive and strictly decreasing for every fixed radius.
5. At each fixed count, `beta_J/alpha` strictly decreases and risk strictly increases over radii `[0,1,2,4,8,16]` that satisfy `J<=N`.
6. Minimum counts are `[87,87,87,87,87,88]`; each predecessor fails, and `N=64` fails for every radius.
7. Orthogonal channel rotation and common geometric scale preserve normalized MSE/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J111-J118 map one-to-one to controls. New category: `pairing_jitter`. Existing J01-J110 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_RADIUS_16_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
MODEL_LEVEL_BOUNDED_PAIRING_JITTER_EROSION_NOT_EVIDENCE
PHYSICAL_KERR_PAIRING_JITTER_DISTRIBUTION_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Uniform jitter, independence, AR(1), shared-noise identity and acquisition timing are toy assumptions, not measured receiver behavior.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
