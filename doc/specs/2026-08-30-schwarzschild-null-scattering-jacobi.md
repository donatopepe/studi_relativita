# Schwarzschild finite-boundary null-scattering Jacobi gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; `ell0_identified=false`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: along the already preregistered future equatorial Schwarzschild null ray with finite static endpoints, one turning point, `R>rho>3`, unit Killing-energy project normalization and explicit incoming/outgoing matching, does the full transported-screen Jacobi phase map add an interior geometric scale direction after affine and endpoint conversions, or does Schwarzschild dilation preserve its dimensionless content?

Classifications:

- Schwarzschild exterior geometry, null first integrals and geodesic deviation/Sachs framework: `KNOWN_RESULT` within cited source scope;
- numerical screen construction, Levi-Civita screen transport, optical tidal projection, full phase-map integration, reciprocity/symplectic checks and rank audit: `PROJECT_DERIVATION`;
- static endpoint tetrads, unit Killing energy, vertex/parallel source preparations and endpoint screen actions: `TOY_CONTROL` / project anchors;
- affine or geometric scale blindness, graph failure at caustics, rank loss and projection collisions: `NEGATIVE_RESULT` if tests pass;
- physical emitter/absorber tetrads, source profile, absolute frequency standard, detector vector readout, covariance and an `ell0` law: `OPEN_PROBLEM`.

No cited source establishes this finite-boundary protocol, endpoint calibration, detector, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Scalar Sachs expansion/shear only.** Rejected as primary: graph variables can fail at caustics and discard phase-space information.
2. **Coordinate finite-difference bundle.** Useful independent check but mixes endpoint coordinate calibration with the optical map. Deferred as a secondary cross-check.
3. **Full transported-screen phase map.** Selected. It preserves the primary `4x4` map through caustics and exposes screen, affine and endpoint actions explicitly.

Autonomous loop authorization ratifies this bounded conservative design. No structural-dead-end or reformulation decision is made here.

## Geometry, path and normalization

Use the path and turning regularization from `schwarzschild_null_scattering_scale_gate.py`:

\[
 r/M=\rho+y^2,\qquad
 \beta=b/M=\frac{\rho}{\sqrt{1-2/\rho}},\qquad R>\rho>3.
\]

The ordered path is incoming boundary to turning point to outgoing boundary. Preserve branch labels and path samples. Critical `rho=3`, capture, multiple winding, infinity limits and horizon crossing remain out of scope.

Affine anchor:

\[
 E_\infty=-k_t=1,
\]

is a project normalization, not a detector-derived frequency standard. For an affine rescaling `k -> a k`, compare phase rates using

\[
 D_a=\operatorname{diag}(I_2,I_2/a).
\]

Test affine normalization separately from geometric dilation.

## Screen and optical tidal matrix

At each path sample construct the static orthonormal tetrad. Let `e_2` be the polar screen vector. Construct the second screen vector in the local radial-azimuthal plane, orthogonal to the local null direction and static observer; fix its sign prospectively at the incoming endpoint and propagate continuously. Record handedness and orthonormality residuals.

Parallel transport the screen along the same ordered null path with Levi-Civita transport, reproject only to control numerical drift, and record transport/reprojection residuals. A mathematical screen trivialization is not physical endpoint calibration.

Project the Riemann tensor:

\[
 \mathcal K_{AB}(\lambda)=-R_{\mu\nu\rho\sigma}
 e_A^\mu k^\nu e_B^\rho k^\sigma,
\]

with the sign convention fixed by the implemented equation

\[
 X''=\mathcal K X.
\]

Record full `2x2` `K` at every retained sample, symmetry residual, vacuum trace residual, endpoint/turning values and independent finite-difference convergence checkpoints. Do not infer generic projections from the equatorial-only connection helper without theta derivatives.

## Primary phase map

Integrate

\[
 \frac{d}{d\lambda}
 \begin{pmatrix}X\\V\end{pmatrix}
 =
 \begin{pmatrix}0&I_2\\\mathcal K&0\end{pmatrix}
 \begin{pmatrix}X\\V\end{pmatrix},
 \qquad P(\lambda_s)=I_4.
\]

Primary raw object:

\[
 P=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]

Preserve ordered profile samples and checkpoint phase maps. Test convergence, identity at zero window, composition across the turning point, reverse propagation, and symplectic residual. The full map remains primary across caustics.

