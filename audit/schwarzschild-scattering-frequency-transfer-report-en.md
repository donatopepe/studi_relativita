# Audit — Schwarzschild scattering static-frequency transfer

## Contract

Status:

`SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate:

`PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

Scope: finite equatorial future-null Schwarzschild scattering, `R>rho>3`, one turning point, static endpoint tetrads, source-local toy frequency, corrected transported screen `(polar,in-plane)`, full phase map, no detector.

Classifications: metric/redshift/null optics are `KNOWN_RESULT` in bounded source scope; transfer/map/rank audit is `PROJECT_DERIVATION`; ideal static clock is `TOY_CONTROL`; retained scale blindness is `NEGATIVE_RESULT`; physical source/absorber/readout/covariance/`ell0` law remain `OPEN_PROBLEM`.

## Counterexample-first result

Static frequency obeys

`omega(r)=E_infinity/sqrt(1-2M/r)`.

Independent endpoint frequencies are rejected unless they satisfy conserved Killing energy. Equal-radius source and observer have equal local frequency. The primary corrected profile remains

`diag(-1,+1) 3 M b^2/r^5`

at `E_infinity=1`. For source tangent scale `a`, `K_a=a^2 K_1`; with `D_a=diag(I,aI)`,

`P_a=D_a P_1 D_a^-1`.

At `M=1`, `rho=4`, `R=12`, `omega_s=0.2`:

```text
tangent_scale=0.18257418583505539
profile_quadratic_ratio=0.03333333333333334
raw_rate_map_difference=1086.2506743368622
converted_phase_map_residual=6.821210263296962e-12
```

Raw rate-coordinate entries move, but explicit affine phase-rate conversion reconciles maps. Full phase map remains primary.

At fixed `nu_s=M omega_s`, Schwarzschild dilation by `1.7` gives converted residual `1.7280399333685637e-11`. Rank audit gives `rank_shape_boundary=2`, `rank_with_log_M=2`, `log_M_column_norm=4.270886111708851e-10`, scale-null direction `[0,0,1]`, and global injectivity `NOT_ESTABLISHED`.

Holding dimensional source frequency fixed changes `M omega_s` and the output. Disposition:

`EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

This is imported clock calibration, not an intrinsic curvature scale or `ell0`.

## Source scope

`Schwarzschild2003Translation` supports metric context; `Darwin1959GravityField` supports null trajectories/critical-orbit context; `Sachs1961` supports null optical/Jacobi framework. They do not establish this full endpoint protocol, physical clock or source spectrum, absorber response, detector, covariance, `ell0`, UMCH, evidence or detection.

## Review and final state

Direct diff/spec review used because user prohibited subagents: `DIRECT_REVIEW_NO_SUBAGENT`.

`UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; maximum `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.
