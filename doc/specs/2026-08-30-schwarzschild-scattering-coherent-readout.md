# Schwarzschild finite-scattering coherent endpoint-readout nuisance gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end remains `NOT_DECLARED`.

Question: for the audited finite-boundary equatorial Schwarzschild null-scattering ray with equal-radius static endpoints, `R>rho>3`, one turning point, source-local toy frequency and corrected transported-screen Jacobi phase map, does a declared coherent endpoint quadrature readout create an interior absolute-scale direction after explicit source-phase, local-oscillator-phase and gain nuisance actions, or does the quotient retain Schwarzschild dilation blindness?

Classifications:

- Schwarzschild exterior propagation, static frequency transfer and Sachs/Jacobi framework: `KNOWN_RESULT` within existing cited source scope;
- endpoint quadrature map, nuisance group, quotient diagnostics and joined rank audit: `PROJECT_DERIVATION`;
- monochromatic scalar carrier, fixed complex source amplitude, ideal phase-preserving receiver and declared local oscillator: `TOY_CONTROL`, not a physical emitter, absorber or detector;
- loss of raw phase/amplitude information under nuisance quotient and persistence of geometric dilation blindness: `NEGATIVE_RESULT` if tests pass;
- source coherence dynamics, emission/absorption interaction, polarization/screen coupling, receiver transfer function, calibrated noise, joint covariance and an `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this complete readout protocol, hardware realization, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Classical coherent scalar carrier with ideal linear I/Q receiver — selected.** Small, deterministic and falsification-first. It exposes which apparent phase and amplitude directions are source/LO/gain nuisance without pretending to derive hardware.
2. **Two-level quantum emitter and absorber.** Rejected for this bounded increment: it requires a quantum field state, switching functions, mode choice, interaction Hamiltonian and detector response not supplied by the repository.
3. **Phase-locked transponder or mirror loop.** Rejected: it adds turnaround delay, lock law, mirror/transponder action and physical closure. Those are unresolved protocol objects, not conservative consequences of the current scattering control.

## Preregistered objects

Retain the previous primary optical object in full:

```text
P_frequency_converted in R^(4x4), screen order (polar,in-plane).
```

Retain the static endpoint clock entry:

```text
Phi_clock = nu_s Delta_tau_R/M,
nu_s = M omega_s.
```

Declare a toy complex source amplitude

```text
z_s = A_s exp(i phi_s),  A_s>0,
```

and an ideal endpoint carrier transfer

```text
z_R = g exp[i(Phi_clock + delta_prop)] z_s.
```

For equal-radius static endpoints on one null geodesic, source and receiver local frequencies agree. `delta_prop` is fixed to zero in the minimal control: no independent photon internal phase, emission action, absorber phase or matched flat-path excess is derived. The ideal receiver compares `z_R` with a declared local-oscillator phase `phi_LO`:

```text
y_IQ = (I,Q)
     = G (Re[z_R exp(-i phi_LO)], Im[z_R exp(-i phi_LO)]),
G>0.
```

The primary joined raw record is

```text
R_readout = (y_IQ, Phi_clock, P_frequency_converted).
```

`y_IQ` does not replace or scalarize `P_frequency_converted`.

## Nuisance group and quotient

Preregister nuisance parameters

```text
eta = (log A_s, phi_s, log G, phi_LO).
```

Only combinations

```text
log amplitude = log A_s + log g + log G,
relative phase = Phi_clock + phi_s - phi_LO
```

enter `y_IQ`. Thus source amplitude and receiver gain are exactly collinear, while source and LO phases are oppositely collinear. The quotient diagnostic removes positive overall amplitude and arbitrary common phase by normalizing the nonzero vector and rotating it to a declared canonical axis. This canonical representative is a mathematical nuisance quotient, not detector calibration.

Preregistered counterexamples:

1. changing `phi_s` and `phi_LO` by the same amount leaves raw `y_IQ` unchanged;
2. changing `A_s` and compensating `G` inversely leaves raw `y_IQ` unchanged;
3. any nonzero two-quadrature vector becomes the same canonical representative after unrestricted positive gain and phase quotient;
4. at fixed `rho`, `R`, and `nu_s`, `M -> sM` preserves `Phi_clock`, the converted full phase map and quotient readout;
5. at fixed dimensional `omega_s`, phase changes track an external frequency standard and are not an interior geometric scale;
6. as `R -> rho+`, `Phi_clock -> 0` and the full map tends to identity, but arbitrary source/LO phase can keep raw `y_IQ` nonzero. This is a protocol limit, not holonomy or evidence.

## Rank and covariance gates

Compute finite-difference local ranks for declared feature vectors under parameters `(rho,R,log_M)`:

```text
raw feature      = flatten(y_IQ, Phi_clock, P_frequency_converted),
quotient feature = flatten(y_IQ_quotient, Phi_clock, P_frequency_converted).
```

Also compute the nuisance Jacobian of `y_IQ` with respect to `eta`, verifying the exact source/gain and source/LO null directions. Local rank does not establish global injectivity. More entries do not establish statistical independence. No covariance matrix will be invented; status remains `DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE`.

## Controls and failure conditions

Use the established baseline `M=1`, `rho=4`, `R=12`, `nu_s=0.2`, deterministic `A_s`, `phi_s`, `G`, `phi_LO`, and the existing corrected full Jacobi map. Tests must cover:

- exact I/Q construction and norm;
- phase and amplitude nuisance invariances;
- canonical quotient collapse;
- orientation labels retained separately from scalar carrier phase;
- zero-window behavior;
- fixed-`nu_s` geometric dilation;
- fixed-`omega_s` external-standard direction;
- local rank and explicit nuisance null vectors;
- deterministic JSON artifact;
- bilingual semantic parity and bounded source scope.

Failure conditions include nonfinite output, loss of prior full-map controls, claimed scale rank after quotient, reinterpretation of fixed dimensional frequency as internal geometry, scalar replacement of the full map, covariance/independence claim without a model, or any `ell0`/detection claim.

## Expected bounded disposition

Passing tests support at most:

```text
SCHWARZSCHILD_COHERENT_ENDPOINT_IQ_READOUT_IS_SOURCE_LO_GAIN_NUISANCE_AND_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0
```

with gate:

```text
PHYSICAL_SOURCE_COHERENCE_EMISSION_ABSORPTION_POLARIZATION_SCREEN_COUPLING_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

Passing does not identify `ell0`, derive a physical detector, establish channel independence, or support UMCH. Maximum interpretation remains `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Structural-dead-end disposition

Dead-end criteria do not pass. Bounded routes remain open through explicit emitter/absorber dynamics, polarization-sensitive screen coupling, receiver response, calibrated covariance and other exact geometries. No reformulation candidate is authorized by this increment; durable loop remains active.
