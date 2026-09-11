# Kerr bounded reference-drift robustness

Corrected collision obstruction requires reference remain strictly inside interval between branch variances. Midpoint gives maximal symmetric open drift radii:

```text
midpoints=[0.11640302,42.028394]
max_radii=[0.077332007,37.595673]
```

At preregistered fraction:

```text
drift_fraction=0.8
safe_radii=[0.061865606,30.076539]
minimum_margin=0.0021528862
minimum_fisher_determinant=0.0024746242
```

Endpoint makes placement product and local determinant vanish:

```text
endpoint_loss=0.0
```

Crossing just outside lower endpoint restores explicit positive gain/noise collision:

```text
outside_collision=8.8817842e-16
```

All `8/8` controls and `62/62` scenarios pass. Robustness is conditional on toy drift bound, not measured calibrator stability.

```text
KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL_AND_FAILS_AT_ENDPOINT_OR_OUTSIDE_NOT_ELL0
MODEL_LEVEL_BOUNDED_REFERENCE_DRIFT_ROBUSTNESS_NOT_EVIDENCE
PHYSICAL_KERR_CALIBRATOR_DRIFT_BOUND_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```
