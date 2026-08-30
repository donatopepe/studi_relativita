# Audit Jacobi dello scattering nullo finito di Reissner–Nordström

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
REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE_BUT_Q_SQUARED_DEGENERACY_AND_JOINT_MQ_DILATION_RETAIN_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Gate:

```text
PHYSICAL_CHARGE_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

## Controllo congelato

Metrica: `f(r)=1-2M/r+Q^2/r^2`. Coordinata di forma: `epsilon=Q/M`. La baseline usa `M=1`, `epsilon=0.8`, `rho=4`, `R=12`, energia di Killing unitaria, `beta=5.4433105`, endpoint finiti allo stesso raggio e ordine screen `(polar,in-plane)`. La full phase map `4x4` è primaria; traccia screen, parte senza traccia e proiezioni a grafo restano diagnostiche secondarie.

La proiezione numerica diretta del Riemann quadridimensionale dà `maximum_abs_Ricci_trace=0.0092592465`. È forma ottica dipendente dalla carica, non un canale misurato indipendente. Non esiste covarianza congiunta: `DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE`.

## Controesempi e conformità

- A `epsilon=0`, il residuo del cammino è zero e la full map Schwarzschild ha `phase_map_residual=8.0925039e-06` alla risoluzione dell'artifact.
- Sostituire `Q` con `-Q` lascia invariati cammino, profilo e mappa: `Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0`.
- L'inversione di orientazione coincide nello screen equatoriale dichiarato. È simmetria scoped, non indipendenza statistica.
- La finestra affine nulla dà l'identità.
- La dilatazione congiunta di `M,Q,r,b,lambda` a `epsilon,rho,R` fissati, seguita dalla conversione dichiarata dei phase rate, preserva profilo e mappa adimensionali entro la tolleranza numerica.
- L'audit di rango dà `rank_with_log_M_and_epsilon=1`, con `scale_null_direction=[1,0]`: il rapporto di carica aggiunge forma, mentre `M` assoluto resta nullo.

Carica, `Q/M`, raggio fotonico, turning radius e impact parameter non sono `ell0`. Più entry matriciali non stabiliscono informazione indipendente.

## Scope fonti e review

`EiroaRomeroTorres2002` supporta metrica RN, sfera fotonica e relazioni closest-approach/impact. `Sachs1961` e `SchneiderEhlersFalco1992` supportano il contesto generale ottico nullo/Jacobi. Non stabiliscono protocollo finite-boundary, proiezione numerica diretta dello screen, preparazione endpoint, receiver, covariance, `ell0`, UMCH, evidenza o detection.

Modalità di chiusura: `DIRECT_REVIEW_NO_SUBAGENT`, richiesta dalla policy utente. È review diretta, non independent review.
