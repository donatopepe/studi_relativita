# Audit miscela di scala per finestra Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_WINDOW_SCALE_MIXTURE_FLOOR_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `166/166`.

```text
rho=0.5
fraction=1.0
Delta_coefficient=304.907367059628
floor_coefficient=0.862883522363
cv=[0,0.1,0.2,0.25]
minimum_counts=[87,106,292,None]
floor_risk=[0,0.008628835224,0.034515340895,0.053930220148]
critical_cv=0.240718192810
```

```text
KERR_WINDOW_LEVEL_SCALE_MIXTURE_CREATES_NONDECAYING_COVARIANCE_RISK_FLOOR_AND_CV_0P240718193_PRECLUDES_ANY_FINITE_TOY_COUNT_GATE_NOT_ELL0
PHYSICAL_KERR_WINDOW_SCALE_DISTRIBUTION_NON_GAUSSIANITY_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Identità esatta della covarianza totale. La variabilità di scala per finestra crea un floor non decadente; al CV critico o sopra nessun count finito passa il ceiling toy. CV è nuisance non misurato, non confidenza, significatività, prescrizione di sample size, evidenza o detection.
