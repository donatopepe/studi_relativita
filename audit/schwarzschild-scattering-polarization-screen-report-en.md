# Schwarzschild finite-scattering polarization/screen audit — English

## Disposition

`SCHWARZSCHILD_LEADING_POLARIZATION_IS_CONSTANT_IN_PARALLEL_SCREEN_AND_ENDPOINT_ANALYZER_IS_BASIS_PREPARATION_NUISANCE_RETAINING_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate: `PHYSICAL_POLARIZATION_SOURCE_STATE_EMISSION_ABSORPTION_ENDPOINT_SCREEN_PREPARATION_POLARIZATION_SENSITIVE_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Authority: `UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; `NO_POSITIVE_DETECTION_CLAIM`; maximum interpretation `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Review mode: `DIRECT_REVIEW_NO_SUBAGENT`.

## Preregistered bounded record

Setting: exterior four-dimensional Schwarzschild geometry; future-directed equatorial null scattering with one turning point; equal-radius static endpoints; `M=1`, `rho=4`, `R=12`, `nu_s=0.2`; screen order `(polar,in-plane)`. Leading geometrical optics transports polarization parallel to the ray. Source and analyzer states remain declared toy boundary labels:

```text
j_s=(cos psi_s,exp(i delta_s) sin psi_s)
U_screen=I_2 in the declared parallel screen modulo null gauge
j_R=U_screen j_s
J_R=j_R j_R^dagger
R_polarization=(j_R,J_R,Phi_clock,P_frequency_converted)
```

`j_R` and Hermitian coherency `J_R` append to, and never replace, the complete corrected frequency-converted `4x4` Jacobi phase map. At `psi_s=0.63`, `delta_s=0.41`, the Jones norm and outer-product residuals are zero, Hermiticity residual is zero, and `coherency_determinant_abs=2.7755575615628914e-17`.

Classifications: null propagation and parallel polarization are `KNOWN_RESULT_WITHIN_CITED_SCOPE`; finite endpoint joining, basis quotient and rank checks are `PROJECT_DERIVATION`; source Jones and analyzer labels are `TOY_CONTROL`; retained scale blindness is `NEGATIVE_RESULT`; physical completion is `OPEN_PROBLEM`.

## Transport, basis and boundary counterexamples

Fine screen diagnostics preserve nonzero raw derivative while the null-gauge quotient converges:

```text
max_interior_raw_covariant_derivative=0.1767889727337515
max_interior_screen_quotient_residual=1.9939515283841326e-05
max_interior_screen_rotation_residual=1.851520265341161e-05
```

Thus component constancy belongs to the declared parallel screen quotient; it is not endpoint hardware calibration. A common screen rotation of Jones state, coherency and analyzer leaves analyzer amplitude and power invariant to `2.7755575615628914e-16`. This is a mathematical basis quotient, not a physical polarization rotation measurement.

Changing analyzer alone from `-0.27` to `0.83` changes secondary projected power by `power_difference=0.5145493419909759`, while raw Jones/coherency differences remain zero. Analyzer power cannot replace the raw record. Reversing equatorial orbit orientation gives zero Jones, coherency, clock and converted-map residual in this declared screen: a scoped symmetry, not statistical independence.

At `R-rho=1e-15`, polarization transfer remains identity boundary transport, while `clock_phase=2.8851987866118024e-08` and phase-map identity residual is `7.297198079605369e-07`. Arbitrary surviving source polarization is boundary data, not geometry.

## Scale and rank audit

Under `M -> 1.7 M` at fixed `rho`, `R`, `nu_s=M omega_s`, source Jones labels and analyzer labels:

```text
jones_residual=0.0
coherency_residual=0.0
clock_phase_residual=0.0
converted_phase_map_residual=5.9117155615240335e-12
```

Polarization therefore does not add an internal geometric scale. A fixed dimensional frequency remains an external source/clock standard as in the prior audit, not `ell0`.

For parameter order `(rho,R,log M)`:

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

More vector/matrix entries do not imply physical rank or independence.

## Source scope and limitations

`Schwarzschild2003Translation` supports only Schwarzschild exterior/static context. `Darwin1959GravityField` supports only nonradial Schwarzschild null-scattering context. `Sachs1961` supports only null optical/Jacobi context. `Dolan2018GeometricalOptics` supports only leading geometrical optics, null-ray propagation and parallel-propagated polarization. These sources do not establish this finite endpoint protocol, physical source polarization preparation, source spectrum, emission, absorption, endpoint screen preparation, analyzer material/hardware, polarization-sensitive receiver transfer, calibrated noise, joint covariance, `ell0`, UMCH, evidence or detection.

No physical gravitational Faraday angle is claimed: a screen-basis rotation is not such an observable without independently prepared endpoint frames and observer/readout protocol. No source polarization dynamics, emission/absorption action, receiver or covariance is invented.
