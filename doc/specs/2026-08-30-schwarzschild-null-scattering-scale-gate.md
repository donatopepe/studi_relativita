# Schwarzschild nonradial null-scattering finite-window scale gate

## Status and bounded question

This specification continues the ratified operator-valued UMCH route without changing its hypothesis contract. UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`.

Question: for a future equatorial Schwarzschild null ray that enters from a finite static boundary, reaches one radial turning point and exits to the same boundary, do the raw open-path Levi-Civita transport and boundary scattering records contain a physically independent geometric scale direction, or do they depend only on dimensionless turning-point and boundary ratios after declared endpoint conversions?

Classifications:

- Schwarzschild exterior geometry and null-geodesic first integrals: `KNOWN_RESULT` in the bounded scope of `Schwarzschild2003Translation` and `Darwin1959GravityField`;
- finite-boundary ray integration, turning-point matching, open-path transport and rank audit: `PROJECT_DERIVATION`;
- static boundary tetrads, unit Killing-energy normalization and symmetric source/observer boundary: `TOY_CONTROL` / project anchors;
- scale blindness, branch collisions or rank loss: `NEGATIVE_RESULT` if tests pass;
- physical emitter/absorber action, freely falling endpoints, absolute frequency standard, vector detector readout, covariance and an `ell0` law: `OPEN_PROBLEM`.

No source establishes this finite-boundary protocol, endpoint calibration, detector, covariance, `ell0`, UMCH, evidence or detection.

## Alternatives and selected design

1. **Asymptotic scattering at infinity.** Familiar, but hides finite-window boundary calibration and introduces limiting conventions. Rejected for this bounded control.
2. **Full Sachs/Jacobi screen map through generic scattering.** Stronger but adds screen transport, source boundary data, caustic continuation and affine calibration simultaneously. Deferred until the simpler trajectory/connection scale symmetry is measured.
3. **Finite symmetric scattering with raw connection transport — selected.** Keeps one turning point, explicit incoming/outgoing branches and finite endpoint bases. It is the smallest generic nonradial Schwarzschild extension that can falsify scale identifiability before adding detector assumptions.

## Geometry and domain

Use Schwarzschild coordinates on the equatorial exterior with `G=c=1`, mass `M>0`, finite boundary

\[
 r_b=M R,\qquad R>\rho>3,
\]

and turning radius

\[
 r_p=M\rho.
\]

Set Killing energy `E=1` as a project affine anchor. The turning condition fixes

\[
 \beta\equiv b/M=\frac{\rho}{\sqrt{1-2/\rho}},\qquad L_z=M\beta.
\]

For `x=r/M`, the two radial branches obey

\[
 \frac{dt}{dx}=\frac{M}{f(x)\sqrt{1-\beta^2 f(x)/x^2}},\qquad
 \frac{d\phi}{dx}=\frac{\beta}{x^2\sqrt{1-\beta^2 f(x)/x^2}},
 \quad f(x)=1-\frac{2}{x}.
\]

The square-root endpoint at `x=\rho` is regularized by `x=\rho+y^2`. Integrate `y` from zero to `sqrt(R-rho)`. Incoming and outgoing branches have opposite radial signs and matched `t,phi` at the turning point. The complete future path runs from the boundary through the turning point back to the boundary.

Required domain labels:

- `SCATTERING_BRANCH`: `R>rho>3`;
- `CRITICAL_LIMIT_EXCLUDED`: `rho=3` is approached only in a convergence diagnostic, never integrated as a regular turning point;
- `CAPTURE_BRANCH_OUT_OF_SCOPE`: `rho<3`;
- `DOMAIN_INCONSISTENT`: any invalid mass, boundary or turning ordering.

## Primary raw records

Preserve before scalarization:

1. ordered path samples with coordinates and branch labels;
2. coordinate Levi-Civita open-path map `T_coord` solving
   \[
   dT/d\lambda=-\Gamma_\mu k^\mu T;
   \]
3. endpoint static-tetrad map
   \[
   T_{\rm tet}=E_o^{-1}T_{\rm coord}E_s;
   \]
4. boundary scattering record
   \[
   S_{\rm ray}=(\Delta t/M,\Delta\phi,\beta,R,\rho,
   k_s^{(a)},k_o^{(a)}).
   \]

`T_tet` is an open-path endpoint map, not holonomy. `Delta t/M`, `Delta phi`, characteristic coefficients, norms and numerical Jacobians are diagnostics; they do not replace raw maps.

## Counterexample-first controls

### Equations, turning point and branch matching

Check nullness and geodesic first integrals along both branches. Check the turning residual and continuity of coordinates and transported vectors at the matched turning point. Reverse-path integration must reconstruct the inverse transport within numerical tolerance.

### Finite-window and boundary dependence

Run at least `rho in {3.2,4,6}` and `R in {8,12,20}` where valid. Changing `R` is an explicit boundary/protocol direction, not automatically an interior curvature direction. Test the near-critical sequence `rho in {3.5,3.2,3.1}` only for increasing dwell/deflection behavior; no critical exponent or detector echo is claimed.

### Orientation

Azimuthal reversal sends `beta -> -beta` and `Delta phi -> -Delta phi`. Preserve both raw maps. Any equality of scalar norms is classified as projection aliasing, not raw-map equality.

### Endpoint quotient

Independent endpoint tetrad actions change raw entries by `T -> Q_o^{-1}TQ_s`. Reconstructing the declared static-basis interior map must remove those actions. No endpoint quotient is called physical until source/observer calibration is derived.

### Geometric scale symmetry

Compare `(M,r_p,r_b,L_z)` with `(sM,sr_p,sr_b,sL_z)` at fixed `(rho,R,beta)` and with endpoint tetrad conversion declared. Test separately:

- dimensionless trajectory record invariance;
- `Delta t -> s Delta t` while `Delta t/M` stays invariant;
- endpoint-tetrad transport invariance;
- coordinate-map changes that disappear after endpoint tetrad conversion.

This is geometric scale blindness, distinct from affine-frequency rescaling.

### Local rank and global injectivity

Build a deterministic feature vector from the full flattened `T_tet` plus `Delta t/M`, `Delta phi` and tetrad endpoint directions. Compute finite-difference Jacobians with respect to `(rho,R,log M)`.

Preregistered interpretations:

- nonzero `rho` column: interior shape direction;
- nonzero `R` column: finite-boundary protocol direction;
- null `log M` column: geometric scale blindness;
- rank in `(rho,R)` does not imply physical channel independence because both records share one geometry/path and covariance is absent;
- local rank does not imply global injectivity; search bounded collisions and report them separately.

No value of `rho`, `R`, `beta`, dwell time or deflection is `ell/ell0` or `ell0`.

## Deterministic artifact

Create `studies/spacetime/schwarzschild-null-scattering-scale-gate-results.json` containing:

- exact status, scope, gate and classification labels;
- domain and normalization declarations;
- raw records for preregistered checkpoints;
- null/geodesic/turning/matching/reversal residuals;
- orientation and endpoint-action controls;
- separate geometric-scale controls;
- Jacobian columns, tolerances, ranks and null directions;
- bounded collision search;
- source scope and explicit nonclaims.

`--check` must reproduce byte-identical JSON.

## Documentation and source authority

Create aligned English/Italian audit reports and a theory note. Update `docs/roadmap.md` and `references/verification-log.md`. Existing canonical entries may be reused only within their recorded scope:

- `Schwarzschild2003Translation`: Schwarzschild exterior metric context;
- `Darwin1959GravityField`: Schwarzschild null trajectories and critical circular-orbit context.

The finite-window integrations, path transport, endpoint quotient and rank conclusions remain project derivations. No new citation is needed unless a new source-backed statement is introduced.

## Acceptance gates

Required tests:

1. domain and turning relation;
2. null and first-integral residuals;
3. incoming/outgoing branch matching;
4. metric-compatible open-path transport and reverse inverse;
5. finite-boundary dependence;
6. orientation raw-map distinction and projected alias classification;
7. endpoint action/reconstruction;
8. separate geometric-scale invariance;
9. local Jacobian/rank/null-direction audit;
10. bounded collision search and no global-injectivity overclaim;
11. deterministic artifact;
12. bilingual status/scope/gate/source/nonclaim parity;
13. focused prior Schwarzschild controls, full suite, extraction/inventory checks and `git diff --check`;
14. green GitHub `tests` and `latex` jobs before merge.

Passing yields at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Preregistered status envelope

If the expected scale symmetry passes, use a bounded status of the form

`SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FINITE_WINDOW_OPEN_TRANSPORT_HAS_TURNING_AND_BOUNDARY_SHAPE_DIRECTIONS_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

If it fails, preserve the failure and classify whether it comes from coordinate endpoints, affine normalization, branch matching, numerical error or a genuine dimensionless map dependence before changing any claim.

Expected unresolved gate:

`PHYSICAL_SCATTERING_WINDOW_EMITTER_ABSORBER_TETRADS_AFFINE_FREQUENCY_STANDARD_SCREEN_JACOBI_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

Generic Sachs/Jacobi scattering and detector-derived readout remain bounded open routes. Therefore this control alone cannot satisfy structural-dead-end criteria and must not trigger reformulation.
