# Implementation plan: Schwarzschild photon-orbit holonomy

> Execute directly in the isolated worktree. Do not dispatch subagents. Follow TDD and preserve every failed expectation in commit/history or audit.

**Goal:** Add a deterministic, bounded exact/algebraically closed control for Levi-Civita transport around a future null circular photon-sphere winding closed by a static worldline segment, then test orientation, ordering, winding and geometric-scale identifiability.

**Architecture:** Reuse the audited Schwarzschild metric/connection and matrix helpers from `schwarzschild_mixed_levi_civita_holonomy.py`. Build constant-generator segment transports with the existing matrix exponential and independently integrate the same paths numerically. Serialize the raw loop matrices and declared controls to JSON with cross-version canonicalization. Add bilingual theory/audits only after scientific tests pass.

## Task 1 — Define the executable scientific contract

**Files:**
- Create `tests/test_schwarzschild_photon_orbit_holonomy.py`
- Later create `studies/spacetime/schwarzschild_photon_orbit_holonomy.py`
- Later create `studies/spacetime/schwarzschild-photon-orbit-holonomy-results.json`

1. Write tests importing the absent module and requiring raw keys from the spec. Run the focused test and preserve the expected `FileNotFoundError`/import failure (RED).
2. Add assertions for photon radius, nullity, geodesic radial residual, exact durations, Lorentz residual, numerical/algebraic agreement, nonidentity, inverse reversal, segment-order difference, winding relation, orientation raw/quotient behavior, scaling orbit and null controls.
3. Commit tests before implementation.

## Task 2 — Implement algebraically closed and numerical transport

**Files:**
- Create `studies/spacetime/schwarzschild_photon_orbit_holonomy.py`
- Create deterministic JSON artifact

1. Import shared Schwarzschild matrix/connection helpers without copying geometry.
2. Implement photon-sphere parameters and tangent validation from the metric and connection.
3. Implement constant-generator null and closure transports, loop composition and reverse/orientation/winding controls.
4. Implement an independent RK4 transport comparison along both segments.
5. Implement anchor/conjugacy, characteristic, scale and shrinking-arc controls without treating scalar quotients as primary.
6. Build/render canonical JSON, rounding platform-sensitive diagnostics or storing conservative bounds.
7. Run focused tests to GREEN; correct hypotheses rather than weakening geometry checks. Commit.

## Task 3 — Bound source claims

**Files:**
- Modify `references/library.bib` only if a canonical source is not already present
- Modify `references/verification-log.md`
- Create `tests/test_schwarzschild_photon_orbit_holonomy_sources.py`

1. Add a RED source-scope test requiring a canonical photon-orbit source and explicit non-support for finite-loop readout, detector covariance, `ell0`, UMCH and detection.
2. Verify DOI/metadata against publisher or trusted index before editing.
3. Add the minimal bibliography/log entry, distinguishing known photon-orbit geometry from project derivations. Run bibliography and focused source tests. Commit.

## Task 4 — Publish bilingual bounded interpretation

**Files:**
- Create `theory/spacetime/schwarzschild-photon-orbit-holonomy.md`
- Create `audit/schwarzschild-photon-orbit-holonomy-report-en.md`
- Create `audit/schwarzschild-photon-orbit-holonomy-report-it.md`
- Create `tests/test_schwarzschild_photon_orbit_holonomy_reports.py`
- Modify `docs/roadmap.md`

1. Write report-contract tests first, requiring identical labels, equations, values, source scope, status, scope and gate across EN/IT.
2. Preserve raw versus quotient distinctions, future null leg versus past timelike closure, and the absence of emitter/absorber/readout.
3. State whether noncommutativity, winding and orientation add physical rank; retain scale blindness and `ell0_identified=false` if shown.
4. Update roadmap conservatively; do not edit authoritative papers unless a contract test demonstrates a current contradiction.
5. Run focused reports and commit.

## Task 5 — Verify and ship conservatively

1. Regenerate artifact and verify byte equality.
2. Run focused photon-orbit, prior Schwarzschild exact controls and bibliography/report tests.
3. Run the complete unittest suite, extraction/inventory checks used by CI, `git diff --check`, and LaTeX workflow commands if configured.
4. Perform direct conformance review because the user forbids subagents; record that exception explicitly in phase tracking.
5. Push branch, open PR, wait for all CI jobs. Auto-merge only if changes remain bounded, conservative and completely green.
6. Verify post-merge main and focused tests, remove worktree/branch if safe, and write a timestamped Hermes Inbox note. Keep durable loop `16588751` active unless structural-dead-end criteria unexpectedly pass (not anticipated by this control).
