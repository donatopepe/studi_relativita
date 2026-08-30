# Schwarzschild finite-boundary scattering screen Jacobi map

## Bounded object

For `R>rho>3`, use the preregistered equatorial future-null path with one turning point,

\[
r/M=\rho+y^2,\qquad \beta=b/M=\rho/\sqrt{1-2/\rho},
\]

and unit Killing energy as a project affine anchor. This anchor is not a detector frequency.

In the declared parallel screen, the project derivation gives

\[
\mathcal K=\operatorname{diag}(+1,-1)\frac{Mb^2}{r^5},\qquad
\frac{d}{d\lambda}\binom{X}{V}=\begin{pmatrix}0&I\\\mathcal K&0\end{pmatrix}\binom{X}{V}.
\]

The raw primary object is `FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS`,

\[
P=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]

Graph diagnostics such as `S=DB^{-1}` are emitted only where `B` is invertible. Full `P` remains defined at graph caustics. The bounded scan does not establish a global caustic count: `NOT_ESTABLISHED`.

## Controls

At `(M,rho,R)=(1,4,12)` with artifact resolution, maximum screen orthonormality residual is `4.440892098500626e-16`, vacuum trace residual is `0.0`, symplectic residual is `7.105427357601002e-15`, reverse-inverse residual is `5.684341886080802e-14`, and turning-composition residual is `1.4210854715202004e-14`.

Vertex and parallel source preparations remain distinct mathematical boundary data. Oriented endpoint screen actions change raw entries but reconstruct the interior map; classification is `TOY_ORIENTED_SCREEN_ENDPOINT_ACTION_NOT_PHYSICAL_CALIBRATION`.

Affine rescaling is blind after the declared phase-rate conversion. Under geometric dilation `M -> 2.5 M` at fixed `(rho,R,beta)`, the dimensionless profile residual is `2.42861286636753e-17` and converted phase-map residual is `9.947598300641403e-14`: `GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_PHASE_RATE_AND_ENDPOINT_CONVERSION`.

The preregistered Jacobian has `rank_shape_boundary = 2`, `rank_with_log_M = 2`, `log_M_column_norm = 1.6269172349983679e-10`, and `scale_null_direction = [0, 0, 1]`. Shape/boundary rank is not channel independence. `independent_channels = false`; bounded collision absence does not prove global injectivity, which remains `NOT_ESTABLISHED`.

## Interpretation and source scope

Result:

`SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FULL_SCREEN_JACOBI_PHASE_MAP_ADDS_OPTICAL_PROFILE_AND_CAUSTIC_STRUCTURE_BUT_RETAINS_AFFINE_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

Open gate:

`PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

`Schwarzschild2003Translation` supports metric context only; `Darwin1959GravityField` supports null-trajectory and critical-orbit context only; `Sachs1961` supports null optical/Jacobi framework only. Screen choice, profile integration, endpoint actions, numerical checks, scale and rank are project derivations/toy controls. Sources do not establish detector calibration, covariance, `ell0`, UMCH or detection.

`UMCH = UNPROVEN`; `ell0_identified = false`; `detection = NO_POSITIVE_DETECTION_CLAIM`; maximum interpretation is `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. Structural dead end remains `NOT_DECLARED`.
