# Kerr auxiliary calibration-channel identifiability

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

## Scientific distinction

Prior composite profiling permits each branch to choose an unconstrained candidate gain/noise point. This MVP adds a branch-independent auxiliary calibration observation produced by same receiver gains/noise. It asks whether known reference variance removes nuisance collision at model level; it does not claim a physical calibrator exists.

For channel `i`, signal and calibration variances are

```text
S_{o,i}=g_i^2 Gamma_{o,i}+n_i^2
B_i=g_i^2 R_i+n_i^2
```

with known positive reference variance `R_i`. Noise is diagonal per channel for minimal algebraic identifiability. Fixed design point:

```text
g=(0.8,1.1)
n=(0.25,0.35)
R=(0.02,0.02)
N_cal=(1,10,100)
```

If two branch/nuisance candidates have equal `(S_i,B_i)`, subtraction gives

```text
x_+(Gamma_{+,i}-R_i)=x_-(Gamma_{-,i}-R_i), x_o=g_{o,i}^2
```

while equal calibration outputs fix noise difference. For `R_i` outside the open interval between branch signal variances, positive exact branch collision is impossible. Channel 1 uses `R=0.02 < Gamma_+=0.039071...`; channel 2 likewise uses `R=0.02` below both branches.

## MVP-first gate

**Objective:** test known-reference identifiability and preserve exact failure when reference variance is unknown.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** joint signal/calibration map, domain, exact known-reference noncollision, Fisher rank, finite calibration precision, weak-calibration limit, unknown-reference collision, scale/nonclaims.

## Eight controls

1. Joint signal/calibration covariance map matches expanded diagonal formula within `2e-10`.
2. Domain rejects invalid branch, nonfinite/nonpositive gains, noise, reference and sample count.
3. Known `R=(0.02,0.02)` gives positive channelwise sign obstruction and no exact relaxed positive-gain branch collision.
4. Calibration-only Fisher matrix for parameters `(log g_i, log n_i)` has rank one per single reference channel; joint signal+calibration map has full local rank two per channel away from `Gamma=R`.
5. Calibration sample variance relative standard deviation follows exact Gaussian value `sqrt(2/N_cal)` for `N_cal=(1,10,100)` and decreases strictly.
6. As `N_cal -> 0` information from auxiliary channel vanishes; `N_cal=(1,0.1,0.01)` is strictly decreasing to preregistered endpoint.
7. If `R_i` is unknown and branch-profiled, an explicit exact positive-gain collision reproduces equal signal and calibration outputs below `2e-10`.
8. Common basis/scale bookkeeping preserves joint result and keeps `L_identified=false`, `ell0_identified=false`, `L_equals_ell0=NOT_DERIVED`, no extra-dimension detection and no positive detection claim.

## Scenarios

J39-J46 map one-to-one to controls above. New category: `calibration_channel`. Existing J01-J38 remain unchanged. Runner must remain fail-closed in total, per-scenario and per-category modes with JSON output.

## Interpretation ceiling

```text
MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE
```

Known reference, diagonal independent noise and Gaussian sample-count law are toy assumptions, not hardware calibration priors or measurements.

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```

## Source scope

Uses existing verified Gaussian covariance/KL identities plus standard chi-square variance of Gaussian sample variance. No empirical Kerr, hardware or extra-dimensional claim is introduced.
