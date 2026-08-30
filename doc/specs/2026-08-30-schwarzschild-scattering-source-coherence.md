# Schwarzschild finite-scattering bounded source-coherence gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end remains `NOT_DECLARED`.

Question: if the existing equal-radius static-endpoint Schwarzschild coherent-readout toy is extended by a preregistered stationary first-order source-coherence envelope, can delay-dependent visibility create an interior geometric scale, or is any dimensional coherence time an external source standard while a dimensionless coherence width retains Schwarzschild dilation blindness?

Classifications:

- Schwarzschild exterior propagation, static clock transfer and transported-screen Jacobi map: `KNOWN_RESULT` within existing cited source scope;
- ensemble first-order coherence propagation through the declared scalar carrier and joined scale/rank controls: `PROJECT_DERIVATION`;
- Gaussian stationary first-order coherence envelope and ideal visibility readout: `TOY_CONTROL`, not derived source microphysics or a detector model;
- source-phase cancellation in the ensemble coherence product and retained scale blindness at fixed dimensionless coherence width: `NEGATIVE_RESULT` if tests pass;
- physical source spectrum/coherence dynamics, emission and absorption, polarization-screen coupling, receiver transfer, calibrated noise, joint covariance and an `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this complete source, readout, covariance, `ell0`, UMCH, evidence or detection protocol.

## Alternatives and selected design

1. **Stationary Gaussian first-order coherence envelope — selected.** Bounded, deterministic and counterexample-first. It adds one physically interpretable but explicitly toy visibility coordinate without inventing microscopic emission.
2. **Lorentzian/exponential envelope — rejected for this increment.** Different spectral line shape, same external-scale issue, extra family selection without a derived source.
3. **Microscopic two-level emitter or stochastic field dynamics — deferred.** Requires Hamiltonian, state, linewidth mechanism, preparation and coupling not supplied by current project.

## Preregistered record

Retain the existing raw record and append, rather than substitute, a coherence vector:

```text
Phi_clock = nu_s Delta_tau_R/M
Gamma_1 = A_c exp[-(Delta_tau_R/tau_c)^2/2] exp[i(Phi_clock+phi_s)]
y_coh = G_c (Re[e^{-i phi_LO} Gamma_1], Im[e^{-i phi_LO} Gamma_1])
V = |Gamma_1|/A_c
R_coherence = (y_coh,V,Phi_clock,P_frequency_converted)
```

`P_frequency_converted` remains the complete corrected transported-screen `4x4` map in screen order `(polar,in-plane)`. `A_c`, `phi_s`, `G_c`, `phi_LO`, and `tau_c` are declared source/receiver toy labels. `V` is a deterministic ensemble first-order-coherence envelope, not measured data.

Use baseline `M=1`, `rho=4`, `R=12`, `nu_s=0.2`, `chi_c=tau_c/M=3`, with positive amplitudes/gains. Preserve fixed `rho`, `R`, `nu_s`, and `chi_c` under `M -> sM`.

## Mandatory counterexample controls

1. **Phase nuisance.** Common source/LO phase shifts leave `y_coh` unchanged.
2. **Amplitude nuisance.** Inverse source-amplitude/receiver-gain changes leave `y_coh` unchanged.
3. **Zero-window limit.** `V -> 1`, `Phi_clock -> 0`, and full phase map approaches identity; raw electronics phase may remain external nuisance.
4. **Geometric dilation.** Under `M -> sM` with fixed `rho`, `R`, `nu_s`, and `chi_c=tau_c/M`, require unchanged `y_coh`, `V`, `Phi_clock`, and dimensionlessly converted full phase map within numerical tolerance.
5. **External source-standard direction.** Holding dimensional `tau_c` fixed while scaling `M` may change `V`; classify this as `EXTERNAL_SOURCE_COHERENCE_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`, not `ell0`.
6. **Rank audit.** Compare raw and nuisance-quotiented feature Jacobians in `(rho,R,log_M)`; extra record entries do not establish statistical independence without joint covariance.
7. **Full-map preservation.** Coherence scalar/vector outputs never replace or scalarize `P_frequency_converted`.

## Acceptance and interpretation

Passing produces at most

```text
SCHWARZSCHILD_GAUSSIAN_SOURCE_COHERENCE_ADDS_VISIBILITY_SHAPE_BUT_FIXED_DIMENSIONLESS_COHERENCE_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0
```

with gate

```text
PHYSICAL_SOURCE_SPECTRUM_COHERENCE_DYNAMICS_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

Passing is `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. It does not identify `ell0`, establish global injectivity or statistical independence, calibrate a receiver, derive source microphysics, or support UMCH.

## Deliverables

- deterministic study and JSON artifact;
- scientific contract tests written RED before implementation;
- bilingual audit reports with matching labels, equations, values and limitations;
- theory note, roadmap and source-scope update;
- focused and full test suites, artifact checks, extraction/inventory checks, `git diff --check`, PR CI and post-merge CI;
- direct review recorded as `DIRECT_REVIEW_NO_SUBAGENT`.
