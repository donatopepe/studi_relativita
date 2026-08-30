# Schwarzschild coherent endpoint I/Q nuisance control

Status: `SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

Gate: `PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`; review `DIRECT_REVIEW_NO_SUBAGENT`.

## Objects kept distinct

For finite future-null equatorial Schwarzschild scattering with equal-radius static endpoints, retain screen order `(polar,in-plane)` and

```text
Phi_clock=nu_s Delta_tau_R/M
relative phase=Phi_clock+phi_s-phi_LO
y_IQ=G A_s (cos(relative phase),sin(relative phase))
R_readout=(y_IQ,Phi_clock,P_frequency_converted)
```

The corrected full `4x4` map `P_frequency_converted` is primary optical information and is not replaced by I/Q. The ideal scalar source, local oscillator and phase-preserving receiver are declared `TOY_CONTROL`. No photon internal phase, emission action, absorption action, polarization-screen coupling or detector transfer function is inferred.

## Exact nuisance null directions

For nuisance order `(log_A_s,phi_s,log_G,phi_LO)`, source amplitude and receiver gain have identical I/Q columns; source and LO phases have opposite columns. Therefore

```text
amplitude null direction=[1,0,-1,0]
phase null direction=[0,1,0,1]
nuisance_jacobian_rank=2
```

Numerically, `common_phase_residual=1.8457457784393227e-15`; both null residuals and source/gain compensation residual are zero. Unrestricted positive-gain and phase quotient collapses every nonzero scalar-carrier I/Q vector to `[1,0]`. This quotient is mathematical, not detector calibration.

Zero window sends `Phi_clock` to zero and `P_frequency_converted` to identity. Raw I/Q need not vanish because source/LO phase and amplitude are external preparation labels. Thus nonzero endpoint electronics in this limit is not holonomy, curvature evidence or an interior scale.

## Dilation and rank

At fixed `rho`, `R`, and `nu_s=M omega_s`, `M -> 1.7M` gives

```text
iq_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
quotient_residual=0.0
```

Holding dimensional `omega_s` fixed instead yields `iq_difference=1.1246427723525296` and clock-phase difference `5.140662394191283`, classified `EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

For `(rho,R,log_M)`:

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

More channels or entries do not imply physical rank or statistical independence.

## Sources and open scope

`Schwarzschild2003Translation` supports Schwarzschild exterior context; `Darwin1959GravityField` supports null-trajectory/critical-orbit context; `Sachs1961` supports null optical/Jacobi context. These sources do not establish this endpoint protocol, source coherence, emission, absorption, polarization-screen coupling, receiver response, calibrated noise, joint covariance, `ell0`, UMCH, evidence or detection.

Physical coherence, emitter/absorber interaction, receiver calibration and covariance remain open. Dead-end criteria do not pass; bounded alternatives and other exact geometries remain available, so no reformulation is authorized and loop remains active.
