# Audit finestra di fase rho per la legge dei ritardi Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_RHO_CRITICAL_LATENT_LAG_LAW_PHASE_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `150/150`.

```text
N=87
fraction=1.0
risk_ceiling=0.05
rho_low=0.499243438917
rho_high=0.501157235677
rho_window_width=0.001913796761
path_rho=[0.4995,0.5,0.5005,0.501]
path_kappa=[12.485595532,3.890241565,2.001949812,1.172518080]
```

```text
KERR_COUNT_87_LATENT_LAG_LAW_SENSITIVITY_EXISTS_ONLY_IN_TOY_AR1_WINDOW_RHO_0P499243439_TO_0P501157236_NOT_ELL0
PHYSICAL_KERR_AR1_RHO_LAG_LAW_RADIUS_SUPPORT_WINDOW_INDEPENDENCE_SYNCHRONY_COMMON_NOISE_MODEL_STATIONARITY_CONDITIONAL_GAUSSIANITY_CALIBRATION_MATCHING_HARDWARE_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Mappa di fase esatta con bisezione bounded. Sotto la finestra il count 87 passa ogni legge del ritardo; dentro conta kappa finito; sopra fallisce già la legge uniforme. La finestra è boundary di assunzioni toy, non confidenza/evidenza di stazionarietà o tolleranza misurata. Nessuna evidenza o detection.
