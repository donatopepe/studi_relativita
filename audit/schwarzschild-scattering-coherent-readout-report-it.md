# Audit del readout coerente agli estremi dello scattering finito di Schwarzschild — Italiano

## Disposizione

`SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Autorità: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; interpretazione massima `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Revisione: `DIRECT_REVIEW_NO_SUBAGENT`.

## Record preregistrato

Per estremi statici allo stesso raggio nello scattering Schwarzschild nullo futuro finito, si usano `M=1`, `rho=4`, `R=12`, `nu_s=0.2` e ordine screen `(polar,in-plane)`. Si preserva

```text
Phi_clock=nu_s Delta_tau_R/M
relative phase=Phi_clock+phi_s-phi_LO
y_IQ=G A_s (cos(relative phase),sin(relative phase))
R_readout=(y_IQ,Phi_clock,P_frequency_converted)
```

`P_frequency_converted` resta la mappa `4x4` completa corretta dello screen trasportato. Il carrier scalare non la sostituisce. `A_s`, `phi_s`, `G` e `phi_LO` sono etichette toy dichiarate di preparazione/calibrazione, non dinamiche derivate di emettitore, assorbitore o ricevitore.

## Counterexample di nuisance

Traslare insieme fase della sorgente e fase LO lascia invariato `y_IQ`:

```text
common_phase_residual=1.8457457784393227e-15
phase_null_direction=[0,1,0,1]
phase_null_residual=0.0
```

Compensare l'ampiezza della sorgente con l'inverso del guadagno del ricevitore lascia ugualmente invariato `y_IQ`:

```text
source_gain_compensation_residual=0.0
amplitude_null_direction=[1,0,-1,0]
amplitude_null_residual=0.0
nuisance_jacobian_rank=2
```

Il quotient per fase arbitraria e guadagno positivo manda ogni vettore I/Q non nullo del carrier scalare in `[1,0]`. È un quotient matematico e non va chiamato calibrazione fisica. Una fase sorgente/LO arbitraria può lasciare I/Q raw non nullo nel limite di finestra zero anche quando `Phi_clock -> 0` e la mappa Jacobi completa tende all'identità.

## Controlli di scala e rango

Sotto `M -> 1.7 M` a `rho`, `R` e `nu_s` fissi:

```text
iq_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
quotient_residual=0.0
```

A `omega_s=0.2` dimensionale fissa, il carrier modificato segue uno standard esterno:

```text
clock_phase_difference=5.140662394191283
iq_difference=1.1246427723525296
EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE
```

Per i parametri `(rho,R,log_M)`:

```text
rank_raw_shape_boundary=2
rank_raw_with_log_M=2
rank_quotient_shape_boundary=2
rank_quotient_with_log_M=2
raw_log_M_column_norm=4.5841522233922306e-09
quotient_log_M_column_norm=4.5841522233922306e-09
scale_null_direction=[0,0,1]
global_injectivity=NOT_ESTABLISHED
statistical_independence=DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE
```

Più entry raw non stabiliscono rango fisico, indipendenza o identificabilità globale.

## Classificazione e scope fonti

Il contesto di propagazione Schwarzschild e l'ottica nulla sono `KNOWN_RESULT` solo negli scope limitati di `Schwarzschild2003Translation`, `Darwin1959GravityField` e `Sachs1961`. Costruzione I/Q agli estremi, quotient dei nuisance e audit del rango sono `PROJECT_DERIVATION`; sorgente monocromatica ideale, LO e ricevitore sono `TOY_CONTROL`; la cecità alla scala preservata è `NEGATIVE_RESULT`.

Queste fonti non stabiliscono dinamica di coerenza della sorgente, interazione di emissione o absorption, accoppiamento polarizzazione-screen, trasferimento del receiver, rumore calibrato, joint covariance, `ell0`, UMCH, evidenza o detection. Non sono stati derivati coerenza fisica, risposta del detector o covariance. I criteri di vicolo cieco non passano perché restano aperte route bounded con modelli fisici e altre geometrie; il loop resta attivo.
