# Audit bounded della coerenza di sorgente nello scattering finito di Schwarzschild — Italiano

## Disposizione

`SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Autorità: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; interpretazione massima `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Modalità di revisione: `DIRECT_REVIEW_NO_SUBAGENT`.

## Record bounded preregistrato

Per endpoint statici allo stesso raggio nello scattering finito futuro-nullo di Schwarzschild, si usano `M=1`, `rho=4`, `R=12`, `nu_s=0.2`, `chi_c=tau_c/M=3` e ordine screen `(polar,in-plane)`. Il record toy di coerenza d'insieme viene aggiunto senza sostituire la mappa ottica completa:

```text
V=exp[-(Delta_tau_R/tau_c)^2/2]
Gamma_1=A_c V exp[i(Phi_clock+phi_s)]
y_coh=G_c (Re[e^{-i phi_LO} Gamma_1],Im[e^{-i phi_LO} Gamma_1])
R_coherence=(y_coh,V,Phi_clock,P_frequency_converted)
```

Il baseline produce `Delta_tau_R/M=36.719017101366305`, `Phi_clock=7.343803420273261` e `visibility=2.9462060018828695e-33`. La visibilità minuscola è un output dell'inviluppo gaussiano toy dichiarato, non decoerenza misurata o evidenza. `P_frequency_converted` resta la mappa completa corretta `4x4` su screen trasportato.

Classificazioni: propagazione di Schwarzschild e contesto Sachs/Jacobi sono `KNOWN_RESULT_WITHIN_CITED_SCOPE`; propagazione della coerenza e audit di rango sono `PROJECT_DERIVATION`; inviluppo gaussiano stazionario e readout ideale visibilità/IQ sono `TOY_CONTROL_NOT_PHYSICAL_SOURCE_OR_DETECTOR`; la cecità di scala preservata è `NEGATIVE_RESULT`; il completamento fisico di sorgente e rivelatore è `OPEN_PROBLEM`.

## Counterexample di nuisance e limite

La fase comune sorgente/LO e le azioni inverse ampiezza-sorgente/gain-ricevitore lasciano invariato `y_coh`:

```text
common_phase_residual=1.6653345369377348e-16
source_gain_compensation_residual=0.0
nuisance_jacobian_rank=2
phase_null_direction=[0,1,0,1]
amplitude_null_direction=[1,0,-1,0]
```

Il quotient senza vincoli di fase e gain positivo elimina l'I/Q di coerenza, anche se la visibilità mantenuta separatamente resta una coordinata di forma toy. Questo quotient è matematico, non una calibrazione fisica.

A `R-rho=1e-15`:

```text
visibility_difference_from_one=1.2212453270876722e-15
clock_phase=2.918879231842149e-08
phase_map_identity_residual=7.297198079605369e-07
```

Il limite numerico bounded tende quindi a visibilità unitaria, fase nulla e mappa completa identità. Un I/Q raw non nullo può restare per label esterne sorgente/LO e non è geometria o holonomy.

## Controlli di dilatazione e standard esterno

Sotto `M -> 1.7 M`, mantenendo fissi `rho`, `R`, `nu_s` e `chi_c`:

```text
coherence_iq_residual=0.0
visibility_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

La visibilità aggiunge quindi forma ritardo/coerenza ma nessuna scala assoluta interna. Mantenendo invece fisso `tau_c=20` dimensionale si ottiene:

```text
chi_c_reference=20.0
chi_c_scaled=11.764705882352942
visibility_difference=-0.17770997834344382
coherence_iq_difference=0.18481837747718158
EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE
```

Questa direzione importa uno standard di coerenza della sorgente. Non è `ell/ell0`, `ell0` o una scala interna derivata dal rivelatore.

## Rango e dipendenza

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

Più entry vettoriali/scalari non stabiliscono rango fisico o indipendenza statistica.

## Scope fonti e fisica irrisolta

`Schwarzschild2003Translation` supporta solo il contesto esterno di Schwarzschild; `Darwin1959GravityField` solo il contesto delle orbite nulle; `Sachs1961` solo il contesto ottico/Jacobi nullo. Queste fonti non stabiliscono lo spettro gaussiano di sorgente, coherence dynamics, emission, absorption, polarization-screen coupling, receiver transfer, calibrated noise, joint covariance, una legge `ell0`, UMCH, evidenza o detection.

Non sono stati derivati stato microscopico di sorgente, meccanismo di linewidth, azione di emissione/assorbimento, preparazione di polarization, dinamica del ricevitore, noise calibrato o likelihood. I criteri di structural dead end non passano perché restano aperte route fisiche bounded e altre geometrie esatte.
