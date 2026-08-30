# Schwarzschild photon-sphere optical Jacobi/Sachs implementation plan

> Execute directly without subagents. Follow test-driven development and preserve each RED result. Work only in `/home/public/studi_relativita/.worktrees/schwarzschild-photon-sphere-jacobi` on `research/schwarzschild-photon-sphere-jacobi`.

**Goal:** Add a deterministic, connection-derived null-screen Jacobi phase-map control on the exact Schwarzschild photon sphere, attack it with caustic, endpoint, affine and geometric-scale counterexamples, and publish bounded bilingual audits without changing the UMCH contract.

**Architecture:** Reuse only low-level matrix/Schwarzschild helpers from `schwarzschild_mixed_levi_civita_holonomy.py`. Derive the optical tidal matrix from four-dimensional connection/curvature data and compare it with an independent perturbative Jacobi calculation. Preserve the full `4x4` phase map; expose Sachs graphs only behind invertibility gates. Serialize canonical JSON and make reports consume the artifact rather than duplicating computation.

**Scientific state:** `UMCH=UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`; no detector, covariance, physical screen preparation, affine-frequency standard, `ell0`, bound, mechanism or evidence.

---

## Task 1: Define RED scientific contract

**Create:**
- `tests/test_schwarzschild_photon_sphere_jacobi.py`

Write failing tests requiring:

1. `r_ph=3M`, local-tetrad null tangent `k=(1,0,0,orientation)`, affine winding length `L=6*pi*M`;
2. screen orthonormality modulo the null direction and tracefree optical tidal matrix;
3. curvature-derived `K` agreement with an independent finite-difference connection/Jacobi control;
4. exact constant-generator phase map agreement with deterministic numerical propagation;
5. symplectic residual below a declared conservative bound;
6. vertex initial data `X(0)=0,V(0)=I` and non-vertex initial data `X(0)=I,V(0)=S0` propagated separately;
7. oscillatory-channel conjugate points and singular vertex endpoint block after one winding;
8. full phase map finite/invertible where `S_vertex` is gated as `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`;
9. zero-window, reversal/orientation, endpoint quotient, affine reparameterization and geometric scaling controls;
10. holonomy cross-map dependence and discrete-winding no-continuous-Jacobian classification;
11. exact raw keys and bounded status/scope/gate strings from the spec;
12. canonical artifact equality after running script.

Run:

```bash
python -m unittest tests.test_schwarzschild_photon_sphere_jacobi -v
```

If environment lacks `pytest`, use repository-supported `python -m unittest`; interpreter absence is environment evidence, not scientific RED. Expected RED: `FileNotFoundError` or import failure because study file does not exist.

Commit:

```bash
git add tests/test_schwarzschild_photon_sphere_jacobi.py
git commit -m "test: define photon-sphere Jacobi controls"
```

## Task 2: Implement minimum connection-derived study

**Create:**
- `studies/spacetime/schwarzschild_photon_sphere_jacobi.py`
- `studies/spacetime/schwarzschild-photon-sphere-jacobi-results.json`

Implement small pure functions for:

- metric/tetrad/null-tangent and screen construction;
- Christoffel derivatives and four-dimensional Riemann contraction in a fixed documented sign convention;
- independent finite-difference neighboring-geodesic acceleration check;
- optical `2x2 K` projection;
- canonical generator and matrix exponential;
- deterministic RK4 phase propagation;
- block split, determinant/inverse, symplectic and safe-graph gates;
- vertex/non-vertex controls;
- conjugate-point location and endpoint caustic classification;
- orientation/reversal and endpoint screen-basis actions;
- affine-rate conversion with `D_a=diag(I,I/a)`;
- Schwarzschild scale orbit;
- bounded holonomy cross-map and winding classification;
- canonical recursive float serialization;
- `build()` and CLI artifact check/write.

Do not hard-code the sign ordering of `K` merely to satisfy expected hyperbolic/elliptic labels. Derive it, record convention, then fix test expectations if the independent connection calculation falsifies the provisional ordering.

Run focused tests until green, then regenerate artifact and require `--check` success.

Commit:

```bash
git add studies/spacetime/schwarzschild_photon_sphere_jacobi.py studies/spacetime/schwarzschild-photon-sphere-jacobi-results.json
git commit -m "feat: audit photon-sphere Jacobi phase map"
```

## Task 3: Bound canonical source scope test-first

**Create:**
- `tests/test_schwarzschild_photon_sphere_jacobi_sources.py`

