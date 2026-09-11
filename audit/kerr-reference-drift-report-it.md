# Audit robustezza al drift del riferimento Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_BOUNDED_REFERENCE_DRIFT_ROBUSTNESS_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `62/62`.

```text
midpoints=[0.11640302,42.028394]
max_radii=[0.077332007,37.595673]
drift_fraction=0.8
safe_radii=[0.061865606,30.076539]
minimum_margin=0.0021528862
endpoint_loss=0.0
outside_collision=8.8817842e-16
minimum_fisher_determinant=0.0024746242
```

```text
KERR_REFERENCE_COLLISION_OBSTRUCTION_SURVIVES_ONLY_WHILE_REFERENCE_DRIFT_STAYS_STRICTLY_INSIDE_BRANCH_VARIANCE_INTERVAL_AND_FAILS_AT_ENDPOINT_OR_OUTSIDE_NOT_ELL0
PHYSICAL_KERR_CALIBRATOR_DRIFT_BOUND_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Il raggio analitico dell'intervallo aperto è esatto. Il box conservativo 0.8 mantiene l'ostruzione. All'endpoint si perdono rango e ostruzione; fuori intervallo torna collisione esatta. Nessuna stabilità misurata né evidenza.
