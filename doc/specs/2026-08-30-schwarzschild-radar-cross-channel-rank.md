# Schwarzschild radar joint-map rank and quotient control

## Bounded question

The prior static-radar control established that one dimensionless duration does not identify the two dimensionless endpoints and that anchored holonomy varies across a fixed-duration pair. This follow-up asks the stronger counterexample-first question: does the joint map from endpoint geometry to channel-native radar timing and Levi-Civita holonomy have independent local rank, and does that rank survive declared orientation, conjugacy and absolute-scale nuisances?

UMCH remains `UNPROVEN`; no detector, covariance, mechanism, `ell0`, data or detection is introduced.

## Alternatives considered

1. **Exact radial radar joint-map rank — selected.** Reduce the `t-r` holonomy to its boost rapidity, verify against numerical transport, compute the Jacobian of `(Delta tau/M, rapidity)` with respect to `(r_o/M,r_m/M)`, and attack rank under reversal/conjugacy and geometric scaling. This directly tests the previous apparent cross-channel separation with minimal new assumptions.
2. **Nonradial photon echo.** Add angular momentum and light bending. It offers richer boundary shape but introduces turning-point branches, capture domains and elliptic integrals before the simpler rank question is settled.
3. **Radar optical Jacobi map.** Propagate screen bundles along null legs. Radial spherical symmetry and reflection boundary require source shape, mirror action and screen matching that are not physically derived.

## Classification

- Schwarzschild exterior metric, radial null curves and Lorentz boost algebra: `KNOWN_RESULT`.
- Closed-form radar timing, rapidity extraction, derivatives and transport comparisons: `PROJECT_DERIVATION`.
- Static observer, ideal mirror, common coordinate-family tetrad identification and selected endpoint domain: `TOY_CONTROL`.
- Rank loss, quotient collisions and scale orbit: `NEGATIVE_RESULT`.
- Detector-derived channel covariance, endpoint calibration and `ell0` law: `OPEN_PROBLEM`.

## Parameter and raw-object contract

Set `rho_o=r_o/M`, `rho_m=r_m/M`, with `2<rho_m<rho_o`. Preserve raw

`M,r_o,r_m,rho_o,rho_m,r_star,Delta_t,Delta_tau,H_radar,eta_radar,orientation,transport_residual,Jacobian_raw,singular_values_raw,determinant_raw,fixed_duration_tangent,holonomy_derivative_along_collision,quotient_maps,scale_factor,scale_orbit`.

The primary map is

`J_raw:(rho_o,rho_m)->(Delta tau/M,H_radar)`.

Because the radial holonomy acts in one `SO^+(1,1)` block, use signed rapidity

`eta_radar=atanh(H^0_1/H^0_0)`

only as an exact coordinate on that raw block, not as an independent channel. Verify reconstruction `H_radar=B(eta_radar)` and agreement with numerical transport before rank interpretation.

## Counterexample-first tests

1. Derive or numerically validate closed-form/automatic finite-difference derivatives for `Delta tau/M` and signed `eta_radar` on a preregistered exterior domain.
2. Show duration-only Jacobian rank is one and construct its fixed-duration tangent.
3. Evaluate `d eta_radar` along that tangent. Nonzero derivative gives local rank two only for the anchored signed toy map.
4. Reverse loop orientation. Signed rapidity changes sign while characteristic coefficients remain invariant; test whether quotient map `(Delta tau/M,cosh eta_radar)` retains generic local rank but loses orientation globally.
5. Exhibit global orientation collision `eta<->-eta` even when local quotient rank is two. Local full rank must not be reported as global injectivity.
6. Apply common tetrad conjugation. Characteristic data remain unchanged while raw matrices differ.
7. Apply `(M,r_o,r_m)->s(M,r_o,r_m)`. Both dimensionless timing and rapidity remain unchanged while `Delta tau` changes; absolute rank including scale is at most two for three geometric variables.
8. Search a deterministic endpoint grid for near-rank-loss regions and boundary degeneration (`rho_m->rho_o`, weak-field dilation). Preserve smallest singular values and domain exclusions without promoting numerical near-zero to an exact theorem.
9. Flat and shrinking controls must collapse holonomy information.

## Interpretation gates

A rank-two dimensionless toy map, if found, means only that two dependent outputs of one exact geometry can locally recover two dimensionless endpoint labels under anchored calibration. It does not prove statistically independent channels, detector observability, global injectivity, absolute-scale recovery or an `ell0` landmark.

Cross-channel label:

`ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0`.

Scope:

`SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE`.

Gate:

`PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end is declared: nonradial causal networks, freely falling endpoints, detector actions and physically restricted covariance/mixing remain open.
