# Connection-path cross-channel quotient in an exact plane wave

Classification: `EXACT_SPACETIME_CONNECTION_PATH_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_INTERNAL_SCREEN_CONNECTION_PATH_MOVES_TRANSPORTED_WINDOW_NOT_COVARIANT_ENDPOINT_MAPS_CROSS_CHANNEL_RANK_NOT_AUTOMATIC_NOT_ELL0`.

Open gate: `PHYSICAL_CONTINUOUS_SCREEN_READOUT_PATH_KERNEL_ENDPOINT_TETRADS_AND_ELL0_LAW_NOT_DERIVED`.

## Endpoint-matched path counterexample

Retain raw `K,omega_1,omega_2,Q_1,Q_2,A_1,A_2,W_1,W_2,P_inertial,P_canonical,P_velocity,R,S_rot,S_0,L`. Two smooth prescribed screen connections have equal source/observer bases and angular rates but distinct internal paths. Their maximum internal basis difference is `0.04595991799966836`.

The transported top-hat tidal windows

`W_i=(1/L) int Q_i^T K Q_i du`

differ by `0.015157779434373101`. Naive propagation using only the conjugated profile differs by `0.017400310040274355`.

The correct canonical endpoint graph

`P_c,i=C_o^-1 P_inertial C_s`, `C=diag(Q,Q)`,

depends on this prescribed coordinate history only through endpoint bases. Because both paths share `Q_s,Q_o`, their canonical map difference is exactly zero at reported precision. Since `A_s,A_o` also agree,

`P_v,i=H(A_o)^-1 P_c,i H(A_s)`

also collides. Non-vertex canonical and velocity Sachs endpoint graphs `R` and `S_rot=R-A_o` likewise have zero difference away from caustics.

Thus internal prescribed screen-path sensitivity can appear in the transported-window channel while vanishing from covariant endpoint channels. It does not automatically supply independent cross-channel rank. Conversely this is not a universal dismissal of continuous screen information: a detector-derived path/readout could make internal samples observable and restrict the quotient.

## Covariance, scale and limits

Common `SO(2)` covariance residuals for window and canonical map are below `3e-14`; `O(2)` reflection flips the signed off-diagonal oriented component. Under `K_s=s^-2 K(u/s)`, `omega_s=s^-1 omega(u/s)`, `S_0s=S_0/s`, `L_s=sL`, `s=1.47`, the maximum dimensionless residual is `3.95516952522712e-16`. Absolute affine scale and `ell0` remain unidentified. Singular `X` triggers `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`.

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation, not prescribed screen paths, finite windows, detector calibration, cross-channel independence, `ell0`, UMCH or detection.

This is not a structural dead end. Physical continuous screen readout, tetrads, causal kernel/support, path transport, endpoint calibration and other exact geometries remain open. UMCH is `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
