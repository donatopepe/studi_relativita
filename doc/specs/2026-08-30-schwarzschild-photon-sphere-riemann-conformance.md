# Schwarzschild photon-sphere full-Riemann conformance audit

## Status and bounded question

This specification is an autonomous, conservative correction audit under the ratified operator-valued UMCH route. It does not change the hypothesis contract. UMCH remains `UNPROVEN`; detection remains `NO_POSITIVE_DETECTION_CLAIM`; `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`.

Question: does the legacy photon-sphere Jacobi control remain conformant after the independent four-dimensional Schwarzschild Riemann reconstruction in PR #95 falsified its generic-scattering continuation's optical profile?

Classification:

- Schwarzschild geometry and circular null orbit: `KNOWN_RESULT` within the bounded scopes of `Schwarzschild2003Translation` and `Darwin1959GravityField`;
- null Jacobi/Sachs framework: `KNOWN_RESULT` within the bounded scope of `Sachs1961`;
- local screen choice, affine normalization, full-Riemann projection, phase-map regeneration and cross-artifact comparison: `PROJECT_DERIVATION`;
- old radial-only connection check, trace-inferred polar channel and boundary preparations: `TOY_CONTROL`;
- any falsification, correction and retained scale blindness: `NEGATIVE_RESULT`.

No cited source establishes project screen preparation, affine/frequency calibration, source/observer boundary, detector readout, covariance, `ell0`, UMCH, evidence or detection.

## Counterexample-first alternatives

1. **Leave legacy result unchanged.** Rejected: its `K=diag(+1,-1)/(9M^2)` conflicts with the independently reconstructed scattering limit and its polar channel was inferred from vacuum trace rather than computed with `theta` derivatives.
2. **Patch signs and factor directly from scattering.** Rejected as non-independent: that would copy the newer formula instead of testing the circular orbit.
3. **Selected: direct circular-orbit full-Riemann projection.** Reconstruct `R_abcd` from the four-dimensional metric with centered `r` and `theta` derivatives, project onto an explicit ordered screen, refine finite-difference step, then regenerate all dependent phase-map, caustic, spectral and scale controls.

## Preregistered geometry and conventions

At `r=3M`, `theta=pi/2`, use the project affine anchor

`k=e_0+orientation*e_3`

in the local static orthonormal tetrad. Thus coordinate components are

`k=(1/sqrt(f),0,0,orientation/r)`, `f=1-2M/r`,

and one winding has affine length `L=6*pi*M`. This is not a detector-derived absolute frequency standard.

Use ordered screen

`(e_polar,e_radial)=((0,0,1/r,0),(0,sqrt(f),0,0))`.

This differs from the legacy `(radial,polar)` order and must be explicit in raw artifacts. With convention `X''=KX`, project

`K_AB=-R_abcd e_A^a k^b e_B^c k^d`.

The direct projection must compute both channels and off-diagonal entries. Vacuum trace is a check only, never a derivation of the uncomputed channel.

## Falsification and correction gates

The legacy profile is falsified if refined direct projection disagrees beyond numerical tolerance with

`diag(+1,-1)/(9M^2)` in legacy `(radial,polar)` order.

A bounded correction is accepted only if:

- coarse/fine full-Riemann projections converge;
- screen metric, null tangent, symmetry and vacuum trace residuals pass;
- corrected analytic `K` matches direct projection in explicit order;
- exact phase map matches an independent RK4 integration and is symplectic;
- orientation, endpoint action, affine conversion and geometric scaling controls rerun;
- caustic locations and graph statuses are regenerated rather than text-patched;
- deterministic JSON, English/Italian audits, theory, roadmap and source scope agree;
- old result remains documented as falsified, not erased.

No preregistered sign or factor is assumed for corrected `K`; direct reconstruction decides it.

## Identifiability interpretation

A corrected local optical profile may change hyperbolic/elliptic channel assignment, characteristic coefficients and caustic positions. It does not identify `ell0`. Under `M -> sM`, dimensionless geometry and properly converted phase maps remain the relevant scale test. Raw full phase map remains primary through caustics; Sachs graph objects are derived only where their required block is invertible.

Maximum interpretation after every passing gate remains `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`.

## Source and history contract

Reuse only canonical keys already present: `Schwarzschild2003Translation`, `Darwin1959GravityField`, `Sachs1961`. Record exact bounded scopes and exclusions. Preserve PR #90 legacy history and PR #95 falsification context. This correction is not `STRUCTURAL_DEAD_END_CANDIDATE`; physical source, endpoint, calibration, readout and covariance routes remain unfinished rather than structurally excluded.

## Delivery

Work test-first in this isolated branch. Produce small RED/GREEN commits, deterministic artifact checks, bilingual audit parity, focused and full suites, `tools/extract_docx.py --check`, `tools/inventory_source.py --check`, `git diff --check`, direct review (`DIRECT_REVIEW_NO_SUBAGENT`), PR CI and Hermes note. Auto-merge only if correction is bounded, unambiguous and all CI is green.
