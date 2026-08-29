# Prescribed screen-connection holonomy in an exact plane wave

Classification: `EXACT_SPACETIME_SCREEN_CONNECTION_HOLONOMY_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_SO2_SCREEN_HOLONOMY_ENDPOINT_MATCHED_AND_TRACE_SIGN_WINDING_ALIASED_CANONICAL_LOOP_NOT_INDEPENDENT_NOT_ELL0`.

Open gate: `PHYSICAL_SPACETIME_CONNECTION_LOOP_FAMILY_ANCHOR_BRANCH_PARITY_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

## Raw holonomy record

Retain `omega_i,A_i,U_i(u),theta_i(u),trace_i(u),spectrum_i(u),H_21,P_canonical_loop,L`. Scope: `PRESCRIBED_SO2_SCREEN_CONNECTION_NOT_FOUR_DIMENSIONAL_LEVI_CIVITA_LOOP`. This is a prescribed `SO(2)` screen connection in an exact Brinkmann plane-wave background, not a four-dimensional Levi-Civita loop holonomy.

With `A_i(u)=-omega_i(u)J`,

`U_i(u_b,u_a)=P exp[integral A_i(u) du]`.

All `A_i(u)` are proportional to the same generator `J`, so they commute and

`U_i=exp[J theta_i]`, `theta_i=-integral omega_i du`.

Numerical ordered products agree with this analytic exponential with maximum residual `6.840271371877088e-15`.

## Endpoint-matched counterexample

The two prescribed connection paths have distinct interiors but equal integrated endpoint angle. Partial holonomies differ by up to `0.04595991799966567`; observer holonomies differ by only `5.852149745441549e-15`. The relative endpoint holonomy

`H_21=U_2(u_o,u_s)^-1 U_1(u_o,u_s)`

has identity residual `7.143920687011176e-15`.

The already-retained canonical endpoint maps also collide. Their relative loop `P_c,2 P_c,1^-1` has identity residual `2.593513125236196e-16`. Calling this ordered exponential a separate channel would double count the canonical Jacobi map rather than add rank.

Thus nontrivial intermediate screen transport does not imply independent endpoint holonomy information. Path ordering also adds no screen rank in this `SO(2)` connection because its generator algebra is Abelian.

## Spectrum, branch and parity

For `U(theta)=exp(J theta)`,

`tr U=2 cos(theta)`, `det U=1`, `spec U={exp(i theta),exp(-i theta)}`.

Raw `U(theta)` and `U(-theta)` differ by `1.8861921643140505`, while trace residual is zero. `theta` and `theta+2 pi` give matrix and trace residuals `2.220446049250313e-16`. Therefore trace loses orientation sign and angle winding/branch. Under common `SO(2)` covariance residual is `1.7554167342883506e-16`; an `O(2)` reflection reverses oriented angle while preserving trace exactly.

Zero connection gives identity exactly. Under `omega_s(u)=s^-1 omega(u/s)` and `L_s=sL`, dimensionless holonomies and angles collide with maximum residual `6.7023824694539325e-15` for `s=1.47`. Absolute affine scale and `ell0` remain unidentified.

## Scope and disposition

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish this prescribed screen connection, detector screen, loop/readout family, anchor, branch, winding, parity, `ell0`, UMCH or detection.

This is a project derivation and negative identifiability result, not an observational no-go. Non-Abelian four-dimensional connection holonomy, detector-derived loops, physical anchors and branch conditioning remain open. Structural dead end is `NOT_DECLARED`; UMCH remains `UNPROVEN`; `ell0` is not identified; `NO_POSITIVE_DETECTION_CLAIM`.
