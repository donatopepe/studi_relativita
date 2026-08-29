# Canonical rotating-screen phase map in an exact plane wave

Classification: `EXACT_SPACETIME_CANONICAL_SCREEN_PHASE_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_VELOCITY_SPECTRUM_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_MAP_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SCREEN_CANONICAL_MOMENTUM_ENDPOINT_ANGULAR_VELOCITY_AND_UNIT_CALIBRATION_NOT_DERIVED`.

## Raw graph and equations

Retain `K,omega,Q,A,x,x_prime,p,P_inertial,P_velocity,P_canonical,H_source,H_observer,L`. Let `y=Qx`, `Q'=QA`, `A=-omega J`, and define

`p=x'+Ax=Q^T y'`.

Then

`x'=p-Ax`, `p'=-Q^T K Q x-Ap`,

and

`M_c=[[-A,I],[-Q^T K Q,-A]]`.

For `C=diag(Q,Q)`, the canonical endpoint map is

`P_c=C_observer^-1 P_inertial C_source`.

Velocity and canonical states obey `z_c=H(A)z_v`, with

`H(A)=[[I,0],[A,I]]`,

hence

`P_c=H(A_observer) P_velocity H(A_source)^-1`.

Because `A` is antisymmetric, `H(A)` is not a standard canonical lower shear. `P_c` preserves the standard symplectic form. `P_velocity` instead preserves endpoint-dependent pullbacks `H(A)^T Omega H(A)`.

## Exact controls

Direct canonical-generator integration agrees with the inertial endpoint graph to `1.823955281067939e-14` and with conversion from the velocity map to `1.7617423914230872e-14`. Canonical standard symplectic residual is `9.223583285220894e-15`; velocity standard residual is `2.9790466121319246`, while its endpoint-pulled-form residual is `4.408342475837773e-14`.

Canonical and velocity characteristic coefficients differ by `0.32091041757227023`. A calibration-only counterexample changes reported endpoint `A_source,A_observer` at fixed `K,Q,P_inertial,P_canonical`: velocity map difference is `0.7876233361697514` and velocity-characteristic difference `0.49508910842587517`, while canonical-map difference is exactly zero. This is not an alternate connection solution.

A common `SO(2)` basis gives canonical similarity with map residual `1.1790722901913857e-14` and characteristic residual `3.2953244754398602e-15`. Under `K_s=s^-2K(u/s)`, `omega_s=s^-1omega(u/s)`, `L_s=sL`, `s=1.47`, canonical maps are related by phase-unit similarity: map residual `6.447625741532216e-14`, characteristic residual `6.274439936211069e-14`. Absolute scale and `ell0` remain unidentified.

## Correction and limits

PR #77 velocity equation and endpoint graph remain correct. Its ordinary characteristic polynomial is relabeled as a velocity-coordinate diagnostic, not a canonical screen invariant. This correction adds `P_c`; it does not erase earlier results.

Canonical momentum here is project-derived from exact Jacobi dynamics. No detector action, tetrad preparation, displacement/momentum unit calibration, endpoint angular velocity, common screen, causal window, or transport path is derived observationally.

Coley–McNutt–Milson 2012, DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish these detector variables or calibrations, finite windows, affine nuisance law, `ell0`, UMCH, or detection.

No structural dead end is declared. UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
