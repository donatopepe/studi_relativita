# Kerr Jacobi tidal-map implementation plan

**Objective:** derive full finite Kerr screen phase map and test orientation shape versus scale null.

**Metric:** `8/8` preregistered controls.

**MVP:** exact equatorial optical tidal amplitude plus RK4 `4x4` phase map on verified PR #109 screen.

**Escalation:** physical source/readout only after phase-map gate; non-equatorial complex screen only if equatorial result is structurally rank deficient.

## Task 1 — Source and scenarios

Add Boero–Moreschi bibliography/log and source tests. Add scenario manifest/runner test RED covering J01–J06, total/granular/category modes, JSON report, fail-closed handler contract. GREEN source metadata, commit.

## Task 2 — Eight scientific controls RED

Create tests for tidal profile, Schwarzschild conformance, symplecticity, reversal/composition/convergence, orientation, preparations/caustics, scaling/rank/nonclaims, stable artifact. Commit RED.

## Task 3 — Jacobi engine

Create standard-library module reusing endpoint/screen path. Implement tidal profile, phase RK4, blocks/graph, reverse/composition, source preparation, scale/rank. GREEN, commit.

## Task 4 — Scenario runner and artifact

Create stable scenario JSON manifest, CLI runner, deterministic report contract, and scientific result artifact. Validate total and granular. Commit.

## Task 5 — Reports

Add theory, EN/IT audits, report tests, roadmap/ledger. Preserve all history. Commit.

## Task 6 — Closure

CodeGraph sync/query; focused/full suite; total scenario battery plus each category; deterministic checks; direct review; push, PR, green CI, merge, post-merge verify, Hermes, cleanup.
