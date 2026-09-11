# Kerr auxiliary calibration-channel audit

> `SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION`: milestone `16c9718` reversed collision polarity. Prior outside reference `[0.02,0.02]` permits exact collision. Corrected record: `kerr-calibration-reference-correction-report-en.md`.

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Corrected J39-J46 controls `8/8`; total scenario battery `54/54`.

```text
known_reference=[0.1,10.0]
placement_products=[-0.0057111803,-387.61661]
calibration_only_rank=[1,1]
joint_rank=[2,2]
relative_std=[1.4142136,0.4472136,0.14142136]
weak_information=[0.5,0.05,0.005]
unknown_reference_collision=8.8817842e-16
```

```text
KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION_AT_MODEL_LEVEL_BUT_UNKNOWN_REFERENCE_RESTORES_EXACT_COLLISION_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
CORRECTED_SCOPE=REFERENCE_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL
PHYSICAL_KERR_CALIBRATOR_REFERENCE_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Known reference strictly inside branch-variance interval blocks positive exact collision; joint signal/calibration map is locally full-rank. Unknown reference collides exactly; finite sample precision weakens with calibration count. Assumptions are toy, not measured priors or evidence.
