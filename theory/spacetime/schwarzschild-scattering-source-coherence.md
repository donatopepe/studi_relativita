# Schwarzschild scattering: bounded source-coherence response

Status: `SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

Gate: `PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`; review `DIRECT_REVIEW_NO_SUBAGENT`.

## Bounded project construction

For the existing equal-radius static-endpoint null-scattering control, declare a Gaussian stationary first-order source-coherence toy:

```text
V=exp[-(Delta_tau_R/tau_c)^2/2]
Gamma_1=A_c V exp[i(Phi_clock+phi_s)]
y_coh=G_c (Re[e^{-i phi_LO} Gamma_1],Im[e^{-i phi_LO} Gamma_1])
R_coherence=(y_coh,V,Phi_clock,P_frequency_converted)
```

Screen order remains `(polar,in-plane)`. `P_frequency_converted` is primary and remains the full corrected transported-screen `4x4` map. Coherence I/Q and visibility append channel-native toy outputs; neither replaces nor scalarizes the map.

The Gaussian envelope is `TOY_CONTROL_NOT_PHYSICAL_SOURCE_OR_DETECTOR`. Propagating it through the existing elapsed-time and clock-phase control is `PROJECT_DERIVATION`. No source spectrum or coherence dynamics is derived.

## Scale symmetry

Write `chi_c=tau_c/M`. Since `Delta_tau_R=M T(rho,R)` and `Phi_clock=nu_s T(rho,R)`,

```text
V=exp[-T(rho,R)^2/(2 chi_c^2)].
```

At fixed dimensionless `(rho,R,nu_s,chi_c)`, `M -> sM` leaves `V`, `y_coh`, `Phi_clock` and the dimensionlessly frequency-converted full phase map invariant. Baseline diagnostics give `visibility=2.9462060018828695e-33`, while dilation gives `converted_phase_map_residual=5.9117155615240335e-12` and exact-zero numerical residuals for coherence I/Q, visibility and clock phase.

Holding dimensional `tau_c=20` fixed instead changes `chi_c`, yielding `visibility_difference=-0.17770997834344382` and `coherence_iq_difference=0.18481837747718158`. This is `EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`, not `ell0`.

## Nuisance, limit and rank controls

Common source/LO phase and inverse source/receiver amplitude actions remain exact toy nuisances: `common_phase_residual=1.6653345369377348e-16`, `nuisance_jacobian_rank=2`. An unrestricted positive-gain/phase quotient removes coherence I/Q but not separately retained visibility. It is a mathematical quotient, not physical calibration.

The zero-window control tends to unit visibility, zero clock phase and identity full map; any remaining raw I/Q phase comes from source/LO labels and is not geometry. The `(rho,R,log_M)` Jacobian has `rank_raw_with_log_M=2`, `rank_quotient_with_log_M=2`, and scale-null direction `[0,0,1]`. Global injectivity is not established; statistical independence remains `DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE`.

## Source scope and open physics

`Schwarzschild2003Translation`, `Darwin1959GravityField`, and `Sachs1961` support only Schwarzschild exterior, null-orbit, and null optical/Jacobi context respectively. They do not establish this Gaussian source model, source spectrum, coherence dynamics, emission, absorption, polarization-screen coupling, receiver transfer, calibrated noise, covariance, `ell0`, UMCH, evidence or detection.

Open: physical spectrum and coherence dynamics, microscopic emission and absorption, polarization-screen preparation/coupling, receiver transfer, calibrated noise, joint covariance, and a geometry-to-`ell/ell0` law. Structural-dead-end criteria remain unmet.
