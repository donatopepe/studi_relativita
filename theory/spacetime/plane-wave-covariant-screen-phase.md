# Covariant rotating-screen phase map in an exact plane wave

Classification: `EXACT_SPACETIME_COVARIANT_SCREEN_PHASE_MAP_CORRECTION_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_CONNECTION_TERMS_REQUIRED_NAIVE_TRANSPORTED_JACOBI_MAP_SUPERSEDED_NOT_ELL0`.

Open gate: `PHYSICAL_SCREEN_CONNECTION_ENDPOINT_ANGULAR_VELOCITY_AND_DETECTOR_PHASE_VARIABLES_NOT_DERIVED`.

## Raw graph

Retain `K,omega,Q,A,A_prime,G_source,G_observer,P_inertial,P_naive_conjugated_profile,P_covariant`. With `y=Qx`, `Q'=QA`, `A=-omega J`, inertial `y''=-Ky` becomes

`x''=-2 A x'-(Q^T K Q+A_prime+A^2)x`.

Therefore

`M_covariant=[[0,I],[-(Q^T K Q+A_prime+A^2),-2A]]`,

`G(u)=[[Q,0],[Q A,Q]]`,

`P_covariant=G_observer^-1 P_inertial G_source`.

Direct generator integration agrees with endpoint graph transformation. Zero connection recovers inertial propagation. `P_naive_conjugated_profile`, obtained by placing only `Q^T K Q` into the inertial-form equation, differs from `P_covariant`; it omits Coriolis-like `-2A`, `A_prime`, `A^2`, and endpoint velocity calibration.

A common basis or right-anchor change produces canonical similarity and preserves characteristic coefficients. Under `K_s=s^-2K(u/s)`, `omega_s=s^-1omega(u/s)`, `L_s=sL`, the endpoint graph and characteristic polynomial collide, so absolute scale and `ell0` remain unidentified.

## Correction ledger

PR #76 finite-window `W_transport`, invariant-average insufficiency, transport-profile mobility, and affine-window collision remain valid. Its former `P_transport` is renamed `P_naive_conjugated_profile`; rotating-coordinate interpretation is superseded. Corrected object is `P_covariant`.

Coley–McNutt–Milson 2012, DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Chosen rotating screen, detector phase variables, endpoint angular velocities, window/kernel, affine nuisance law, UMCH, `ell0`, and detection are not established by the source.

Physical tetrads, Fermi/parallel transport, causal paths/windows, displacement/derivative calibration, and common detector standards remain open. This is not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
