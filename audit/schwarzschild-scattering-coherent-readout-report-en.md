# Schwarzschild finite-scattering coherent endpoint-readout audit — English

## Disposition

`SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; maximum interpretation `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Review mode: `DIRECT_REVIEW_NO_SUBAGENT`.

## Preregistered record

For equal-radius static endpoints on finite future-null Schwarzschild scattering, use `M=1`, `rho=4`, `R=12`, `nu_s=0.2`, and screen order `(polar,in-plane)`. Retain

```text
Phi_clock=nu_s Delta_tau_R/M
relative phase=Phi_clock+phi_s-phi_LO
y_IQ=G A_s (cos(relative phase),sin(relative phase))
R_readout=(y_IQ,Phi_clock,P_frequency_converted)
```

`P_frequency_converted` remains the complete corrected transported-screen `4x4` map. The scalar carrier does not replace it. `A_s`, `phi_s`, `G`, and `phi_LO` are declared toy preparation/calibration labels, not derived emitter, absorber or receiver dynamics.

## Nuisance counterexamples

Simultaneously shifting source and LO phase leaves `y_IQ` unchanged:

```text
common_phase_residual=1.8457457784393227e-15
phase_null_direction=[0,1,0,1]
phase_null_residual=0.0
```

Compensating source amplitude by inverse receiver gain also leaves `y_IQ` unchanged:

```text
source_gain_compensation_residual=0.0
amplitude_null_direction=[1,0,-1,0]
amplitude_null_residual=0.0
nuisance_jacobian_rank=2
```

The unrestricted positive-gain and phase quotient sends every nonzero scalar-carrier I/Q vector to `[1,0]`. This is a mathematical quotient and must not be called physical calibration. Arbitrary source/LO phase can leave nonzero raw I/Q in the zero-window limit even while `Phi_clock -> 0` and the full Jacobi map tends to identity.

## Scale and rank controls

Under `M -> 1.7 M` at fixed `rho`, `R`, and `nu_s`:

```text
iq_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
quotient_residual=0.0
```

At fixed dimensional `omega_s=0.2`, the changed carrier follows an external standard:

```text
clock_phase_difference=5.140662394191283
iq_difference=1.1246427723525296
EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE
```

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

Extra raw entries do not establish physical rank, independence or global identifiability.

## Classification and source scope

Schwarzschild propagation context and null optics are `KNOWN_RESULT` only within the bounded scopes of `Schwarzschild2003Translation`, `Darwin1959GravityField`, and `Sachs1961`. Endpoint I/Q construction, nuisance quotient and rank audit are `PROJECT_DERIVATION`; ideal monochromatic source, LO and receiver are `TOY_CONTROL`; retained scale blindness is `NEGATIVE_RESULT`.

These sources do not establish coherent source dynamics, emission or absorption interaction, polarization-screen coupling, receiver transfer, calibrated noise, joint covariance, `ell0`, UMCH, evidence or detection. No physical coherence, detector response or covariance was derived. Dead-end criteria do not pass because bounded physical-model and other-geometry routes remain open; loop remains active.
