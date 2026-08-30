# Schwarzschild scattering with static endpoint frequency transfer

## Bounded object

This project derivation retains the corrected generic Schwarzschild scattering screen and the full `4x4` phase map as primary:

`FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY`.

Geometry is finite-boundary equatorial future-null scattering with `R>rho>3`, one turning point, static endpoint tetrads and screen order `(polar,in-plane)`. At project normalization `E_infinity=1`, the audited optical profile is

`K_1=diag(-1,+1) 3 M b^2/r^5`.

No scalar Sachs graph replaces the full map through caustics.

## Static-tetrad frequency normalization

For a static tetrad at radius `r`, conservation of Killing energy gives

`omega(r)=E_infinity/sqrt(1-2M/r)`.

A declared source-local frequency therefore fixes

`E_infinity=omega_s sqrt(1-2M/r_s)`,

and the observer frequency must obey the same conserved energy. Assigning source and observer frequencies independently is inconsistent unless an extra interaction is introduced. None is introduced here.

Relative to `E_infinity=1`, let `a=E_infinity`. Then

`lambda_a=lambda_1/a`, `K_a=a^2 K_1`.

For phase state `(X,dX/dlambda)`, with `D_a=diag(I,aI)`, the full map transforms as

`P_a=D_a P_1 D_a^-1`.

The deterministic control at `M=1`, `R=12`, `rho=4`, `omega_s=0.2` gives `a=0.18257418583505539`, profile ratio `0.03333333333333334`, raw rate-coordinate map difference `1086.2506743368622`, and converted residual `6.821210263296962e-12`. Thus source frequency fixes affine normalization relative to an external clock; it does not create a new intrinsic Jacobi object.

## Scale and identifiability counterexample

Define the dimensionless source-frequency product `nu_s=M omega_s`. Under Schwarzschild dilation, keep `rho`, `R`, and `nu_s` fixed, scale endpoint radii with `M`, and convert phase-rate units. For factor `1.7`, converted full-map residual is `1.7280399333685637e-11` and frequency-product residual is zero.

The local Jacobian in `(rho,R,log M)` has `rank_shape_boundary=2`, `rank_with_log_M=2`, `log_M_column_norm=4.270886111708851e-10`, and scale-null direction `[0,0,1]`; global injectivity remains `NOT_ESTABLISHED`.

Holding dimensional `omega_s` fixed instead changes `M omega_s` and moves the output. That direction is classified

`EXTERNAL_FREQUENCY_STANDARD_DIRECTION_NOT_INTERIOR_GEOMETRIC_SCALE`.

It compares geometry to an imported clock unit. It is not an interior geometric scale, an `ell/ell0` law, or identification of `ell0`.

## Sources and limitations

`Schwarzschild2003Translation` supports Schwarzschild metric context. `Darwin1959GravityField` supports null-trajectory and critical-orbit context. `Sachs1961` supports null optical/Jacobi framework. These sources do not establish this finite-boundary source-clock protocol, physical source spectrum, absorber response, screen preparation, detector vector readout, covariance, `ell0`, UMCH, evidence or detection.

Source clock status is `TOY_EXTERNAL_FREQUENCY_STANDARD_NOT_DETECTOR_DERIVED`. Joint channel independence is not assumed.

## Disposition

Status:

`SCHWARZSCHILD_STATIC_ENDPOINT_FREQUENCY_TRANSFER_FIXES_AFFINE_NORMALIZATION_RELATIVE_TO_EXTERNAL_CLOCK_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`

Gate:

`PHYSICAL_SOURCE_CLOCK_SPECTRUM_ABSORBER_RESPONSE_SCREEN_PREPARATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

`UMCH=UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; detection is `NO_POSITIVE_DETECTION_CLAIM`. Maximum interpretation remains `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.
