# Reissner–Nordström finite null-scattering Jacobi audit

## State

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

Result:

```text
REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE_BUT_Q_SQUARED_DEGENERACY_AND_JOINT_MQ_DILATION_RETAIN_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Gate:

```text
PHYSICAL_CHARGE_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

## Frozen control

Metric: `f(r)=1-2M/r+Q^2/r^2`. Shape coordinate: `epsilon=Q/M`. Baseline uses `M=1`, `epsilon=0.8`, `rho=4`, `R=12`, unit Killing energy, `beta=5.4433105`, equal-radius finite endpoints and screen order `(polar,in-plane)`. Full `4x4` phase map is primary; screen trace, trace-free entries and graph projections remain secondary diagnostics.

Direct numerical four-dimensional Riemann projection gives `maximum_abs_Ricci_trace=0.0092592465`. This is charge-dependent optical shape, not an independent measured channel. No joint covariance exists, hence `DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE`.

## Counterexamples and conformance

- At `epsilon=0`, path residual is zero and Schwarzschild full-map `phase_map_residual=8.0925039e-06` at artifact resolution.
- Replacing `Q` by `-Q` leaves path, profile and map unchanged: `Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0`.
- Orientation reversal agrees in declared equatorial screen. This is scoped symmetry, not statistical independence.
- Zero affine window gives identity.
- Joint dilation of `M,Q,r,b,lambda` at fixed `epsilon,rho,R`, followed by declared phase-rate conversion, preserves dimensionless profile and map within numerical tolerance.
- Rank audit gives `rank_with_log_M_and_epsilon=1`, with `scale_null_direction=[1,0]`: charge ratio supplies shape while absolute `M` remains null.

Charge, `Q/M`, photon radius, turning radius and impact parameter are not `ell0`. More matrix entries do not establish independent information.

## Source scope and review

`EiroaRomeroTorres2002` supports RN metric, photon sphere and closest-approach/impact relations. `Sachs1961` and `SchneiderEhlersFalco1992` support general null-optical/Jacobi context. They do not establish finite-boundary protocol, direct numerical screen projection, endpoint preparation, receiver, covariance, `ell0`, UMCH, evidence or detection.

Closure mode: `DIRECT_REVIEW_NO_SUBAGENT`, required by user policy. This is direct review, not independent review.
