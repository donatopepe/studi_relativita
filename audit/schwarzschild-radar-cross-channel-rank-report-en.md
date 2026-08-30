# Audit: Schwarzschild radar cross-channel rank

## Verdict

`ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0`

Scope: `SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE`.

Gate: `PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Detection: `NO_POSITIVE_DETECTION_CLAIM`. Structural dead end: `NOT_DECLARED`.

## Reproducible result

At `M=1,r_o=7,r_m=4`, boost reconstruction residual is `4.76247466510716e-12`. Joint Jacobian determinant is `0.24720445606033067`; smaller raw singular value is `0.05792048249378249`. Fixed-duration tangent changes signed rapidity by `-0.05796531852116355` per unit tangent parameter.

Even orientation quotient remains locally rank two with smaller singular value `0.009280233527716465`, but reversal gives global collision between `eta` and `-eta`. Common conjugation preserves characteristic data. Scale dilation preserves dimensionless joint output while changing proper duration. Interior scan minimum singular value is `0.00017366826156943785`; finite grid proves no global theorem.

## Interpretation boundary

local rank is not channel independence. Timing and holonomy derive from same Schwarzschild geometry and selected boundary; no joint noise/covariance or vector readout is derived. Global collision, absolute scale blindness, ideal mirror, accelerated static endpoints and common tetrad anchor prevent an `ell0` interpretation.

Sources `Schwarzschild2003Translation`, `AmbroseSinger1953`, and `Lin2020RadarCoordinates` support geometry, holonomy background and radar-coordinate context only. They do not establish endpoint rank, detector covariance, UMCH or detection.
