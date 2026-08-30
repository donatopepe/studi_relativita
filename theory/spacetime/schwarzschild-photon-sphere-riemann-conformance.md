# Schwarzschild photon-sphere full-Riemann conformance

`classification=FULL_FOUR_DIMENSIONAL_RIEMANN_CROSS_CONFORMANCE_AND_NEGATIVE_AFFINE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_FULL_RIEMANN_CONFIRMS_LEGACY_PROFILE_AFTER_SCREEN_ORDER_AND_AFFINE_NORMALIZATION_NOT_ELL0`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_ABSOLUTE_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

## Direct projection

At `r=3M`, use the circular project anchor `k=e_0+e_3` and ordered screen `(polar,radial)`. Full four-dimensional reconstruction includes centered derivatives in `r` and `theta` and computes both screen channels directly:

`K_AB=-R_abcd e_A^a k^b e_B^c k^d=diag(-1,+1)/(9M^2)`.

Refinement mismatch falls from `3.455052488702422e-08` to `2.308480787357262e-09`. Legacy mismatch is `2.308480787357262e-09`. Hence the old photon-sphere profile is not falsified; its former `(radial,polar)` order needed explicit conversion.

## Affine-frequency counterexample

The corrected scattering limit `diag(-1,+1)/(3M^2)` uses `E_infinity=1`. Its local frequency at `3M` is `sqrt(3)`, versus unit local frequency for the circular control. Because `K` is quadratic in null-tangent normalization, converting by `1/(sqrt(3))^2` yields the circular profile with residual `1.962615573354719e-17`.

Therefore `FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON`: comparing the matrices without phase-rate/frequency conversion creates a false factor-three contradiction.

`FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY`. Caustics, graph objects and phase rates must retain declared affine normalization and block-invertibility domains. Scale conversion resolves cross-control conformance but supplies no physical absolute frequency standard and no internal scale.

## Scientific scope

- `UMCH=UNPROVEN`
- `ell0_identified=false`
- `structural_dead_end=NOT_DECLARED`
- `detection=NO_POSITIVE_DETECTION_CLAIM`
- maximum `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`
- review `DIRECT_REVIEW_NO_SUBAGENT`

`Schwarzschild2003Translation` supports metric context only. `Darwin1959GravityField` supports null trajectories and critical-orbit context. `Sachs1961` supports null optical/Jacobi framework. Sources do not establish project boundary data, screen preparation, affine/frequency standard, detector calibration/readout, covariance, `ell0`, UMCH, evidence or detection.
