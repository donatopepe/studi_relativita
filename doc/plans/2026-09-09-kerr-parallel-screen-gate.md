# Kerr parallel-screen transport implementation plan

**Objective:** establish metric-compatible parallel screen transport on PR #108 finite Kerr paths and classify endpoint screen-map orientation/scale behavior.

**Metric:** `8/8` preregistered controls.

**MVP:** analytic equatorial Kerr connection plus direct RK4 transport; reuse endpoint path/tetrads; no Jacobi solver.

**Escalation:** Jacobi/Sachs only after GREEN.

## Task 1 — Source scope

Create source tests. Extend Dolan verification log with inspected sections/equations and strict exclusions. Preserve RED, GREEN, commit.

## Task 2 — Eight controls RED

Create focused tests for connection, tangent, screen, endpoint map, reversal, orientation, Schwarzschild, dilation/rank/nonclaims. Require stable artifact. Commit RED.

## Task 3 — Transport engine

Create `studies/spacetime/kerr_parallel_screen_gate.py`. Implement metric derivatives, inverse metric, Christoffels, signed-y path, RK4 transport, endpoint ZAMO screens, quotient map, reverse/composition and scale controls. GREEN, commit.

## Task 4 — Artifact

Create deterministic JSON with exact eight controls, raw transported vectors/maps, equal/unequal endpoints, convergence, result classification, physical gate, thresholds, and nonclaims. Commit.

## Task 5 — Reports

Add theory note, EN/IT audits, report tests, roadmap and ledger updates. Preserve all prior results. Commit.

## Task 6 — Closure

Run focused/full tests, deterministic checks, direct review, push, PR, green CI, merge, post-merge verification, Hermes, cleanup.
