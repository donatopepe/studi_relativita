# Schwarzschild radar cross-channel rank

## Question and raw map

For the ideal static radial-radar boundary, set `rho_o=r_o/M` and `rho_m=r_m/M`. The raw dimensionless map tested here is

`(rho_o,rho_m) -> (Delta tau/M,H_radar)`.

The finite Levi-Civita holonomy lies numerically in one `SO^+(1,1)` block. Its signed coordinate is

`eta_radar = atanh(H_radar[0,1]/H_radar[0,0])`,

and direct reconstruction by the boost matrix agrees to `4.76247466510716e-12`. This is a coordinate on the same holonomy, not an extra channel.

## Local result

At `(rho_o,rho_m)=(7,4)`, the Jacobian for `(Delta tau/M,eta_radar)` is

`[[2.5998191581422248,-3.3806170203209973],[-0.056356635431131785,0.1683673480272485]]`.

Thus `determinant_raw=0.24720445606033067`, singular values are `[4.267997181943059,0.05792048249378249]`, and `rank_raw = 2`. Along the normalized fixed-duration tangent, the duration derivative is `4.440892098500626e-16` while the rapidity derivative is `-0.05796531852116355`. This resolves the previous fixed-duration endpoint collision only inside the anchored, signed, dimensionless toy map.

## Quotient and global counterexample

Loop reversal sends `eta_radar -> -eta_radar`. The even orientation quotient `(Delta tau/M,cosh eta_radar)` still has local rank two at the baseline; its smaller singular value is `0.009280233527716465`. Yet `eta` and `-eta` are a global collision in that quotient. Common tetrad changes conjugate the raw holonomy and preserve characteristic coefficients. Therefore local rank is not global injectivity, and orientation quotient must be separated from an anchored signed record.

## Scale null direction

Under `(M,r_o,r_m)->s(M,r_o,r_m)`, both `Delta tau/M` and `eta_radar` are unchanged while `Delta tau` changes. The three-variable map has a scale null direction and rank at most two. No absolute scale or `ell0` is recovered.

A deterministic 16-point interior scan has minimum smaller singular value `0.00017366826156943785`; this finite scan is not a theorem over the full exterior domain. Shrinking separation and the flat control lose holonomy rank as required.

## Scope and limits

This is not a detector-derived covariance model. Duration and holonomy share one metric, one boundary and one connection history. `rank_raw=2` does not establish statistical cross-channel independence. Static accelerated endpoints, ideal mirror, reflection/closure, common static tetrad family, orientation, gains and readout remain prescribed. No fundamental scale law appears.

Status: `ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0`.

Scope: `SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE`.

Gate: `PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end is `NOT_DECLARED`.
