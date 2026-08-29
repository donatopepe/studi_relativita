# Einstein-static spatial Levi-Civita holonomy implementation plan

> Execute directly without subagents, per explicit user instruction. Preserve RED failures and use small commits.

**Goal:** Add an algebraically closed four-dimensional product-spacetime control showing that genuine non-Abelian Levi-Civita holonomy can remain a dependent finite-window channel and absolute-curvature-radius-scale blind.

**Architecture:** A dependency-free Python module implements spherical triangle geometry, embedded `SO(3)` tetrad rotations, ordered products, scaling/null controls, equal-excess shape collision, and great-circle Jacobi segment maps. It writes one sorted deterministic JSON artifact. Focused scientific tests precede implementation; report-contract tests precede theory/audits. Canonical source additions are test-first and scope-limited.

## Task 1: Scientific test contract — RED

**Files:**
- Create `tests/test_einstein_static_spatial_holonomy.py`

1. Test right-spherical-triangle identities and positive excess.
2. Test Lorentz metric compatibility and fixed time basis.
3. Test reversal and noncommuting rotations in distinct spatial planes.
4. Test exact `H=exp(W_T)` cross-channel dependence.
5. Test trace/sign aliasing and common `SO(3)` conjugacy.
6. Test bounded equal-excess/different-shape collision and distinct labelled Jacobi segment maps.
7. Test `(R,L)->(sR,sL)` orbit and flat limit at fixed proper lengths.
8. Test raw-record keys and nonconfirmatory status fields.
9. Run focused tests and preserve missing-module RED output.
10. Commit tests only.

## Task 2: Minimal deterministic implementation — GREEN

**Files:**
- Create `studies/spacetime/einstein_static_spatial_holonomy.py`
- Create `studies/spacetime/einstein-static-spatial-holonomy-results.json`

1. Implement dependency-free matrix/vector operations and `SO(3)` plane rotations embedded in tetrad basis.
2. Implement right spherical triangle side/angle/excess/area formulas with explicit domain checks.
3. Implement loop, reversal, ordered-product, commutator, characteristic data, and conjugacy controls.
4. Implement `W_T=E J_ij` and analytic exponential as the same rotation; retain dependence flag.
5. Implement deterministic bisection for equal-excess shape collision and great-circle transverse Jacobi blocks.
6. Implement scale-orbit and flat controls.
7. Build sorted JSON with full raw record and epistemic labels.
8. Run `--write`, focused tests, `--check`; adjust only justified tolerances.
9. Commit implementation and artifact.

## Task 3: Canonical bibliography — RED/GREEN

**Files:**
- Modify `references/library.bib`
- Modify `references/verification-log.md`
- Modify or create a focused bibliography test if existing generic tests do not assert the new entries.

1. Verify canonical metadata and exact passages for Einstein-static product geometry and spherical holonomy/Gauss--Bonnet.
2. Add failing tests for required citation keys/DOIs and explicit non-support limits.
3. Run focused bibliography RED and preserve output.
4. Add entries and verification-log records distinguishing known geometry from project loop/readout/identifiability choices.
5. Run focused bibliography GREEN.
6. Commit tests, then bibliography changes separately.

## Task 4: Bilingual authority and audit — RED/GREEN

**Files:**
- Create `tests/test_einstein_static_spatial_holonomy_reports.py`
- Create `theory/spacetime/einstein-static-spatial-holonomy.md`
- Create `audit/einstein-static-spatial-holonomy-report-en.md`
- Create `audit/einstein-static-spatial-holonomy-report-it.md`
- Modify `docs/roadmap.md` only if a bounded state update is needed.

1. Add report tests requiring shared classification/status/scope/gate, formulas, deterministic values, source limits, `ell0_identified=false`, `UNPROVEN`, and no detection claim.
2. Run report RED and preserve missing-file output; commit tests.
3. Write theory derivation and semantically aligned English/Italian audits.
4. Record non-Abelianity without rank overclaim, exact window dependence, shape/Jacobi distinction, scale orbit, physical loop limits, and no structural dead end.
5. Run report/public-doc tests; commit docs.

## Task 5: Full verification and conservative delivery

1. Run new artifact `--check` and related Levi-Civita/holonomy/Jacobi artifact checks.
2. Run `python3 -m unittest discover -s tests`.
3. Run extraction, inventory, legacy identifiability, and `git diff --check origin/main...HEAD`.
4. Verify clean status and deterministic artifact regeneration.
5. Push branch and open PR with bounded negative-result wording.
6. Require GitHub tests and LaTeX green. No local TeX success claim if unavailable.
7. Auto-merge only if diff is conservative, checks all green, and no substantive ambiguity appears.
8. Sync `main`, rerun focused post-merge checks, update Hermes via timestamped Inbox note if concurrent, and remove worktree/branch.
9. Keep durable loop active because no structural dead end is declared.
