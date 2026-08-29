# Covariant Sachs graph in a rotating exact-plane-wave screen

Classification: `EXACT_SPACETIME_COVARIANT_SACHS_SCREEN_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_SACHS_TWIST_CONNECTION_AND_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_GRAPH_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SACHS_SCREEN_TRANSPORT_CANONICAL_BOUNDARY_ENDPOINT_RATE_AND_PARITY_NOT_DERIVED`.

## Raw graph

Retain `K,omega,Q,A,Y,U,X,P,V,R,S_rot,S_0,L`. For inertial `Y'=U`, set `Y=QX`, `Q'=QA`, `A=-omega J`, and `P=Q^TU`. Away from caustics,

`R=P X^-1=Q^T(UY^-1)Q`,

`V=X'=P-AX`,

`S_rot=V X^-1=R-A`.

`R` is the canonical momentum graph; `S_rot` is the coordinate-velocity Sachs graph. Their direct and endpoint constructions agree within `1.487222375023867e-14`; `S_rot=R-A` residual is `1.1775693440128312e-16`.

With source fixed, exact Riccati equations are

`R'=-Q^TKQ-A R-R^2+R A`,

`S_rot'=-Q^TKQ-A'-A^2-2A S_rot-S_rot^2`.

Numerical residuals are `2.94611574439817e-10` and `2.9466757892120056e-10`.

## Twist and calibration counterexample

Canonical twist is `0.20595370725657275`; connection twist is `-0.606626`; velocity twist is `0.8125797072565728`, satisfying

`twist(S_rot)=twist(R)-twist(A)`

exactly at reported precision. At fixed canonical graph, changing only reported observer endpoint rate by `0.29 J` moves velocity graph by `0.4101219330881975` and velocity twist by `0.2899999999999999`; canonical graph movement is zero. This is a phase-variable calibration counterexample, not another physical transport solution.

Common `SO(2)` preserves oriented twist and graph covariance within `1.1102230246251565e-16`; `O(2)` reflection flips twist sign exactly. Under `K_s=s^-2K(u/s)`, `omega_s=s^-1omega(u/s)`, `S_0s=S_0/s`, `L_s=sL`, `s=1.47`, dimensionless `X,LP,LR,LS_rot,LA` collide within `3.393940618659158e-14`. Absolute scale and `ell0` remain unidentified.

## Ledger and limits

Earlier inertial non-vertex twist-area conservation remains valid in its declared screen. This control adds canonical/velocity graph distinction and connection term; it does not erase boundary dependence or raw history. Caustics return `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`.

Coley–McNutt–Milson 2012, DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish rotating Sachs detector screens, canonical boundary preparation, endpoint rate, parity, finite windows, affine nuisance, `ell0`, UMCH, or detection.

Physical tetrads, Fermi/parallel transport, detector congruence/action, causal support, parity anchor, unit calibration, and caustic continuation remain open. No structural dead end is declared. UMCH stays `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
