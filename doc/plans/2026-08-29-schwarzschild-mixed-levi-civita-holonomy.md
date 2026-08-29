# Schwarzschild mixed-plane Levi-Civita holonomy implementation plan

> Execute directly without subagents per binding user instruction. Preserve test-first failures and use small commits.

**Goal:** Add a deterministic exact-geometry/numerical-transport control for finite mixed-plane Schwarzschild Levi-Civita holonomies, emphasizing path/boundary ordering and absolute-scale non-identifiability.

**Architecture:** A dependency-free Python module supplies Schwarzschild metric and Christoffel matrices, RK4 segment transport, tetrad conversion, deterministic refinement, reversal/composition, local curvature-flux comparison, boundary collision, scaling and null controls. One sorted JSON artifact retains raw matrices and histories. Focused scientific, source and bilingual report contracts precede their implementations.

## Task 1: Scientific contract — RED

**Files:** create `tests/test_schwarzschild_mixed_levi_civita_holonomy.py`.

1. Require metric-connection compatibility and Lorentz tetrad holonomy.
2. Require nonidentity, reversal/inverse and step-refinement convergence.
3. Require noncommuting `tr` and `rphi` common-base holonomies.
4. Require shrinking-loop local-curvature agreement and nonzero finite-window naive-flux mismatch.
5. Require equal-area/boundary-position collision counterexample.
6. Require spectrum/conjugacy quotient controls.
7. Require exact simultaneous scaling orbit and flat/shrinking identity limits.
8. Require full raw record and nonconfirmatory labels.
9. Run focused test; preserve missing-module RED; commit tests.

## Task 2: Deterministic transport implementation — GREEN

**Files:** create module and JSON under `studies/spacetime/`.

1. Implement matrix operations, metric, analytic Christoffel matrices and static tetrad.
2. Implement labelled rectangle vertices and RK4 transport on each coordinate segment.
3. Convert closed-loop coordinate transport to common-base tetrad holonomy.
4. Implement reversal, mixed-plane ordered products/commutator and convergence history.
5. Compute local curvature generator numerically from connection derivatives plus commutator; test shrinking loops.
6. Implement boundary-placement/equal-coordinate-area comparison, conjugacy, scaling and null controls.
7. Write/check deterministic sorted JSON; run focused GREEN; commit.

## Task 3: Canonical sources — RED/GREEN

**Files:** create focused source test; modify `references/library.bib` and `references/verification-log.md`.

1. Verify DOI-backed canonical sources for Schwarzschild geometry and connection/holonomy-curvature relation.
2. Require citation keys, identifiers, exact supported topics and explicit project non-support limits.
3. Preserve RED, commit test, add entries/log, run generic bibliography GREEN, commit.

## Task 4: Bilingual authority — RED/GREEN

**Files:** create report test, theory note, English/Italian audits; update roadmap conservatively.

1. Require shared classification/status/scope/gate, equations, values, limitations and nonclaims.
2. Preserve missing-report RED; commit.
3. Explain coordinate-loop scope, numerical convergence, path ordering, boundary collision, quotient, scaling orbit and null limits.
4. Keep `UNPROVEN`, `NO_POSITIVE_DETECTION_CLAIM`, `ell0_identified=false`, `structural_dead_end=NOT_DECLARED` aligned.
5. Run report/public-doc tests; commit.

## Task 5: Verification and delivery

1. Run new and related artifact checks.
2. Run full unittest suite, extraction, inventory, legacy identifiability and `git diff --check`.
3. Push and open bounded negative-result PR.
4. Require duplicate tests and LaTeX CI green.
5. Auto-merge only if conservative and unambiguous; otherwise stop.
6. Sync main, run focused post-merge tests, record Hermes Inbox note, clean worktree/branch.
7. Keep durable loop active: this route cannot satisfy structural-dead-end criteria.
