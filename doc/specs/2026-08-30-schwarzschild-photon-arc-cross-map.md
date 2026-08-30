# Schwarzschild photon-sphere finite-arc holonomy/Jacobi cross-map

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: along a future equatorial null **finite arc** on the Schwarzschild photon sphere, does the joint raw connection transport and optical Jacobi phase map provide more than one physically calibrated continuous shape direction, or do both channels collapse onto the same dimensionless arc parameter once affine, endpoint and Schwarzschild scale nuisances are exposed?

Classifications:

- Schwarzschild photon sphere and circular null trajectory: `KNOWN_RESULT` within the bounded scope of `Darwin1959GravityField`;
- null optical/Jacobi framework: `KNOWN_RESULT` within the bounded scope of `Sachs1961`;
- finite-arc connection transport, optical phase map, endpoint quotient and joint-rank audit: `PROJECT_DERIVATION`;
- declared static-tetrad affine normalization and endpoint bases: `TOY_CONTROL` / project anchors;
- rank loss, collisions and scale blindness: `NEGATIVE_RESULT` if tests pass;
- physical emitter/observer action, endpoint tetrads, frequency standard, vector readout, covariance and `ell0` law: `OPEN_PROBLEM`.

No source may be used to support detector calibration, endpoint preparation, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

Three next controls were considered.

1. **Generic nonradial scattering/echo.** Strongest geometric generalization, but radial turning points, capture/scatter branch matching, asymptotic endpoint calibration and numerical elliptic structure would be introduced simultaneously. This risks attributing branch or endpoint effects to operator shape.
2. **Freely falling endpoints.** Removes the static closure acceleration used in the closed photon-orbit loop, but emitter/absorber action and vector readout remain underived and would dominate interpretation.
3. **Finite photon-sphere arc cross-map — selected.** Keeps exact constant generators and the already checked screen curvature while opening the window continuously. It directly tests finite-window shape, endpoint actions, caustic landmarks, cross-channel rank and scale reparameterization before adding scattering complexity.

The selected control is minimal, exact and counterexample-first. Generic scattering and freely falling endpoints remain open routes, so no structural dead end is declared.

## Geometry and finite-window parameter

Fix `M>0`, `r_ph=3M`, orientation `epsilon in {-1,+1}`, and a positive arc angle `alpha`. Use the project affine anchor

`k = e_0 + epsilon e_3`,

so

`dphi/dlambda = epsilon/(3M)`,

`L(alpha)=3M alpha`,

`Delta t(alpha)=3 sqrt(3) M alpha`.

`alpha` is a dimensionless protocol/window parameter, not `ell/ell0`. The primary family is continuous for `alpha>=0`; integer winding is only the subset `alpha=2*pi*n` and remains a discrete protocol label there.

The null arc is open unless `alpha=2*pi*n`. Therefore no artificial past-directed static closure is included in the primary object. Any comparison with the closed-loop photon holonomy must be labelled a derived endpoint/closure comparison, not an equality of channels.

## Raw channel-native objects

### Connection channel

Let `T_arc(alpha)` be Levi-Civita parallel transport along the future null arc, represented between declared static tetrads at source and observer. It is an endpoint map, not a closed holonomy. Preserve:

- coordinate generator and transport;
- source/observer tetrads;
- raw tetrad map `T_arc`;
- Lorentz residual;
- characteristic coefficients/spectrum surrogate;
- orientation-reversed map;
- endpoint-action controls.

### Optical channel

With the screen classes and sign convention already independently checked in the one-winding control,

`K=diag(1/(9M^2),-1/(9M^2))`, `X''=KX`.

The primary optical object is

`P_arc(alpha)=exp([[0,I],[K,0]] L(alpha))=[[A,B],[C,D]]`.

Preserve the full `4x4` phase map through all caustics. Vertex and nonvertex Sachs graphs are derived only when their required `X` block is invertible.

## Counterexample-first tests

### 1. Zero-window and local generator

At `alpha=0`, both raw maps must be identity in their declared endpoint trivializations. Finite differences at zero must recover their independent connection/phase generators. This prevents a nonzero intercept from being misread as curvature response.

### 2. Finite-window composition

For constant circular generators and endpoint-matched tetrads,

`T_arc(alpha+beta)=T_arc(beta) T_arc(alpha)`

with the declared ordering, and likewise

`P_arc(alpha+beta)=P_arc(beta) P_arc(alpha)`.

This semigroup property is an exact-geometry control, not evidence of channel independence.

### 3. Caustic landmarks

The oscillatory optical channel has

`sqrt(|K|) L = alpha`.

Vertex conjugate points occur at `alpha=n*pi`. At those windows `B` is singular but `P_arc` remains finite and invertible. The first landmark `alpha=pi` and full-winding landmark `alpha=2*pi` are dimensionless orbit/caustic landmarks tied to `r_ph=3M`; neither is an `ell0` landmark.

### 4. Orientation and endpoint quotient

Raw orientation reversal may change `T_arc` and endpoint labels while leaving characteristic data or a common-conjugacy quotient unchanged. For the diagonal parallel-screen optical map, orientation may collide exactly. Apply independent declared endpoint Lorentz/tetrad actions to `T_arc` and `SO(2)` phase-space screen actions to `P_arc`; raw entries are not calibration invariants.

