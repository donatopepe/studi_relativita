# Audit canale ausiliario di calibrazione Kerr

> `SUPERSEDED_BY_REFERENCE_PLACEMENT_CORRECTION`: il milestone `16c9718` invertiva la polarità della collisione. Il precedente riferimento esterno `[0.02,0.02]` consente collisione esatta. Record corretto: `kerr-calibration-reference-correction-report-it.md`.

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_AUXILIARY_CALIBRATION_CHANNEL_IDENTIFIABILITY_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `46/46`.

```text
known_reference=[0.02,0.02]
sign_obstruction=[0.0033133027,351.27054]
calibration_only_rank=[1,1]
joint_rank=[2,2]
relative_std=[1.4142136,0.4472136,0.14142136]
weak_information=[0.5,0.05,0.005]
unknown_reference_collision=8.8817842e-16
```

```text
KNOWN_AUXILIARY_REFERENCE_CHANNEL_REMOVES_RELAXED_GAIN_NOISE_BRANCH_COLLISION_AT_MODEL_LEVEL_BUT_UNKNOWN_REFERENCE_RESTORES_EXACT_COLLISION_AND_ABSOLUTE_SCALE_REMAINS_BLIND_NOT_ELL0
PHYSICAL_KERR_CALIBRATOR_REFERENCE_STABILITY_CROSS_CHANNEL_NOISE_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Il riferimento noto impedisce collisioni positive esatte e la mappa segnale/calibrazione è localmente a rango pieno. Un riferimento ignoto collide esattamente; la precisione finita cala con i campioni. Assunzioni toy, non prior misurati né evidenza.
