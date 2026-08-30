# Schwarzschild scattering screen and Riemann conformance correction

## Result

The counterexample-first audit tested two claims separately.

First, the declared equatorial screen is not represented by componentwise zero covariant derivative, but its in-plane derivative is parallel to the ray tangent. After explicitly fitting and subtracting that null-gauge direction, the interior residual falls from `7.965045099585612e-05` at `n=60` to `1.9939515283841326e-05` at `n=120`; fine screen-rotation residual is `1.851520265341161e-05`. Raw derivative remains `0.1767889727337515`, so the quotient is recorded rather than hidden. This is `PROJECT_DERIVATION`, not physical screen preparation.

Second, an independent coordinate reconstruction differentiates all metric components in both `r` and `theta`, constructs the full four-dimensional Christoffel and Riemann tensors, lowers the first index, and projects them onto the raw `(polar,in-plane)` screen. It falsifies the prior project profile

```text
diag(+1,-1) M b^2/r^5
```

and gives the corrected profile

```text
diag(-1,+1) 3 M b^2/r^5
```

for the implemented convention `X''=K X`. Coarse/fine maximum profile mismatch is `2.2914168372714706e-08` / `1.8971899374401116e-09`; fine vacuum-trace residual is `1.3529229958564315e-09`. Both orientations give the same projected matrix while preserving different raw screen representatives.

At `rho=3.000001`, the turning values approach `(-1/3,+1/3)` in `(polar,in-plane)` order. Thus the earlier `diag(+1,-1)/9` anchor was not an independent check: it repeated the same incorrect project formula. This correction preserves history rather than rewriting it.

Status:

`SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0`.

## Corrected phase-map consequences

The full phase map was regenerated with corrected `K`. It remains the primary object through caustics. Checks at the deterministic resolution are:

```text
symplectic_residual = 5.684341886080802e-14
reverse_inverse_residual = 1.000444171950221e-11
turning_composition_residual = 5.684341886080802e-14
dimensionless_profile_residual = 4.163336342344337e-17
converted_phase_map_residual = 3.410605131648481e-13
rank_shape_boundary = 2
rank_with_log_M = 2
log_M_column_norm = 5.724578281939044e-09
scale_null_direction = [0,0,1]
global_injectivity = NOT_ESTABLISHED
```

Profile correction changes raw map entries and caustic diagnostics; it does not create an absolute scale. Affine and geometric conversion controls still preserve the `log M` null direction. Existing status therefore remains a negative identifiability result, not evidence.

## Classification and source scope

- Schwarzschild geometry, Levi-Civita transport, null geodesic deviation: `KNOWN_RESULT` within `Schwarzschild2003Translation`, `Darwin1959GravityField`, and `Sachs1961` scope.
- Coordinate conversion, null-gauge fit, finite-difference Christoffel/Riemann reconstruction, corrected phase map and rank audit: `PROJECT_DERIVATION`.
- Finite endpoints, static tetrad, unit Killing energy, selected handedness and numerical schedule: `TOY_CONTROL`.
- Failure of `diag(+1,-1) M b^2/r^5`: `NEGATIVE_RESULT` against prior project implementation.
- Emitter/absorber realization, absolute frequency, physical screen preparation, caustic continuation, vector readout, covariance and any `ell0` law: `OPEN_PROBLEM`.

Those sources do not establish project finite boundaries, screen preparation, detector calibration/readout, covariance, `ell0`, UMCH, evidence or detection.

## Gate and ceiling

`PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

`UMCH=UNPROVEN`, `ell0_identified=false`, `structural_dead_end=NOT_DECLARED`, `NO_POSITIVE_DETECTION_CLAIM`. Maximum interpretation: `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

Review mode: `DIRECT_REVIEW_NO_SUBAGENT`, required by explicit user policy. Physical routes remain open, so no structural dead end or reformulation is declared.
