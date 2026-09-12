# Audit rumore comune su stream appaiati Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_PAIRED_COMMON_NOISE_COVARIANCE_GAIN_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `102/102`.

```text
rho=0.5
independent_coefficient=923.6933349
paired_coefficient=916.1381349
rms_ratio=0.995901934
rms=[9.6935525,4.8837780,2.4424379]
minimum_count=87
risk_87=0.049670477
risk_86=0.050247654
risk_64=0.067498804
zero_shared_minimum_count=88
```

```text
KERR_PAIRED_SIGNAL_CALIBRATION_COMMON_NOISE_CANCELS_A_SMALL_SAMPLING_TERM_BUT_DOES_NOT_REMOVE_AR1_SAMPLE_BURDEN_NOT_ELL0
PHYSICAL_KERR_CROSS_STREAM_SYNCHRONY_COMMON_NOISE_MODEL_AR1_STATIONARITY_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Calcolo cross-Wishart esatto per coppie con rumore gaussiano additivo condiviso e AR(1) comune. L'appaiamento riduce RMS solo dello `0.4098%` e il gate di un campione; `N=64` fallisce ancora. Nessun modello di sincronizzazione/rumore misurato, significatività, potenza, evidenza o detection.
