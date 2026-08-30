# Audit Jacobi dello scattering nullo finito di Kottler

## Stato

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

Risultato:

```text
KOTTLER_LAMBDA_ADDS_STATIC_BOUNDARY_NORMALIZATION_BUT_NULL_RICCI_FOCUSING_AND_CONVERTED_NULL_JACOBI_SHAPE_CANCEL_WHILE_JOINT_MLAMBDA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Gate:

```text
PHYSICAL_COSMOLOGICAL_MATCHING_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

## Controllo congelato

Metrica: `f(r)=1-2M/r-Lambda*r^2/3`; `alpha=Lambda*M^2`. Baseline: `M=1`, `alpha=0.003`, `rho=4`, `R=8`, energia di Killing unitaria, `beta=5.7495957`, endpoint finiti allo stesso raggio nella carta statica, un turning point, screen `(polar,in-plane)`. Qui `b=Phi/E` è una costante canonica, non un parametro d'impatto misurato asintoticamente. La mappa completa `4x4` resta primaria.

Kottler è uno spazio di Einstein. Anche se Ricci dello spaziotempo è nonzero, `R_mn k^m k^n=0` per `k` nullo; la baseline dà `maximum_abs_null_Ricci_trace=0.0`. Classificazione: `NULL_RICCI_FOCUSING_IN_EINSTEIN_SPACE_NOT_ZERO_SPACETIME_RICCI`. Ricci, contrazione nulla e profilo screen appartengono a un solo record grezzo di curvatura; `DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE`.

## Controesempi e controlli

- L'orbita coordinata canonica obbedisce a `u''+u=3M*u^2`; la cancellazione di Lambda non elimina dipendenze da boundary statico o normalizzazione.
- Dopo conversione affine/frequenza Schwarzschild effettiva, path e forma Jacobi nulla si cancellano entro tolleranza numerica bounded. Non è identificazione della scala operatoriale.
- `alpha=0` coincide con Schwarzschild: `phase_map_residual=1.0249681e-05`.
- de Sitter puro è trattato analiticamente fuori da `x=r/M`: matrice ottica nulla mentre lo spaziotempo non è piatto.
- La dilatazione congiunta `(M,Lambda)` preserva il record adimensionale dopo la conversione dichiarata: `JOINT_M_LAMBDA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE`.
- Il rappresentante di rango dà `rank_with_log_M_and_alpha=0`, `scale_null_direction=[1,0]` dopo la conversione.
- Lambda dimensionale fissata può recuperare `M` da alpha solo importando uno standard: `FIXED_EXTERNAL_LAMBDA_IS_IMPORTED_DIMENSIONAL_STANDARD_NOT_ELL0`.

## Scope e review

Rindler–Ishak supporta metrica, equazione orbitale canonica e distinzione tra path coordinato e angolo locale. Non supporta protocollo Jacobi finite-window, detector, covarianza, `ell0`, UMCH, evidenza o detection. Nessun matching cosmologico, source/receiver fisico, rumore calibrato, covarianza congiunta o legge geometria-`ell/ell0` è derivato.

Review: `DIRECT_REVIEW_NO_SUBAGENT`; non è review indipendente. Nessun vicolo cieco strutturale dichiarato.
