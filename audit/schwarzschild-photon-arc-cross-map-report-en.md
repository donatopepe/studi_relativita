# Audit — Schwarzschild photon-sphere finite-arc cross-map

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_CONNECTION_JACOBI_CROSS_MAP_CAUSTIC_LANDMARKED_LOCALLY_ONE_SHAPE_DIRECTION_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_CONNECTION_AND_SCREEN_PHASE_MAP_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_ENDPOINT_BASES_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_FINITE_ARC_WINDOW_SELECTION_SOURCE_OBSERVER_TETRADS_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Contract: `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`; at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Audited result

Project affine anchor: `k=e_0+epsilon e_3`. Geometry: `r_ph=3M`, `L=3M alpha`, `Delta t=3 sqrt(3) M alpha`. Main artifact uses `M=1`, `alpha=pi/3`, hence `L=pi`; null residual is `2.220446049250313e-16` and geodesic residual `2.7755575615628914e-17`.

Primary objects remain raw `T_arc` and full `P_arc=[[A,B],[C,D]]`. The connection object is `OPEN_ARC_ENDPOINT_TRANSPORT_NOT_HOLONOMY`. Characteristic coefficients, graph blocks and rank are diagnostics only.

Exact/numerical residuals at the main arc are `8.973730906160965e-14` for connection transport and `5.556515941082763e-14` for optical RK4. Lorentz and symplectic residuals are `4.775249788392736e-16` and `2.5829094694428234e-15`; phase determinant is `1.0000000000000004`. Semigroup residuals are below `6e-15`.

Vertex caustics occur at `alpha=pi` and `alpha=2*pi`. At each, the vertex graph reports `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`, while full `P_arc` stays finite/invertible. Nonvertex toy boundary remains regular. Caustic behavior is a domain gate, not evidence.

Orientation changes raw connection entries, while characteristic data collide; diagonal optical propagation collides under orientation reversal. Endpoint actions change raw entries. Without physical endpoint tetrads, handedness and screen calibration, those entries are not detector invariants.

Affine-factor control `1.7` gives converted phase residual `9.459807063569745e-15`. Geometric factor `2.4` gives connection and converted-phase residuals `4.685680459230494e-16` and `1.4001608167315755e-14`, while affine length changes by `4.3982297150257095` and coordinate duration by `7.617957329783713`. Affine and geometric blindness are separate exact nuisances.

For parameters `(alpha,log_M)`, derived cross-channel `rank_joint=1`; scale-column norm is below `8e-11`, step convergence below `2e-9`, and `independent_channels=false`. This says only that this exact shared-geometry family has one calibrated local shape direction. It does not prove global injectivity, statistical independence, detector identifiability or an absolute scale.

The elliptic phase subblock collides under `alpha->alpha+2*pi`, but full hyperbolic/phase and joint features do not collide in the tested pair. At `alpha=2*pi`, future-null transport matches the prior photon segment exactly; adding the prior closure matches its holonomy within `6.2e-14`. Closure is `DERIVED_PAST_DIRECTED_STATIC_CLOSURE_CROSS_CHECK_ONLY`, not another independent channel.

## Sources and limitations

`Darwin1959GravityField` supports Schwarzschild trajectory and critical circular-orbit context only. `Sachs1961` supports null optical framework only. Neither supports open-arc transport, finite-window selection, endpoint tetrads, project affine frequency standard, screen preparation, caustic continuation, vector readout, detector, covariance, `ell0`, UMCH, evidence or detection.

No real data, detector response, covariance, emitter/observer calibration, absolute standard, `ell0` law, bound, replication or detection was introduced.

Generic scattering and freely falling endpoints remain open bounded routes. Physical vector readout and covariance remain blockers. Therefore no structural dead end and no reformulation candidate are declared.

## Direct review exception

User explicitly prohibited subagent use. Direct review replaced subagent closure review: spec, plan, implementation, canonical artifact, theory, English report and Italian report were compared in-session. This process exception does not weaken scientific gates and creates no evidence.
