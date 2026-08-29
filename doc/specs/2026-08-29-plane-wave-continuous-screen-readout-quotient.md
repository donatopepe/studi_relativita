# Exact plane-wave continuous screen-readout quotient

## Question

Does continuously sampling the canonical Jacobi propagator along the support recover independent physical information from two prescribed screen histories that share endpoint basis/rate but differ internally, or is the apparent history removable under a local screen-gauge quotient?

## Classification

`EXACT_SPACETIME_CONTINUOUS_SCREEN_READOUT_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Project derivation and exact-geometry negative identifiability control. Not detector model, data result, UMCH evidence or `ell0` law.

## Design

Use the endpoint-matched connection paths from the preceding control in the same exact Brinkmann plane wave. For every intermediate affine point `u`, compute:

- inertial partial propagator `P_I(u,u_s)`;
- canonical rotating-screen partial map
  `P_c,i(u,u_s)=C_i(u)^-1 P_I(u,u_s) C_i(u_s)`;
- velocity partial map with endpoint rate conversions;
- raw sampled canonical/velocity histories;
- gauge-reconstructed inertial history
  `C_i(u) P_c,i(u,u_s) C_i(u_s)^-1`;
- relative path map between screen descriptions
  `G_21(u)=C_2(u)^-1 C_1(u)`.

Retain sampled histories rather than only endpoint scalars. Use fixed sample grid, exact declared affine support and raw matrices.

## Counterexample-first predictions

Distinct internal `Q_i` make raw coordinate canonical and velocity histories differ at intermediate points, even though endpoint maps collide. But pointwise reconstruction of the common inertial propagator must collide for every sample. The two canonical histories obey the local gauge relation

`P_c,2(u)=G_21(u) P_c,1(u) G_21(u_s)^-1`.

Since source anchors agree, the right factor is identity. Therefore continuous canonical coordinate readout supplies no independent geometry under the full allowed local screen-gauge quotient. It becomes informative only if a physical detector fixes or measures the internal tetrad/readout path.

For velocity variables, include `A_i(u)` in the local conversion. Raw velocity histories can differ more strongly, but canonical reconstruction remains the declared invariant control. Do not interpret ordinary velocity-map spectra as canonical invariants.

## Controls

1. Endpoint maps collide while intermediate raw canonical and velocity histories differ.
2. Reconstructed inertial histories collide pointwise.
3. Local gauge relation for canonical histories holds pointwise.
4. Characteristic coefficients of raw intermediate canonical maps may differ under left endpoint changes; this is not common conjugation and is not an invariant claim.
5. Zero path difference collapses every raw history.
6. Common `SO(2)` basis covariance and `O(2)` parity are explicit.
7. Affine/profile/connection/boundary scaling preserves dimensionless histories and collision.
8. Caustic handling applies only when forming intermediate Sachs graphs; full phase maps remain retained.
9. Deterministic JSON, bilingual audits and semantic parity tests.

## Source scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish continuous detector readout, local screen-gauge quotient, tetrad calibration, causal support/kernel, endpoint units, affine nuisance, `ell0`, UMCH or detection.

## Decision

If raw histories differ but reconstructed histories and gauge-relation residuals vanish, classify continuous coordinate readout as gauge-conditional rather than independent cross-channel rank. This does not rule out detector-fixed continuous tetrads.

Expected status: `EXACT_PLANE_WAVE_CONTINUOUS_CANONICAL_SCREEN_HISTORY_LOCAL_GAUGE_EQUIVALENT_RAW_VELOCITY_HISTORY_CALIBRATION_DEPENDENT_NOT_ELL0`.

Expected gate: `PHYSICAL_CONTINUOUS_TETRAD_READOUT_LOCAL_SCREEN_GAUGE_CAUSAL_SAMPLING_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end: detector-fixed tetrads, local readout action, causal sampling, physical transport, holonomy paths and other exact geometries remain open.
