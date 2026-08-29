# Exact plane-wave screen-connection holonomy and spectrum quotient

## Question

Can finite holonomy or its spectrum recover independent cross-channel information from the two endpoint-matched rotating-screen histories, beyond transported windows and continuous Jacobi histories?

## Classification

`EXACT_SPACETIME_SCREEN_CONNECTION_HOLONOMY_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Project derivation and negative identifiability control in an exact Brinkmann plane-wave background. Screen connection remains prescribed; this is not a detector-derived spacetime loop, data result, `ell0` law or UMCH evidence.

## Alternatives considered

1. **Screen `SO(2)` Wilson line.** Exact and bounded. In two screen dimensions its generator is one-dimensional, so path ordering collapses and holonomy depends only on integrated connection angle. This is selected as strongest immediate counterexample to “holonomy implies extra rank.”
2. **Canonical phase-space Wilson line.** Its ordered exponential is the already-retained Jacobi map, so treating it as another channel would double count rather than add rank. Retain as algebraic cross-check, not independent observable.
3. **Four-dimensional Levi-Civita loop holonomy.** Scientifically stronger but requires a spacetime loop family, anchor, tangent transport and connection pullback not yet derived by current detector protocol. Keep open rather than invent it.

## Declared construction

For `A_i(u)=-omega_i(u) J`, define screen transport

`U_i(u_b,u_a)=P exp[integral_(u_a)^(u_b) A_i(u) du]`.

Because every `A_i(u)` is proportional to the same `J`, all values commute and

`U_i=exp[J theta_i]`, `theta_i=-integral omega_i du`.

For the endpoint-matched paths of PR #80/#81, the bump has zero total integral, so source-to-observer `U_1=U_2` although their partial Wilson-line histories differ. Define relative closed screen holonomy

`H_21=U_2(u_o,u_s)^-1 U_1(u_o,u_s)`.

It must be identity. Its characteristic spectrum and trace add no rank.

For open paths, conjugacy-invariant screen data are `tr U=2 cos(theta)` and `det U=1`. Trace loses sign (`theta` versus `-theta`) and winding (`theta+2 pi n`). Under `O(2)` reflection, oriented angle changes sign while trace does not. Therefore even nontrivial screen holonomy trace is orientation/winding aliased unless anchor, parity and branch are fixed.

For canonical partial maps already retained,

`P_c,i(u)=C_i(u)^-1 P_I(u) C_i(u_s)`.

The relative endpoint loop `P_c,2(u_o) P_c,1(u_o)^-1` is identity for endpoint-matched screens. At intermediate `u`, relative coordinate history is fixed by local gauge and is not an independent channel under that quotient.

## Tests

1. Numerically integrate prescribed `A_i`; compare ordered product with analytic `exp[J theta_i]`.
2. Show nonzero intermediate Wilson-history difference but endpoint equality.
3. Show relative endpoint holonomy and relative canonical endpoint loop equal identity.
4. Show trace sign and winding aliasing with raw matrices retained.
5. Show common `SO(2)` covariance and `O(2)` angle reversal/trace invariance.
6. Show zero connection collapse.
7. Show affine/connection scaling preserves dimensionless angle and relative collision.
8. Preserve deterministic raw matrices, sampled partial holonomies, angles, traces, spectra and cross-channel maps.
9. Add bilingual audits and exact source-scope limits.

## Source scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish the prescribed screen connection, detector screen, loop family, Wilson-line readout, branch/winding/parity calibration, `ell0`, UMCH or detection. Matrix-exponential and `SO(2)` identities here are project algebra, not attributed physical results.

## Decision

Expected status:

`EXACT_PLANE_WAVE_SO2_SCREEN_HOLONOMY_ENDPOINT_MATCHED_AND_TRACE_SIGN_WINDING_ALIASED_CANONICAL_LOOP_NOT_INDEPENDENT_NOT_ELL0`.

Expected gate:

`PHYSICAL_SPACETIME_CONNECTION_LOOP_FAMILY_ANCHOR_BRANCH_PARITY_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end: non-Abelian four-dimensional connection holonomy, detector-derived loops, physical anchors and branch conditioning remain open.
