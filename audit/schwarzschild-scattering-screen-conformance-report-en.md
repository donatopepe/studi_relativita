# Audit — Schwarzschild scattering screen/Riemann conformance (EN)

- Status: `SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0`
- Gate: `PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`
- `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`
- Detection: `NO_POSITIVE_DETECTION_CLAIM`
- Maximum interpretation: `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`
- Review: `DIRECT_REVIEW_NO_SUBAGENT`

## Falsified and corrected project formulas

Independent four-dimensional finite-difference Riemann projection, including both radial and polar metric derivatives, falsifies prior project formula `diag(+1,-1) M b^2/r^5`. Corrected formula for `X''=K X`, in `(polar,in-plane)` order, is `diag(-1,+1) 3 M b^2/r^5`.

At `rho=3.000001`, turning values approach `diag(-1,+1)/3`, not prior `diag(+1,-1)/9`. This is a bounded `NEGATIVE_RESULT` against project implementation, preserved explicitly.

## Raw transport and reconstruction checks

The in-plane screen has nonzero raw derivative `0.1767889727337515`, mostly null gauge. Explicit quotient residual refines from `7.965045099585612e-05` (`n=60`) to `1.9939515283841326e-05` (`n=120`); fine screen rotation is `1.851520265341161e-05`. Endpoints use separate one-sided diagnostics.

Riemann profile mismatch refines from `2.2914168372714706e-08` to `1.8971899374401116e-09`; fine symmetry residual is `0.0`, vacuum-trace residual `1.3529229958564315e-09`, orientation profile residual `0.0`.

Corrected phase map remains symplectic and scale blind:

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

## Classification and source limits

`Schwarzschild2003Translation`, `Darwin1959GravityField`, and `Sachs1961` support only `KNOWN_RESULT` metric/null-geodesic/Jacobi context. Null-gauge quotient, finite-difference reconstruction, profile correction and phase-map rerun are `PROJECT_DERIVATION`. Finite boundary, static tetrad, unit Killing energy, handedness and step schedule are `TOY_CONTROL`. Physical source, endpoint realization, absolute standard, detector vector readout, covariance and `ell0` law remain `OPEN_PROBLEM`.

These sources do not establish project boundary protocol, detector calibration, covariance, `ell0`, UMCH, evidence or detection. Correction does not identify `ell0` and does not trigger reformulation.
