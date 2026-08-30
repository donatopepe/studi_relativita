# Schwarzschild photon-sphere Jacobi audit — English

## Decision

`classification=EXACT_NONRADIAL_NULL_SCREEN_JACOBI_PHASE_MAP_AND_NEGATIVE_SCALE_IDENTIFIABILITY_CONTROL`

`status=SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

`scope=FOUR_DIMENSIONAL_SCHWARZSCHILD_NULL_SCREEN_JACOBI_PHASE_MAP_ON_FUTURE_PHOTON_SPHERE_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_BOUNDARIES_AND_NO_DETECTOR_READOUT`

`gate=PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`

UMCH is `UNPROVEN`. Detection state is `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`. Passing this audit means at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Exact and numerical controls

The project normalization is `STATIC_TETRAD_K_EQUALS_E0_PLUS_ORIENTATION_E3_PROJECT_ANCHOR`. For `M=1`, `r_ph=3`, `L=18.84955592`; null residual is `2.220446049e-16` and geodesic residual is `2.775557562e-17`.

Four-dimensional connection curvature gives `K=diag(0.1111111111,-0.1111111111)` in the original `(radial,polar)` order and declared `X''=KX` convention. The original radial finite-difference residual is `1.23788757e-11`; screen trace is zero. A later full-Riemann audit computes both channels using `r` and `theta` derivatives and confirms `diag(-1,+1)/(9M^2)` in explicit `(polar,radial)` order with fine mismatch `2.308480787357262e-09`; it also resolves the apparent factor-three scattering conflict by affine-frequency conversion. Exact/numerical phase-map residual is `3.070206877e-12`; symplectic residual is `2.057951833e-11`.

Raw `P_phase=[[A,B],[C,D]]` is primary. Characteristic coefficients and spectrum surrogate are quotient diagnostics only.

## Counterexamples and limitations

Vertex boundary has conjugate locations `9.424777961` and `18.84955592`; endpoint `abs(det B)=2.140247132e-12`. Hence `S_vertex` is `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`, while full phase map remains finite/invertible. Nonvertex toy preparation remains regular: boundary choice matters.

Circular orientation reversal is raw-invisible in this diagonal parallel-screen control. Endpoint screen rotations change raw entries. Affine rate conversion and Schwarzschild scale orbit preserve dimensionless phase content while dimensional length changes. No `ell0` follows.

Holonomy and Jacobi phase map share path and geometry: no independent channel without detector covariance/readout. Winding is `DISCRETE_PROTOCOL_LABEL`; `Jacobian_joint=NOT_APPLICABLE_DISCRETE_WINDING_NO_CONTINUOUS_JACOBIAN`.

Missing: physical source/observer endpoint screen preparation, affine-frequency standard, caustic continuation, oriented tetrad, vector readout, detector action, covariance, calibration, `ell0` law, evidence and detection protocol.

## Classification and sources

Photon sphere: known result. Connection projection and phase map: project derivation. Vertex/nonvertex boundaries: toy controls. Caustic, quotient and scale blindness: negative results. Physical readout: open problem.

`Darwin1959GravityField` supports Schwarzschild trajectory and critical circular-orbit context. `Sachs1961` supports null optical context. Neither source establishes endpoint screens, affine normalization, finite-window map, caustic readout, detector, covariance, `ell0`, UMCH, evidence, or detection.

## Direct conformance review

Review was performed directly because explicit project policy forbids subagents for this task. Spec/raw-key alignment, sign convention, both independently finite-differenced Riemann screen projections, full-map primacy, graph invertibility gates, endpoint action, affine/geometric conversions, source scope and bilingual machine labels were checked. No positive claim or structural-dead-end trigger was found.
