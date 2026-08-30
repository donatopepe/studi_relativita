# Schwarzschild finite-scattering bounded source-coherence audit — English

## Disposition

`SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; maximum interpretation `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Review mode: `DIRECT_REVIEW_NO_SUBAGENT`.

## Preregistered bounded record

For equal-radius static endpoints on finite future-null Schwarzschild scattering, use `M=1`, `rho=4`, `R=12`, `nu_s=0.2`, `chi_c=tau_c/M=3`, and screen order `(polar,in-plane)`. Append the toy ensemble coherence record without replacing the full optical map:

```text
V=exp[-(Delta_tau_R/tau_c)^2/2]
Gamma_1=A_c V exp[i(Phi_clock+phi_s)]
y_coh=G_c (Re[e^{-i phi_LO} Gamma_1],Im[e^{-i phi_LO} Gamma_1])
R_coherence=(y_coh,V,Phi_clock,P_frequency_converted)
```

The baseline gives `Delta_tau_R/M=36.719017101366305`, `Phi_clock=7.343803420273261`, and `visibility=2.9462060018828695e-33`. Tiny visibility here is a declared Gaussian toy-envelope output, not measured decoherence or evidence. `P_frequency_converted` remains the complete corrected transported-screen `4x4` map.

Classifications: Schwarzschild propagation and Sachs/Jacobi context are `KNOWN_RESULT_WITHIN_CITED_SCOPE`; coherence propagation and rank audit are `PROJECT_DERIVATION`; the Gaussian stationary envelope and ideal visibility/IQ readout are `TOY_CONTROL_NOT_PHYSICAL_SOURCE_OR_DETECTOR`; retained scale blindness is `NEGATIVE_RESULT`; physical source and detector completion is `OPEN_PROBLEM`.

## Nuisance and limit counterexamples

Common source/LO phase and inverse source-amplitude/receiver-gain actions leave `y_coh` unchanged:

```text
common_phase_residual=1.6653345369377348e-16
source_gain_compensation_residual=0.0
nuisance_jacobian_rank=2
phase_null_direction=[0,1,0,1]
amplitude_null_direction=[1,0,-1,0]
```

The unrestricted positive-gain/phase quotient removes coherence I/Q, although separately retained visibility remains a toy shape coordinate. This quotient is mathematical, not a physical calibration.

At `R-rho=1e-15`:

```text
visibility_difference_from_one=1.2212453270876722e-15
clock_phase=2.918879231842149e-08
phase_map_identity_residual=7.297198079605369e-07
```

Thus the bounded numerical limit approaches unit visibility, zero phase and identity full map. Nonzero raw coherence I/Q may persist from external source/LO labels and is not geometry or holonomy.

## Dilation and external-standard controls

Under `M -> 1.7 M`, holding `rho`, `R`, `nu_s` and `chi_c` fixed:

```text
coherence_iq_residual=0.0
visibility_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

Visibility therefore adds delay/coherence shape but no interior absolute scale. Holding dimensional `tau_c=20` fixed instead gives:

```text
chi_c_reference=20.0
chi_c_scaled=11.764705882352942
visibility_difference=-0.17770997834344382
coherence_iq_difference=0.18481837747718158
EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE
```

This direction imports a source coherence standard. It is not `ell/ell0`, `ell0`, or a detector-derived interior scale.

## Rank and dependence

For parameters `(rho,R,log_M)`:

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

More vector/scalar entries do not establish physical rank or statistical independence.

## Source scope and unresolved physics

`Schwarzschild2003Translation` supports Schwarzschild exterior context only; `Darwin1959GravityField` supports null-orbit context only; `Sachs1961` supports null optical/Jacobi context only. These sources do not establish the Gaussian source spectrum, coherence dynamics, emission, absorption, polarization-screen coupling, receiver transfer, calibrated noise, joint covariance, an `ell0` law, UMCH, evidence or detection.

No microscopic source state, linewidth mechanism, emission/absorption action, polarization preparation, receiver dynamics, calibrated noise or likelihood was derived. Structural-dead-end criteria do not pass because bounded physical routes and other exact geometries remain open.
