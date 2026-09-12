# Kerr paired-stream common-noise cancellation

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Model

Within each branch, signal and calibration samples are paired in time and share same additive Gaussian receiver noise:

```text
x_t = s_t + e_t
y_t = r_t + e_t
Cov(x_t)=C_S, Cov(y_t)=C_B, Cov(x_t,y_t)=K=N.
```

Latent signal `s`, reference `r`, and common noise `e` are mutually independent. All use same separable AR(1) time matrix at fixed rho `0.5`; branch pairs remain independent. For centered covariance estimators with common factor `alpha(N,rho)`, Wick contraction gives

```text
E||[(Sx-C_S)-(Sy-C_B)]||_F^2
 = alpha * [q(C_S)+q(C_B)-2 q(K)],
q(A)=(tr A)^2+tr(A A^T).
```

For two independent branch pairs, coefficients add. Cross term cancels part of common-noise sampling fluctuation. Fixed counts `[16,64,256]`, same noise anchor and risk ceiling `0.05`.

Baseline preregistration expects small gain: shared-noise coefficient is minor relative to Kerr minus-branch variance, so pairing should reduce RMS only about `0.4%` and count gate from `88` to `87`, not solve sample burden.

## MVP-first gate

**Objective:** derive exact paired covariance MSE and preserve small-gain negative result.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** joint block domain, cross-Wishart identity, paired coefficient, AR(1) RMS, safe count, zero-shared limit, basis/scale invariance, nonclaims.

## Eight controls

1. Each branch joint `4x4` block covariance `[[C_S,K],[K^T,C_B]]` is SPD; invalid cross-covariance is rejected.
2. Direct componentwise cross-Wick contraction agrees with compact paired Frobenius coefficient within `2e-10`.
3. Paired total coefficient is positive and strictly below independent coefficient; RMS reduction ratio lies in preregistered small range `[0.99,1.0)`.
4. At rho `0.5`, paired RMS at `[16,64,256]` is finite, positive and strictly decreasing.
5. Minimum count meeting conservative risk `<=0.05` is `87`; predecessor fails; `N=64` remains unsafe.
6. Setting shared cross-covariance `K=0` exactly recovers independent-stream AR(1) coefficient/count `88` within `2e-10`.
7. Orthogonal basis rotation and common geometric scale preserve normalized paired MSE/risk within `2e-10`.
8. Artifact preserves all `L`/`ell0`/extra-dimension/detection nonclaims.

## Scenarios

J95-J102 map one-to-one to controls. New category: `cross_stream_dependence`. Existing J01-J94 remain unchanged. Runner remains fail-closed total/scenario/category with JSON.

## Interpretation ceiling

```text
KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
MODEL_LEVEL_PAIRED_COMMON_NOISE_COVARIANCE_GAIN_NOT_EVIDENCE
PHYSICAL_KERR_CROSS_STREAM_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Pairing/common-noise synchrony is toy assumption, not measured receiver behavior.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
