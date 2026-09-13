# Audit erosione da jitter di appaiamento Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_BOUNDED_PAIRING_JITTER_EROSION_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `118/118`.

```text
rho=0.5
jitter_radii=[0,1,2,4,8,16]
beta_over_alpha_N64=[1.0,0.789485810,0.623302468,0.404555012,0.204269692,0.073046173]
risk_N64=[0.067498804,0.067615986,0.067708492,0.067830258,0.067941746,0.068014792]
minimum_counts=[87,87,87,87,87,88]
radius_16_risk_88=0.049473762
radius_16_risk_87=0.050042318
```

```text
KERR_BOUNDED_UNIFORM_PAIRING_JITTER_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_RADIUS_16_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
PHYSICAL_KERR_PAIRING_JITTER_DISTRIBUTION_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Calcolo esatto della traccia gaussiana con kernel misto centrato. La media sul supporto erode monotonicamente la già piccola cancellazione; il raggio 16 ripristina il count 88. `N=64` fallisce per tutti i raggi fissati. Non è una miscela latente non gaussiana di covarianze a livello di finestra. Nessun jitter/modello di rumore misurato, significatività, potenza, evidenza o detection.
