# Exact plane-wave connection-path cross-channel quotient

## Question

Can internal screen-connection history create independent cross-channel information between a transported finite-window tidal operator and covariant Jacobi/Sachs endpoint maps, when curvature, endpoint screen bases, endpoint angular rates, affine support and boundary data are fixed?

## Classification

`EXACT_SPACETIME_CONNECTION_PATH_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

This is a project derivation and exact-geometry negative identifiability control, not a detector model, data result, UMCH evidence or derivation of `ell0`.

## Selected design

Use the existing exact Brinkmann plane-wave tidal profile `K(u)` and construct two smooth prescribed screen histories

`Q_i'=Q_i A_i`, `A_i=-omega_i J`,

on the same affine interval. Choose `omega_1` and `omega_2` so that:

- their integrals over the interval agree, hence `Q_1(u_s)=Q_2(u_s)` and `Q_1(u_o)=Q_2(u_o)` under the common source anchor;
- their endpoint values agree, hence `A_1(u_s,o)=A_2(u_s,o)`;
- their internal histories differ.

Retain raw `K,omega_i,Q_i,A_i,W_i,P_inertial,P_canonical_i,P_velocity_i,X_i,P_i,V_i,R_i,S_rot_i,S_0,L`. Compare:

`W_i=(1/L) int Q_i^T K Q_i du`,

`P_canonical,i=C_o^-1 P_inertial C_s`,

`P_velocity,i=H(A_o)^-1 P_canonical,i H(A_s)`,

and the corresponding non-vertex Sachs endpoint graphs.

## Counterexample-first prediction

The transported window generally changes because it samples the complete screen path. In contrast, the correctly covariant canonical endpoint map depends on the prescribed screen only through endpoint graph transformations. With equal `Q_s,Q_o`, it is identical for the two histories. Equal endpoint `A_s,A_o` also makes the velocity map and endpoint Sachs graphs identical. Thus an internal connection-path difference can move one raw channel while leaving the covariant endpoint channels fixed.

This disproves any automatic inference that prescribed screen-connection order sensitivity supplies independent physical rank across transported-window and Jacobi/Sachs channels. It also distinguishes the path-sensitive naive propagation of `Q^T K Q` from the covariant phase map.

## Controls

1. Verify equal endpoint `Q` and `A`, unequal internal `Q` histories and unequal transported windows.
2. Verify canonical and velocity endpoint maps collide.
3. Verify canonical and velocity Sachs graphs collide away from caustics.
4. Verify naive conjugated-profile propagation changes, while the covariant map does not.
5. Verify common `SO(2)` covariance and `O(2)` parity behavior.
6. Verify affine/profile/connection/boundary scaling preserves the dimensionless collision.
7. Preserve a caustic gate and raw records.
8. Produce deterministic JSON, bilingual audits and semantic-parity tests.

## Source scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish the prescribed screen histories, finite-window kernel, detector tetrads, endpoint calibration, boundary preparation, cross-channel independence, affine nuisance, `ell0`, UMCH or detection.

## Decision rule

A nonzero transported-window difference together with zero covariant endpoint-map/Sachs difference is a negative cross-channel-rank result under the declared equal-endpoint screen quotient. It does not make the transported window unphysical in every protocol: a detector-derived path or continuously sampled screen could restrict the quotient. Passing controls gives at most exact-control validity, never evidence.

Expected status: `EXACT_PLANE_WAVE_INTERNAL_SCREEN_CONNECTION_PATH_MOVES_TRANSPORTED_WINDOW_NOT_COVARIANT_ENDPOINT_MAPS_CROSS_CHANNEL_RANK_NOT_AUTOMATIC_NOT_ELL0`.

Expected gate: `PHYSICAL_CONTINUOUS_SCREEN_READOUT_PATH_KERNEL_ENDPOINT_TETRADS_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end is declared because detector-derived continuous screen readout, spacetime tetrads, causal windows, physical path transport, restricted endpoint groups and additional exact geometries remain open.
