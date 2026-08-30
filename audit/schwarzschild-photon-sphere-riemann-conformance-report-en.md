# Schwarzschild photon-sphere full-Riemann conformance audit — English

## Decision

`classification=FULL_FOUR_DIMENSIONAL_RIEMANN_CROSS_CONFORMANCE_AND_NEGATIVE_AFFINE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_FULL_RIEMANN_CONFIRMS_LEGACY_PROFILE_AFTER_SCREEN_ORDER_AND_AFFINE_NORMALIZATION_NOT_ELL0`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_ABSOLUTE_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

`review=DIRECT_REVIEW_NO_SUBAGENT`

UMCH remains `UNPROVEN`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; detection remains `NO_POSITIVE_DETECTION_CLAIM`. Passing means at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Counterexample-first result

The suspected conflict with the corrected scattering profile was a normalization/order trap, not a falsification of the legacy circular profile. Direct reconstruction of the full four-dimensional Schwarzschild Riemann tensor uses centered derivatives in both `r` and `theta`, then projects both channels onto the explicit `(polar,radial)` screen. For local circular frequency one,

`K_circular=diag(-1,+1)/(9M^2)`.

Coarse and fine projection mismatches are `3.455052488702422e-08` and `2.308480787357262e-09`; fine legacy mismatch is also `2.308480787357262e-09`. Both polar and radial entries are direct projections; vacuum trace is only a check. Therefore the PR #90 legacy profile is confirmed, not falsified, after converting its former `(radial,polar)` presentation to explicit `(polar,radial)` order.

The PR #95 scattering limit is

`K_scattering=diag(-1,+1)/(3M^2)`

for the project anchor `E_infinity=1`. At `r=3M` its local static-tetrad frequency is `sqrt(3)`, whereas the circular control sets local frequency to one. Since optical tidal matrices scale quadratically with affine frequency, division by `3` gives the circular matrix. Converted residual is `1.962615573354719e-17`; unconverted residual is `0.31426968052735443`.

Thus the naive cross-control is `FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON`. Both prior profiles are mutually conformant only after explicit screen order and affine-frequency conversion.

## Interpretation and sources

`FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY`; graph reductions remain conditional on block invertibility. This conformance adds no absolute standard and no `ell0` direction.

`Schwarzschild2003Translation` supports metric context only; `Darwin1959GravityField` supports null trajectories and critical-orbit context; `Sachs1961` supports null optical/Jacobi framework. These sources do not establish project screen preparation, source/observer boundary, detector calibration or readout, covariance, `ell0`, UMCH, evidence or detection.
