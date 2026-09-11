# Kerr calibration-reference placement correction

`CORRECTION_OF_16c9718`

Prior auxiliary-channel result reversed collision polarity. Equal signal and calibration outputs require

```text
x_+(Gamma_+-R)=x_-(Gamma_--R)
```

with positive squared gains. Collision is possible when product `(Gamma_+-R)(Gamma_--R)` is positive. Reference strictly inside branch-variance interval makes product negative and blocks positive collision; reference outside interval permits it.

Correct inside control:

```text
inside_reference=[0.1,10.0]
inside_products=[-0.0057111803,-387.61661]
```

Exact outside collision:

```text
outside_reference=[0.02,0.02]
outside_minus_gains=[0.26505327,0.25898719]
outside_collision=1.7763568e-15
```

Unknown reference still collides:

```text
unknown_reference_collision=8.8817842e-16
```

All corrected `8/8` controls and `54/54` scenarios pass. Local Fisher rank two remains true but does not prove global branch identifiability. Reference placement/stability is unmeasured toy input.

```text
KNOWN_REFERENCE_BLOCKS_POSITIVE_GAIN_NOISE_BRANCH_COLLISION_ONLY_WHEN_PLACED_STRICTLY_BETWEEN_BRANCH_VARIANCES_WHILE_OUTSIDE_OR_UNKNOWN_REFERENCE_COLLIDES_EXACTLY_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
MODEL_LEVEL_REFERENCE_PLACEMENT_CORRECTION_NOT_EVIDENCE
PHYSICAL_KERR_CALIBRATOR_REFERENCE_PLACEMENT_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
