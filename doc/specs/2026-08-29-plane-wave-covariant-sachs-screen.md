# Covariant Sachs matrix under rotating screen transport

## Question

How must the non-vertex Sachs object transform when the screen basis varies, and which apparent twist/expansion/shear features are physical versus connection or endpoint-calibration terms?

## Approaches

1. Rotate `S=VX^-1` only by `Q^T S Q`: rejected for velocity derivative in a varying basis; connection term is omitted.
2. Use the canonical momentum graph only: insufficient for Sachs expansion because optical rate is defined from coordinate velocity.
3. Selected: derive both canonical graph `R=p x^-1` and velocity Sachs graph `S=x' x^-1`, verify direct rotating-coordinate propagation against inertial endpoint transformation, and attack twist interpretation with calibration/path counterexamples.

## Derivation

For inertial `Y'=U`, non-vertex boundary `Y_s=I`, `U_s=S_0`, set `Y=QX`, `Q'=QA`, `A=-omega J`. Then

`X=Q^T Y`,

`X'=Q^T U-A X`,

`P=Q^T U`,

`R=P X^-1=Q^T (U Y^-1) Q`,

`S_rot=X'X^-1=R-A`.

Thus canonical graph `R` transforms homogeneously, while velocity Sachs graph has inhomogeneous connection term `-A`. Boundary preparation transforms as

`X_s=Q_s^T`, `P_s=Q_s^T S_0`, `S_rot,s=Q_s^T S_0 Q_s-A_s`.

For `SO(2)`, oriented twist obeys

`twist(S_rot)=twist(S_inertial)-twist(A)`

in common orientation conventions. Therefore a rotating screen can create apparent velocity-coordinate twist even from vertex/self-adjoint canonical graph; it is not an independent curvature channel.

## Counterexample-first controls

- `omega=0`: inertial, canonical, and velocity Sachs graphs coincide.
- Direct propagation through canonical rotating generator with transformed non-vertex boundary agrees with inertial endpoint graph.
- Exact relation `S_rot=R-A` and Riccati equations hold away from caustics.
- At fixed `K,Q,Y,U,R`, change only reported endpoint `A_o`: `S_rot` twist shifts while canonical `R` does not. Label as endpoint phase-variable calibration counterexample, not alternate physical transport.
- Change declared connection profile at fixed curvature and inertial congruence: canonical coordinates rotate, while raw invariant eigenvalues of symmetric inertial/canonical graph remain basis-covariant; velocity twist acquires connection contribution. This is protocol dependence.
- Common `SO(2)` basis gives covariance; `O(2)` reflection flips oriented twist sign.
- Affine/profile/connection/boundary scaling preserves dimensionless `X,LP,LR,LS_rot,LA,LS_0`; absolute scale remains unidentified.
- Caustics return explicit gate.

## Classification and limits

Classification: `EXACT_SPACETIME_COVARIANT_SACHS_SCREEN_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_SACHS_TWIST_CONNECTION_AND_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_GRAPH_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SACHS_SCREEN_TRANSPORT_CANONICAL_BOUNDARY_ENDPOINT_RATE_AND_PARITY_NOT_DERIVED`.

Prior non-vertex twist-area conservation remains valid in the inertial declared screen. This iteration adds the distinction between canonical graph `R` and rotating velocity Sachs `S_rot`; it does not erase the boundary result.

Coley–McNutt–Milson 2012 supports exact Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish rotating detector screens, Sachs boundary preparation, endpoint rates, parity, finite windows, affine nuisance, `ell0`, UMCH, or detection.

No structural dead end: physical tetrads, Fermi/parallel screen transport, detector congruence/action, causal support, parity anchor, and caustic continuation remain open. UMCH stays `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
