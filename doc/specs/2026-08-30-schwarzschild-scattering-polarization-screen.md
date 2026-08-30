# Schwarzschild finite-scattering polarization/screen transport gate

Status: `PREREGISTERED_BOUNDED_AUDIT`

## Question and scope

Does leading-order electromagnetic polarization transport add an internal scale direction to the corrected finite Schwarzschild null-scattering record, once screen basis, endpoint preparation labels, orientation and nuisance actions are explicit?

Scope is four-dimensional exterior Schwarzschild geometry, future-directed equatorial finite null scattering with one turning point, equal-radius static endpoints, corrected transported screen order `(polar,in-plane)`, unit Killing-energy project normalization followed by the existing endpoint frequency conversion, and leading geometrical optics only. No source spectrum, microscopic emission or absorption, polarization-sensitive material, receiver transfer, calibrated noise, covariance, `ell0` law or observation is supplied.

Classifications: null propagation and leading geometric-optics parallel polarization transport are `KNOWN_RESULT_WITHIN_CITED_SCOPE`; finite endpoint screen/Jones joining, quotient and rank checks are `PROJECT_DERIVATION`; source Jones state and analyzer labels are `TOY_CONTROL`; retained scale blindness is `NEGATIVE_RESULT`; physical preparation/detection completion is `OPEN_PROBLEM`.

## Alternatives and selection

1. **Transported-screen Jones/coherency record — selected.** Preserve complex Jones vector and Hermitian coherency matrix in the already tested screen. This is smallest append-only control and exposes basis/analyzer nuisance directly.
2. **Stokes/Mueller receiver chain — deferred.** Stokes coordinates are a projection of coherency; a Mueller chain would add uncalibrated hardware and may hide raw complex-vector structure.
3. **Microscopic dipole emitter/absorber — rejected for this increment.** Requires matter state, Hamiltonian, coupling, linewidth, preparation and absorber dynamics not derived by current geometry.

## Preregistered record

Use baseline `M=1`, `rho=4`, `R=12`, orientation `+1`, normalized source Jones label

```text
j_s=(cos psi_s, exp(i delta_s) sin psi_s)
```

in screen order `(polar,in-plane)`. Let `U_screen` be the endpoint screen transfer induced by Levi-Civita parallel propagation modulo the null direction. Leading geometrical optics gives

```text
j_R=U_screen j_s
J_R=j_R j_R^dagger
R_polarization=(j_R,J_R,Phi_clock,P_frequency_converted)
```

`j_R` and `J_R` append to, and never replace, the corrected complete `4x4` Jacobi phase map. A declared linear analyzer label `a(psi_R)=(cos psi_R,sin psi_R)` may form `z_R=a^T j_R` and power `|z_R|^2` only as a secondary toy projection.

For the existing equatorial screen, test whether fitted null-gauge screen derivatives imply `U_screen=I_2` to numerical tolerance. Preserve raw derivative and quotient residual separately. Never call a basis rotation physical gravitational Faraday rotation without an independently prepared endpoint frame and observer protocol.

## Counterexample-first controls

1. **Screen conformance:** reuse coarse/fine null-gauge quotient diagnostics; require decreasing quotient/rotation residual while raw covariant derivative remains reported.
2. **Jones/coherency identities:** norm and Hermiticity, rank-one determinant, and `J_R=j_Rj_R^dagger` must hold.
3. **Common screen rotation:** under `j -> Q(alpha)j`, `J -> QJQ^T`, analyzer `a -> Qa`, analyzer amplitude/power remain invariant. This is a basis quotient, not physical calibration.
4. **Analyzer nuisance:** changing analyzer alone changes projected power while raw `j_R,J_R` stay fixed; projected power cannot replace raw record.
5. **Orientation reversal:** audit `+/-` scattering orientations explicitly. Any equality is a scoped symmetry result, not statistical independence.
6. **Zero window:** as `R-rho -> 0`, `U_screen -> I_2`, clock phase -> 0 and full phase map -> identity; arbitrary source polarization may remain because it is boundary data, not geometry.
7. **Geometric dilation:** under `M -> sM` at fixed `rho`, `R`, `nu_s=M omega_s` and source/analyzer labels, require polarization transfer, raw polarization record, clock phase and frequency-converted full map invariant to tolerance.
8. **Fixed dimensional source frequency:** retain existing classification as external standard, not interior geometric scale.
9. **Rank:** finite-difference features from the raw polarization-plus-clock/full-map record and basis-quotiented record over `(rho,R,log M)`. Require no rank claim beyond numerical tolerance; test `log M` null direction directly. Global injectivity remains unestablished and dependence remains unresolved without joint covariance.

## Acceptance and disposition

Accept only if deterministic artifact checks pass, source scope is bounded, bilingual audits are semantically aligned, focused and full suites pass, and PR plus post-merge CI are green. Expected conservative result if controls hold:

```text
SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0
```

Expected gate:

```text
PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

Always retain:

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

## Sources and source limits

Use `Schwarzschild2003Translation` only for Schwarzschild exterior/static context, `Darwin1959GravityField` only for nonradial Schwarzschild null-scattering context, `Sachs1961` only for null optical/Jacobi context, and `Dolan2018GeometricalOptics` only for leading curved-spacetime geometrical optics, including null rays and parallel-propagated polarization. These sources do not establish this finite endpoint screen protocol, source state, emission, absorption, analyzer hardware, receiver, covariance, `ell0`, UMCH, evidence or detection.

## Direct closure review

`DIRECT_REVIEW_NO_SUBAGENT`. Direct diff, scientific-contract, bilingual-parity and source-scope review found no promotion of source Jones labels, analyzer projection, screen-basis quotient, rank diagnostics or numerical controls into physical calibration, independent evidence, `ell0` identification or detection. Full `4x4` phase map and raw transport diagnostics remain preserved. Focused cross-control suite passed 43 tests; deterministic artifact, extraction and inventory checks passed; full discovery passed 939 tests; `git diff --check` passed. This is direct review, not independent review.
