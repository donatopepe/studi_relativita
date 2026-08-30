# Audit polarizzazione/screen nello scattering finito di Schwarzschild — Italiano

## Disposizione

`SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Autorità: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; interpretazione massima `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Modalità di revisione: `DIRECT_REVIEW_NO_SUBAGENT`.

## Record bounded preregistrato

Ambito: geometria Schwarzschild esterna quadridimensionale; scattering nullo equatoriale futuro con un turning point; endpoint statici allo stesso raggio; `M=1`, `rho=4`, `R=12`, `nu_s=0.2`; ordine screen `(polar,in-plane)`. Nell'ottica geometrica leading la polarizzazione è trasportata parallelamente al raggio. Stato della sorgente e analizzatore restano label toy al bordo:

```text
j_s=(cos psi_s,exp(i delta_s) sin psi_s)
U_screen=I_2 nello screen parallelo dichiarato modulo gauge nulla
j_R=U_screen j_s
J_R=j_R j_R^dagger
R_polarization=(j_R,J_R,Phi_clock,P_frequency_converted)
```

`j_R` e la coerenza Hermitiana `J_R` si aggiungono, senza mai sostituirla, alla mappa di fase Jacobi completa corretta e convertita in frequenza `4x4`. Per `psi_s=0.63`, `delta_s=0.41`, i residui della norma Jones e dell'outer product sono nulli, il residuo di Hermiticità è nullo e `coherency_determinant_abs=2.7755575615628914e-17`.

Classificazioni: propagazione nulla e polarizzazione parallela sono `KNOWN_RESULT_WITHIN_CITED_SCOPE`; joining finito degli endpoint, quotient di base e controlli di rango sono `PROJECT_DERIVATION`; Jones della sorgente e label dell'analizzatore sono `TOY_CONTROL`; la cecità alla scala mantenuta è `NEGATIVE_RESULT`; il completamento fisico è `OPEN_PROBLEM`.

## Counterexample di trasporto, base e bordo

Le diagnostiche screen fini preservano una derivata raw non nulla mentre il quotient di gauge nulla converge:

```text
max_interior_raw_covariant_derivative=0.1767889727337515
max_interior_screen_quotient_residual=1.9939515283841326e-05
max_interior_screen_rotation_residual=1.851520265341161e-05
```

La costanza delle componenti appartiene quindi al quotient dello screen parallelo dichiarato; non è calibrazione hardware agli endpoint. Una rotazione comune di screen applicata a stato Jones, coerenza e analizzatore lascia invariati ampiezza e potenza dell'analizzatore entro `2.7755575615628914e-16`. È un quotient matematico di base, non una misura fisica di rotazione della polarizzazione.

Cambiare solo l'analizzatore da `-0.27` a `0.83` cambia la potenza proiettata secondaria di `power_difference=0.5145493419909759`, mentre le differenze raw di Jones/coerenza restano nulle. La potenza dell'analizzatore non può sostituire il record raw. Invertire l'orientazione orbitale equatoriale produce residui nulli per Jones, coerenza, clock e mappa convertita nello screen dichiarato: simmetria con scope limitato, non indipendenza statistica.

Per `R-rho=1e-15`, il trasferimento di polarizzazione resta l'identità dei dati al bordo, mentre `clock_phase=2.8851987866118024e-08` e il residuo della mappa dall'identità è `7.297198079605369e-07`. Una polarizzazione arbitraria della sorgente che sopravvive è dato al bordo, non geometria.

## Audit di scala e rango

Sotto `M -> 1.7 M` a `rho`, `R`, `nu_s=M omega_s`, label Jones della sorgente e label dell'analizzatore fissati:

```text
jones_residual=0.0
coherency_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

La polarizzazione non aggiunge quindi una scala geometrica interna. Una frequenza dimensionale fissata resta uno standard esterno sorgente/clock come nell'audit precedente, non `ell0`.

Per l'ordine dei parametri `(rho,R,log M)`:

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

Più entry vettoriali/matriciali non implicano rango fisico o indipendenza.

## Scope fonti e limitazioni

`Schwarzschild2003Translation` supporta solo il contesto esterno/statico di Schwarzschild. `Darwin1959GravityField` supporta solo il contesto di scattering nullo non radiale in Schwarzschild. `Sachs1961` supporta solo il contesto ottico nullo/Jacobi. `Dolan2018GeometricalOptics` supporta solo ottica geometrica leading, propagazione lungo raggi nulli e polarizzazione trasportata parallelamente. Queste fonti non stabiliscono questo protocollo finito agli endpoint, preparazione fisica della source polarization, spettro della sorgente, emission, absorption, screen preparation agli endpoint, materiale/hardware dell'analizzatore, receiver transfer sensibile alla polarizzazione, calibrated noise, joint covariance, `ell0`, UMCH, evidenza o detection.

Non si dichiara alcun angolo fisico di Faraday gravitazionale: una rotazione di basis dello screen non è tale osservabile senza frame agli endpoint preparati indipendentemente e un protocollo osservatore/readout. Non si inventano dinamiche della source polarization, azione di emission/absorption, receiver o covariance.