Derived graph objects such as `S=DB^{-1}` are emitted only where the required block is invertible. Caustics are landmarked by bounded sign/bracket or singular-value checks; no unsupported global caustic count.

## Boundary preparations and endpoint actions

Evaluate at least:

- **vertex preparation:** `X_s=0`, `V_s=I` (the `B,D` columns);
- **parallel preparation:** `X_s=I`, `V_s=0` (the `A,C` columns).

These are mathematical source preparations, not physical source models.

For oriented endpoint screen actions `Q_s,Q_o in O(2)`, use phase actions `G=diag(Q,Q)` and verify

\[
 P' = G_o^{-1} P G_s.
\]

Preserve raw changes and quotient/reconstruction residuals. Handedness/parity labels remain protocol labels unless physically calibrated.

## Counterexample-first controls

Required controls:

1. domain, turning relation and branch matching;
2. screen orthonormality, handedness and transport continuity;
3. optical-tidal symmetry, vacuum trace and finite-difference convergence;
4. full-map convergence, symplecticity, reverse inverse and turning composition;
5. zero-window identity;
6. vertex and parallel source preparations kept distinct;
7. caustic-safe full map and guarded graph diagnostics;
8. orientation/parity endpoint action and exact reconstruction;
9. affine rescaling with phase-rate conversion `D_a`;
10. geometric dilation `M -> sM` at fixed `(rho,R,beta)` with coherently converted endpoints, affine parameter and phase rates;
11. finite-difference rank for `(rho,R,log M)` using preregistered raw/derived feature blocks;
12. bounded collision search, explicitly not a proof of global injectivity;
13. deterministic byte-identical artifact generation.

## Scale and rank gate

Under `M -> sM`, hold `rho`, `R`, `beta`, branch, orientation and dimensionless sample locations fixed. Convert endpoint coordinates coherently. Compare the phase map after the declared geometric phase-rate conversion

\[
 D_s=\operatorname{diag}(I_2,I_2/s),
 \qquad P_{\rm converted}=D_s^{-1}P(sM)D_s.
\]

A nonzero coordinate/raw-rate difference before conversion is not scale identification. A vanishing converted `log M` Jacobian column is a geometric scale-null direction, not evidence for `ell0`.

Preregister rank features from:

- flattened converted full phase map;
- dimensionless optical-tidal profile checkpoints `M^2 K`;
- caustic landmarks normalized by `M` where defined.

Report separate ranks for `(rho,R)` and `(rho,R,log M)`, Jacobian columns, finite-difference step, tolerance, null directions and feature provenance. `rho` and `R` directions are shape/boundary directions, not internal-scale directions. Local rank does not establish global injectivity or statistical independence.

## Artifact contract

Create deterministic JSON containing:

- `status`, `scope`, `classification`, `gate`, `UMCH`, `ell0_identified`, `detection`, `maximum_interpretation`;
- complete path, branch, affine and endpoint conventions;
- screen bases/transport controls and full optical-tidal profiles;
- primary full phase maps and checkpoint maps;
- convergence, symplectic, reverse, composition and zero-window controls;
- source preparations, caustic/graph diagnostics and endpoint-action controls;
- affine and geometric scale controls with conversion matrices;
- rank Jacobian columns, steps, tolerance, null directions and bounded collision results;
- source scope and explicit unsupported claims.

Expected maximum interpretation, even if every gate passes: `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Sources and scope

- `Schwarzschild2003Translation`: Schwarzschild metric/context only.
- `Darwin1959GravityField`: Schwarzschild null trajectories and critical-orbit context only.
- `Sachs1961`: null optical/Jacobi framework only.

All finite-boundary integration, screen choice, endpoint action, numerical controls, rank features and scale audit are project derivations or toy controls. None of these sources establishes detector calibration, covariance, `ell0`, UMCH or detection.

## Decision rule

Promote only the exact bounded result supported by tests. Likely admissible negative result if dilation remains null:

`SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FULL_SCREEN_JACOBI_PHASE_MAP_ADDS_OPTICAL_PROFILE_AND_CAUSTIC_STRUCTURE_BUT_RETAINS_AFFINE_AND_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

Keep the following gate open unless physically derived:

`PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

No passing mathematical control supports a positive UMCH claim. No structural dead end may be declared from this bounded control alone.
