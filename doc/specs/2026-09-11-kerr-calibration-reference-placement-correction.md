# Kerr calibration-reference placement correction

## Status

`RATIFIED_CORRECTION_FOR_IMMEDIATE_IMPLEMENTATION`

## Root cause

Published auxiliary-channel milestone `16c9718` reversed collision polarity. From equal signal and calibration outputs,

```text
x_+(Gamma_+-R)=x_-(Gamma_--R), x_+,x_->0
```

positive gains exist iff `(Gamma_+-R)(Gamma_--R)>0`, not when product is negative. Therefore reference outside branch-variance interval permits collision; reference strictly inside interval obstructs it. Prior `[0.02,0.02]` was below both variances in both channels and does not remove collision.

Historical artifact and reports must be corrected explicitly, not silently erased.

## MVP-first gate

**Objective:** correct polarity and preserve exact inside/outside outcomes.

**Metric and threshold:** exactly `8/8` controls.

**Cases/order:** corrected algebra, inside-interval collision obstruction, outside-interval exact collision, two-channel joint witness, Fisher rank, unknown-reference collision, weak-channel limit, scale/nonclaims.

**Fixed references:**

```text
Gamma_+=[0.0390710115,4.432720985]
Gamma_-=[0.1937350255,79.624067525]
R_inside=[0.1,10.0]
R_outside=[0.02,0.02]
```

Use plus gains `[0.8,1.1]`, plus noise `[0.25,0.35]`. For each reference placement, exact candidate minus gain follows squared-gain ratio; minus noise is solved from equal calibration variance and must be positive for recorded witness.

## Eight controls

1. Algebraic collision criterion residual below `2e-10`; sign polarity regression is explicit.
2. Inside references lie strictly between branch variances in both channels and produce negative products.
3. Positive exact collision is impossible for inside references by sign contradiction.
4. Outside references produce explicit positive gain/noise two-channel exact joint collision below `2e-10`.
5. Joint signal/reference Jacobian remains local rank two per channel whenever `Gamma != R`; this does not imply branch identifiability.
6. Unknown branch-profiled reference preserves exact collision below `2e-10`.
7. Weak-channel information sequence and finite-sample precision remain valid controls.
8. Scale bookkeeping/nonclaims remain unchanged: no `L`, `ell0`, extra dimension or detection identification.

## Scenarios

J47-J54 map one-to-one to controls. New category: `reference_placement`. Existing J01-J46 remain preserved, but J41 interpretation must be corrected in implementation. Runner remains fail-closed total/scenario/category with JSON.

## Corrected interpretation

```text
KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES_WHILE_OUTSIDE_OR_UNKNOWN_REFERENCE_COLLIDES_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_REFERENCE_PLACEMENT_CORRECTION_NOT_EVIDENCE
PHYSICAL_KERR_CALIBRATOR_REFERENCE_PLACEMENT_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
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
