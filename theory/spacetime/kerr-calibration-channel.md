# Kerr auxiliary calibration-channel identifiability

> **SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION:** milestone `16c9718` reversed collision polarity. See [`kerr-calibration-reference-correction.md`](kerr-calibration-reference-correction.md). Correct result: only a reference strictly inside branch-variance interval blocks positive collision; prior outside reference `[0.02,0.02]` permits exact collision.

A branch-independent auxiliary Gaussian channel observes same gains/noise as Kerr signal channel against known reference covariance. For each diagonal channel, equality of signal and calibration outputs requires squared branch gains with sign ratio controlled by `(Gamma_+-R)/(Gamma_--R)`. A known reference outside interval between branch variances blocks positive exact collision.

```text
known_reference=[0.02,0.02]
sign_obstruction=[0.0033133027,351.27054]
```

Single calibration variance alone constrains only one gain/noise combination. Adding signal variance gives full local rank when `Gamma != R`:

```text
calibration_only_rank=[1,1]
joint_rank=[2,2]
```

Finite Gaussian sample-variance uncertainty and weak-channel limit remain explicit:

```text
relative_std=[1.4142136,0.4472136,0.14142136]
weak_information=[0.5,0.05,0.005]
```

An unknown reference restores exact collision:

```text
unknown_reference_collision=8.8817842e-16
```

All `8/8` controls and `46/46` scenarios pass. This is model-level identifiability conditional on known stable reference, diagonal noise and Gaussian sampling, not hardware evidence.

```text
KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION_AT_MODEL_LEVEL_BUT_UNKNOWN_REFERENCE_RESTORES_EXACT_COLLISION_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE
PHYSICAL_KERR_CALIBRATOR_REFERENCE_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
