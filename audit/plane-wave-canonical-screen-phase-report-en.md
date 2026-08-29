# Exact plane-wave canonical rotating-screen audit

Classification: `EXACT_SPACETIME_CANONICAL_SCREEN_PHASE_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_VELOCITY_SPECTRUM_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_MAP_AFFINE_SCALE_BLIND_NOT_ELL0`.

Open gate: `PHYSICAL_SCREEN_CANONICAL_MOMENTUM_ENDPOINT_ANGULAR_VELOCITY_AND_UNIT_CALIBRATION_NOT_DERIVED`.

Raw `K,omega,Q,A,x,x_prime,p,P_inertial,P_velocity,P_canonical,H_source,H_observer,L` remain primary. With `p=x'+Ax=Q^T y'`, the canonical generator is `M_c=[[-A,I],[-Q^TKQ,-A]]`; `P_c=C_o^-1 P_inertial C_s`, `C=diag(Q,Q)`. Also `P_c=H(A_o)P_velocity H(A_s)^-1`, `H(A)=[[I,0],[A,I]]`.

Direct/endpoint residual is `1.823955281067939e-14`; velocity-conversion residual `1.7617423914230872e-14`. Canonical standard symplectic residual is `9.223583285220894e-15`. Velocity standard residual is `2.9790466121319246`, but its endpoint pulled-form residual is `4.408342475837773e-14`.

Canonical/velocity characteristic difference is `0.32091041757227023`. At fixed `K,Q,P_inertial,P_canonical`, a calibration-only endpoint-`A` change moves the velocity map by `0.7876233361697514` and its characteristic coefficients by `0.49508910842587517`; canonical map movement is zero. Thus PR #77 ordinary characteristic polynomial is a velocity-coordinate diagnostic, not a canonical screen invariant. PR #77 velocity differential equation and endpoint graph remain valid.

Common-basis covariance residuals are at most `1.1790722901913857e-14`. Affine/profile/connection scaling with factor `1.47` collides canonically within `6.447625741532216e-14`; absolute scale and `ell0` remain unidentified.

Coley–McNutt–Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish detector canonical momentum, endpoint angular velocity, displacement/momentum units, common screen, causal window, affine nuisance, `ell0`, UMCH, or detection.

Detector action/readout, physical tetrads, path, window, endpoint calibration, and allowed block-preserving group remain open. This is not a structural dead end. UMCH is `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
