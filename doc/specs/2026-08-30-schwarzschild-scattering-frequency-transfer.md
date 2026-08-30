# Schwarzschild finite-scattering physical-frequency transfer gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end remains `NOT_DECLARED`.

Question: for the already audited finite-boundary equatorial Schwarzschild null-scattering ray with `R>rho>3`, can static source/observer tetrads and a declared source-local frequency replace the project anchor `E_infinity=1` and create an interior absolute-scale direction in the full transported-screen Jacobi phase map, or is this only an endpoint frequency-unit calibration that leaves Schwarzschild dilation exact?

Classifications:

- Schwarzschild exterior metric, Killing energy, static tetrads, gravitational redshift, null geodesics and Sachs/Jacobi framework: `KNOWN_RESULT` within cited source scope;
- finite-boundary frequency transfer, tangent renormalization, phase-rate conversion, full-map comparison and rank audit: `PROJECT_DERIVATION`;
- ideal static emitter/absorber and fixed source-local frequency: `TOY_CONTROL` / project anchor, not a detector model;
- endpoint calibration degeneracy, affine blindness, geometric scale blindness and quotient collisions: `NEGATIVE_RESULT` if tests pass;
- physical emitter clock, source spectrum, absorber response, screen preparation, vector readout, covariance and an `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this complete finite-boundary protocol, detector response, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Reuse `E_infinity=1`.** Rejected as new primary control: already audited and not an absolute physical standard.
2. **Assign arbitrary source and observer frequencies independently.** Rejected: inconsistent with one null ray unless an interaction or frequency-changing mechanism is added. No such mechanism is derived.
3. **Selected: source-local normalization plus geometric transfer.** Set a declared positive source-local frequency `omega_s` in the source static tetrad. Then `E_infinity=omega_s sqrt(f_s)` and `omega_o=E_infinity/sqrt(f_o)`. Rescale the audited profile and full phase map by this constant tangent normalization, retaining explicit phase-rate conversion.
4. **Build detector response/covariance.** Deferred: no canonical source currently supplies the missing apparatus model.

## Preregistered objects and conventions

- Geometry: Schwarzschild exterior, `M>0`, finite static endpoints at `r_s=r_o=RM`, turning radius `r_min=rho M`, `R>rho>3`.
- Branches: incoming, turning, outgoing; same orientation and screen transport convention as PR #95.
- Screen order: `(polar,in-plane)`.
- Correct optical profile at `E_infinity=1`:
  `K_1=diag(-1,+1) 3 M b^2/r^5`.
- Static frequency relation: `omega(r)=E_infinity/sqrt(1-2M/r)`.
- Source anchor: `omega_s>0`, declared externally. For equal endpoint radii, `omega_o=omega_s`; an asymmetric-radius algebraic transfer check may be included but is not the primary phase-map path.
- Tangent rescaling factor relative to project anchor: `a=E_infinity=omega_s sqrt(f_s)`.
- Affine parameter and optical profile transform as `lambda_a=lambda_1/a`, `K_a=a^2 K_1`.
- Phase state uses `(X,dX/dlambda)`; comparison uses `D_a=diag(I,a I)` with the exact relation `P_a=D_a P_1 D_a^{-1}`.
- Full `4x4` phase map remains primary. Graph objects only when relevant blocks are invertible.
- Scale test: under `(M,r_s,r_o,r_min)->s(M,r_s,r_o,r_min)` at fixed dimensionless endpoint/turning labels and fixed dimensionless frequency product `nu_s=M omega_s`, convert phase rates explicitly before comparison.
- Absolute source frequency in inverse-length units is an external dimensional standard. Holding it fixed while varying `M` measures `M omega_s`; that does not derive `ell0` or an intrinsic curvature scale.

## Counterexample-first tests

1. Reject independently assigned endpoint frequencies that violate `omega_s sqrt(f_s)=omega_o sqrt(f_o)`.
2. Verify direct rescaled profile/map against `D_a P_1 D_a^{-1}`.
3. Verify source-frequency change moves raw rate-coordinate entries but disappears after declared rate-unit conversion.
4. Verify equal-radius transfer returns `omega_o/omega_s=1`; asymmetric transfer depends only on endpoint compactness ratios.
5. Verify Schwarzschild dilation at fixed `rho`, `R`, and `nu_s=M omega_s` preserves the converted full map.
6. Show holding dimensional `omega_s` fixed makes output depend on `M omega_s`, explicitly classed as `EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.
7. Audit local Jacobian in shape/boundary/log-scale variables after the declared conversion. Expected scale-null direction remains.
8. Preserve corrected PR #95 optical profile, PR #96 affine reconciliation, raw full map, all negative results and source limitations.

## Falsifiers and disposition

Falsify the expected negative result if, after all preregistered tangent/rate conversions at fixed dimensionless protocol and `nu_s`, the full map acquires a reproducible nonzero `log M` column that cannot be represented by endpoint calibration, source-frequency input, boundary shape or numerical error.

A passed gate supports at most:

`SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Expected unresolved gate:

`PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

No outcome here is evidence for UMCH. No structural dead end is declared because physical clock realization, source/absorber dynamics, detector response, covariance and other exact geometries remain open routes.

## Post-run disposition

The preregistered negative expectation passed. Static source-local frequency fixes affine normalization relative to an imported clock. The full phase map obeys the declared phase-rate similarity; at fixed `nu_s=M omega_s`, Schwarzschild dilation remains exact within numerical tolerance and the `log M` Jacobian column remains null. Holding dimensional `omega_s` fixed changes `M omega_s` and is therefore `EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

No corrected PR #95 profile, PR #96 affine reconciliation, prior negative result, source scope or hypothesis contract was changed. Final status is `SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`. `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`.
