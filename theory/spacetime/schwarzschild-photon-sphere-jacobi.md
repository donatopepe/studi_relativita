# Schwarzschild photon-sphere optical Jacobi phase map

## Scope

This is an exact bounded control, not a detector model or UMCH evidence.

`classification=EXACT_NONRADIAL_NULL_SCREEN_JACOBI_PHASE_MAP_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

`scope=FOUR_DIMENSIONAL_SCHWARZSCHILD_NULL_SCREEN_JACOBI_PHASE_MAP_ON_FUTURE_PHOTON_SPHERE_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_BOUNDARIES_AND_NO_DETECTOR_READOUT`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

UMCH remains `UNPROVEN`; result remains `NO_POSITIVE_DETECTION_CLAIM`, `ell0_identified=false`, `structural_dead_end=NOT_DECLARED`, and at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Connection-derived optical system

At `r_ph=3M`, choose `STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR`. Thus the affine winding length is `L=6*pi*M`. This frequency/affine choice is a project anchor, not detector-derived.

Project the four-dimensional Schwarzschild Riemann tensor onto radial and polar screen classes. With the code convention `X''=K X`,

`K=diag(1/(9M^2),-1/(9M^2))`.

The original control used a radial finite difference of the four-dimensional connection for the radial projection and vacuum tracefreeness for the second eigenchannel. A later independent full-Riemann audit, with both `r` and `theta` derivatives, computes both channels directly and confirms this matrix: in explicit `(polar,radial)` order it is `diag(-1,+1)/(9M^2)`. At `M=1`, the full-Riemann fine mismatch is `2.308480787357262e-09`. See `schwarzschild-photon-sphere-riemann-conformance.md`.

The primary object is

`P_phase=exp([[0,I],[K,0]] L)=[[A,B],[C,D]]`.

It is symplectic and retains hyperbolic plus elliptic evolution. `characteristic_coefficients=[1.0,-537.493523,1072.987046,-537.493523,1.0]` are a quotient diagnostic, not a substitute for `P_phase`.

## Boundary and caustic counterexample

Vertex data use `X(0)=0,V(0)=I`. The oscillatory channel reaches conjugate locations `lambda=3*pi*M` and `6*pi*M`; after one winding `abs(det B)=2.140247132e-12`. Therefore `S_vertex=V X^-1` is correctly gated as `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`. Full `P_phase` remains finite and invertible: caustic does not destroy phase-space transport.

Nonvertex toy data `X(0)=I,V(0)=S0` produce a regular endpoint graph in the declared case. This difference is boundary dependence, not a second independent curvature channel.

## Quotients and scale orbits

Independent endpoint screen bases act as `P -> G_o P G_s^-1`; raw entries change while the action is exactly reversible. Circular orientation reversal is invisible in this diagonal parallel-screen control. This is a stronger negative result than an expected raw orientation signal and must be preserved.

Under affine reparameterization, rate variables require `D_a=diag(I,I/a)`. Under Schwarzschild scaling `(M,r_ph,L)->s(M,r_ph,L)`, the same rate conversion preserves dimensionless phase content while dimensional length changes. Neither orbit identifies `ell0`.

`H_photon` and `P_phase` share geometry and path. Without detector readout and covariance they are not independent channels. Winding remains `DISCRETE_PROTOCOL_LABEL`; `Jacobian_joint=NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN`.

## Source scope

`Darwin1959GravityField` supports Schwarzschild trajectories and critical circular-orbit context. `Sachs1961` supports null-radiation/optical context. Neither derives project affine normalization, endpoint screen, finite-window phase map, caustic readout, detector, covariance, `ell0`, UMCH, evidence, or detection.
