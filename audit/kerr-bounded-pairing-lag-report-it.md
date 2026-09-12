# Audit erosione da ritardo di appaiamento Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_BOUNDED_PAIRING_LAG_EROSION_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `110/110`.

```text
rho=0.5
fractions=[0,0.25,0.5,1.0]
beta_over_alpha_N64=[1.0,0.740204882,0.482882271,0.004159271]
risk_N64=[0.067498804,0.067643419,0.067786657,0.068053137]
minimum_counts=[87,87,87,88]
one_window_risk_88=0.049510145
one_window_risk_87=0.050078845
```

```text
KERR_BOUNDED_PAIRING_LAG_MONOTONICALLY_ERODES_COMMON_NOISE_CANCELLATION_AND_A_ONE_WINDOW_LAG_RESTORES_THE_INDEPENDENT_AR1_COUNT_GATE_NOT_ELL0
PHYSICAL_KERR_PAIRING_LAG_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Calcolo esatto della traccia cross-time centrata. Il ritardo erode monotonicamente il già piccolo beneficio del rumore comune; un ritardo di una finestra ripristina il count 88. `N=64` fallisce per tutte le frazioni fissate. Nessun ritardo/modello di rumore misurato, significatività, potenza, evidenza o detection.