### 5. Schwarzschild and affine scaling

Under

`(M,r_ph,L,Delta t) -> s(M,r_ph,L,Delta t)`

at fixed `alpha`, convert phase rates using `D_s=diag(I,I/s)`. Test that dimensionless content of `T_arc` and `P_arc` is unchanged while dimensional durations and affine lengths change.

Under affine reparameterization by `a`, use the corresponding `D_a=diag(I,I/a)` rate conversion. Affine blindness and Schwarzschild geometric-scale blindness are separate controls.

### 6. Joint cross-channel rank

Build a deterministic feature map only as a **derived diagnostic**, while preserving both raw maps:

`z(alpha,M)=(chi_T(T_arc), chi_P(P_arc))`,

where `chi_T` and `chi_P` are preregistered characteristic-coefficient vectors or fixed matrix invariants. Evaluate a finite-difference Jacobian with respect to `(alpha, log M)` after required rate conversions.

Expected strongest counterexample: the scale column vanishes while the arc column does not, so joint dimensionless rank is one. Multiple nonconstant entries and two raw operator maps do not create two physical parameter directions. Repeat with raw fixed-anchor entries to show any apparent scale rank is removed by the declared endpoint/rate conversion.

Also test collisions across `alpha`, especially periodic optical components versus nonperiodic hyperbolic components and connection quotients. Local rank one does not imply global injectivity; global injectivity, if observed on a bounded interval, does not supply an absolute scale.

### 7. Closed-loop cross-check

At `alpha=2*pi`, compare the future-null arc transport with the null segment used by the existing photon-orbit study. Keep the prior past-directed static closure separate. Verify that composing the same closure reproduces `H_photon` within numerical tolerance. This checks provenance and ordering without counting open transport, closure and optical map as independent observations.

## Deterministic numerical controls

Implement exact constant-generator maps and independent fixed-step RK4 propagation. Require:

- null/geodesic residual controls;
- Lorentz and symplectic residuals;
- exact/numerical agreement at several preregistered arc angles including `0`, `pi/3`, `pi`, `3*pi/2`, `2*pi`;
- semigroup residuals for nontrivial `alpha,beta`;
- finite-difference step convergence for the joint Jacobian;
- cross-version canonical JSON under Python 3.12 and local repository runner.

The local baseline runner is `python3 -m unittest`; `/usr/bin/python3 -m pytest` remains unavailable and its prior `No module named pytest` observation is preserved as an environment fact, not a scientific failure.

## Raw artifact contract

The canonical artifact must retain at least:

`M,r_ph,alpha,orientation,affine_normalization,k_tetrad,L,Delta_t,connection_generator,T_arc,connection_characteristic_coefficients,connection_spectrum_or_surrogate,screen_classes,screen_metric,screen_transport,optical_tidal_K,phase_generator,A,B,C,D,P_arc,phase_characteristic_coefficients,phase_spectrum_or_surrogate,vertex_X,vertex_V,S_vertex,nonvertex_S0,nonvertex_X,nonvertex_V,S_nonvertex,caustic_flags,conjugate_angles,zero_window_controls,composition_controls,orientation_controls,endpoint_quotient_controls,affine_scale_controls,geometric_scale_controls,joint_feature_map,Jacobian_joint,singular_values_joint,rank_joint,scale_null_direction,collision_controls,closed_loop_cross_check,scale_factor,scale_orbit`.

Scalar invariants and Jacobians remain derived diagnostics. `T_arc` and `P_arc` remain primary.

## Expected bounded state

If the preregistered counterexamples pass:

`SCHWARZSCHILD_PHOTON_SPHERE_FINITE_ARC_CONNECTION_JACOBI_CROSS_MAP_CAUSTIC_LANDMARKED_LOCALLY_ONE_SHAPE_DIRECTION_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Scope:

`FOUR_DIMENSIONAL_SCHWARZSCHILD_FUTURE_NULL_PHOTON_SPHERE_FINITE_ARC_CONNECTION_AND_SCREEN_PHASE_MAP_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_ENDPOINT_BASES_AND_NO_DETECTOR_READOUT`.

Gate:

`PHYSICAL_FINITE_ARC_WINDOW_SELECTION_SOURCE_OBSERVER_TETRADS_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Passing gives at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Stop conditions

Stop rather than overclaim if:

- endpoint actions or affine-rate conversions are not explicit;
- either raw map is replaced by scalar diagnostics;
- graph objects are evaluated through singular blocks;
- open arc transport is called holonomy without closure;
- rank depends on uncalibrated raw entries or arbitrary feature rescaling;
- source scope is widened beyond verified content;
- bilingual labels, values or limitations diverge;
- `alpha`, `M`, a caustic angle or photon-sphere radius is relabelled as `ell0`.

No structural-dead-end criterion currently passes. Generic scattering, freely falling endpoints and physical detector/readout derivation remain bounded open alternatives. No `REFORMULATION_CANDIDATE_UNRATIFIED` is created; loop `16588751` remains active.