Require existing bibliography entries and verification-log sections for `Darwin1959GravityField` and `Sachs1961`. Require text that limits them to known Schwarzschild critical circular-orbit and null-radiation/optical context. Require explicit exclusions for project affine normalization, endpoint screens, finite-window phase map, caustic readout, detector/covariance, `ell0`, UMCH and detection.

Run source test and preserve RED if current wording lacks required scope. Edit only:

- `references/verification-log.md`

Add no new source unless a canonical-source ambiguity cannot be resolved from existing verified entries. If external verification becomes necessary, stop on ambiguity rather than invent support.

Commit test and source-scope correction separately:

```bash
git commit -m "test: require bounded photon-sphere Jacobi sources"
git commit -m "docs: bound photon-sphere Jacobi source claims"
```

## Task 4: Define bilingual report contract RED

**Create:**
- `tests/test_schwarzschild_photon_sphere_jacobi_reports.py`

Require English and Italian reports plus theory note to contain identical machine-stable values for:

- classification, status, scope and gate;
- `UNPROVEN`, `NO_POSITIVE_DETECTION_CLAIM`;
- `ell0_identified=false` and `structural_dead_end=NOT_DECLARED`;
- affine normalization and toy-boundary labels;
- raw phase-map primacy and graph caustic gate;
- endpoint quotient and scale-orbit limitations;
- dependence of phase map/holonomy on common geometry;
- exact source keys and source limitations;
- no detector, covariance, readout, evidence or detection claim.

Expected RED: missing report/theory files.

Commit:

```bash
git add tests/test_schwarzschild_photon_sphere_jacobi_reports.py
git commit -m "test: define photon-sphere Jacobi report contract"
```

## Task 5: Write theory and semantically aligned audits

**Create:**
- `theory/spacetime/schwarzschild-photon-sphere-jacobi.md`
- `audit/schwarzschild-photon-sphere-jacobi-report-en.md`
- `audit/schwarzschild-photon-sphere-jacobi-report-it.md`

**Modify conservatively:**
- `docs/roadmap.md`

Explain equations, sign conventions, boundary data, graph domains, caustic preservation via the full phase map, endpoint action, affine-rate conversion, scale orbit and cross-map dependence. Reports must classify known results, project derivations, toy controls, negative results and open gates separately. Italian/English labels, values, equations, references, scope and limitations must remain semantically aligned.

Do not modify authoritative UMCH papers unless a directly contradictory statement is found; such a theoretical-contract change would require separate human ratification.

Run focused study/source/report tests and artifact check.

Commit:

```bash
git add theory/spacetime/schwarzschild-photon-sphere-jacobi.md audit/schwarzschild-photon-sphere-jacobi-report-en.md audit/schwarzschild-photon-sphere-jacobi-report-it.md docs/roadmap.md
git commit -m "docs: audit photon-sphere Jacobi phase map"
```

## Task 6: Direct conformance and deterministic verification

Because user forbids subagents, perform direct review and record this as explicit exception to any reviewer-dispatch gate.

Check full diff against binding prompt, spec and plan. Verify raw contract keys individually. Run:

```bash
python studies/spacetime/schwarzschild_photon_sphere_jacobi.py --check
python -m unittest \
  tests.test_schwarzschild_photon_sphere_jacobi \
  tests.test_schwarzschild_photon_sphere_jacobi_sources \
  tests.test_schwarzschild_photon_sphere_jacobi_reports -v
python -m unittest discover -s tests -v
python tools/inventory_source.py --check
python tools/extract_docx.py --check
git diff --check origin/main...HEAD
git status --short
```

Use repository's available Python environment. If local and CI Python versions serialize floats differently, fix canonical serialization and widen only numerically justified convergence bounds; preserve failure provenance in audit or commit history.

## Task 7: Push, CI, conservative PR and Hermes

Push exact SHA, open PR, and wait for all GitHub `tests` and `latex` jobs. Do not auto-merge if source scope is ambiguous, tests are flaky, bilingual claims diverge, theoretical contract changes, or any structural-dead-end/reformulation state appears.

For fully green bounded additions only:

1. verify PR head SHA equals local head;
2. auto-merge conservatively;
3. sync clean `main` to merge SHA;
4. run focused post-merge tests;
5. remove local/remote feature branch and worktree;
6. create timestamped Hermes Inbox note containing PR, merge SHA, exact results, status/scope/gate, failures/corrections, tests/CI and unresolved blockers.

Keep loop `16588751` active. Cancel it only if binding stop/dead-end criteria are met. This control alone cannot meet those criteria because generic scattering, freely falling endpoints, physical screen preparation and detector/covariance routes remain unfinished.
