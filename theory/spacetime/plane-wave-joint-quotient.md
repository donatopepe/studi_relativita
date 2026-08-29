# Exact plane-wave joint endpoint-frame quotient

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_JOINT_QUOTIENT_REVERSAL_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

Use the same smooth, real, symmetric optical profile `K(u)` of the exact vacuum Brinkmann plane-wave control, a centered affine interval, parallel screen, and vertex boundary conditions. The joint raw record is

`W(L)=int_{-L/2}^{L/2} K(u) du`,

`B(L)=D(L/2)`, with `D''+K D=0`, `D(-L/2)=0`, `D'(-L/2)=I`.

For profile reversal `K_rev(u)=K(-u)`, centered integration gives `W_rev=W`. Continuous symmetric-profile reciprocity gives `B_rev=B^T`. The asymmetric rotating profile has `raw B_rev != raw B`, so unquotiented Jacobi propagation retains order. However, eigenvalues of symmetric `W`, and singular values, determinant and Frobenius norm of `B`, are unchanged. Moreover `B` and `B^T` lie in the same orbit under independent source/observer endpoint rotations. Thus the minimal individual endpoint-frame quotient of `(W,B)` is profile-reversal blind.

A separate exact nuisance remains: `L2=s L1`, `K2(u)=K1(u/s)/s^2` preserves spectra of `L W` and singular values of `B/L`. Hence absolute affine support scale is not recovered without independently fixed profile and affine normalization.

This does not prove failure of all joint invariants. A common anchored frame could preserve cross-orientation information, but requires physical source/observer anchors, handedness, transport path and calibration beyond the metric/profile declaration. This route remains `COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN` and is not evidence. No `ell0` enters either degeneracy. Result is not a structural dead end and supplies no mechanism, data result or detection.
