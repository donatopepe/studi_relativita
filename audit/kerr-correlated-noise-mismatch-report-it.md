# Audit mismatch del rumore correlato Kerr

```text
ell0_identified=false
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_CORRELATED_NOISE_MISMATCH_THRESHOLD_NOT_EVIDENCE
DIRECT_REVIEW_NO_SUBAGENT
```

Controlli `8/8`; batteria scenari `70/70`.

```text
noise_eigenvalues=[0.35790627,0.74209373]
cancellation_residual=8.8817842e-16
tau=18.797837
safe_bound=15.038269
remaining_separation=3.7595673
threshold_collision=1.3322676e-15
minimum_observed_eigenvalue=0.39954509
```

```text
KERR_SHARED_CORRELATED_RECEIVER_NOISE_CANCELS_IN_SIGNAL_MINUS_CALIBRATION_BUT_DIFFERENTIAL_MISMATCH_AT_THE_EXACT_CONE_MARGIN_RESTORES_COLLISION_NOT_ELL0
PHYSICAL_KERR_SIGNAL_CALIBRATION_NOISE_MATCHING_DRIFT_HARDWARE_PRIORS_SAMPLING_SYSTEMATICS_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Il rumore correlato pieno condiviso si cancella esattamente. La distanza operatoriale usa matrici di branca complete. Mismatch aggregato sotto 0.8 lascia separazione positiva; alla soglia completa collidono. Nessun limite misurato né evidenza.
