# Schwarzschild photon-sphere optical Jacobi/Sachs control

## Status and bounded question

This specification is an autonomous bounded continuation of the ratified operator-valued UMCH research route. It does not change the hypothesis contract. UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: for the future null circular geodesic at `r=3M`, does the connection-derived screen Jacobi phase map contain nonradial finite-window structure beyond the closed-loop holonomy already audited, and does that structure identify an absolute scale or `ell0` after affine, endpoint, orientation and screen nuisances are exposed?

Classification:

- Schwarzschild photon sphere and null circular geodesic: `KNOWN_RESULT` within the verified scope of `Darwin1959GravityField`;
- null screen/Jacobi/Sachs framework: `KNOWN_RESULT` within the limited verified scope of `Sachs1961`;
- the declared affine normalization, screen quotient, finite-window phase map, caustic controls and nuisance tests: `PROJECT_DERIVATION`;
- vertex and non-vertex boundary preparations: `TOY_CONTROL`;
- scale, quotient and identifiability conclusions: `NEGATIVE_RESULT` unless the tests falsify them.

No source is allowed to establish the project-specific boundary, detector action, covariance, `ell0`, UMCH or detection.

## Alternatives and selected design

Three continuations were considered. Generic nonradial scattering would add turning-point and capture/scatter branches plus endpoint solves before the screen observable is controlled. Freely falling endpoints would attack static-frame acceleration but still leave emitter/absorber action and vector readout underived. The selected minimal continuation is therefore the circular photon-sphere optical bundle: it is exact, nonradial, connection-derived and counterexample-rich.

Use the equatorial future null tangent normalized in the local static tetrad by

`k = e_0 + orientation*e_3`,

so `lambda` has length units, `dphi/dlambda=orientation/(3M)`, and one winding has affine length `L=6*pi*M`. This normalization is explicitly a project anchor, not detector-derived. The screen is the quotient orthogonal to `k` modulo `k`, represented initially by radial and polar classes. The induced screen transport is fixed before interpreting matrix entries. Orientation, affine scale, endpoint basis and parity remain nuisance controls.

The primary object is the full canonical screen phase map

`P(L)=[[A,B],[C,D]]`,

not a scalar expansion, determinant, trace, eigenvalue or Lyapunov exponent. Derived graph objects are emitted only where their required blocks are invertible.

## Exact optical system and raw contract

In the declared parallel screen quotient, compute the optical tidal matrix directly from the four-dimensional Schwarzschild Riemann tensor and the normalized null tangent. Test it against an independent finite-difference connection/Jacobi calculation. With project sign conventions fixed by the implementation tests, the two eigenchannels must be tracefree and have equal magnitude `3M/r^3=1/(9M^2)` at `r=3M`; one is hyperbolic and one oscillatory. The implementation must not assume the final sign ordering without the independent check.

Propagate

`d/dlambda (X,V)^T = [[0,I],[K,0]] (X,V)^T`

by an exact constant-generator exponential and independently by deterministic numerical integration. Preserve raw:

`M,r_ph,orientation,winding,affine_normalization,k_tetrad,screen_classes,screen_metric,screen_transport,optical_tidal_K,L,A,B,C,D,P_phase,characteristic_coefficients,spectrum_or_surrogate,vertex_X,vertex_V,nonvertex_S0,nonvertex_X,nonvertex_V,S_vertex,S_nonvertex,caustic_flags,conjugate_locations,orientation_controls,endpoint_quotient_controls,affine_scale_controls,geometric_scale_controls,holonomy_cross_map,Jacobian_joint,scale_factor,scale_orbit`.

`S_vertex=V X^-1` and `S_nonvertex=V X^-1` are conditional diagnostics. A singular `X` yields `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`; the full phase map remains primary and must not be discarded.

## Counterexample-first controls

The strongest expected counterexample is an endpoint caustic in the oscillatory channel. Under the stated normalization, `sqrt(|K|) L=2*pi`; therefore the vertex `B` block is expected to be singular at a complete winding even though the full symplectic phase map remains finite and invertible. The code must locate intermediate conjugate points, test both sides of each point and prohibit a Sachs graph claim at the singular endpoint.

Additional controls:

1. zero-window limit gives identity phase map and the correct first generator derivative;
2. exact and numerical phase maps agree and satisfy the symplectic condition;
3. orientation reversal changes only data justified by the oriented screen/path convention; any spectral collision is retained;
4. independent endpoint screen rotations act as `P -> G_o P G_s^-1`; unrestricted endpoint calibration can remove raw entry labels and must not be represented as new physics;
5. affine reparameterization `lambda -> a lambda`, `k -> k/a`, `K -> K/a^2` acts with the phase-rate conversion `D_a=diag(I,I/a)` and preserves dimensionless phase content;
6. Schwarzschild scaling `(M,r,L)->s(M,r,L)` preserves the dimensionless phase map after rate conversion while changing dimensional lengths;
7. the photon-orbit holonomy and optical phase map share the same geometry/path and are not independent channels without a detector covariance/readout model;
8. no continuous `Jacobian_joint` is inferred from discrete winding.

## Deterministic artifact, reports and gates

Add one deterministic Python study, canonical JSON artifact, focused scientific tests, source-scope tests, theory note, and semantically aligned English/Italian audit reports. Floating output must use canonical serialization stable across supported Python versions. Existing bibliography entries are reused unless metadata verification demonstrates that an additional canonical source is necessary.

Expected bounded status if the controls pass:

`SCHWARZSCHILD_PHOTON_SPHERE_OPTICAL_PHASE_MAP_HYPERBOLIC_ELLIPTIC_VERTEX_CAUSTIC_AFFINE_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Expected scope:

`FOUR_DIMENSIONAL_SCHWARZSCHILD_NULL_SCREEN_JACOBI_PHASE_MAP_ON_FUTURE_PHOTON_SPHERE_WITH_PROJECT_AFFINE_NORMALIZATION_TOY_BOUNDARIES_AND_NO_DETECTOR_READOUT`.

Expected gate:

`PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Passing tests yields at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. It does not identify `ell0`, establish channel independence, provide a detector, or justify structural-dead-end or reformulation status.
