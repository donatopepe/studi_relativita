# Continuous screen histories and local gauge quotient in an exact plane wave

Classification: `EXACT_SPACETIME_CONTINUOUS_SCREEN_READOUT_QUOTIENT_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_CONTINUOUS_CANONICAL_SCREEN_HISTORY_LOCAL_GAUGE_EQUIVALENT_RAW_VELOCITY_HISTORY_CALIBRATION_DEPENDENT_NOT_ELL0`.

Open gate: `PHYSICAL_CONTINUOUS_TETRAD_READOUT_LOCAL_SCREEN_GAUGE_CAUSAL_SAMPLING_AND_ELL0_LAW_NOT_DERIVED`.

## Sampled raw histories

Retain `K,omega_i,Q_i,A_i,P_inertial(u),P_canonical_i(u),P_velocity_i(u),G_21(u),L` at thirteen preregistered affine samples. The two prescribed rotating screens have the same source/observer basis and angular rate but distinct interiors.

For the inertial partial map `P_I(u,u_s)` and `C_i(u)=diag(Q_i(u),Q_i(u))`,

`P_c,i(u,u_s)=C_i(u)^-1 P_I(u,u_s) C_i(u_s)`.

Raw intermediate canonical histories differ by as much as `0.06888558039493263`; raw velocity histories differ by `0.18058782579069355`. At the observer, canonical difference is zero and velocity difference is `3.4631051129946596e-14`.

## Local quotient counterexample

Define

`G_21(u)=C_2(u)^-1 C_1(u)`.

Then

`P_c,2(u)=G_21(u) P_c,1(u) G_21(u_s)^-1`.

The maximum sampled residual is `5.098567434843205e-16`. Reconstructing

`P_I(u)=C_i(u) P_c,i(u) C_i(u_s)^-1`

from either screen gives maximum difference `6.397467560108161e-16`. Equal screen paths collapse all raw-history differences exactly at reported precision.

Thus continuous coordinate histories do not automatically add independent geometric rank when arbitrary local screen gauge is quotiented. They become physical only if a detector fixes or records the internal tetrad/readout standard. This is a negative identifiability result for the declared project nuisance, not a universal observational no-go.

Velocity histories additionally depend on local `A_i(u)` and endpoint rate calibration. Their ordinary spectra are not promoted to canonical invariants.

## Orientation, scaling and caustics

Common `SO(2)` history covariance and `O(2)` signed-component reversal are tested. Under `K_s(u)=s^-2 K(u/s)`, `omega_s(u)=s^-1 omega(u/s)`, `L_s=sL`, rate states require the phase-unit similarity `D=diag(I,I/s)`; maximum residual is `2.8053161131044195e-14` for `s=1.47`. Absolute affine scale and `ell0` remain unidentified.

Full phase maps remain defined through conjugate points. Sachs graphs require separate block-invertibility gates; no singularity is interpreted as `ell0`.

## Source scope and disposition

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish continuous detector readout, local screen-gauge quotient, tetrad calibration, causal sampling/kernel, affine nuisance, `ell0`, UMCH or detection.

UMCH remains `UNPROVEN`; no `ell0` is identified and there is `NO_POSITIVE_DETECTION_CLAIM`. Structural dead end is `NOT_DECLARED` because detector-fixed tetrads, local readout actions, causal sampling, physical transport, holonomy paths and other exact geometries remain open.
